# Plan: the recipe of the two AI sectors

Status: 28 Sep 2026. Phases 1–4 implemented in `data_construction/ai_recipe.py` (engineering recipe by
generation, baseline A3; the 2026 recipe is `ai_recipe_cnt2026.py`), and the paper rerun (N20).
Still open: R1–R2 (training and the labs' labour), R3 (where electricity sits), R5 (imports in the baseline). The engineering research behind
Phases 1–3 is done: synthesis in `notes/dc_recipe_engineering.tex`, reports and observations in
`notes/recipe_research/`, PDFs in `References/engineering/`. The recipe is one of the paper's
contributions, so the data section should show each cell with its source and a range. This plan
recovers the earlier Stage 1 work, adds 2024–26 sources, and lists the decisions for the authors.

Current builder: `data_construction/ai_recipe.py`, whose `recipe()` function
`Multi-Sector-Macro-Solver/PandPproyect/code/model.py` imports directly (`ai_recipe.json` is an output
for reading). Sections below that describe "the recipe now" refer to the 2026 rack recipe, now
`ai_recipe_cnt2026.py`; `output/news/news_inputs.json` has the current values. Paper: `RbcProdNet_PandP/paper.tex`,
paragraph "The AI sectors", and Table 1.

Abbreviations for the notes cited below: DCN `notes/data_center_notes.tex`, ED
`notes/exercise_design.tex`, FC `notes/dc_facilities_column.tex`, CB `notes/dc_cost_buildup.tex`,
SS `notes/dc_structures_sizing.tex`, IT `notes/dc_it_stock.tex`, UP `notes/dc_upstream_plan.tex`,
S1A `data_construction/stage1_assumptions.py`. CNT = Carpinelli, Natoli & Taboga (2026, Bank of
Italy; local PDF `References/Bank of Italy WP (2016) AI in the US national accounts.pdf`, the
file name has the wrong year). VN = Van Nieuwerburgh (2026 BPEA draft). K–M = Korinek & McKelvey
(2026).

## 1. What the recipe is now

Per $1 of AI services, from `ai_recipe.py`:

| Cell | Value | Source now | Quality |
|---|---|---|---|
| z: inference compute | 0.667 | K–M revenue / inference = 1.5 | Supported by Anthropic 2025 (1.67) and OpenAI 2025 (1.56), press via Epoch |
| z: labs' labour | 0.067 | K–M 0.1 × inference | **Weak.** K–M call it "a first-pass figure" (PIIE WP26-9, lines 449–456). Labs report staff ≈ 0.7–1.1 × inference |
| z: margin → training compute | 0.267 | Closure assumption | Untested. Labs spend 60–73% of compute on R&D (OpenAI 2024, Anthropic 2025) |
| z: IT capital services vs space | 0.669 / 0.264 | CNT NVL72 rack + user costs | Good. The IT/non-IT split of ≈68/32 agrees with VN, Epoch, Fed FEDS 2025-109, Microsoft |
| z: other purchases | none | Design | **Gap.** CNT Table A3 has network $20k per rack-year; Stage 1 had 6% of output |
| f: electricity | 0.080 | CNT $105k per rack-year | Good. 30% of f's output, against 21–27% at Digital Realty and 25–30% in engineering notes |
| f: other opex split | 50/25/25 labour/Admin/Prof_Tech | **Unsourced** (ai_recipe.py:41) | Contradicts FC (KPMG) and CNT Table A3 |
| f: labour | 0.032 (12% of f's output) | From the unsourced split | High against 4–5% (Epoch, engineering notes) |
| δ_IT | 0.25 | "Between 6-year VN and 3-year" | Contradicts IT:126 (δ = 0.30) |
| δ_f | 0.075 | Rack shares, shell 0.025 / plant 0.10 | The rack puts shell at 33% of the facility; Turner & Townsend (T&T) put it at 9–14%, so δ_f ≈ 0.085 |
| z investment | Computers 78, Wholesale 22, Transport 1 | BEA 2017 PEQ bridge, codes 334111/2/8 | Wholesale 22% looks high (ED:688); Stage 1 had 5%. No networking |
| f investment | Construction 33, Electrical 40, Machinery 27 | Rack capex shares | T&T element shares are better; land is overweighted in CNT |
| Capital per $1 | 3.32 (IT 2.29, facilities 1.03) | Capital services ÷ user cost | Follows from the above |

## 2. Decisions for the authors (before rebuilding)

These change the model or the story, not just the numbers.

- **R1. What training is.** Now: the 0.267 margin pays for training compute, which is a current
  cost inside z. Alternative: capitalise model development as own-account R&D. BEA does this, and
  the labs' staff are mostly R&D. Then z's investment bundle includes its own labour and compute,
  and model weights depreciate at δ ≥ 0.36 (BEA R&D rates; frontier tenure about 4 months per
  Epoch). This is the choice that decides where the labs' labour goes (R2).
- **R2. Labs' labour.** Now 0.067. Evidence says total staff ≈ 1.0 × inference (Anthropic 2025:
  $2.9B staff against $2.7B inference; OpenAI 2024: $1.5B against $1.8B; Cottier et al.: staff
  29–49% of frontier development cost including equity).
  - Under R1 with training capitalised, most labour sits in R&D and about 0.1–0.2 in service
    production.
  - Under the current closure, labour would take most of the margin.
  - Labs are loss-making in the build-out, so we need a **steady-state** recipe, not a 2025 P&L.
    Say so in the paper.
- **R3. Where electricity sits.** In f (as now, "powered space") or passed through to z, as colo
  leases and CoreWeave's books do. The totals don't change, but the BEA 518 comparison does.
- **R4. Integral plant in the investment column.** National accounts route integral electrical
  and mechanical plant through construction: the NIPA 5.4 data-center line from Census C30, and
  ONS (Aug 2026) does the same. The model's Construction sector has the 2017 average recipe, which
  buys almost no transformers or switchgear (UP:184). So routing through Construction would hide
  the Electrical and Machinery channel that drives the paper's industry results.
  - Proposal: keep sending the equipment directly (supply-chain view), and state the difference
    from the national accounts.
  - Split T&T's electrical 48–54% into equipment vs installation labour. No source yet (gap G1).
- **R5. Imports in the baseline.** 95% of computers are imported. Transformers ≈80% (power) and
  50% (distribution) per Wood Mackenzie; BEA 2017 shares are transformers 29%, switchgear 26%,
  generators 64%. Now: closed baseline plus an IT-imports alternative (N8, N16). Decide whether the
  data section reports import shares per cell.
- **R6. δ_IT.** 0.25 (now), 0.30 (IT note, BEA hosting ≈0.33), or 5-year straight line (Epoch;
  Amazon 2025 cut to 5 years, Meta 5.5, Microsoft/Alphabet 6, CoreWeave 6). Proposal: 0.30 with a
  0.20–0.33 band.

## 3. Work plan

### Phase 1: reuse what we already have (quick, sourced)

1. **f operating costs from CNT Table A3** (same source as now).
   - Per rack-year: maintenance $25k, network $20k, other $40k.
   - Maintenance → Construction (repairs, 230301), as in FC.
   - Network → Info (telecom); it becomes a purchase of z, not f.
   - "Other" → split with KPMG's security and cleaning (46% → Admin) and Epoch's property taxes
     (16% of facility opex). Taxes are not a purchase: decide whether they are a wedge or part of
     value added.
   - Drop the 50/25/25 split and Prof_Tech from f (FC:38).
2. **f labour** from Epoch's 1 GW TCO (4% of facility opex) or the engineering notes (5% of facility
   cost), instead of the residual.
3. **Water** (LBNL × $10 per thousand gallons ≈ 1% of power, FC:35): fold into Utilities.
4. **Facility capex by element.**
   - Source: T&T 2025, liquid-cooled 48/33/9/10 electrical/mechanical/shell/general contractor
     fees; air-cooled 54/22/14/10.
   - Land at 1–1.5% (Cushman & Wakefield 2026, $584k/MW) instead of CNT's 3%.
   - Grid allowance 2–5% (VN $2M/MW). Decide the owner: f or Utilities.
   - Recompute δ_f with shell 0.0247 (BEA offices) and plant 0.10 (JLL refresh) or 1/14–1/20
     (Epoch, VN). Expected δ_f ≈ 0.085–0.09.
5. **IT capital composition.**
   - Add networking and storage: VN rack 57 / network 5.7 / storage 2.8 / integration 2.8.
   - Epoch has networking at 13% of the campus, 19% of hardware; SemiAnalysis has networking plus
     storage at ≈21% of an NVL72.
   - Networking is NAICS 3342, inside the VLW Computers group, so the investment column barely
     changes, but K_IT and δ do (communications equipment lives 11–15 years).
6. **z investment margins.** Replace the 22% wholesale margin with direct-purchase margins
   (Stage 1 D6: 0.92/0.05/0.02/0.01, S1A:139-142). Hyperscalers buy from ODMs, not wholesalers.
   Look for evidence on actual distribution margins (gap G5).
7. **Reconcile the contradictions** listed in Section 1 (δ_IT, δ_f, shell share, opex split,
   wholesale margin). Record each resolution in one table.

### Phase 2: new research (the parts that need judgement)

8. **Lab cost structure (R1, R2).**
   - Sources:
     - Epoch company-spending breakdown (4 Feb 2026) and OpenAI compute spend (10 Oct 2025).
     - Epoch "Can AI companies become profitable" (GPT-5 bundle).
     - Cottier et al. (arXiv 2405.21015 v2).
     - CoreWeave 10-K FY2025 for the GPU-cloud layer.
   - Output: a steady-state split of $1 of AI services into inference compute, R&D compute, R&D
     labour, service labour, sales and admin, and the Microsoft revenue share (royalty).
   - Flag press numbers.
9. **Opex of z besides space:** software, telecom and bandwidth, sales and marketing, admin.
   Sources: CNT network line, Epoch GPT-5 bundle (sales and marketing $0.5B, legal/admin $0.2B on
   $6B), CoreWeave S&M 3%, G&A 13%. Map to Info, Prof_Tech and Admin.
10. **Import shares for facility equipment.** USITC DataWeb for HS 8504, 8537 and 8502 against
    Census Annual Survey of Manufactures shipments, 2023–25. Also Census end-use 21300 for
    computers (88.5 / 116.8 / 218.2 $bn in 2023–25, DCN:337), and the Fed FEDS 2025-109 figure of
    80% of high-tech equipment imported.
11. **Owner-furnished equipment** (N11). Look for a size in Brandsaas et al. (FEDS 2025-109) or
    the Fed's Nichols et al. project-level paper (local copy in
    `econ-of-ai/macro-of-ai/data-centers/`).
12. **Source the missing citations.** Makridis & Brynjolfsson (2026) is cited in the paper but
    could not be found. N12 also lists unverified bib entries.

### Phase 3: top-down validation (from the Stage 1 levels)

The recipe is per $1 and scale-free. Check its implications against levels we already built:

| Check | Model object | Data (already built) |
|---|---|---|
| Electricity | 0.080 × AI revenue | LBNL TWh × node share × price: $8.9 / 11.1 / 12.4 bn for 2022–24 (CB) |
| IT stock | K_IT per $ × AI revenue | BEA 5140 servers 51.6 / 57.4 / 65.0 $bn for 2022–24 (IT); networking 64–84 $bn |
| Facility stock and investment | K_f, I_f | Census C30 cumulation 67 / 87 / 115 / 156 $bn for 2022–25 (SS); C30 flow 1.8 → 49.7 $bn |
| Capex split | investment columns | Microsoft 57/39/1, Alphabet 60/40, Fed 70/30, Epoch 56/13/30 |
| Facility cost shares | f's column | Engineering: electricity 25–30%, other 10%, labour 5%, capital 55–65% (DCN:171) |
| Colo operating costs | f's column | Digital Realty utilities 23% of revenue, operating costs 18%; Equinix utilities 14–16% |
| Rent | f's output per MW | CBRE $196/kW-month (electricity $51); JLL $152 plus power |

### Phase 4: rebuild, rerun, write

13. Rewrite `ai_recipe.py` so every number sits in one `SOURCES` table (value, source, year,
    range, file:line), and have it emit the appendix table directly.
14. Rerun `run_news.sh`, plus a recipe sensitivity table: labs' labour, δ_IT, electricity, and the
    facility column (T&T vs CNT).
15. Data section in the paper (about 1 page in the main text plus an appendix table): recipe per
    $1 with sources, the two investment columns, and the validation table.

## 4. Gaps with no sourced number yet

- G1: equipment vs installation labour inside electrical and mechanical capex.
- G2: size of owner-furnished equipment.
- G3: labs' compensation in a steady state, separate from R&D.
- G4: post-2017 import shares for switchgear and generators.
- G5: actual distribution margins on hyperscaler server purchases.
- G6: who owns grid-interconnection capital.
- G7: consumer share of AI sales (N9).

## 5. Where the sources are

- **Local:**
  - CNT and VN PDFs in `PandP/References/`.
  - K–M and technical appendix; Korinek et al. (2026).
  - JLL 2026 outlooks and the Fed's Nichols et al. in `econ-of-ai/macro-of-ai/data-centers/`.
  - BEA fixed assets, PEQ bridge, IO tables and C30 in `Data/raw/bea_2024/` and `privsatime.xlsx`.
- **Web** (to download into `References/`):
  - Epoch: https://epoch.ai/data-insights/ai-datacenter-cost-breakdown,
    https://epoch.ai/data-insights/company-spending-breakdown,
    https://epoch.ai/data-insights/openai-compute-spend,
    https://epoch.ai/data-insights/microsoft-ppe-breakdown
  - Turner & Townsend DCCCI 2025:
    https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/data-centre-cost-trends
  - Fed FEDS 2025-109: https://www.federalreserve.gov/econres/feds/files/2025109pap.pdf
  - CoreWeave 10-K FY2025:
    https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm
  - Digital Realty 10-K FY2025:
    https://www.sec.gov/Archives/edgar/data/1297996/000110465926015365/dlr-20251231x10k.htm
  - BEA depreciation rates: https://apps.bea.gov/national/pdf/BEA_depreciation_rates.pdf
  - ONS data centres in the national accounts:
    https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/methodologies/datacentresandtheuknationalaccounts
  - K–M PIIE WP26-9: https://www.piie.com/sites/default/files/2026-05/wp26-9.pdf
  - Cottier et al.: arXiv 2405.21015
