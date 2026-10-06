#!/usr/bin/env python3
"""Where does the AI shock land inside each VLW sector? (2017 detail tables)

A partial-equilibrium input-output exercise: push an illustrative AI shock
through 2017 detail commodity-by-commodity total requirements, then ask, for
each VLW 37-sector group, whether the requirement is spread like the group's
output or concentrated in a few detail codes. The "narrowing" factor is the
load on the most-hit pieces over the load on the whole group (both as % of
2017 output); a large factor means a split would narrow the general-equilibrium
impact onto the affected producers.

Requirements are built from the 2017 detail Use, Make and Import matrices
(before redefinitions, producers' prices, September 2025 vintage), with the
industry-technology assumption:
  total:    A = B D,          B = U / g
  domestic: A = B_dom D,  B_dom = (U - Imports) / g,
            and the shock is scaled by the domestic share of private
            equipment investment in each commodity (F02E00).
The constructed total table is checked against BEA's published one.

Shock components, $bn (illustrative; engineering splits unsourced):
  facility_capex 50: 54% office/commercial construction, 32% electrical
                     equipment, 14% mechanical equipment
  electricity    10: electricity bought by the facilities
  power_capex    30: power-sector investment split like FA 2211 in 2017
                     (electric and wind/solar structures, T&D equipment,
                     turbines and engines)
  it_capex      150: servers, storage, networking (reported separately)

Run: python3 code/upstream_concentration.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
BEA = ROOT / "data/raw/bea_2024"
MUI = BEA / "extracted/MAKE-USE-IMPORTS_BEFORE_REDEFINITIONS"
BEA_TR = BEA / "extracted/AllTablesSUP_sep2024/CxC_TR_2017_PRO_DET.xlsx"
USE_FILE = MUI / "IOUse_Before_Redefinitions_PRO_Detail.xlsx"
PEQ_FILE = BEA / "PEQBridge_Detail.xlsx"

WEIGHTS = {"facility_capex": 50.0, "electricity": 10.0, "power_capex": 30.0}
IT_CAPEX = 150.0

CANDIDATES = {
    "Construction": ["2332A0", "233240"],
    "Machinery": ["333415", "333611", "333618", "333413"],
    "PrimMetals": ["331410", "331420"],
    "Electrical": ["335311", "335312", "335313", "335314", "335999"],
    "FabMetals": ["332310", "332320"],
    "Minerals": ["327390", "327100"],
    "Utilities": ["221100"],
}


def vlw37(code):
    """Map a BEA detail code to its vom Lehn-Winberry 37-sector group."""
    c = str(code)
    prefixes = [
        ("21", "Mining"), ("22", "Utilities"), ("23", "Construction"),
        ("321", "Wood"), ("327", "Minerals"), ("331", "PrimMetals"),
        ("332", "FabMetals"), ("333", "Machinery"), ("334", "Computers"),
        ("335", "Electrical"), ("3361", "MotorVeh"), ("3362", "MotorVeh"),
        ("3363", "MotorVeh"), ("336", "OthTransEq"), ("337", "Furniture"),
        ("339", "MiscMfg"), ("311", "Food"), ("312", "Food"), ("313", "Textile"),
        ("314", "Textile"), ("315", "Apparel"), ("316", "Apparel"),
        ("322", "Paper"), ("323", "Printing"), ("324", "Petroleum"),
        ("325", "Chemical"), ("326", "Plastics"), ("42", "Wholesale"),
        ("44", "Retail"), ("45", "Retail"), ("4B", "Retail"),
        ("48", "TranspWare"), ("49", "TranspWare"), ("51", "Info"),
        ("52", "Finance"), ("53", "RealEstate"), ("54", "ProfTech"),
        ("55", "Mgmt"), ("56", "Admin"), ("61", "Educ"), ("62", "Health"),
        ("71", "Arts"), ("721", "Accom"), ("722", "FoodServ"), ("81", "Other"),
    ]
    for p, name in sorted(prefixes, key=lambda t: -len(t[0])):
        if c.startswith(p):
            return name
    return None


def _load(name):
    d = pd.read_excel(MUI / name, sheet_name="2017", header=None)
    b = d.iloc[6:].copy()
    b.columns = [str(c) for c in d.iloc[5]]
    b = b.set_index("Code")
    b.index = [str(i) for i in b.index]
    drop = [c for c in b.columns if c in ("nan", "Commodity Description", "Industry Description")]
    return b.drop(columns=drop).apply(pd.to_numeric, errors="coerce").fillna(0.0)


def build_requirements():
    """Total and domestic commodity-by-commodity total requirements, 2017."""
    use = _load("IOUse_Before_Redefinitions_PRO_Detail.xlsx")
    imp = _load("ImportMatrices_Before_Redefinitions_Detail.xlsx")
    make = _load("IOMake_Before_Redefinitions_PRO_Detail.xlsx")
    inds = [i for i in make.index if i in use.columns and i not in ("T007", "T008")]
    comms = [c for c in make.columns if c in use.index and c not in ("T007", "T008")]
    g = make.loc[inds, comms].sum(axis=1).replace(0, np.nan)
    q = make.loc[inds, comms].sum(axis=0)
    shares = make.loc[inds, comms].div(q.replace(0, np.nan), axis=1).fillna(0.0)
    b_tot = use.loc[comms, inds].div(g, axis=1).fillna(0.0)
    b_dom = (use.loc[comms, inds] - imp.reindex(index=comms, columns=inds).fillna(0.0)).div(g, axis=1).fillna(0.0)
    eye = np.eye(len(comms))
    tr_tot = pd.DataFrame(np.linalg.inv(eye - b_tot.values @ shares.values), index=comms, columns=comms)
    tr_dom = pd.DataFrame(np.linalg.inv(eye - b_dom.values @ shares.values), index=comms, columns=comms)
    fd = use.loc[comms, "F02E00"]
    imp_share = (imp.reindex(index=comms)["F02E00"].fillna(0.0) / fd.replace(0, np.nan)).clip(0, 1).fillna(0.0)
    return tr_tot, tr_dom, q / 1000.0, imp_share  # q in $bn


def check_against_bea(tr_tot, codes=("221100", "2332A0", "233240", "335311", "333415")):
    d = pd.read_excel(BEA_TR, sheet_name="2017", header=None)
    bea = d.iloc[5:, 2:].apply(pd.to_numeric, errors="coerce").fillna(0.0)
    bea.index = [str(c) for c in d.iloc[5:, 0]]
    bea.columns = [str(c) for c in d.iloc[4, 2:]]
    common = [c for c in tr_tot.index if c in bea.index]
    print("Check vs BEA published total requirements (column sums; correlation of columns):")
    for c in codes:
        a, b = tr_tot.loc[common, c], bea.loc[common, c]
        print(f"  {c}: ours {a.sum():.3f}  BEA {b.sum():.3f}  corr {np.corrcoef(a, b)[0, 1]:.3f}")


def peq_line_shares(line):
    d = pd.read_excel(PEQ_FILE, sheet_name="2017", header=None).iloc[5:, :5]
    d.columns = ["line", "cat", "code", "desc", "prod"]
    d["prod"] = pd.to_numeric(d["prod"], errors="coerce").fillna(0.0)
    s = d[d["line"] == line].groupby(d["code"].astype(str))["prod"].sum()
    s = s[s > 0]
    return s / s.sum()


def shock_components():
    facility = {"2332A0": 0.54}
    for c, w in {"335313": .30, "335312": .20, "335311": .15, "335999": .15,
                 "335911": .10, "335920": .05, "335930": .05}.items():
        facility[c] = facility.get(c, 0.0) + 0.32 * w
    for c, w in {"333415": .70, "333413": .10, "333914": .10, "332410": .10}.items():
        facility[c] = facility.get(c, 0.0) + 0.14 * w
    power = {"233240": 54.0 / 99.6}  # FA 2211, 2017: SU30 + SU60 structures
    for c, w in peq_line_shares(16).items():  # EI60 T&D equipment, 36.1
        power[c] = power.get(c, 0.0) + 36.1 / 99.6 * w
    for c, w in peq_line_shares(12).items():  # EI21 + EI22 engines and turbines, 9.5
        power[c] = power.get(c, 0.0) + 9.5 / 99.6 * w
    it = {"334111": 0.7, "334112": 0.1, "334210": 0.2}
    return {"facility_capex": facility, "electricity": {"221100": 1.0},
            "power_capex": power, "it_capex": it}


def shock(tr, weights, imp_share=None):
    f = pd.Series(0.0, index=tr.columns)
    comps = shock_components()
    for name, w in weights.items():
        for c, v in comps[name].items():
            dom = 1.0 - imp_share.get(c, 0.0) if imp_share is not None else 1.0
            f[c] += w * v * dom
    return pd.Series(tr.values @ f.values, index=tr.index), f.sum()


def report(req, q, label):
    df = pd.DataFrame({"req": req, "out": q.reindex(req.index)})
    df["sector"] = [vlw37(c) for c in df.index]
    df = df[df["sector"].notna() & (df["out"] > 0)]
    rows = []
    for sec, sub in CANDIDATES.items():
        t = df[df["sector"] == sec]
        s = t.loc[[c for c in sub if c in t.index]]
        load, sub_load = t["req"].sum() / t["out"].sum(), s["req"].sum() / s["out"].sum()
        rows.append({"sector": sec, "req_bn": t["req"].sum(), "load_pct": 100 * load,
                     "sub_share_req": 100 * s["req"].sum() / t["req"].sum(),
                     "sub_share_out": 100 * s["out"].sum() / t["out"].sum(),
                     "sub_load_pct": 100 * sub_load, "narrowing": sub_load / load})
    print(f"\n{label}")
    print(pd.DataFrame(rows).sort_values("narrowing", ascending=False).round(1).to_string(index=False))
    top = df.groupby("sector")["req"].sum().sort_values(ascending=False)
    print("  largest requirements, $bn: " + ", ".join(f"{k} {v:.1f}" for k, v in top.head(8).items()))
    return df


def main():
    tr_tot, tr_dom, q, imp_share = build_requirements()
    check_against_bea(tr_tot)
    print("\nImport share of 2017 private equipment investment:",
          ", ".join(f"{c} {imp_share.get(c, np.nan):.2f}" for c in
                    ["335311", "335312", "335313", "335999", "335911", "335920",
                     "333415", "333611", "333618", "334111"]))

    req_t, f_t = shock(tr_tot, WEIGHTS)
    report(req_t, q, f"TOTAL requirements (imports treated as domestic), shock {f_t:.0f} $bn")
    req_d, f_d = shock(tr_dom, WEIGHTS, imp_share)
    df_d = report(req_d, q, f"DOMESTIC requirements, domestic shock {f_d:.0f} of {f_t:.0f} $bn")
    print(f"  domestic output generated per $ of shock: {req_d.sum() / f_t:.2f} (total basis {req_t.sum() / f_t:.2f})")

    req_it, f_it = shock(tr_dom, {"it_capex": IT_CAPEX}, imp_share)
    top = pd.DataFrame({"req": req_it, "sector": [vlw37(c) for c in req_it.index]}).groupby("sector")["req"].sum()
    print(f"\nIT capex {IT_CAPEX:.0f} $bn at 2017 import shares: domestic shock {f_it:.1f} $bn; "
          "largest domestic requirements: " + ", ".join(f"{k} {v:.1f}" for k, v in top.sort_values(ascending=False).head(5).items()))

    print("\nTop detail codes within each group, domestic basis (lift = share of requirement / share of output):")
    for sec in ["Construction", "Machinery", "PrimMetals", "Electrical", "FabMetals"]:
        t = df_d[df_d["sector"] == sec].copy()
        t["lift"] = (t["req"] / t["req"].sum()) / (t["out"] / t["out"].sum())
        for c, r in t.sort_values("req", ascending=False).head(3).iterrows():
            print(f"  {sec:12s} {c}  {100 * r['req'] / t['req'].sum():5.1f}% of req, lift {r['lift']:.1f}")


if __name__ == "__main__":
    main()
