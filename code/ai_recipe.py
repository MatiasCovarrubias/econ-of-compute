#!/usr/bin/env python3
"""The recipe of the two AI sectors, by data-center generation, from engineering sources.

AI_facilities (f) owns the shell and the electrical and mechanical plant, buys electricity and
runs the building, and sells powered space to AI_compute. AI_compute (z) owns the servers,
networking and storage, rents space from f, and sells AI services.

The recipe is built per MW of IT load at 6-digit NAICS and then scaled to $1 of AI services:
  1. Facility (f): capex by building element, the investment column by producer, electricity
     (utilisation x PUE x price), water, and the other operating lines.
  2. IT (z): capex per MW, its composition (compute systems, network, storage, integration),
     depreciation by component, trade and transport margins, and the compute layer's operating
     inputs as shares of its cost.
  3. Labs: Korinek and McKelvey (2026). Services revenue = 1.5 x inference compute; labs'
     labour = 0.10 x inference; the margin pays for training compute (steady-state closure).
     Compute (inference + training) is bought at its steady-state cost: capital at user cost
     r + delta plus operating inputs.
Generations (notes/ai-compute-recipe/dc_recipe_engineering.tex, Table 1): A0 legacy (<2015), A1 hyperscale
air-cooled (2015-22), A2 AI air/hybrid (2023-24), A3 AI liquid-cooled GB200 NVL72 (2025-26,
baseline), A3_GB300 (A3 facility with GB300 IT), A4 next generation (2027+).

Every number cites a key in SOURCES. Evidence and ranges are in notes/ai-compute-recipe/research/ (one
report and one *_obs.csv per topic); the synthesis is notes/ai-compute-recipe/dc_recipe_engineering.tex. The
earlier recipe (Bank of Italy rack, 2026) is ai_recipe_cnt2026.py.

Conventions:
  * Capital is valued at new cost per MW of IT load; its service flow is (r + delta) K.
  * Taxes on production (property taxes) are folded into capital services, as in the VLW data,
    where the capital share is value added less compensation. K is capital services / (r + delta).
  * Land is not produced and is excluded from capital (Section 3 of the synthesis note).

Writes data/derived/ai_recipe.json (baseline A3) and data/derived/ai_recipe_detail.csv
(every generation, NAICS detail, per MW and per $1), for reading; the model
(PandPproyect/code/model.py) imports recipe() directly.

Run: python3 code/ai_recipe.py
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DERIVED = HERE.parent / "data" / "derived"
BETA = 0.96
R = 1 / BETA - 1                                  # RbcProdNet
BASELINE = "A3"

SOURCES = {
    "KM": "Korinek and McKelvey (2026), PIIE WP26-9, App. eq. 23 (services / inference = 1.5; "
          "labs = 0.1 x inference, 'a first-pass figure')",
    "TT": "Turner & Townsend, Data Centre Construction Cost Index 2019-2025 (hard cost per MW "
          "IT; element shares 54/22/14/10 air, 48/33/9/10 liquid); recipe_research/facility_capex.md s1, s2.1",
    "CAPEX_OUT": "Items outside hard cost as shares of hard cost (land, site, substation, fees, "
                 "contingency): C&W 2026, KPMG 2026, Epoch, Uptime 2008; facility_capex.md s1",
    "EQUIP": "Equipment vs installation: Schneider WP61 (electrical 50-60% equipment), WP218 "
             "(materials 71%), KPMG 2026 owner-furnished split; facility_capex.md s4, power_energy.md s1.4",
    "ELEC_BOM": "Electrical equipment by maker, bottom-up from Schneider unit costs x BLS PPI, "
                "checked against T&T and Eaton; power_energy.md s1.2, s1.4, s6",
    "MECH_SPLIT": "Mechanical equipment by maker: UNSOURCED assumption (70/10/10/10), open gap",
    "LIVES": "Service lives: BEA office buildings (delta 0.0247); plant delta = 1.65/L with L = "
             "18-20 years (ASHRAE, Uptime, filings); operations.md s4",
    "POWER": "Electricity: operating PUE (Google, Meta, AWS, Microsoft; LBNL; Uptime), "
             "utilisation (EPRI, Microsoft, LBNL), delivered price (EIA, tariffs); power_energy.md s3-4",
    "OPEX": "Facility operating lines per MW-IT-year: KPMG 2026, Epoch 1 GW TCO, Digital Realty "
            "10-K, Virginia JLARC 2024, Uptime; operations.md table 0",
    "WATER": "Water: LBNL 2024 WUE by cooling technology, operator WUE, $6/kgal; operations.md s1",
    "OPEX_MAP": "Mapping of software/IT (60% Info, 40% Prof_Tech) and 'other' (50% Petroleum for "
                "generator fuel, 50% Admin): assumption",
    "IT_CAPEX": "IT capex per MW IT and composition: SemiAnalysis (GB200 architecture, AI cloud "
                "TCO), Epoch 1 GW, Cottier et al. 2025, CNT 2026, VN 2026; it_equipment.md s0, s3, s9",
    "IT_DELTA": "IT depreciation by component: 31 SEC filings, GPU rent indices (vintage "
                "gradient 0.27), resale profiles, Epoch price-performance; it_equipment.md s6, "
                "gpu_rental.md, sec_useful_lives.md, gpu_failure_priceperf.md",
    "IT_MARGINS": "Trade margins on hyperscale IT purchases: BEA 2017 PEQ bridge vs direct "
                  "purchase from ODMs and distributor margins; it_equipment.md s7, s11",
    "Z_OPEX": "Compute-layer operating inputs as shares of cost: CoreWeave 10-K FY2025, Nebius "
              "20-F, IREN, Census SAS 518, BEA 2017 use table; it_equipment.md s8",
}

# ---- NAICS -> model sector (VLW 37 names used in model.py) ----
SECTOR = {
    "2332A0": "Construction", "238210": "Construction", "238220": "Construction",
    "230301": "Construction", "335311": "Electrical", "335312": "Electrical",
    "335313": "Electrical", "335314": "Electrical", "335911": "Electrical",
    "335929": "Electrical", "335999": "Electrical", "333415": "Machinery",
    "333914": "Machinery", "333413": "Machinery", "332996": "Fabricated_Metals",
    "541330": "Prof_Tech", "541512": "Prof_Tech", "5415": "Prof_Tech", "5416": "Prof_Tech",
    "334111": "Computers", "334112": "Computers", "334210": "Computers",
    "423430": "Wholesale_Trade", "48-49": "Transp_and_Wareh", "221100": "Utilities",
    "221300": "Utilities", "561600": "Admin", "561700": "Admin", "5616": "Admin",
    "524": "Finance", "517": "Info", "5132": "Info", "811": "Other", "324110": "Petroleum",
}
DESC = {
    "2332A0": "Commercial structures (shell, core, contractor fees, site works)",
    "238210": "Electrical installation", "238220": "Mechanical installation",
    "230301": "Nonresidential maintenance and repair", "335311": "Transformers",
    "335312": "Generators (gensets)", "335313": "Switchgear, switchboards, busway",
    "335314": "Controls", "335911": "Batteries", "335929": "Cable and wire",
    "335999": "UPS, PDUs, misc. electrical", "333415": "HVAC, chillers, CRAH, CDU",
    "333914": "Pumps", "333413": "Fans", "332996": "Fabricated pipe and manifolds",
    "541330": "Engineering, design, commissioning", "541512": "Systems integration",
    "5415": "Computer services", "5416": "Management and admin services",
    "334111": "Computers (servers)", "334112": "Storage devices",
    "334210": "Communications equipment (switches, routers)", "423430": "Wholesale margin",
    "48-49": "Transport margin", "221100": "Electricity", "221300": "Water and sewer",
    "561600": "Security services", "561700": "Cleaning and building services",
    "5616": "Security and support services", "524": "Insurance", "517": "Telecommunications",
    "5132": "Software", "811": "Repair and maintenance", "324110": "Fuel",
}

# ---- facility, per MW of IT load (capex $m; operating lines $k per year) ----
FAC = {
    #        hard   elec  mech  shell  gc    plant delta   u     PUE   $/MWh
    "A0": dict(hard=9.0, elec=0.45, mech=0.25, shell=0.20, gc=0.10, d_plant=0.090,
               u=0.50, pue=1.70, price=110,
               opex=dict(payroll=400, maint=150, security=150, cleaning=40, insurance=10,
                         proptax=80, software=100, other=40, water=26)),
    "A1": dict(hard=9.8, elec=0.54, mech=0.22, shell=0.14, gc=0.10, d_plant=0.090,
               u=0.65, pue=1.15, price=75,
               opex=dict(payroll=133, maint=70, security=43, cleaning=13, insurance=10,
                         proptax=50, software=60, other=25, water=4)),
    "A2": dict(hard=10.6, elec=0.52, mech=0.25, shell=0.12, gc=0.10, d_plant=0.085,
               u=0.70, pue=1.25, price=80,
               opex=dict(payroll=90, maint=100, security=30, cleaning=7, insurance=12,
                         proptax=70, software=50, other=25, water=7)),
    "A3": dict(hard=12.0, elec=0.48, mech=0.33, shell=0.09, gc=0.10, d_plant=0.088,
               u=0.75, pue=1.15, price=85,
               opex=dict(payroll=60, maint=120, security=20, cleaning=5, insurance=15,
                         proptax=80, software=50, other=30, water=0.6)),
    "A4": dict(hard=14.5, elec=0.50, mech=0.325, shell=0.08, gc=0.095, d_plant=0.090,
               u=0.80, pue=1.10, price=85,
               opex=dict(payroll=40, maint=150, security=15, cleaning=3, insurance=20,
                         proptax=95, software=55, other=30, water=0.2)),
}
FAC_SRC = dict(hard="TT", elec="TT", mech="TT", shell="TT", gc="TT", d_plant="LIVES",
               u="POWER", pue="POWER", price="POWER", opex="OPEX")
# Outside the hard cost, as shares of hard cost (A3 anchors: 0.6/0.3/0.9/0.6/0.6 on 12).
OUT = dict(site=0.05, substation=0.025, fees=0.075, contingency=0.05, land=0.05)
EQ_ELEC, EQ_MECH = 0.60, 0.65                       # equipment share (EQUIP)
D_SHELL = 0.0247                                    # BEA office buildings (LIVES)
ELEC_SPLIT = {                                      # share of electrical equipment (ELEC_BOM)
    "air": {"335312": 0.31, "335999": 0.21, "335313": 0.22, "335311": 0.08, "335929": 0.07,
            "335911": 0.05, "335314": 0.06},
    "liquid": {"335312": 0.29, "335999": 0.22, "335313": 0.22, "335311": 0.09, "335929": 0.07,
               "335911": 0.06, "335314": 0.05},
}
ELEC_KIND = {"A0": "air", "A1": "air", "A2": "air", "A3": "liquid", "A4": "liquid"}
MECH_SPLIT = {"333415": 0.70, "333914": 0.10, "333413": 0.10, "332996": 0.10}   # MECH_SPLIT
OPEX_NAICS = {                                      # facility operating line -> NAICS shares
    "maint": {"230301": 1.0}, "security": {"561600": 1.0}, "cleaning": {"561700": 1.0},
    "insurance": {"524": 1.0}, "software": {"517": 0.6, "5415": 0.4},        # OPEX_MAP
    "other": {"324110": 0.5, "5616": 0.5}, "water": {"221300": 1.0},         # OPEX_MAP
}

# ---- IT, per MW of IT load ($m) ----
IT = {
    #          capex  network storage integ  delta of compute systems
    "A0": dict(capex=15.0, net=0.15, sto=0.15, integ=0.03, d_comp=0.30),
    "A1": dict(capex=15.0, net=0.15, sto=0.15, integ=0.03, d_comp=0.30),
    "A2": dict(capex=24.0, net=0.15, sto=0.04, integ=0.03, d_comp=0.27),
    "A3": dict(capex=27.0, net=0.14, sto=0.04, integ=0.03, d_comp=0.27),
    "A3_GB300": dict(capex=37.0, net=0.13, sto=0.04, integ=0.03, d_comp=0.27),
    "A4": dict(capex=50.0, net=0.12, sto=0.08, integ=0.03, d_comp=0.27),
}
D_NET, D_STO = 0.20, 0.30                           # IT_DELTA
WHOLESALE, TRANSPORT = 0.06, 0.01                   # share of IT capex (IT_MARGINS)
# Compute layer's operating inputs, shares of its cost (Z_OPEX). Labour here is the cloud
# operator's staff; the labs' labour is added separately (KM).
Z_OPEX = {"5132": 0.02, "517": 0.01, "811": 0.0075, "334111": 0.0075, "541512": 0.0,
          "5416": 0.0125, "5616": 0.0125}
Z_LABOUR, Z_TAX = 0.09, 0.01
SERVICES_OVER_INFERENCE, LABS_OVER_INFERENCE = 1.5, 0.10   # KM


def facility(gen):
    """Per MW of IT: produced capex by NAICS ($m), delta, and annual lines ($m)."""
    p = FAC[gen]
    h = p["hard"]
    el, me, sh, gc = (p[k] * h for k in ("elec", "mech", "shell", "gc"))
    site, sub, fees, cont, land = (OUT[k] * h for k in ("site", "substation", "fees",
                                                         "contingency", "land"))
    cap = {"2332A0": sh + gc + site + 0.5 * sub, "238210": (1 - EQ_ELEC) * el,
           "238220": (1 - EQ_MECH) * me, "541330": fees}
    for k, s in ELEC_SPLIT[ELEC_KIND[gen]].items():
        cap[k] = cap.get(k, 0) + s * EQ_ELEC * el
    for k, s in {"335311": 0.5, "335313": 0.5}.items():          # substation equipment
        cap[k] += s * 0.5 * sub
    for k, s in MECH_SPLIT.items():
        cap[k] = cap.get(k, 0) + s * EQ_MECH * me
    base = sum(cap.values())
    cap = {k: v * (base + cont) / base for k, v in cap.items()}   # contingency pro rata
    long_lived = sh + site + 0.5 * sub
    plant = el + me + 0.5 * sub
    w = long_lived / (long_lived + plant)
    delta = w * D_SHELL + (1 - w) * p["d_plant"]
    K = sum(cap.values())
    mwh = 8760 * p["u"] * p["pue"]
    ann = {"electricity": mwh * p["price"] / 1e6}                 # $m per MW-year
    ann.update({k: v / 1000 for k, v in p["opex"].items()})
    return dict(cap=cap, K=K, delta=delta, land=land, ann=ann, mwh=mwh, hard=h,
                allin=h + site + sub + fees + cont + land)


def it(gen):
    """Per MW of IT: capex by NAICS at producers' value plus margins ($m), and delta."""
    p = IT[gen]
    comp = 1 - p["net"] - p["sto"] - p["integ"]
    goods = comp + p["net"] + p["sto"]
    prod = goods - WHOLESALE - TRANSPORT                          # goods at producers' value
    cap = {"334111": comp / goods * prod, "334112": p["sto"] / goods * prod,
           "334210": p["net"] / goods * prod, "541512": p["integ"],
           "423430": WHOLESALE, "48-49": TRANSPORT}
    cap = {k: v * p["capex"] for k, v in cap.items()}
    delta = (comp + p["integ"]) * p["d_comp"] + p["net"] * D_NET + p["sto"] * D_STO
    return dict(cap=cap, K=p["capex"], delta=delta)


def agg(d):
    out = {}
    for k, v in d.items():
        out[SECTOR[k]] = out.get(SECTOR[k], 0) + v
    return out


def normalise(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}


def recipe(generation=BASELINE, delta_it=None, labs_over_inference=LABS_OVER_INFERENCE,
           detail=False):
    """Recipe per $1 of AI services. generation: A0, A1, A2, A3, A3_GB300, A4.
    delta_it overrides the IT depreciation rate (None: the component-weighted rate)."""
    fgen = generation.split("_")[0]
    fa, ti = facility(fgen), it(generation)
    d_it = ti["delta"] if delta_it is None else delta_it
    # --- per MW-IT-year, $m ---
    a = fa["ann"]
    f_kserv = (R + fa["delta"]) * fa["K"]
    f_purch_mw = {"221100": a["electricity"]}
    for line, split in OPEX_NAICS.items():
        for k, s in split.items():
            f_purch_mw[k] = f_purch_mw.get(k, 0) + s * a[line]
    f_go_mw = f_kserv + a["proptax"] + a["payroll"] + sum(f_purch_mw.values())
    it_kserv = (R + d_it) * ti["K"]
    z_other_share = sum(Z_OPEX.values()) + Z_LABOUR + Z_TAX
    compute_mw = (it_kserv + f_go_mw) / (1 - z_other_share)       # compute cost per MW-year
    # --- scale to $1 of AI services ---
    inference = 1 / SERVICES_OVER_INFERENCE
    labs = labs_over_inference * inference
    compute = 1 - labs                                             # inference + training
    sc = compute / compute_mw                                      # MW-years per $1
    z_purch = {"AI_facilities": f_go_mw * sc}
    for k, s in Z_OPEX.items():
        z_purch[SECTOR[k]] = z_purch.get(SECTOR[k], 0) + s * compute
    z_purch = {k: v for k, v in z_purch.items() if v > 0}
    z_cap = it_kserv * sc + Z_TAX * compute
    z = {"GO": 1.0, "labour": labs + Z_LABOUR * compute, "capital_services": z_cap,
         "purchases": z_purch, "delta": d_it, "K": z_cap / (R + d_it),
         "K_physical": ti["K"] * sc, "invcol": normalise(agg(ti["cap"]))}
    f_cap = (f_kserv + a["proptax"]) * sc
    f = {"GO": f_go_mw * sc, "labour": a["payroll"] * sc, "capital_services": f_cap,
         "purchases": {k: v * sc for k, v in agg(f_purch_mw).items()},
         "electricity": a["electricity"] * sc, "delta": fa["delta"],
         "K": f_cap / (R + fa["delta"]), "K_physical": fa["K"] * sc,
         "invcol": normalise(agg(fa["cap"])),
         # the 2026 Bank of Italy rack column, kept for comparison (Config.fac_col)
         "invcol_alt": {"Construction": 1 / 3, "Electrical": 0.4, "Machinery": 4 / 15}}
    checks = {
        "generation": generation, "inference_share": inference, "labs_share": labs,
        "margin_share": 1 - inference - labs,
        "compute_cost_per_MW_year_$m": compute_mw,
        "AI_services_per_MW_year_$m": 1 / sc,
        "it_capex_per_MW_$m": ti["K"], "facility_capex_per_MW_$m": fa["K"],
        "facility_allin_per_MW_$m": fa["allin"], "land_per_MW_$m": fa["land"],
        "it_share_of_capex": ti["K"] / (ti["K"] + fa["K"]),
        "capital_per_dollar": z["K"] + f["K"],
        "electricity_per_dollar": f["electricity"],
        "electricity_share_of_f": a["electricity"] / f_go_mw,
        "water_share_of_electricity": a["water"] / a["electricity"],
        "MWh_per_MW_IT_year": fa["mwh"],
        "z_cost_shares": {"it_capital": it_kserv / compute_mw, "space": f_go_mw / compute_mw,
                          "purchases": sum(Z_OPEX.values()), "labour": Z_LABOUR, "tax": Z_TAX},
        "f_cost_shares": {"capital": f_kserv / f_go_mw, "electricity": a["electricity"] / f_go_mw,
                          "other_purchases": (sum(f_purch_mw.values()) - a["electricity"]) / f_go_mw,
                          "labour": a["payroll"] / f_go_mw, "tax": a["proptax"] / f_go_mw},
    }
    out = {"r": R, "AI_compute": z, "AI_facilities": f, "checks": checks}
    if detail:
        out["detail"] = dict(f_cap=fa["cap"], z_cap=ti["cap"], f_purch_mw=f_purch_mw,
                             f_ann=a, scale=sc, compute=compute, labs=labs)
    return out


def detail_rows(gen):
    rec = recipe(gen, detail=True)
    d = rec["detail"]
    sc, compute = d["scale"], d["compute"]
    f, z = rec["AI_facilities"], rec["AI_compute"]
    rows = []

    def add(sector, block, code, per_mw, unit, per_dollar, src):
        rows.append(dict(generation=gen, sector=sector, block=block, naics=code,
                         description=DESC.get(code, code), model_sector=SECTOR.get(code, code),
                         per_MW=round(per_mw, 5), unit=unit,
                         per_dollar_AI=round(per_dollar, 6), source=src))
    kf, kz = sum(d["f_cap"].values()), sum(d["z_cap"].values())
    for k, v in sorted(d["f_cap"].items()):
        src = ("TT;CAPEX_OUT" if k in ("2332A0", "541330") else "EQUIP;ELEC_BOM"
               if k.startswith("335") else "EQUIP;MECH_SPLIT" if k[:3] in ("333", "332")
               else "EQUIP")
        add("AI_facilities", "investment", k, v, "$m per MW (share of column in per_dollar_AI)",
            v / kf, src)
    for k, v in sorted(d["z_cap"].items()):
        add("AI_compute", "investment", k, v, "$m per MW (share of column in per_dollar_AI)",
            v / kz, "IT_CAPEX;IT_MARGINS")
    for k, v in sorted(d["f_purch_mw"].items()):
        add("AI_facilities", "intermediate", k, v * 1000, "$k per MW-year", v * sc,
            "POWER" if k == "221100" else "WATER" if k == "221300" else "OPEX;OPEX_MAP")
    add("AI_facilities", "labour", "labour", d["f_ann"]["payroll"] * 1000, "$k per MW-year",
        f["labour"], "OPEX")
    add("AI_facilities", "capital_services", "capital", 0, "", f["capital_services"],
        "LIVES;OPEX (incl. property tax)")
    add("AI_compute", "intermediate", "AI_facilities", 0, "", z["purchases"]["AI_facilities"],
        "derived")
    for k, s in Z_OPEX.items():
        if s > 0:
            add("AI_compute", "intermediate", k, 0, "", s * compute, "Z_OPEX")
    add("AI_compute", "labour", "labour", 0, "", z["labour"], "KM;Z_OPEX")
    add("AI_compute", "capital_services", "capital", 0, "", z["capital_services"],
        "IT_DELTA;Z_OPEX (incl. property tax)")
    return rows


def main():
    rec = recipe()
    (DERIVED / "ai_recipe.json").write_text(json.dumps(
        {**rec, "sources": SOURCES}, indent=2, default=float))
    rows = [r for g in ("A0", "A1", "A2", "A3", "A3_GB300", "A4") for r in detail_rows(g)]
    with open(DERIVED / "ai_recipe_detail.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    # --- comparison across generations and with the 2026 recipe ---
    from ai_recipe_cnt2026 import recipe as old
    o = old()
    gens = ("A0", "A1", "A2", "A3", "A3_GB300", "A4")
    recs = {g: recipe(g) for g in gens}

    def line(label, fn, fmt="{:.3f}", old_val=None):
        vals = [fmt.format(fn(recs[g])) for g in gens]
        ov = "" if old_val is None else fmt.format(old_val)
        print(f"{label:42s}" + "".join(f"{v:>10s}" for v in vals) + f"{ov:>10s}")
    print(f"{'Per $1 of AI services':42s}" + "".join(f"{g:>10s}" for g in gens) + f"{'2026':>10s}")
    Z, F = (lambda r: r["AI_compute"]), (lambda r: r["AI_facilities"])
    line("z: labour (labs + cloud staff)", lambda r: Z(r)["labour"], old_val=o["AI_compute"]["labour"])
    line("z: capital services", lambda r: Z(r)["capital_services"], old_val=o["AI_compute"]["capital_services"])
    line("z: space from f", lambda r: Z(r)["purchases"]["AI_facilities"],
         old_val=o["AI_compute"]["purchases"]["AI_facilities"])
    line("z: other purchases", lambda r: sum(v for k, v in Z(r)["purchases"].items()
                                              if k != "AI_facilities"), old_val=0.0)
    line("f: electricity", lambda r: F(r)["electricity"], old_val=o["AI_facilities"]["purchases"]["Utilities"])
    line("f: other purchases", lambda r: sum(F(r)["purchases"].values()) - F(r)["electricity"],
         old_val=sum(o["AI_facilities"]["purchases"].values()) - o["AI_facilities"]["purchases"]["Utilities"])
    line("f: labour", lambda r: F(r)["labour"], old_val=o["AI_facilities"]["labour"])
    line("f: capital services", lambda r: F(r)["capital_services"], old_val=o["AI_facilities"]["capital_services"])
    line("K_IT per $1", lambda r: Z(r)["K"], "{:.2f}", o["AI_compute"]["K"])
    line("K_facilities per $1", lambda r: F(r)["K"], "{:.2f}", o["AI_facilities"]["K"])
    line("delta IT", lambda r: Z(r)["delta"], old_val=o["AI_compute"]["delta"])
    line("delta facilities", lambda r: F(r)["delta"], old_val=o["AI_facilities"]["delta"])
    line("IT share of capex", lambda r: r["checks"]["it_share_of_capex"], "{:.2f}",
         o["checks"]["it_share_of_capital"])
    line("electricity share of f", lambda r: r["checks"]["electricity_share_of_f"], "{:.2f}")
    line("water / electricity", lambda r: r["checks"]["water_share_of_electricity"], "{:.3f}")
    line("AI services per MW-year, $m", lambda r: r["checks"]["AI_services_per_MW_year_$m"], "{:.1f}")
    for sec in ("Construction", "Electrical", "Machinery", "Prof_Tech"):
        line(f"f investment: {sec}", lambda r, s=sec: F(r)["invcol"].get(s, 0), "{:.2f}",
             o["AI_facilities"]["invcol"].get(sec, 0))
    for sec in ("Computers", "Prof_Tech", "Wholesale_Trade"):
        line(f"z investment: {sec}", lambda r, s=sec: Z(r)["invcol"].get(s, 0), "{:.2f}",
             o["AI_compute"]["invcol"].get(sec, 0))
    print(f"\nWrote ai_recipe.json (baseline {BASELINE}) and ai_recipe_detail.csv ({len(rows)} rows).")


if __name__ == "__main__":
    main()
