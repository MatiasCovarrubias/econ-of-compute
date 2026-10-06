#!/usr/bin/env python3
"""The recipe of the two AI sectors, per $1 of AI services, from modern sources.

The AI sectors are new: they do not exist in the 2017 base, and nothing is carved
out of other sectors. Their recipes come from 2024-26 sources, not from the 2018
Stage 1 node (which was cloud generally, carved from Info and Real estate).

AI_compute (z) sells AI services. Per $1 of sales:
  - inference compute 1/1.5 and labs' labour 0.1 x inference compute
    (Korinek and McKelvey 2026, App. eq. 23); the rest is the margin;
  - closure: in a steady state the margin pays for training compute (a frontier
    model is obsolete in about a year, so the return to model capital is close
    to training spending). Total compute = inference + margin.
  - compute is split into IT capital services (owned by z) and powered space
    rented from AI_facilities (f), using the Bank of Italy NVL72 rack
    (Carpinelli, Natoli and Taboga 2026, Tables A1-A3) and the model's user costs.
AI_facilities (f) owns the shell and the power and cooling plant, buys
electricity, and has other operating costs.

Writes data_construction/ai_recipe_cnt2026.json. Superseded on 28 Sep 2026 by ai_recipe.py (engineering recipe by generation); kept to reproduce earlier results.

Run: uv run python data_construction/ai_recipe.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---- sources ----
BETA = 0.96
R = 1 / BETA - 1                      # RbcProdNet
SERVICES_OVER_INFERENCE = 1.5         # Korinek-McKelvey, services revenue / inference compute
LABS_OVER_INFERENCE = 0.10            # Korinek-McKelvey, labs' labour / inference compute
RACK_CAPEX = 4.5                      # $m, NVL72 rack (Bank of Italy)
RACK_SHARES = {"server": 0.67, "land": 0.03, "building": 0.05, "electrical": 0.12,
               "cooling": 0.08, "other": 0.05}
RACK_OPEX = 0.19                      # $m a year (Bank of Italy)
RACK_ELEC = 0.105                     # $m a year, of which electricity (Bank of Italy)
DELTA_IT = 0.25                       # between a 6-year (Van Nieuwerburgh) and a 3-year life
DELTA_SHELL, DELTA_PLANT = 0.025, 0.10  # exercise_design.tex
OPEX_SPLIT = {"labour": 0.5, "Admin": 0.25, "Prof_Tech": 0.25}  # assumption, unsourced
# IT investment: BEA 2017 PEQ bridge, computers and peripherals (334111, 334112, 334118),
# producers' value and transport and wholesale margins; retail and design services left out.
PEQ_IT = {"Computers": 31369 + 3230 + 9557, "Wholesale_Trade": 8736 + 900 + 2662,
          "Transp_and_Wareh": 309 + 32 + 91}
# Facilities investment: the rack's non-server, non-land capex. Building and other go to
# Construction, electrical to Electrical, cooling to Machinery.
FAC_COL = {"Construction": RACK_SHARES["building"] + RACK_SHARES["other"],
           "Electrical": RACK_SHARES["electrical"], "Machinery": RACK_SHARES["cooling"]}
FAC_COL_ALT = {"Construction": 0.54, "Electrical": 0.32, "Machinery": 0.14}  # illustrative


def normalise(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}


def recipe(delta_it=DELTA_IT, labs_over_inference=LABS_OVER_INFERENCE):
    inference = 1 / SERVICES_OVER_INFERENCE
    labs = labs_over_inference * inference
    compute = 1 - labs                               # inference + training (= margin)

    it_capex = RACK_SHARES["server"] * RACK_CAPEX
    shell = (RACK_SHARES["building"] + RACK_SHARES["other"]) * RACK_CAPEX
    plant = (RACK_SHARES["electrical"] + RACK_SHARES["cooling"]) * RACK_CAPEX
    fac_capex = shell + plant                        # land is not produced
    delta_f = (shell * DELTA_SHELL + plant * DELTA_PLANT) / fac_capex
    cost = {"it_capital": (R + delta_it) * it_capex,
            "fac_capital": (R + delta_f) * fac_capex,
            "electricity": RACK_ELEC,
            "other_opex": RACK_OPEX - RACK_ELEC}
    total = sum(cost.values())
    share = {k: v / total for k, v in cost.items()}

    it_serv = compute * share["it_capital"]
    rent = compute * (1 - share["it_capital"])
    fac_serv = compute * share["fac_capital"]
    elec = compute * share["electricity"]
    opex = compute * share["other_opex"]
    z = {"GO": 1.0, "labour": labs, "capital_services": it_serv,
         "purchases": {"AI_facilities": rent},
         "delta": delta_it, "K": it_serv / (R + delta_it),
         "invcol": normalise(PEQ_IT)}
    f = {"GO": rent, "labour": opex * OPEX_SPLIT["labour"], "capital_services": fac_serv,
         "purchases": {"Utilities": elec, "Admin": opex * OPEX_SPLIT["Admin"],
                       "Prof_Tech": opex * OPEX_SPLIT["Prof_Tech"]},
         "delta": delta_f, "K": fac_serv / (R + delta_f),
         "invcol": normalise(FAC_COL), "invcol_alt": normalise(FAC_COL_ALT)}
    checks = {"inference_share": inference, "margin_share": 1 - inference - labs,
              "training_share_of_compute": (1 - inference - labs) / compute,
              "compute_cost_shares": share,
              "electricity_per_dollar": elec,
              "capital_per_dollar": z["K"] + f["K"],
              "it_share_of_capital": z["K"] / (z["K"] + f["K"]),
              "z_capital_share_of_VA": it_serv / (1 - rent),
              "f_capital_share_of_VA": fac_serv / (rent - elec - opex * (1 - OPEX_SPLIT["labour"]))}
    return {"r": R, "AI_compute": z, "AI_facilities": f, "checks": checks}


def main():
    rec = recipe()
    (HERE / "ai_recipe_cnt2026.json").write_text(json.dumps(rec, indent=2))
    z, f, c = rec["AI_compute"], rec["AI_facilities"], rec["checks"]
    print("Per $1 of AI services:")
    print(f"  AI_compute:    labs' labour {z['labour']:.3f}, IT capital services "
          f"{z['capital_services']:.3f}, powered space {z['purchases']['AI_facilities']:.3f}; "
          f"K_IT {z['K']:.2f} (delta {z['delta']:.2f})")
    print(f"  AI_facilities: output {f['GO']:.3f}; capital services {f['capital_services']:.3f}, "
          f"electricity {f['purchases']['Utilities']:.3f}, labour {f['labour']:.3f}, "
          f"services {f['purchases']['Admin'] + f['purchases']['Prof_Tech']:.3f}; "
          f"K_fac {f['K']:.2f} (delta {f['delta']:.3f})")
    print("  checks:", {k: (round(v, 3) if isinstance(v, float) else
                         {a: round(b, 3) for a, b in v.items()}) for k, v in c.items()})
    print("  IT investment column:", {k: round(v, 3) for k, v in z["invcol"].items()})
    print("  facilities investment column:", {k: round(v, 3) for k, v in f["invcol"].items()})
    for d in [0.20, 0.33]:
        alt = recipe(delta_it=d)
        print(f"  delta_IT = {d}: capital per $1 {alt['checks']['capital_per_dollar']:.2f}, "
              f"electricity per $1 {alt['checks']['electricity_per_dollar']:.3f}")
    alt = recipe(labs_over_inference=0.25 / (1 / 1.5))
    print(f"  labs' labour at 25% of revenue (Bekkers et al.): capital per $1 "
          f"{alt['checks']['capital_per_dollar']:.2f}")


if __name__ == "__main__":
    main()
