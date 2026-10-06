# References

Source documents behind the notes and the cost database. [catalog.csv](catalog.csv) lists all of them, public and private.

## What is in the public tree

Only documents that can be redistributed: US federal documents (BEA, EIA, DOE, FERC, CRS, Federal Register, IRS, BIS, NREL, LBNL, PNNL, NIAC, Federal Reserve), SEC filings (10-Ks), and official legal texts (Texas SB 6, Spain's draft Royal Decree on data centers). Everything else (consultants' cost indices, vendor white papers, broker reports, sustainability reports, academic papers, earnings transcripts) is in `private/references/`, with the same folder structure.

## Folders

| Folder | Contents |
| --- | --- |
| `engineering/facility_capex/` | Construction cost indices and capex studies (Turner & Townsend, KPMG, Schneider, Uptime) |
| `engineering/it_equipment/` | NVIDIA datasheets and guides, BEA depreciation methodology, reliability papers, CoreWeave and Nebius filings, semiconductor tariff notices |
| `engineering/operations/` | Operating costs, water, staffing, sustainability reports, 10-Ks, Virginia JLARC study |
| `engineering/power_energy/` | Transformers, PUE, capacity markets (PJM, ERCOT), EIA cost data, utility tariffs for large loads |
| `measurement/` | Measuring data centers and AI in national accounts (BEA, Fed FEDS 2025-109, Korinek et al., PwC/IMPLAN studies, LBNL energy report) |
| `finance/` | Van Nieuwerburgh, *Financing the AI Buildout* (drafts) |
| `market-reports/` | JLL data-center outlooks |
| `latam/`, `spain/`, `local-effects/` | Regional reports and the draft decree; local effects of data centers |

## catalog.csv

| Column | Meaning |
| --- | --- |
| `topic` | Folder under `references/` or `private/references/` |
| `file` | File name: `Publisher (year) Title.pdf` |
| `publisher`, `year`, `title` | Parsed from the file name |
| `access` | `public` (in this repo), `private` (in the private repo), or `duplicate` (same file as `path`) |
| `path` | Where the file is, relative to the repo root |
| `origin` | Where it was copied from on 6 Oct 2026 |
| `url` | Source URL. Mostly empty for now; filling it in is work plan task 0. Many URLs are already in the `url` column of `data/cost-database/*_obs.csv`. |

## Adding a document

Name it `Publisher (year) Title.pdf` and put it under the right topic: in `references/` if it is a US government document, an SEC filing or an official legal text, otherwise in `private/references/`. Then add a row to `catalog.csv`.
