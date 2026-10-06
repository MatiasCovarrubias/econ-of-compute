# Stage 1 plan: `DC_facilities` and `Compute`

> **Status 30 Sep 2026: parallel data track.** The news-boom model does not read `calibration_data_dc.mat`. It appends the AI sectors of `data_construction/ai_recipe.py` to the 2017 VLW tables (see `PandP_AGENTS.md`). The instructions below apply to Stage 1 only.

The build is a series for recent years, from the same code each year. Some inputs are static shares; that is intentional. Picking the model's initial steady state is a later choice (working slice: 2022, D1). Do not freeze the series before the October 2026 BEA and fixed-asset release. Finished chapters are written up in the notes. The 17 Sep classification audit is closed; its corrections are D2, D3, and D3b.

Do not start Stage 2 (labs) or Stage 3 (`GPU_servers`). Shock is parked (D9). Ask before changing D1–D6 or D3b.

## Chapters

| # | Chapter | Series | Static on purpose |
|---|---|---|---|
| 1 | Capital stocks. **Done.** | Facility stock, 2014–2025, cumulated from C30 (`facilities_stock.py`, `dc_structures_sizing.tex`). Server stock, 2018–2024, industry 5140 (`it_stock.py`, `dc_it_stock.tex`). Investment each year is `δK`. | Shell 15% / plant 85%. Software 4% of servers. Depreciation rates. |
| 2 | Gross output. **Done.** | 2018–2024 (`cost_buildup.py`, `dc_cost_buildup.tex`). The power bill follows TWh × node share × price. | `r`. Four cost ratios. No plug: GO = `(r+δ)K` + M + L. |
| 3 | Data-center columns. **Done.** | The input column moves with the power bill; water moves with TWh. Investment moves with `δK`. | Investment is all Construction. Leftover inputs: 54% repairs / 46% admin. **The builder still codes 30/40/30.** Note: `dc_facilities_column.tex`. |
| 4 | Compute columns. **Next.** | Input dollars move with Compute's gross output. Investment moves with the server stock. | Supplier shares, once chosen. Investment split: computers, margins, software (D6). |
| 5 | Rows. | Facilities sells its gross output to Compute, every year. | Compute's customer shares (D5), until reviewed. Facilities consumption is 0. |
| 6 | Carve. | Each year's dollars come out of that year's Info and Real estate. | Which old cell loses them, once chosen. |

Headline path ($bn). The scripts print the full series.

| | 2018 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Facility stock | 25.7 | 67.1 | 87.1 | 115 | 156 |
| Server stock | 29.1 | 51.6 | 57.4 | 65.0 | — |
| Facilities GO | 9.8 | 22.3 | 28.3 | 33.9 | — |
| Compute GO | 22.3 | 45.0 | 53.8 | 63.1 | — |
| Power bill | 4.2 | 8.9 | 11.1 | 12.4 | — |

2025 servers and gross output wait on the October fixed-asset release. The 2022 TWh figure is interpolated.

## Object

Two sectors appended to the 37-sector VLW network, for every year the base exists.

| Sector | Owns | Sells | Buys |
|---|---|---|---|
| 38 `DC_facilities` | One facility stock: shell (δ 0.0247) + installed plant (δ 0.10), both from C30 | Powered space, one cell, to Compute | Utilities; construction repairs; admin |
| 39 `Compute` | 5140 servers (δ 0.30) + 4% software (δ 0.22). Publishing 5110 is a ceiling | IaaS/PaaS. SaaS stays in `Info` | Powered space, telecom, software, IT services. Servers are **investment** from `Computers` |

Node = hyperscale + colocation only (owned or leased). Enterprise, government, and crypto stay out. Labs stay in `Info` / `Prof_Tech` and buy Compute. Servers stay in `Computers`. Closed economy.

```text
Construction ──I──▶ DC_facilities ◀── electricity
                        │ powered space
                        ▼
   Computers ──I──▶ Compute ──services──▶ Info, Prof_Tech, …, PCE
```

Output: `data_construction/calibration_data_dc.mat` (millions; `IOmat` columns = buyers; `invmat` columns sum to 1). The 2018 file exists, sliced from the VLW arrays. Any later year waits on that year's 37-sector base. Builder: `build_stage1.py`. Assumptions: `stage1_assumptions.py`.

## Decisions

| # | Choice |
|---|---|
| D1 | Build the series. The initial steady state is one slice of it; the working choice is 2022. Revisit when the October vintage is in. The terminal steady state waits on the shock. |
| D2 | Hyperscale + colocation only. Touches only `Info` and `Real_estate`. |
| D3 | Two sectors, appended 38 then 39. `Computers` keeps all of 334. |
| D3b | Owned campuses are rentals through `DC_facilities`. One stock cumulated from C30, split 15/85. No separate equipment stock on top. |
| D4 | Competitive cost build-up, no balancing item. `r = 1/β − 1 = 0.0417` (β = 0.96). |
| D5 | Facilities row: one cell, sold to Compute. Compute row: fixed-asset computers and software by industry, with Info 30% (own-use), Prof_Tech 15% (labs), consumption 10%. Do not copy the 2017 518200 customer row. Under review in chapter 5. |
| D6 | Investment columns match the stocks. Facilities: 100% Construction. Compute: about 0.92 from `Computers` at producers' value, plus margins, and software from `Prof_Tech`. |
| D8 | No extra good, no GPU sector, no compute nest. |

Rejected in this stage: a GPU column; adding Nvidia into 334; gross operating surplus as a plug; copying 518200's customers; QCEW payroll as this node's labor; scaling the C30 stock up to the filings range.

## Open

**Chapter 4.** Who Compute buys from, including the whole facilities gross output. D6 is the current investment split.

**Chapter 5.** Whether the D5 customer shares stay.

**Chapter 6.** Which old cell loses the power bill, year by year. Still coded real-estate first: in the years checked, hosting's own utilities cell is smaller than the bill. Which old cell loses the rent. Still coded as real estate sold to Info; taking it off Info's own diagonal is parked. Then Info's sales, Info's remaining column, and value added. Info and Real estate investment columns: a 75/25 structures split is still in the code. Wholesale rent-plus-electricity stays parked; powered space stays one cell.

## Outside the chapters

1. Rebuild the 37-sector use table, gross output, value added, and consumption for 1997–2024 from `Data/raw/bea_2024/` (September 2025 vintage; before redefinitions; producers' prices; consumption = PCE + exports). Validate 1997–2018 against the VLW arrays. Utilities cells move by more than a revision: 2018 utilities→Info 4.5→11, utilities→real estate 104→44.
2. Port `invmat` for the recent years (`buildinvmat.m`, new fixed-asset sheets). Until that port exists, hold the 2018 investment columns fixed.
3. After 30 Sep / October 2026, re-pull and extend the series through 2025.
4. Toy Dynare, in parallel: slow facilities capital, fast capital invested in the existing Computers sector, facilities consumption zero.

## Still to pull

Economic Census 518210 receipts by product line. Annual capital-expenditure survey expenses for 518, including the electricity line. LBNL terawatt-hours as an annual series. Equinix's utility bill. Operator megawatts where they are public.

## Model, after the tables

39 sectors, one year at a time, structural zeros kept, no TFP process. Labels `DC_facilities` and `Compute`. Facilities are a zero-consumption good. No nest.
