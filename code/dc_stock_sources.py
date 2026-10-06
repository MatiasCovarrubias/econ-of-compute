#!/usr/bin/env python3
"""Rebuild DC facility-stock sources from the September 2025 BEA vintage.

Prints Tables A–B and the C30 PIM grid to stdout; writes
notes/us-national-accounts/figures/dc_stock_sources.pdf.

Run from the repo root:
    python3 code/dc_stock_sources.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/dcfa/mpl")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
BEA = RAW / "bea_2024"
STK_XLSX = BEA / "detailnonres_stk1.xlsx"
INV_XLSX = BEA / "detailnonres_inv1.xlsx"
C30_XLSX = RAW / "privsatime.xlsx"
NIPA_XLSX = BEA / "NIPA_Section5All_xls.xlsx"
FIG_PATH = ROOT / "notes" / "us-national-accounts" / "figures" / "dc_stock_sources.pdf"

YEARS_A = [2005, 2010, 2014, 2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
YEARS_FIG = list(range(2014, 2025))
YEARS_INV = list(range(2010, 2025))
YEARS_C30 = list(range(2014, 2026))
YEARS_PIM = [2018, 2020, 2022, 2024, 2025]
DELTAS = (0.03, 0.085)
GS = (0.05, 0.10, 0.20, 0.40)
SERVER_CODES = ("EP1A", "EP1G", "EP1H")

# Named structure types shown in the tables; residual is Total minus these.
STRUCT_TYPES = [
    ("SOO1", "Office"),
    ("SU20", "Communication"),
    ("SI00", "Manufacturing"),
    ("SU30", "Electric"),
    ("SB20", "Educational"),
    ("SC02", "Other commercial"),
    ("SC01", "Warehouses"),
]


def _num(v):
    if v is None or v == "" or v == ".....":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _to_bn(v):
    if v is None:
        return None
    return v / 1000.0


def load_bea_detail(path: Path, sheet: str) -> dict:
    """Industry sheet: header years on row 6 (index 5), data from row 8."""
    wb = load_workbook(path, read_only=True, data_only=True)
    ws = wb[sheet]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    header = rows[5]
    year_cols = {}
    for j, v in enumerate(header):
        if j < 2 or v is None:
            continue
        try:
            year_cols[int(v)] = j
        except (TypeError, ValueError):
            continue
    out = {}
    for r in rows[7:]:
        if not r or r[0] is None:
            continue
        code = str(r[0]).strip()
        name = str(r[1]).strip() if r[1] else ""
        vals = {}
        for y, j in year_cols.items():
            if j < len(r):
                vals[y] = _num(r[j])
        out[code] = {"name": name, "values": vals}
    return out


def series_bn(block: dict, code: str, years) -> dict:
    vals = block[code]["values"]
    return {y: _to_bn(vals.get(y)) for y in years}


def sum_codes_bn(block: dict, codes, years) -> dict:
    out = {}
    for y in years:
        parts = [_to_bn(block[c]["values"].get(y)) for c in codes]
        out[y] = None if any(p is None for p in parts) else sum(parts)
    return out


def load_c30_annual_bn() -> dict:
    """Monthly SAAR $m, column header contains 'Data center'. Annual = mean."""
    wb = load_workbook(C30_XLSX, read_only=True, data_only=True)
    ws = wb["Private SA"]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    header = rows[3]
    dc_col = next(j for j, h in enumerate(header) if h and "Data center" in str(h))
    pat = re.compile(r"^([A-Za-z]{3})-(\d{2})[pr]?$")
    by_year = defaultdict(list)
    for r in rows[4:]:
        if not r or r[0] is None:
            continue
        m = pat.match(str(r[0]).strip())
        if not m:
            continue
        year = 2000 + int(m.group(2))
        val = _num(r[dc_col])
        if val is not None:
            by_year[year].append(val)
    annual = {}
    for y in YEARS_C30:
        months = by_year.get(y, [])
        if len(months) != 12:
            raise RuntimeError(f"C30 year {y} has {len(months)} months, need 12")
        annual[y] = float(np.mean(months)) / 1000.0
    return annual


def load_price_index() -> tuple[dict, str]:
    """Office (NIPA 5.4.4 line 4); 2025 spliced with 5.3.4 Commercial and health care."""
    wb = load_workbook(NIPA_XLSX, read_only=True, data_only=True)

    def _read(sheet, pred):
        ws = wb[sheet]
        rows = list(ws.iter_rows(values_only=True))
        header = rows[7]
        year_cols = {}
        for j, v in enumerate(header):
            try:
                year_cols[int(v)] = j
            except (TypeError, ValueError):
                continue
        for r in rows[8:]:
            line = str(r[0]).strip() if r[0] else ""
            name = str(r[1]).strip() if r[1] else ""
            code = str(r[2]).strip() if len(r) > 2 and r[2] else ""
            if pred(line, name, code):
                vals = {y: _num(r[j]) for y, j in year_cols.items() if j < len(r)}
                return name.replace("\\1\\", "").replace("\\8\\", ""), line, code, vals
        return None

    office = _read("T50404-A", lambda l, n, c: l == "4" and n.strip() == "Office")
    comm = _read(
        "T50304-A",
        lambda l, n, c: "Commercial and health care" in n,
    )
    wb.close()
    if office is None or comm is None:
        raise RuntimeError("Could not find Office / Commercial and health care price indexes")
    _, _, office_code, office_vals = office
    _, _, comm_code, comm_vals = comm
    p = {y: office_vals[y] for y in range(2014, 2025)}
    if comm_vals.get(2024) and comm_vals.get(2025) and p[2024]:
        p[2025] = p[2024] * comm_vals[2025] / comm_vals[2024]
    used = (
        "NIPA Table 5.4.4 line 4 Office (W031RG, 2017=100), 2014–2024; "
        f"2025 spliced with Table 5.3.4 line 4 Commercial and health care "
        f"({comm_code}) growth {comm_vals[2024]:.3f}→{comm_vals[2025]:.3f}"
    )
    return p, used


def pim_end_year(i_flow: dict, delta: float, g, years_out, prices=None) -> dict:
    """K_t = (1-δ)K_{t-1} + I_t. Presample K_2013 = I_2014/(δ+g) or 0.

    If `prices` is given (2017=100), flows are deflated, the stock is accumulated
    in constant dollars, then each year is revalued to current cost by P_t/100.
    """
    i_use = {}
    for y, v in i_flow.items():
        if prices is None:
            i_use[y] = v
        else:
            i_use[y] = v * 100.0 / prices[y]
    i2014 = i_use[2014]
    if g is None:
        k = 0.0
    else:
        k = i2014 / (delta + g)
    stock = {}
    for y in YEARS_C30:
        k = (1.0 - delta) * k + i_use[y]
        if prices is None:
            stock[y] = k
        else:
            stock[y] = k * prices[y] / 100.0
    return {y: stock[y] for y in years_out}


def fmt(v, nd=1):
    if v is None:
        return ""
    return f"{v:.{nd}f}"


def print_wide(title, rows, years, nd=1):
    print(title)
    header = "| | " + " | ".join(str(y) for y in years) + " |"
    sep = "| --- | " + " | ".join("---" for _ in years) + " |"
    print(header)
    print(sep)
    for name, series in rows:
        cells = " | ".join(fmt(series.get(y), nd) for y in years)
        print(f"| {name} | {cells} |")
    print()


def build_tables(stk5140, stk5110, stk5310, inv5140, c30, prices):
    struct_5140 = series_bn(stk5140, "STRUCTURES", YEARS_A)
    office_5140 = series_bn(stk5140, "SOO1", YEARS_A)
    type_rows = []
    named_sum = {y: 0.0 for y in YEARS_A}
    for code, label in STRUCT_TYPES:
        s = series_bn(stk5140, code, YEARS_A)
        type_rows.append((label, s))
        for y in YEARS_A:
            named_sum[y] += s[y] or 0.0
    residual = {y: (struct_5140[y] or 0.0) - named_sum[y] for y in YEARS_A}
    servers = sum_codes_bn(stk5140, SERVER_CODES, YEARS_A)
    equip = series_bn(stk5140, "EQUIPMENT", YEARS_A)
    ex_office = {y: (struct_5140[y] or 0.0) - (office_5140[y] or 0.0) for y in YEARS_A}

    print("### Table A. Current-cost net stock, $bn, September 2025 vintage")
    print()
    print_wide(
        "#### Industry 5140",
        [("Total structures", struct_5140)]
        + type_rows
        + [
            ("Other types", residual),
            ("Servers (EP1A+EP1G+EP1H)", servers),
            ("Total equipment", equip),
        ],
        YEARS_A,
    )
    print_wide(
        "#### Industry 5110",
        [
            ("Total structures", series_bn(stk5110, "STRUCTURES", YEARS_A)),
            ("Office", series_bn(stk5110, "SOO1", YEARS_A)),
            ("Manufacturing", series_bn(stk5110, "SI00", YEARS_A)),
        ],
        YEARS_A,
    )
    print_wide(
        "#### Industry 5310",
        [("Communication structures (SU20)", series_bn(stk5310, "SU20", YEARS_A))],
        YEARS_A,
    )

    inv_total = series_bn(inv5140, "STRUCTURES", YEARS_INV)
    inv_rows = [("5140 structures total", inv_total)]
    for code, label in STRUCT_TYPES:
        inv_rows.append((f"5140 {label}", series_bn(inv5140, code, YEARS_INV)))
    c30_inv_years = {y: c30.get(y) for y in YEARS_INV}
    inv_rows.append(("C30 data-center (annual SAAR)", c30_inv_years))
    ratio = {
        y: (inv_total[y] / c30[y]) if y in c30 and c30[y] else None for y in YEARS_INV
    }
    print("### Table B. Industry 5140 structures investment vs C30, $bn")
    print()
    print_wide("", inv_rows, YEARS_INV)
    print_wide("#### Ratio 5140 structures investment / C30", [("Ratio", ratio)], YEARS_INV, nd=2)

    def grid(deflated: bool):
        out = {}
        for d in DELTAS:
            out[d] = {}
            for g in GS:
                out[d][g] = pim_end_year(c30, d, g, YEARS_PIM, prices if deflated else None)
            out[d][None] = pim_end_year(c30, d, None, YEARS_PIM, prices if deflated else None)
        return out

    def print_grid(title, grid_d):
        print(title)
        cols = [f"g={g:.2f}" for g in GS] + ["K_2013=0"]
        print("| | " + " | ".join(cols) + " |")
        print("| --- | " + " | ".join("---" for _ in cols) + " |")
        for d in DELTAS:
            print(f"| δ={d:.3f} | | | | | |")
            for y in YEARS_PIM:
                cells = [fmt(grid_d[d][g][y]) for g in GS] + [fmt(grid_d[d][None][y])]
                print(f"| {y} | " + " | ".join(cells) + " |")
        print()

    print("### Item 3. C30 PIM end-year current-cost stock, $bn")
    print()
    print_grid(
        "#### Deflated (2017$ accumulation, revalued with the Office price index)",
        grid(True),
    )
    print_grid("#### Nominal (undeflated) PIM", grid(False))

    return {
        "struct_5140": series_bn(stk5140, "STRUCTURES", YEARS_FIG),
        "ex_office": {
            y: _to_bn(stk5140["STRUCTURES"]["values"][y])
            - _to_bn(stk5140["SOO1"]["values"][y])
            for y in YEARS_FIG
        },
        "servers": sum_codes_bn(stk5140, SERVER_CODES, YEARS_FIG),
        "c30": c30,
        "prices": prices,
    }


def draw_figure(bundles):
    c30 = bundles["c30"]
    prices = bundles["prices"]
    years_bea = [y for y in YEARS_C30 if y <= 2024]
    pim_03 = pim_end_year(c30, 0.03, 0.10, YEARS_C30, prices)
    pim_085 = pim_end_year(c30, 0.085, 0.10, YEARS_C30, prices)

    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.labelsize": 9,
            "legend.fontsize": 9,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "axes.linewidth": 0.7,
            "pdf.fonttype": 42,
        }
    )
    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    ax.set_yscale("log")

    ax.plot(
        YEARS_C30,
        [pim_03[y] for y in YEARS_C30],
        color="#0072B2",
        lw=1.6,
        label=r"C30 PIM $\delta{=}0.03$, $g{=}0.10$",
    )
    ax.plot(
        YEARS_C30,
        [pim_085[y] for y in YEARS_C30],
        color="#D55E00",
        lw=1.6,
        label=r"C30 PIM $\delta{=}0.085$, $g{=}0.10$",
    )
    ax.plot(
        years_bea,
        [bundles["struct_5140"][y] for y in years_bea],
        color="#000000",
        lw=1.6,
        label="BEA 5140 structures",
    )
    ax.plot(
        years_bea,
        [bundles["ex_office"][y] for y in years_bea],
        color="#009E73",
        lw=1.6,
        label="BEA 5140 ex-office",
    )
    ax.plot(
        years_bea,
        [bundles["servers"][y] for y in years_bea],
        color="#CC79A7",
        lw=1.6,
        ls="--",
        label="BEA 5140 servers",
    )

    fil_x = np.array([2018, 2022, 2024])
    # Listed REITs + hyperscalers + private colocation operators priced at construction cost.
    fil_y = np.array([56.0, 134.0, 224.0])
    fil_lo = fil_y - np.array([44.0, 102.0, 179.0])
    fil_hi = np.array([69.0, 166.0, 269.0]) - fil_y
    ax.errorbar(
        fil_x,
        fil_y,
        yerr=[fil_lo, fil_hi],
        fmt="o",
        color="#E69F00",
        ms=5.5,
        capsize=2.5,
        elinewidth=1.0,
        zorder=5,
        label="Filings",
    )
    inv_y = np.array([35.0, 96.0, 203.0])
    inv_lo = inv_y - np.array([26.0, 78.0, 158.0])
    inv_hi = np.array([44.0, 114.0, 248.0]) - inv_y
    ax.errorbar(
        fil_x,
        inv_y,
        yerr=[inv_lo, inv_hi],
        fmt="s",
        color="#56B4E9",
        ms=5.0,
        capsize=2.5,
        elinewidth=1.0,
        zorder=5,
        label="Inventory",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("$bn, current cost")
    ax.set_xlim(2013.5, 2025.5)
    ax.set_xticks([2014, 2016, 2018, 2020, 2022, 2024, 2025])
    ax.yaxis.set_major_formatter(lambda x, _pos: f"{x:g}")
    ax.grid(True, which="major", ls=":", lw=0.5, alpha=0.65)
    ax.legend(loc="upper left", frameon=True, framealpha=0.92, borderpad=0.35)
    fig.tight_layout()
    FIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_PATH)
    plt.close(fig)


def main():
    stk5140 = load_bea_detail(STK_XLSX, "5140")
    stk5110 = load_bea_detail(STK_XLSX, "5110")
    stk5310 = load_bea_detail(STK_XLSX, "5310")
    inv5140 = load_bea_detail(INV_XLSX, "5140")
    c30 = load_c30_annual_bn()
    prices, price_note = load_price_index()
    print("Price index:", price_note)
    print()
    bundles = build_tables(stk5140, stk5110, stk5310, inv5140, c30, prices)
    draw_figure(bundles)
    print(f"Figure: {FIG_PATH}")


if __name__ == "__main__":
    main()
