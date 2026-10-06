# Notes inventory

Every note in `notes/`, with what it says, its status, and the known issues to fix before anyone quotes it. Status dates are when the note was last substantively revised. `.tex` notes come with their compiled `.pdf`.

The data behind each note is described in [../data/README.md](../data/README.md). Source documents are in [../references/catalog.csv](../references/catalog.csv).

## ai-compute-recipe/: what a dollar of AI compute is made of

The engineering recipe of the two AI sectors, by data-center generation (A0–A4), at 6-digit NAICS: capex per MW of IT by building element and by IT component, electricity, water, labour, depreciation, and the split of each dollar of AI services. It rests on ~1,070 sourced observations in [../data/cost-database/](../data/cost-database/).

| File | What it is | Status | Known issues |
| --- | --- | --- | --- |
| `dc_recipe_engineering.tex` + `dc_recipe_section.tex` | **Synthesis.** The wrapper compiles the section. Headline (GB200, per $1 of AI services): IT capital services 0.59, space 0.20, labour 0.15, electricity 0.046 (0.027 for the next generation). Facility hard cost ~$12m/MW (all-in $15m); IT $27m/MW (GB200), $37m (GB300). | Done, 28 Sep 2026. The same text is the P&P appendix (`RbcProdNet_PandP/appendix_recipe.tex`). | The text says "IT share 68–72% confirmed" but the recipe computes 65%. The labs' labour is about 10× too low. The recipe's cost of $13m/MW-yr is above CoreWeave's revenue of $8.5m/MW-yr. |
| `recipe_plan.md` | Plan and decision log for the recipe (phases 1–4 done; R1–R5 open). | Live, 28 Sep 2026 | Written for the P&P model; paths point to `PandP/`. |
| `research/facility_capex.md` | Facility capex by archetype: shell, mechanical, electrical, site; cost indices across countries (Turner & Townsend). | Done, 28 Sep 2026 | — |
| `research/it_equipment.md` | IT bill of materials, costs, lives, supply chain (server imports $62bn→$164bn 2024–25, 49% Mexico, 42% Taiwan), operating inputs of the compute layer. | Done, 28 Sep 2026 | — |
| `research/operations.md` | Operations and resource use: utilisation, PUE, water (peak-day vs volume), staffing, maintenance, depreciation of plant. | Done, 28 Sep 2026 | Uses old recipe parameters in places. |
| `research/power_energy.md` | The power chain: electrical capex, PUE, transformers (PPI +76%, lead times ~50→120 weeks, import share 26.5%→≥38.5%), gensets, on-site gas (~90 GW announced vs ~2 GW operating), PJM capacity costs. | Done, 28 Sep 2026 | — |
| `research/sec_useful_lives.md` | Server and GPU useful lives in 31 SEC filings of 11 firms, 2020–26. | Verified, 28 Sep 2026 | Extend with Q2–Q3 2026 filings. |
| `research/gpu_rental.md` | GPU rental and resale prices and the depreciation they imply (δ ≈ 0.17–0.28). | Data verified, 28 Sep 2026 | Short (21 lines). The "rent gradient = depreciation" step needs a defence. |
| `research/gpu_failure_priceperf.md` | Physical failure (0.4–0.8%/yr replaced) vs obsolescence (0.28–0.36 log/yr). The "9% H100 failure rate" counts job interruptions. | Done, 28 Sep 2026 | — |

## us-national-accounts/: sizing US data centers in official statistics

Built for the plan to carve data centers out of the US input-output network ("Stage 1"). The P&P model no longer uses it, but the measurement is finished and stands on its own. The planned outlet is a short paper, "Data centers in the U.S. national accounts".

| File | What it is | Status | Known issues |
| --- | --- | --- | --- |
| `data_center_notes.tex` | **Start here.** Facts and sources: where DCs sit in NAICS and BEA, where their power bill is booked (with real-estate landlords, not the hosting industry), Nvidia in the national accounts, domestic content of DC IT, boom facts. | Sep 2026 | The model-design sections (shock design, σ<1) are superseded; the facts stand. |
| `dc_structures_sizing.tex` | US stock of DC buildings and plant, four ways: Census C30 cumulated, BEA industry 514, 10-K filings, MW × cost per MW. 2024: $115–143bn / $304bn / $179–269bn / $158–248bn. | Sep 2026 | "The ranges overlap at $45–70bn" (lines 23, 250) is false: the ranges don't intersect. Open: BEA query on who reports in 514; private-operator MW. |
| `dc_it_stock.tex` | US server stock in BEA (5140: $29bn 2018, $65bn 2024) and a rebuild of the Fed (Brandsaas et al.) residual. | Sep 2026 | Update with BEA's 2026 fixed-assets release. |
| `dc_cost_buildup.tex` | Output and value added of the facilities and compute sectors by cost build-up, with eight cross-checks. 2022: facilities $22bn output, compute $45bn. | Sep 2026 | Capital share comes out at 38% vs the engineering 55–65% (stock is low). |
| `dc_facilities_column.tex` | The facilities sector's purchases (input column). Water is $0.1bn, ~10× below the old cell. | Sep 2026 | — |
| `dc_upstream_plan.tex` | Upstream routing: IMPLAN's electricity split, BEA vs EIA fuel gaps, power gear booked as equipment, data feasibility. | Sep 2026 | A plan; steps 4–5 not run. |
| `stage1_plan.md` | The Stage 1 build plan (chapters, decisions D1–D9). Chapters 1–3 are done. | 30 Sep 2026 | Parallel track, parked. |
| `figures/dc_stock_sources.pdf` | Figure for `dc_structures_sizing.tex`, written by `code/dc_stock_sources.py`. | — | — |

## us-boom/: size of the US boom and the data landscape

| File | What it is | Status | Known issues |
| --- | --- | --- | --- |
| `us_dc_boom_macro_ballpark.tex` | Macro ballparks: DC investment reaches ~8% of GPDI by 2030 (central case); Census C30 as a check on the Fed nowcast; 10–30bp on r\* but ~30% of net IG issuance; power-price elasticities by market layer. | First pass, Sep 2026 | The Census ×10/3 gross-up likely double-counts IT. The r\* formula uses a 4% real rate. The external-finance share is unsourced. A table is mislabelled. The IMF +0.9% is unverified. |
| `data_on_us_data_centers.md` | Landscape memo: official, regulatory and commercial sources on the pipeline, financing and project durations. Start with Brandsaas et al. (FEDS 2025-109). | Sep 2026 | — |

## time-to-build/: project lifecycles from permit filings

| File | What it is | Status | Known issues |
| --- | --- | --- | --- |
| `DataCenterTTB.tex` | **Working paper draft.** Gazette-dated clocks across seven gates for Spanish DC projects, from a public census of 232 filings (112 projects) checked against BOA/DOCM/BOE. Amazon Aragón: 36 months from announcement to service, the one completed greenfield campus. Spain has granted >43 GW of demand access against a 38.2 GW peak. | Sep 2026 | The claim that Meta's "grid side finished first" (lines 137, 195) is likely wrong: the 208 m line was for the rail substations; Meta's own connection was authorised on 27 Apr 2026 (BOE-A-2026-9171). The ">50 MW thermal backup" generalisation fails for Meta (12.9 MW). Not yet in the text: 600 MW IT of off-grid gas campuses (Mora, Vianos) and a Nostrum contract at €8.49m/MW IT. |
| `next_steps.md` | Working list for the paper: data to request, cases to watch. | Sep 2026 | — |
| `portugal_france_first_pass.md` | Out-of-sample check in Portugal and France: a two-track pattern. | Sep 2026 | AI-assisted web research (Grok subagents). Verify dates against primary documents. |
| `us_lifecycle_research.md` | US project lifecycle: stages, data sources (C30, CPRS, Dodge), durations. | Sep 2026 | AI-generated research report (Claude). Check every figure. |

## europe/

| File | What it is | Status | Known issues |
| --- | --- | --- | --- |
| `data_on_european_data_centers.md` | Landscape memo: the EED registry (Art. 12, first aggregates 2026: 776 sites, 6.4 GW, ~36% coverage), national sources, AnaCredit (NACE 63.1), a research design. No agency publishes DC investment. | Sep 2026 | — |

## latam/

| File | What it is | Status | Known issues |
| --- | --- | --- | --- |
| `latam_dc_stock_and_crosschecks.pdf` | LatAm DC capital stock vs announcements: 1,307 MW, ~US$13bn of capital at $10m/MW; 2025 flow ~$2.3bn against $45.6bn announced. TikTok's Ceará project (US$37.7bn) is ~3× the region's stock. | 18 Sep 2026 | The Chile $10m/MW cross-check uses the 2013 stock (35 MW) as the 2020 base. "16% CAGR" is closer to 19%. |
| `latam_sources_and_figures.md` | Source list and figures by country. | 17 Sep 2026 | Calls Colombia's $1.16bn IDB-backed; the PDF says it is from Arizton. |

## Path mapping

The notes still cite their old locations. Use this table to find a file:

| Old path (in the notes) | New path |
| --- | --- |
| `PandP/notes/dc_*.tex`, `data_center_notes.tex`, `stage1_plan.md` | `notes/us-national-accounts/` |
| `PandP/notes/dc_recipe_*.tex`, `recipe_plan.md` | `notes/ai-compute-recipe/` |
| `PandP/notes/recipe_research/*.md` | `notes/ai-compute-recipe/research/` |
| `PandP/notes/recipe_research/*_obs.csv` | `data/cost-database/` |
| `PandP/data_construction/*.py` | `code/` |
| `PandP/data_construction/*.json`, `*.csv`, `*.mat` (outputs) | `data/derived/` |
| `PandP/Data/raw/…` | `data/raw/…` |
| `PandP/VLW_replicaton/Replication Packet/Raw Data/detailnonres_inv1.xlsx` | `data/raw/vlw/` |
| `PandP/References/engineering/<topic>/` | `references/engineering/<topic>/` (public) or `private/references/engineering/<topic>/` |
| `econ-of-ai/macro-of-ai/data-centers/Time to Build/` | `notes/time-to-build/` |
| `econ-of-ai/macro-of-ai/data-centers/LATAM/` | `notes/latam/` |
| `econ-of-ai/macro-of-ai/data-centers/data_on_*.md`, `us_dc_boom_macro_ballpark.tex` | `notes/us-boom/`, `notes/europe/` |

## In the private repository

These notes are in `private/notes/` (see the main README for access). Listed here so you know they exist:

- `financing-risk/`: the stress-scenario note on AI-infrastructure finance; the financial-stability data plan; roundtable material (Chatham House rule).
- `ai-investment-measurement/`: measured US AI investment and AI revenue, 2020–26, compared with published projections.
- `spain/`: DC investment and Spanish potential output; the draft Royal Decree on data centers; BdE-internal briefs.
- `latam/`: the BdE box on LatAm data centers and correspondence.
- `time-to-build/`: notes on colleagues' regional working file.
- `ai-generated-and-meetings/`: AI-generated reports and meeting debriefs, kept for facts only.
- `../strategy/outlets_and_theses.md`: scoring of all topics, outlets and the fix list.

## Not copied

Superseded or duplicate files, left in their original folders:

- `econ-of-ai/macro-of-ai/data-centers/`: `research_on_spain_scenarios.md`, `ai_capital_addendum.md` (headline numbers wrong), `ai_capital_report_upside.tex`, `Time to Build/spain_dc_expediente_lifecycle.md`, `LATAM/LatAm data centers 2025 stock and cross-checks.pdf` (older version), `US vs. Europe Data Center Electricity….pdf` (same as a private AI-generated md).
- `PandP/notes/`: `data_center_nowcast_plan.md`, `shock_archive_8sep.md`, `plan_summary_email.html` (superseded plans). `ai_demand_*`, `exposure_plan.md`, `efficiency_price_plan.md`, `scenarios_plan.md`, `calibration_evaluation.md`, `exercise_design.tex`, `data_notes.tex` are about the P&P model or the energy paper, not about compute. The import-leakage exercise (1.47 vs 1.99 domestic output per $1 of AI capex) is in `exercise_design.tex`, lines 263–410.
- `PandP/data_construction/`: exposure and placement scripts (P&P model only).
