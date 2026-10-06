#!/usr/bin/env python3
"""Yearly cost build-up of DC_facilities and Compute.

GO = (r+δ)K + electricity + other intermediates + labour, no residual.
Electricity is LBNL TWh × hyperscale-and-colo share × 8.5¢/kWh.
Facility other-M and labour are ratios to the power bill; Compute other-M
and labour are shares of Compute GO. Powered space (the whole facilities
GO) is Compute's main intermediate.

Run alone:
    python3 code/cost_buildup.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from facilities_stock import c30_annual_m, facility_stock, office_price_index
from it_stock import it_stock
from stage1_assumptions import (
    COMPUTE_L_SHARE,
    COMPUTE_OTHER_M_SHARE,
    DELTA_IT,
    DELTA_PLANT,
    DELTA_SHELL,
    DELTA_SOFT,
    ELEC_PRICE_PER_KWH,
    FACILITY_L_OVER_ELEC,
    FACILITY_OTHER_M_OVER_ELEC,
    LBNL_TWH,
    NODE_ENERGY_SHARE,
    R,
)

REPORT_YEARS = (2018, 2022, 2023, 2024)


def electricity_bill(year: int, price: float = ELEC_PRICE_PER_KWH) -> dict[str, float]:
    if year not in LBNL_TWH or year not in NODE_ENERGY_SHARE:
        raise KeyError(f"no LBNL TWh / node share for {year}")
    twh = LBNL_TWH[year]
    share = NODE_ENERGY_SHARE[year]
    return {
        "TWh_all": twh,
        "share": share,
        "TWh_node": twh * share,
        "price": price,
        "elec": twh * share * price * 1000.0,
    }


def node_costs(
    year: int,
    fac_row: dict[str, float],
    it_row: dict[str, float],
    *,
    price: float = ELEC_PRICE_PER_KWH,
) -> dict[str, float]:
    bill = electricity_bill(year, price)
    k_shell, k_plant = fac_row["K_shell"], fac_row["K_plant"]
    k_it, k_soft = it_row["K_IT"], it_row["K_soft"]
    elec = bill["elec"]

    gos_f = (R + DELTA_SHELL) * k_shell + (R + DELTA_PLANT) * k_plant
    other_m_f = FACILITY_OTHER_M_OVER_ELEC * elec
    l_f = FACILITY_L_OVER_ELEC * elec
    go_f = gos_f + elec + other_m_f + l_f
    va_f = gos_f + l_f

    gos_c = (R + DELTA_IT) * k_it + (R + DELTA_SOFT) * k_soft
    go_c = (gos_c + go_f) / (1.0 - COMPUTE_OTHER_M_SHARE - COMPUTE_L_SHARE)
    other_m_c = COMPUTE_OTHER_M_SHARE * go_c
    l_c = COMPUTE_L_SHARE * go_c
    va_c = gos_c + l_c

    out = {
        "K_shell": k_shell,
        "K_plant": k_plant,
        "K_fac": k_shell + k_plant,
        "K_IT": k_it,
        "K_soft": k_soft,
        "GOS_fac": gos_f,
        "elec": elec,
        "other_M_fac": other_m_f,
        "L_fac": l_f,
        "GO_fac": go_f,
        "VA_fac": va_f,
        "GOS_cmp": gos_c,
        "other_M_cmp": other_m_c,
        "L_cmp": l_c,
        "GO_cmp": go_c,
        "VA_cmp": va_c,
        "I_fac": fac_row["I_ss"],
        "I_IT": DELTA_IT * k_it,
        "I_soft": DELTA_SOFT * k_soft,
        "delta_fac": fac_row["delta"],
        "delta_cmp": (DELTA_IT * k_it + DELTA_SOFT * k_soft) / (k_it + k_soft),
        "capsh_fac": gos_f / va_f,
        "capsh_cmp": gos_c / va_c,
    }
    out.update(bill)
    return out


def main() -> int:
    fac = facility_stock(c30_annual_m(), office_price_index())
    it = it_stock()
    years = [y for y in REPORT_YEARS if y in fac and y in it]
    rows = {y: node_costs(y, fac[y], it[y]) for y in years}

    print("Cost build-up ($bn, current). Electricity = LBNL TWh × node share × 8.5¢")
    hdr = f"{'':22}" + "".join(f"{y:>9}" for y in years)
    print(hdr)
    keys = (
        ("TWh_all", "LBNL TWh (all DC)", 1.0),
        ("share", "node energy share", 1.0),
        ("elec", "electricity $bn", 0.001),
        ("K_fac", "K_fac", 0.001),
        ("GOS_fac", "return on K_fac", 0.001),
        ("other_M_fac", "other M facilities", 0.001),
        ("L_fac", "labour facilities", 0.001),
        ("GO_fac", "GO facilities", 0.001),
        ("VA_fac", "VA facilities", 0.001),
        ("K_IT", "K_IT", 0.001),
        ("GOS_cmp", "return on IT", 0.001),
        ("other_M_cmp", "other M Compute", 0.001),
        ("L_cmp", "labour Compute", 0.001),
        ("GO_cmp", "GO Compute", 0.001),
        ("VA_cmp", "VA Compute", 0.001),
    )
    for key, lab, scale in keys:
        if key == "share":
            print(f"{lab:22}" + "".join(f"{rows[y][key]:9.2f}" for y in years))
        elif key == "TWh_all":
            print(f"{lab:22}" + "".join(f"{rows[y][key]:9.1f}" for y in years))
        else:
            print(f"{lab:22}" + "".join(f"{rows[y][key]*scale:9.2f}" for y in years))

    print("\nFacility shares of GO (notes target: K 55–65, E 25–30, M ~10, L ~5)")
    print(f"{'':22}" + "".join(f"{y:>9}" for y in years))
    for lab, fn in (
        ("capital", lambda r: r["GOS_fac"] / r["GO_fac"]),
        ("electricity", lambda r: r["elec"] / r["GO_fac"]),
        ("other M", lambda r: r["other_M_fac"] / r["GO_fac"]),
        ("labour", lambda r: r["L_fac"] / r["GO_fac"]),
    ):
        print(f"{lab:22}" + "".join(f"{fn(rows[y]):9.2f}" for y in years))

    print("\nAll-in shares of Compute GO (notes target: K 75–85, E 7–10, M 5–8, L 3–5)")
    print(f"{'':22}" + "".join(f"{y:>9}" for y in years))
    for lab, fn in (
        ("capital", lambda r: (r["GOS_fac"] + r["GOS_cmp"]) / r["GO_cmp"]),
        ("electricity", lambda r: r["elec"] / r["GO_cmp"]),
        ("other M", lambda r: (r["other_M_fac"] + r["other_M_cmp"]) / r["GO_cmp"]),
        ("labour", lambda r: (r["L_fac"] + r["L_cmp"]) / r["GO_cmp"]),
    ):
        print(f"{lab:22}" + "".join(f"{fn(rows[y]):9.2f}" for y in years))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
