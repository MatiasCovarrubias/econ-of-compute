# Agent guide: econ-of-compute

You are answering questions about the economics of AI compute: data centers, their costs, power, chips, financing, time to build, and measurement in national accounts. Read this file first.

## Where to look

| Question about… | Look in |
| --- | --- |
| Cost of AI compute; capex per MW; IT vs facility split; electricity share; PUE; water; staffing | `notes/ai-compute-recipe/dc_recipe_section.tex` (synthesis), then `notes/ai-compute-recipe/research/*.md`, then the rows in `data/cost-database/*_obs.csv` |
| GPU useful lives, depreciation, rental prices, failure rates | `research/sec_useful_lives.md`, `gpu_rental.md`, `gpu_failure_priceperf.md`, `it_equipment.md`, and their `*_obs.csv` |
| Transformers, switchgear, gensets, on-site gas, PJM/ERCOT, interconnection queues | `research/power_energy.md`, `power_energy_obs.csv` |
| US data-center stock, investment, output; NAICS/BEA placement; Census C30 | `notes/us-national-accounts/` (start with `data_center_notes.tex`, then `dc_structures_sizing.tex`, `dc_it_stock.tex`, `dc_cost_buildup.tex`) and `data/raw/` |
| Where AI capex lands in the US I-O tables; imports; electrical equipment | `notes/us-national-accounts/dc_upstream_plan.tex`, `code/upstream_concentration.py` |
| How big the US boom is; Fed nowcast; financing flows; power prices | `notes/us-boom/` |
| Time to build; permits; grid access; Spain, Portugal, France, US lifecycles | `notes/time-to-build/` |
| Latin America | `notes/latam/` |
| Europe; EED registry; what data exist | `notes/europe/data_on_european_data_centers.md` |
| Which document says X | `references/catalog.csv` (then the PDF under `path`) |

`notes/README.md` has the full inventory with status and known issues. `data/README.md` describes each dataset and which script reads it.

## The private folder

`private/` is a separate private repository and may not be present. If it is, it holds the financing-risk notes, the AI-investment measurement notes, the Spain potential-output and decree notes, BdE-internal material, copyrighted PDFs and the work plan (`private/WORKPLAN.md`). Rules:

- Never copy text or numbers from `private/` into files outside `private/`. This repo is public.
- Notes in `private/notes/financing-risk/roundtable-chatham-house/` come from a meeting held under the Chatham House rule. Never attribute anything from them to a person or institution.
- If `private/` is absent and a question needs it, say so; don't guess.

## How to answer

- Cite the file and line (`notes/us-national-accounts/dc_it_stock.tex:37`) or the database row (file + `source` + `metric`) for every number.
- Check `notes/README.md` for known issues before you give a number. Several notes have flagged errors; say so when one applies.
- Keep units straight: MW of IT vs MW of total facility power; nominal vs real; calendar vs fiscal year; SAAR vs annual.
- Prefer primary rows (`primary_or_requote = primary`, notes starting with `VERIFIED`) over requotes.
- Rows marked unverified, and the AI-generated research files (`notes/time-to-build/us_lifecycle_research.md`, `portugal_france_first_pass.md`), need a check against the primary source before anyone uses them.

## Changing things

- To change a number, change the script in `code/` and rerun it. Don't edit `data/derived/` by hand.
- `code/ai_recipe.py` has a twin in `PandP/data_construction/` that the P&P model imports. Say so when you change the recipe.
- Notes cite old paths (`data_construction/`, `Data/raw/`, `notes/recipe_research/`). The mapping is in `notes/README.md`.
- Add new source documents to `references/catalog.csv`. Put a PDF in the public tree only if it is a US government document, an SEC filing or an official legal text.
- No commits or pushes unless the user asks.
