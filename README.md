# Economics of Compute

Notes, data and code on the supply chain of AI compute: the data centers, the chips and electrical gear inside them, the power that runs them, how they are financed, how long they take to build, and how the national accounts record them.

This is working material, not published research. Every note has a status and a list of known issues in [notes/README.md](notes/README.md). Check those before you quote a number.

Maintained by Matías Covarrubias. Consolidated on 6 October 2026 from two earlier project folders (see [Origin](#origin)).

## Start here

1. **Ask questions.** Clone the repo and open it in Claude Code, Cursor or another coding agent. The agent reads [AGENTS.md](AGENTS.md), which tells it where everything is. Some questions it can answer straight away:
   - "What share of the cost of AI compute is electricity, and how does it change across GPU generations?"
   - "How big is the US data-center building stock, and why do the four sources disagree?"
   - "What do 10-K filings say about server useful lives, and what does that imply for depreciation?"
   - "How long does it take to build a data center in Spain, from announcement to service?"
   - "Where do data centers sit in the BEA input-output tables?"
2. **Browse.** [notes/README.md](notes/README.md) lists every note by topic. [data/README.md](data/README.md) lists every dataset. [references/catalog.csv](references/catalog.csv) lists every source document.
3. **Reproduce.** See [Running the code](#running-the-code).

## What is here

```text
econ-of-compute/
├── notes/                    # research notes, by topic (inventory: notes/README.md)
│   ├── ai-compute-recipe/    # what a dollar of AI compute is made of, by DC generation
│   │   └── research/         # topic reports behind the cost database
│   ├── us-national-accounts/ # sizing US data centers in BEA/Census data
│   ├── us-boom/              # size of the US boom; US data landscape
│   ├── time-to-build/        # project lifecycles from permit filings (Spain, PT, FR, US)
│   ├── europe/               # European data landscape
│   └── latam/                # Latin American capital stock vs announcements
├── data/                     # inventory: data/README.md
│   ├── cost-database/        # ~1,070 sourced observations on DC costs (our own)
│   ├── raw/                  # BEA, Census, EIA downloads (public domain)
│   └── derived/              # outputs of code/ (AI recipe, 39-sector table)
├── code/                     # scripts that produce the numbers in the notes
├── references/               # public-domain sources (US government, SEC filings)
│   └── catalog.csv           # every source document, public and private
├── AGENTS.md                 # guide for AI agents (CLAUDE.md points here)
└── private/                  # NOT in this repo: see below
```

## Topics at a glance

| Topic | Main note | Data | Status |
| --- | --- | --- | --- |
| What a dollar of AI compute is made of (capex, power, labour, depreciation by GPU generation) | [dc_recipe_engineering.tex](notes/ai-compute-recipe/dc_recipe_engineering.tex) | [cost-database/](data/cost-database/), [ai_recipe.py](code/ai_recipe.py) | Synthesis done (28 Sep 2026); database needs cleanup |
| GPU depreciation: filings, rents, failure rates | [research/sec_useful_lives.md](notes/ai-compute-recipe/research/sec_useful_lives.md), [gpu_rental.md](notes/ai-compute-recipe/research/gpu_rental.md) | `sec_useful_lives_obs.csv`, `gpu_rental_obs.csv` | Data verified; prose thin |
| Electrical bottlenecks: transformers, gensets, on-site gas, PJM | [research/power_energy.md](notes/ai-compute-recipe/research/power_energy.md) | `power_energy_obs.csv` | Report done |
| US data centers in the national accounts (structures, servers, output, inputs) | [us-national-accounts/](notes/us-national-accounts/) | [raw/bea_2024](data/raw/bea_2024/), `privsatime.xlsx` | Measurement done; open items listed |
| Size of the US boom (investment share, Fed nowcast vs Census, power prices) | [us_dc_boom_macro_ballpark.tex](notes/us-boom/us_dc_boom_macro_ballpark.tex) | — | First pass; several fixes pending |
| Time to build in Spain, with Portugal, France and the US | [DataCenterTTB.tex](notes/time-to-build/DataCenterTTB.tex) | — | Working paper draft |
| Latin America: capital stock vs announcements | [latam_dc_stock_and_crosschecks.pdf](notes/latam/latam_dc_stock_and_crosschecks.pdf) | — | Note done; one fix pending |
| Data sources for the US and Europe | [data_on_us_data_centers.md](notes/us-boom/data_on_us_data_centers.md), [data_on_european_data_centers.md](notes/europe/data_on_european_data_centers.md) | — | Landscape memos |

## Conventions

- **Generations.** A0 legacy (before 2015), A1 hyperscale air-cooled (2015–22), A2 AI air or hybrid cooling (2023–24), A3 AI liquid-cooled GB200 NVL72 (2025–26, the baseline), A3_GB300 (A3 facility with GB300 IT), A4 next generation (2027+).
- **Megawatts.** "MW" means MW of critical IT load unless a note says otherwise. Total facility power is IT MW × PUE. Mixing the two is the most common error in published figures.
- **Money.** US dollars, nominal, unless stated. "bn" is 10⁹.
- **Two AI sectors.** `AI_facilities` (f) owns the building and plant and sells powered space. `AI_compute` (z) owns servers, network and storage and sells AI services. The recipe is expressed per MW of IT and per $1 of AI services.
- **Cost-database rows.** Each row has a source, a URL or page, `primary` vs `requote`, and a note that starts with `VERIFIED` when the number was checked against the document.

## Running the code

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 code/ai_recipe.py             # AI recipe by generation -> data/derived/ai_recipe*.{json,csv}
python3 code/facilities_stock.py      # DC facility stock from Census C30
python3 code/it_stock.py              # server stock from BEA fixed assets
python3 code/cost_buildup.py          # output and value added of the two DC sectors
python3 code/dc_stock_sources.py      # four-source comparison + figure for dc_structures_sizing.tex
python3 code/upstream_concentration.py  # where AI capex lands in the 2017 detail I-O tables
python3 code/build_stage1.py          # 39-sector table with DC columns -> data/derived/calibration_data_dc.mat
```

Each script reproduces the numbers of the note it belongs to (checked on 6 Oct 2026). The notes still cite the old script paths (`data_construction/…`, `Data/raw/…`); [notes/README.md](notes/README.md) maps them to the new ones.

## Public and private parts

This repository is public. Some material can't be published: notes written under the Chatham House rule, drafts that are not ready to circulate, Banco de España internal notes, copyrighted reports and papers, and data shared by colleagues. That material lives in a separate **private** repository with the same layout. Collaborators with access clone it into `private/`, which git ignores here:

```bash
git clone https://github.com/MatiasCovarrubias/econ-of-compute-private.git private
```

[references/catalog.csv](references/catalog.csv) lists every document in both places. The `access` column says whether a file is in `references/` (public) or `private/references/`. Only US government documents, SEC filings and official legal texts are in the public tree.

## Origin

Copied on 6 October 2026 from:

- `econ-of-ai/macro-of-ai/data-centers/` (financing, Spain, LatAm, time to build, US ballpark), and
- `PandP/` (the measurement notes, the AI-compute recipe and its research, the BEA/Census/EIA data, and the scripts). These were built for the AER P&P "News about AI in a Production and Investment Network" (Carvalho, Covarrubias, Nuño).

The P&P model still imports its own copy of `ai_recipe.py` from `PandP/data_construction/`. If you change the recipe here, port the change there, or the other way round.

Superseded drafts were not copied. They are listed at the end of [notes/README.md](notes/README.md).

## Reuse

No license has been chosen yet. Ask before you reuse the notes or the cost database. The US government documents and SEC filings in `references/` are public records.
