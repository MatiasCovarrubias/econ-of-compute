# Data inventory

Three kinds of data: our own **cost database**, **raw** downloads from statistical agencies, and **derived** files written by `code/`. Everything here is either our own work or public-domain US government data. Licensed or shared data is in the private repository (listed at the end).

## cost-database/: sourced observations on data-center costs (our own)

Collected 28 Sep 2026 for the AI-compute recipe. One row per observation, each with a source, a URL or page, and a verification note. The topic reports in [../notes/ai-compute-recipe/research/](../notes/ai-compute-recipe/research/) explain the numbers. [../code/ai_recipe.py](../code/ai_recipe.py) turns them into the recipe.

| File | Rows | Sources | Primary | Covers |
| --- | ---: | ---: | ---: | --- |
| `facility_capex_obs.csv` | 173 | 41 | 88% | Shell, mechanical, electrical, site costs per MW; cost indices by city |
| `it_equipment_obs.csv` | 289 | 208 | 86% | Rack and system prices, network/storage shares, lives, imports, operating inputs of compute |
| `operations_obs.csv` | 311 | 161 | 81% | Utilisation, PUE, water, staffing, maintenance, insurance, property tax, plant lives |
| `power_energy_obs.csv` | 212 | 129 | 86% | Electrical capex, transformers, gensets, on-site generation, power prices, capacity markets |
| `sec_useful_lives_obs.csv` | 22 | 22 | 100% | Server/GPU useful lives in SEC filings, 2020–26 |
| `gpu_rental_obs.csv` | 36 | 33 | 78% | GPU rental indices and resale prices |
| `gpu_failure_priceperf_obs.csv` | 23 | 21 | 87% | GPU failure and replacement rates; price-performance |

The last three files are helper files whose rows are also merged into `it_equipment_obs.csv`, so the total of 1,066 rows holds about 985 unique observations.

**Columns.** `component`, `metric`, `archetype` (generation A0–A4), `value`, `unit`, `year_of_data`, `source`, `source_type` (cost_consultant, operator_filing, academic, analyst, vendor, national_lab, press…), `primary_or_requote`, `origin_if_requote`, `url`, `page_or_table`, `notes`. A note that starts with `VERIFIED` was checked against the document. `url` values that start with `local:` point to a PDF; look it up by name in [../references/catalog.csv](../references/catalog.csv).

**Before treating it as a release:** values are sometimes ranges in text (`40-50`, `4.8 per rack; 34 per MW`). They need numeric low/central/high columns, normalised archetype and source names, a verification column, and the helper duplicates removed. Analyst figures (SemiAnalysis, Silicon Data and others) are quoted as single numbers; check their terms before bulk redistribution. This is task 5 of the work plan.

## raw/: downloads from statistical agencies (public domain)

| Path | Source | Vintage / downloaded | Used by |
| --- | --- | --- | --- |
| `bea_2024/detailnonres_stk1.xlsx`, `detailnonres_inv1.xlsx`, `detailnonres_dep1.xlsx`, `DetailNonres_rate.xlsx`, `detailresidential.xlsx` | BEA, detailed fixed assets by industry and asset type (net stock, investment, depreciation, implied depreciation rates). Sheet `5140` = hosting and internet publishing. | Sep 2025 release; downloaded 18 Sep 2026 | `it_stock.py`, `dc_stock_sources.py`, `build_stage1.py` |
| `bea_2024/FixedAssets_Section3All_xls.xlsx`, `FixedAssets_Section5All_xls.xlsx` | BEA Fixed Assets tables, sections 3 (by industry) and 5 (investment by type) | same | Not read by current scripts. Downloaded to rebuild the 37-sector base for 1997–2024 (`stage1_plan.md`, S1) |
| `bea_2024/NIPA_Section5All_xls.xlsx` | BEA NIPA section 5 (saving and investment), incl. table 5.4.5U with the "Data centers" line under office structures | same | `facilities_stock.py`, `dc_stock_sources.py` |
| `bea_2024/GDPxInd_GrossOutput.xlsx`, `GDPxInd_ValueAdded.xlsx` | BEA GDP by industry | same | Same as above (base rebuild) |
| `bea_2024/AllTablesIO.zip`, `AllTablesSUP.zip`, `MAKE-USE-IMPORTS_BEFORE_REDEFINITIONS.zip`, `SUPPLY-USE.zip` and `extracted/` | BEA input-output accounts: make, use, import matrices, total requirements, supply-use tables (summary 1997–2023; detail 2017) | Sep 2025 release | `upstream_concentration.py`; facilities column and upstream notes |
| `bea_2024/PEQBridge_*.xlsx`, `PCEBridge_Summary.xlsx`, `Margins_Before_Redefinitions_Summary.xlsx` | BEA bridges from equipment investment and PCE to I-O commodities; margins | same | `PEQBridge_Detail.xlsx`: `upstream_concentration.py`. The others: base rebuild |
| `privsatime.xlsx` | Census, Value of Construction Put in Place (C30), private, SAAR monthly, with the "Data center" line (from Jan 2014) | downloaded 17 Sep 2026 | `facilities_stock.py`, `dc_stock_sources.py` |
| `calibration_data.mat` | vom Lehn and Winberry replication data: 37-sector BEA use, investment and value-added tables, 1947–2018 | VLW packet | `build_stage1.py` |
| `vlw/detailnonres_inv1.xlsx` | BEA detailed investment as shipped in the VLW packet (2019 vintage), so the 2018 build matches the vintage of VLW's base | VLW packet | `build_stage1.py` |
| `eia_2017/epa_08_03.xlsx`, `epa_08_04.xlsx` | EIA Electric Power Annual tables 8.3 (IOU revenue and expenses) and 8.4 (O&M and fuel per kWh by plant type) | downloaded 26 Sep 2026 | `dc_upstream_plan.tex` |
| `eia_2017/ex_all.csv` | EIA SEDS, energy expenditures by state and sector, 1970–2024 | same | `dc_upstream_plan.tex` |
| `eia_2017/f923_2017.zip`, `eia8602017.zip` | EIA-923 (plant generation, fuel) and EIA-860 (generators), 2017 | same | `dc_upstream_plan.tex` |
| `census_2017_sector22/EC1722*.zip` | 2017 Economic Census, Utilities (NAICS 22): basic statistics, energy expenses, purchased electricity and gas | same | `dc_upstream_plan.tex` |
| `census_2017_sector22/sas-17.xlsx` | Census Service Annual Survey 2017, revenue by NAICS | same | `dc_upstream_plan.tex` |

Landing pages: BEA input-output (bea.gov/industry/input-output-accounts-data), BEA fixed assets (apps.bea.gov/national/FA2004/Details/Index.htm), Census C30 (census.gov/construction/c30), EIA electricity data (eia.gov/electricity/data), EIA SEDS (eia.gov/state/seds). The folder is called `bea_2024` for historical reasons; the contents are the September 2025 release. BEA's September 2026 annual update will supersede it (work plan task 7).

## derived/: outputs of code/

| File | Written by | What it is |
| --- | --- | --- |
| `ai_recipe.json` | `ai_recipe.py` | Recipe of the two AI sectors per $1 of AI services, baseline generation A3 |
| `ai_recipe_detail.csv` | `ai_recipe.py` | Every generation, NAICS detail, per MW and per $1 (252 rows) |
| `calibration_data_dc.mat`, `.json` | `build_stage1.py` | 39-sector VLW table for 2018 with `DC_facilities` and `Compute` columns, plus audit tables |

Regenerate with the commands in the main README. On 6 Oct 2026 the scripts reproduced these files byte for byte (`ai_recipe*`) and value for value (`calibration_data_dc.mat`).

## In the private repository

- `private/data/implan/`: IMPLAN 528 sector lists, construction detail and NAICS bridge (IMPLAN licence).
- `private/data/time-to-build/centros_datos_expedientes_CLM.xlsx`: colleagues' regional working file behind the public census of Spanish DC filings (Castilla-La Mancha). Not ours to publish.
- `private/data/iea/Data_annex_Energy_and_AI.xlsx`: IEA, *Energy and AI* data annex.

## Data we know about but have not downloaded

See [../notes/us-boom/data_on_us_data_centers.md](../notes/us-boom/data_on_us_data_centers.md) and [../notes/europe/data_on_european_data_centers.md](../notes/europe/data_on_european_data_centers.md): Dodge project microdata, Census CPRS, the EU EED registry, Ireland CSO, KBRA/Trepp securitisation data, interconnection queues and others.
