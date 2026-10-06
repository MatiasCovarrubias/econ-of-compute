# The power chain and energy: cost structure of AI_facilities

Status: research note, 28 Sep 2026. Scope: topic (a)–(d) of the recipe plan (`notes/recipe_plan.md`). Companion file: `power_energy_obs.csv`, with 212 observations, each with source type, primary/re-quote and URL. PDFs are in `References/engineering/power_energy/` (60 files). Nothing in `data_construction/` was changed.

## 0. Summary

| Quantity | A0 legacy/colo | A1 hyperscale air | A2 AI air/hybrid | A3 AI liquid (NVL72) | A4 800 VDC / on-site |
|---|---|---|---|---|---|
| Installed electrical capex, $M per MW IT (2025$) | 5.5 (4–8) | 5.0 (4–7) | 5.2 (4–7) | 6.0 (4.5–8) | 5.5 (4–8) + on-site generation ≈3 (2–5) |
| of which equipment / installation / design | 55/30/15 | 55/30/15 | 55/30/15 | ≈58/28/14 | ≈60/27/13 |
| Operating PUE | 1.70 (1.55–2.00) | 1.15 (1.08–1.25) | 1.25 (1.15–1.40) | 1.15 (1.08–1.25) | 1.10 (1.05–1.20) |
| Mature utilisation u (avg IT draw / provisioned IT) | 0.50 (0.35–0.60) | 0.65 (0.55–0.75) | 0.70 (0.55–0.85) | 0.75 (0.60–0.85) | 0.80 (0.65–0.90) |
| Delivered price, $/MWh | 110 (85–135) | 75 (55–95) | 80 (60–100) | 85 (60–110) | 85 (55–120) |
| **Electricity, $k per MW-IT-year** | **819** (573–1,005) | **491** (360–622) | **613** (460–766) | **642** (453–831) | **655** (424–925) |
| Import share of electrical equipment (value, 2024–25) | transformers ≈40% (HV >75%); switchgear ≈25%; gensets ≈30%; UPS ≈50%; Li-ion ≈50% | ← same for all archetypes | | | |

Corrections to the indicative archetype specs:

- **A0.** Uptime 2024 puts the most common rack density at 4–6 kW, with an 8 kW average. That fits the spec.
- **A3.** NVIDIA's Gen-1 power racks support up to 145 kW, with 8-to-make-6 power shelves. That fits the spec.
- **A4.** Vera Rubin NVL72 (2026) is already 330 kW per rack. Gen-3 racks reach 570 kW; native 800 VDC ("Gen 4") arrives with Kyber in 2027. So "~600 kW" is right for 2027+.
- **On-site generation.** Only ≈2 GW of behind-the-meter capacity was operating in 2026, against ≈90 GW announced. Treat on-site generation as a scenario, not the A4 baseline.

## 1. Electrical bill of materials per MW of IT load

### 1.1 How the numbers are built

No free, current, engineering-grade source gives an itemised electrical BOM per MW. SemiAnalysis, Omdia, Dell'Oro and the cost consultants' detailed element tables are paywalled. The table below is therefore a **bottom-up engineering build, anchored on primary vendor white papers and escalated to 2025 prices with BLS PPIs**. It is then **checked top-down** against cost-consultant totals (Turner & Townsend 2025, Cushman & Wakefield) and vendor "content per MW" disclosures (Eaton).

Ingredients (all primary; see the CSV):

| Ingredient | Value | Source |
|---|---|---|
| Electrical share of DC capex, excluding the building | 40–50% | Schneider WP61 Rev 2 (2015), p.12 |
| Split of electrical capex | equipment 50–60%, installation 25–35%, design 15–20% | WP61 p.12. **Answers gap G1.** |
| UPS + generators | ≈ half of electrical *equipment*; the other half is switchgear, transformers, panelboards, PDUs, rack PDUs | WP61 p.12 |
| Equipment $/kW of DC capacity (2015$) | MV switchgear 8–92; transformers 35–90; LV switchboards 80–200; panelboards 20–40; PDU/RPP 100–400 | WP61 Table 2 |
| 1N UPS, material | €0.20/W IT (2016) | Schneider WP228 p.8 (9.6 MW project, actual deployed costs) |
| VRLA / Li-ion batteries, material | $0.06 / $0.12 per W of UPS (6 min, 2018); service life 4 vs 12 years; Li-ion capex +82% installed, 10-yr TCO −39% | Schneider WP229 Rev 1, Tables 1–3 |
| Generator plant in a 2N design | ≈30% of the electrical-distribution investment (grid connection to rack PDU); N+1/N+2 is now standard | Schneider WP262 (2018) p.2 |
| Grid + diesel backup vs on-site gas engines | €44M vs €64.7M capex for a 67 MW (facility-load) campus, 2019 | Schneider & Wärtsilä WP286 (2020) pp.16–18 |
| Price escalation to 2025 (annual-average PPI) | transformers 335311 +92% (2015→25), +76% (2019→25); switchgear 335313 +77%, +67%; generators 335312 +48%, +41%; engines 333618 +23%; misc. electrical incl. UPS 335999 +43% | BLS PPI API (PCU series) |

Engineering quantities per MW of IT (my judgement, stated so it can be changed):

| Parameter | A0 | A1 | A2 | A3 | A4 |
|---|---|---|---|---|---|
| Design-peak facility load / IT load | 1.7 | 1.35 | 1.4 | 1.3 | 1.2 |
| Generator redundancy on facility load | N+1 on few units (1.25) | N+1 (1.1) | N+1 (1.1) | N+1/N+2 (1.15) | standby 1.0, or on-site prime power N+2 |
| UPS capacity / IT | 2N (2.0) | 4N/3 distributed or block N+1 (1.33) | 1.33 | 1.33 × 1.1 (CDUs and pumps on UPS) = 1.45 | DC UPS / MV rectifier, 4-to-make-3 (1.33) |
| Battery | VRLA 10 min | VRLA → Li-ion, 5 min | Li-ion | Li-ion central + rack BBU (in IT capex) | rack BBU (80 kW × 60 s per shelf) + grid-side BESS |
| Distribution | PDUs with isolation transformers, STS, raised floor | busway + rack PDU | high-amp busway | 2× high-amp busway, 415/480 V AC to 33 kW power shelves (8-to-make-6) | 800 VDC or ±400 VDC busway, sidecar power racks, SST/TRU |

Unit prices (2025$): generators ≈ $500/kW of genset (range 350–700)[^gen]; UPS ≈ $0.31/W of UPS (WP228 €0.20 × 1.1 $/€ × PPI 335999 1.42; range 0.20–0.45); batteries $0.08–0.10/W at 5–10 min; WP61 distribution items × PPI.

[^gen]: Derived from WP286: grid + diesel capex of €44M for 67 MW facility load, assuming gensets are about 55% of that (the rest is MV distribution and grid connection), converted at 1.12 $/€ and escalated with PPI 335312 2019→25 (+41%). **This is the weakest price in the table.** I found no free, primary $/kW for 2–3 MW standby diesel gensets. Press ranges of "$0.5–2M per 2–3 MW unit" ($170–1,000/kW; globaldatacenterhub, not traceable to a primary) bracket it.

### 1.2 Electrical equipment per MW IT (bottom-up, 2025$, $M; share of electrical equipment in brackets)

| Component (NAICS of maker) | A0 legacy/retail colo | A1 hyperscale air | A2 AI air/hybrid | A3 AI liquid NVL72 | A4 800 VDC next-gen |
|---|---|---|---|---|---|
| Standby generators (335312; engines 333618) | 1.06 (35%) | 0.74 (31%) | 0.77 (31%) | 0.75 (29%) | 0.60 (27%) |
| UPS / DC UPS / MV rectifier (335999) | 0.62 (20%) | 0.41 (17%) | 0.41 (17%) | 0.45 (17%) | 0.41 (19%) |
| UPS batteries (335911) | 0.16 (5%) | 0.11 (5%) | 0.13 (5%) | 0.14 (6%) | 0.10 (5%) |
| MV switchgear (335313) | 0.05 (2%) | 0.09 (4%) | 0.09 (4%) | 0.10 (4%) | 0.10 (5%) |
| MV/LV distribution transformers (335311) | 0.10 (3%) | 0.12 (5%) | 0.12 (5%) | 0.12 (5%) | 0.08 (4%) |
| HV substation incl. power transformers (335311, 335313, construction) | 0 (utility MV feed) | 0.15 (6%) | 0.15 (6%) | 0.20 (8%) | 0.25 (11%) |
| LV switchboards (335313) | 0.30 (10%) | 0.25 (11%) | 0.25 (10%) | 0.25 (10%) | 0.12 (5%) |
| Panelboards (335313) | 0.05 (2%) | 0.03 (1%) | 0.03 (1%) | 0.02 (1%) | 0.01 (0%) |
| PDU/RPP, busway, rack PDU (335313 busway; 335999/335931 PDUs) | 0.40 (13%) | 0.20 (8%) | 0.22 (9%) | 0.25 (10%) | 0.15 (7%) |
| Cable and wire (335929; copper 331420) | 0.20 (7%) | 0.17 (7%) | 0.17 (7%) | 0.18 (7%) | 0.12 (5%) |
| Controls, ATS/STS, EPMS, grounding (335313/334513) | 0.12 (4%) | 0.10 (4%) | 0.10 (4%) | 0.12 (5%) | 0.12 (5%) |
| Grid-side BESS (335911/335999) | 0 | 0 | 0 | 0 (some sites) | 0.15 (7%) |
| **Equipment total** | **3.1** | **2.4** | **2.5** | **2.6** | **2.2** |
| **Installed electrical (equipment ÷ 0.55)** | **5.6** | **4.3** | **4.5** | **4.7** | **4.0** |

Not included: on-site *prime* generation for A4 (Section 1.5), utility-side transmission upgrades (Section 3.5), and IT-side power (server PSUs, NVL72 power shelves and BBUs, which are in the IT capex).

### 1.3 Top-down cross-checks and best estimates

| Check | A0 | A1/A2 | A3 | Verdict |
|---|---|---|---|---|
| T&T 2025: US $9.5–13.3/W × electrical 54% (air) or 48% × 1.07–1.10 (liquid) | – | 5.1–7.2 | 4.9–7.0 | Bottom-up is 15–25% **below** T&T. PPI escalation of 2015–16 list prices misses 2023–25 backlog premiums, expediting and electrician wage growth. |
| Schneider WP282 (2020): 2 MW, 10 kW/rack, 2N UPS, $7.02/W total × 40–50% (WP61), × 1.3 to 2025 | 3.7–4.6 | – | – | Bottom-up A0 (5.6) is **above** this small-site Schneider build. Legacy enterprise sites vary widely with redundancy and scale. |
| Uptime/Turner & Seader 2006: Tier III kW-related infrastructure $23.8k/kW (2007$; electrical + mechanical) | ≈ 14–17k/kW electrical in 2007$ | – | – | An upper bound for small Tier III/IV enterprise rooms. Not representative of colo at scale. |
| Eaton (Q3 2025 call): its grid-to-chip content $1.2M/MW cloud, $2.4M/MW AI (no large gensets) | – | bottom-up same scope 1.22 | bottom-up same scope 1.33 | **A1 agrees exactly.** For A3, Eaton's $2.4M is 1.8× the bottom-up. Either AI halls carry much more switchgear, UPS and busway per MW (UPS for liquid-cooling loads, more MV, 2025 prices) or Eaton counts IT-side power (power shelves, BBUs, sidecars). Unresolved. |
| Dell'Oro: DCPI ≈ $120bn in 2030, 22% CAGR, ~200 GW added through 2030 → ≈ $2M of DCPI per MW added (my derivation; DCPI = UPS, thermal, busway, rPDU, racks, services) | – | consistent with UPS + busway + rPDU (~0.8) plus thermal (~1.0–1.3) | – | Order of magnitude agrees. |

**Best estimate of installed electrical capex (2025$ per MW of IT; the range covers bottom-up to top-down):**

| | A0 | A1 | A2 | A3 | A4 (excl. prime generation) |
|---|---|---|---|---|---|
| Best | 5.5 | 5.0 | 5.2 | 6.0 | 5.5 |
| Range | 4–8 | 4–7 | 4–7 | 4.5–8 | 4–8 |
| Equipment / installation / design | 55/30/15 | 55/30/15 | 55/30/15 | 58/28/14 (more factory-built skids) | 60/27/13 (prefabricated power blocks) |

For earlier vintages, deflate with the PPIs above. Prices were broadly flat from 2015 to 2020, then rose 40–90% between 2020 and 2025, most for transformers and switchgear.

### 1.4 Shares for the model's investment column (electrical part only; A1 → A3)

Equipment is ≈55% of installed electrical capex, installation (NAICS 238210, in Construction) ≈30%, design (541330, Prof_Tech) ≈15%. **Within equipment:**

| Maker | A1 | A3 | `upstream_concentration.py` (unsourced) | Verdict |
|---|---|---|---|---|
| 335312 generators (gensets) | 31% | 29% | 20% | Too low in the script |
| 335999 UPS, PDUs, misc. | 21% | 22% | 15% | Too low |
| 335313 switchgear, switchboards, panelboards, busway, controls | 22% | 22% | 30% | Too high |
| 335311 transformers (distribution + share of substation) | 8% | 9% | 15% | Too high for data-center-owned plant. Grid-side power transformers belong to Utilities. |
| 335911 batteries | 5% | 6% | 10% | Too high (Li-ion at 5 min is small; see note) |
| 335920/335929 cable and wire | 7% | 7% | 5% | OK |
| 335930 wiring devices | ~1% | ~1% | 5% | Too high |
| Construction (substation civils, grounding) | 5% | 5% | – | Missing from the script |

Battery note: VRLA needed replacement every ~4 years (WP229). In a steady-state recipe that is a *replacement investment* flow of about 0.25 × battery capex per year for A0. With Li-ion (12-year life) it is negligible.

### 1.5 Redundancy, 800 V DC, on-site generation, lead times

- **2N vs N+1 / distributed redundancy.** Schneider WP228 (9.6 MW project costs) finds that redundant components are 31% of a 2N power chain from MV switchgear to server PSUs, so 2N ≈ 1.45× 1N. Simplifying the architecture (no cross-ties or load bank, one UPS path) saves a further 14%.
  - Microsoft's 4N/3 design reserves 25% of UPS capacity (Flex, ISCA 2021). Typical high-availability sites reserve 10–50% of power and cooling (same paper).
  - Hyperscalers moved from 2N (A0) to 4N/3, block-redundant or N+1 designs (SemiAnalysis). That cuts UPS capacity per MW from 2.0 to ≈1.33 and generator capacity by ~40%.
  - For AI power shelves, NVIDIA uses 8-to-make-6. For 800 VDC power centres it uses 4-to-make-3 at 1.6 MW, giving 4.8 MW blocks.
- **800 V DC (A4).** NVIDIA's claims (blog, May 2025; vendor, not measured):
  - up to 5 pp higher end-to-end efficiency;
  - 45% less copper, or 157% more power per conductor than 415 VAC;
  - up to 70% lower maintenance and up to 30% lower TCO;
  - SST or MV rectifier units up to 7.5 MVA at ≥98.5%.

  NVIDIA's own 2026 execution white paper lists cost, reliability and lifecycle analyses as work *still to be done*, so none of the capex savings is documented yet.

  In the BOM I cut LV switchboards by ~50%, distribution copper and busway by ~30–40%, and transformers by ~⅓. I add a grid-side BESS for load smoothing: NVIDIA reports rack load swings from ≈30% to 100% within milliseconds. The net is roughly −10% of equipment; within the uncertainty, not a proven saving.
- **On-site prime generation (A4, behind the meter).** Overnight capex per kW (EIA / Sargent & Lundy):

  | Technology | $/kW | Price year |
  |---|---|---|
  | Aeroderivative CT | 1,606 | 2023$ |
  | H-class simple cycle | 836 | 2023$ |
  | Combined cycle | 868–921 | 2023$ |
  | Reciprocating engines | 1,810 | 2019$ |
  | SOFC fuel cells | 6,700 | 2019$ |
  | 4-h BESS | 1,744 ($436/kWh) | 2023$ |

  These predate the 2024–26 turbine price surge. EIA AEO2026 (2025$) is higher:

| Technology | $/kW |
|---|---|
| Combined cycle | 1,032 |
| Frame CT | 1,158 |
| Aeroderivative CT | 2,275 |
| Fuel cell | 8,287 |
| Reciprocating engines (AEO2023, 2022$) | 2,240 |

Project disclosures (Section 3.4) span a wide range:

| Project | $/kW | Note |
|---|---|---|
| Williams Socrates, for Meta Ohio | ≈4,000 | incl. pipelines; 1.54× redundancy |
| Entergy Hyperion CCGTs | ≈1,415 | – |
| xAI/Solaris joint venture | ≈720 | equipment only |

Sized at facility load 1.2 × N+2 (≈1.4 kW per kW IT) at $1.5–3.5k/kW, on-site generation adds **$2–5M per MW IT (best ≈$3M)**. That is as large as the whole electrical plant, and it is **power-sector capital** (NAICS 2211 / turbines 333611, engines 333618, fuel cells 335999). Recommendation: book it in Utilities' investment, or in a separate on-site power block, not in AI_facilities' electrical plant.
  - WP286 (2019): a 67 MW gas-engine plant costs 47% more capex than grid + diesel backup (€64.7M vs €44M). 80% of its opex is gas.
- **Lead times.** SemiAnalysis gives >12 months for 50–100 MVA HV transformers. See Section 2.4 for Wood Mackenzie and DOE figures from the trade workstream.

## 2. Where the equipment is made: import shares, 2017–2025

### 2.1 Method

Import penetration is imports / (domestic shipments − exports + imports), in value.

| Series | Source | Caveat |
|---|---|---|
| Imports and exports | US-reported HS6 data via the UN Comtrade public API | The Census trade API now needs a key; USITC DataWeb needs a login and was not used. Check: our 2019 total for HS 8504.21–.34 is $2.568bn, against BIS (2020) $2.56bn. |
| Domestic shipments, 2017 and 2022 | Economic Census, by industry and product line | – |
| Domestic shipments, 2018–21 | ASM, benchmarked to 2022 | – |
| Domestic shipments, 2023–24 | AIES total revenue | 2025 is not published. |

Imports are general imports, not imports for consumption, and exports include re-exports. HS6 cannot isolate UPS or low-voltage switchgear.

### 2.2 Import shares (value)

| Product (HS → NAICS) | 2017 | 2019 | 2022 | 2023 | 2024 | 2025 | Notes |
|---|---|---|---|---|---|---|---|
| Transformers >16 kVA (8504.21–23, .33–.34 → 335311) | 26.5% (30.7% on product basis) | 24.4% (27.9%) | 25.5% (29.7%) | 30.2% | **38.5%** (lower bound) | n/a; imports +24% y/y | Imports $7.19bn in 2024, $8.89bn in 2025. Mexico 32–34%, Korea 19%, Canada 8%, Brazil 6–7%, China <5%. |
| – of which >10 MVA liquid (8504.23) | – | – | – | – | – | – | Imports $2.90bn in 2024, $4.03bn in 2025 (+39%). |
| Large power transformers >100 MVA | – | **82% by units, 73% by value** (BIS 2020) | – | – | – | WoodMac: ≈80% of power-transformer supply imported | No Census domestic series above 100 MVA. |
| Liquid distribution transformers ≤10 MVA | – | 18–20.6% (BIS) | – | – | – | WoodMac: ≈50% of distribution-transformer supply imported | BIS and WoodMac disagree (Section 5). |
| Switchgear >1 kV (8535 excl. arresters + 8537.20 → 335313) | 9.0% (15.2% product basis) | 9.1% | 10.4% (15.1%) | 13.0% | 14.4% | n/a | Imports $2.73bn in 2024, $3.29bn in 2025. Mexico 32–36%, Germany 13–14%, Canada 13–14%. |
| Switchgear + boards + controls, all voltages (8535 + 8537 → 335313+335314) | 42.7% | 45.0% | 48.5% | 49.1% | 50.2% | n/a | 8537.10 includes PLCs and CNC controls, so this overstates LV switchboards. |
| Reciprocating gensets (8502.11–13, .20 → 335312 genset product line) | 44% (upper bound) | 47% | 83% (implausible) | – | – | imports $2.40bn | The domestic genset product line is undercounted (51–69 establishments; exports 76% of it in 2022). Caterpillar, Cummins, Generac and Kohler output partly sits in 333618 or suppressed cells. Vietnam and China are the top sources of the small-genset imports. |
| Lead-acid, stationary incl. VRLA (8507.20; with 8507.10) | 36.5% | 36.1% | 33.1% | – | – | – | – |
| Li-ion (8507.60) | not meaningful | – | 48.3% | – | – | imports $19.7bn | Mostly EV packs. China is 59–69% of imports. |
| Static converters incl. UPS (8504.40 vs 335999, loose) | 58% | 55% | 56% | – | 53% | – | Dominated by computer power supplies. |

**BEA 2017 shares used in the project, for comparison:**

| Product | BEA 2017 | Our range | Verdict |
|---|---|---|---|
| Transformers | 29% | 26.5–30.7% | Agrees |
| Switchgear | 26% | narrow 9–15%, broad 43% | In between; OK as a mixed LV/MV average |
| Generators | 64% | 44% upper bound on our data | Likely **too high** for the large (>375 kVA) diesel gensets data centers buy. The HS 8502.13 (>375 kVA) import value ($0.04–0.27bn a year in 2017–24) is small next to US genset makers' output, which suggests mostly domestic assembly (our judgement; not measured). But 8502.13 imports jumped from $0.17bn to $0.50bn in 2025. |

**Recommendation for the recipe (share of each equipment cell imported, 2024–25):**

| Equipment | Best | Range | Basis |
|---|---|---|---|
| Transformers | 40% | 30–55% | HV power transformers ~75–80%; MV/LV distribution 25–50%. A data center's own transformers are mostly 2.5–3 MVA units. |
| Switchgear | 25% | 15–45% | MV/HV 15%; LV boards higher |
| Gensets | 30% | 20–50% | – |
| UPS | 50% | 35–60% | Loose 8504.40 proxy |
| Batteries (Li-ion) | 50% | 40–70% | – |
| Cable | – | – | Not studied |

### 2.3 NAICS of domestic producers

| Product | NAICS |
|---|---|
| Transformers | 335311 (NAICS 2022: 335311 power, distribution and specialty transformers) |
| Switchgear, switchboards, panelboards, busway | 335313 |
| Relays and industrial controls | 335314 |
| Prime-mover (reciprocating) generator sets | **335312**; turbine gensets are 333611 |
| Reciprocating engines | 333618 |
| UPS | **335999** (Census NAICS 2022 index) |
| Storage batteries | 335911 (merged into 335910 in NAICS 2022) |
| Building wire | 335929 |
| Wiring devices | 335931 |

### 2.4 Prices and lead times (supply-chain analysts and agencies)

- **Transformer prices.**
  - Unit costs since 2019: GSU +45%, power transformers +77%, distribution transformers +78–95% (Wood Mackenzie, Aug 2025). Earlier WoodMac notes gave +60–80% since Jan 2020 (Nov 2023) and +70–75% since 2020 (Jun 2024).
  - NIAC draft (2024): +80% since the start of the pandemic.
  - BLS PPI 335311: +76% from 2019 to 2025. **Agrees.**
- **Transformer lead times.**

  | Source | Year | Lead time |
  |---|---|---|
  | WoodMac | 2021 | average ~50 weeks |
  | WoodMac | 2024 | average ~120 weeks; large power transformers and GSUs 80–210 weeks |
  | WoodMac | Jun 2024 | power and GSU transformers ~150 weeks after receipt of order; pad-mount distribution transformers ~75 weeks |
  | NREL (2024) | 2024 | distribution transformers up to 104 weeks, 4× the pre-2022 level |
  | DOE (2014) | 2010 | large power transformers 5–12 months domestic, 6–16 months foreign |

  WoodMac (Aug 2026) expects a 15% power-transformer shortfall and 8% for substations in 2026, and says EO 14420 (a ban on Chinese bulk power equipment) affects >$22bn of imports since 2025.
- **Switchgear and generator lead times.** No primary source found (gap). Press reports of 1–2 years for large gensets are not verified here.

## 3. Energy use

Definitions used throughout this section:

- **PUE** is the *annualised operating* value (The Green Grid WP49: design projections "are not considered measurements").
- **u** is the annual average IT draw divided by provisioned critical IT capacity, at a site that has finished ramping up.
- **Energy per MW-IT-year** = 8,760 × u × PUE (MWh).

### 3.1 PUE

**Surveys and fleet series (primary):**

| Series | Years | Values |
|---|---|---|
| Uptime survey, per-site average | 2007 / 2011 / 2013–14 | 2.50 (members only) / 1.98 (announced as 1.8) / 1.65 |
| | 2018–2021 | 2018 1.58; 2019 1.67; 2020 1.59; 2021 1.57 |
| | 2022–2026 | 2022 1.55; 2023 1.58; 2024 1.56; 2025 1.54; 2026 1.52 |
| Uptime, capacity-weighted | 2023 / 2026 | 1.47 / 1.36 |
| EPRI, US capacity-weighted | 2024 | 1.32 |
| IEA, global weighted | 2024 → 2030 | 1.41 → 1.29 |
| LBNL, US average | 2014 / 2023 / 2028 | 1.6 / 1.4 / 1.15–1.35 |
| Google fleet, trailing 12 months | 2008 → 2025 | 1.20 (2008) … 1.10 (2019–23), 1.09 (2024–25) |
| Meta | 2017–2024 | 1.10 → 1.08 (1.08 in 2022–24) |
| AWS | 2022–2025 | 1.15 (2022–24), 1.14 (2025) |
| Microsoft | FY24 / FY25 | 1.16 / 1.17; new-site design 1.12 |
| Equinix | 2019 / 2023 / 2024 / 2025 | 1.54 / 1.42 / 1.39 / 1.37 |
| Digital Realty | 2025 | 1.38 portfolio; 1.20 design for new builds |

**LBNL 2024 modelled operating PUE (2023):**

| Site type | PUE |
|---|---|
| Small | 1.91 |
| Mid-size and colo | 1.68 |
| Hyperscale | 1.22 |
| AI-specialised | 1.14 (1.09–1.19) |
| Liquid cooling with dry cooler | ≈1.10 |

| Archetype | Operating PUE, best (range) | Design PUE | Notes |
|---|---|---|---|
| A0 | **1.70** (1.55–2.00) | – | Uptime 2007 model assumed 2.0 |
| A1 | **1.15** (1.08–1.25) | 1.12 (Microsoft) | Operators report 1.08–1.17, below LBNL's modelled 1.22 (their own boundaries; new sites excluded) |
| A2 | **1.25** (1.15–1.40) | <1.3 (SemiAnalysis) | Vertiv/NVIDIA hybrid 1.38 → 1.34 |
| A3 | **1.15** (1.08–1.25) | 1.20 (Digital Realty new builds) | No AI operator publishes a measured PUE |
| A4 | **1.10** (1.05–1.20) | – | 800 VDC's gain (≤5 pp claimed) is *inside* the IT/PUE boundary, not a PUE change |

Liquid cooling moves PUE less than it moves energy. Vertiv found total energy fell 10.2% while PUE fell only 3.3%, because server fan power leaves the IT denominator.

### 3.2 Utilisation of IT load

| Archetype | u best (range) | Evidence |
|---|---|---|
| A0 | **0.50** (0.35–0.60) | Schneider WP37: final actual load ~60% of design. Uptime 2024: 1 in 4 sites <40% of UPS capacity. EPRI: multi-tenant <75 MW average 0.57, peak 0.64. |
| A1 | **0.65** (0.55–0.75) | EPRI: single-tenant >75 MW average 0.75, peak 0.80. Microsoft (128 rooms): peak 65–80% of non-reserve power. Google 2007: 59.5% of actual peak. |
| A2 | **0.70** (0.55–0.85) | LBNL-implied AI server average 60% of rated (training), 40% (inference). Measured 8×H100 training 74–78% of rated. Microsoft peaks: training 97%, inference 79% of provisioned. |
| A3 | **0.75** (0.60–0.85) | Dedicated, training-heavy sites. |
| A4 | **0.80** (0.65–0.90) | IEA ~90% utilisation of accelerated servers. E3 load factor 86%. |

**Fleet-average caveat.** EPRI finds the US fleet fell from ~0.7 to ~0.4 of nominal capacity over 2021–24 because new capacity was still ramping. In the same data, US 2024 energy is 177–192 TWh on 35–44 GW nominal IT, only 4,000–5,500 MWh per MW-IT. For the per-$ recipe use mature u; for levels, add a ramp haircut.

### 3.3 Electricity prices paid

| Evidence | Values |
|---|---|
| EIA average US price, commercial | 10.66 ¢/kWh (2017) → 13.41 (2025) |
| EIA average US price, industrial | 6.88 ¢/kWh (2017) → 8.62 (2025) |
| Virginia, where data centers are mostly billed as commercial | commercial 8.0–9.7 ¢; industrial 9.45 (2025) and 10.08 (2026 YTD) |
| PJM all-in wholesale | $55.5/MWh (2024) → $82.7 (2025) |
| PJM capacity charge | alone $11–18.5/MWh at 100% load factor from 2025/26 |
| ERCOT all-in wholesale | ≈$34–38/MWh |
| Nuclear deal | Talen–Amazon implied ≈$63–67/MWh |

| Archetype | $/MWh best (range) |
|---|---|
| A0 | 110 (85–135) |
| A1 | 75 (55–95) |
| A2 | 80 (60–100) |
| A3 | 85 (60–110) |
| A4 | 85 (55–120) |

Large-load tariffs impose take-or-pay minimums:

| Tariff | Terms |
|---|---|
| Dominion GS-5 (from 2027; from secondary summaries) | ≥25 MW; minimums of 85% of contracted T&D demand and 60% of generation demand; 14-year contracts |
| AEP Ohio | 85% minimum demand |
| Georgia Power | >100 MW; contracts of 5–15 years |
| APS XHLF | 4.2 ¢/kWh (6.2 ¢ incl. riders), at a 92% load factor |

So below u ≈ 0.6–0.85, the bill no longer scales down with use.

**EIA average retail price by sector and state, ¢/kWh (2025 preliminary):**

| Sector | Region | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Commercial | US | 10.66 | 10.67 | 10.68 | 10.59 | 11.22 | 12.41 | 12.59 | 12.75 | 13.41 |
| Commercial | VA | 8.01 | 8.32 | 8.18 | 7.63 | 7.79 | 9.66 | 8.95 | 8.72 | 9.55 |
| Commercial | TX | 8.26 | 8.16 | 8.06 | 7.60 | 8.72 | 9.05 | 8.82 | 8.55 | 8.64 |
| Commercial | GA | 10.09 | 9.79 | 10.02 | 10.08 | 10.61 | 12.10 | 10.70 | 10.87 | 11.50 |
| Commercial | OH | 10.05 | 10.11 | 9.72 | 9.53 | 9.75 | 10.39 | 10.75 | 10.66 | 11.60 |
| Commercial | AZ | 10.50 | 10.64 | 10.25 | 10.11 | 10.33 | 10.80 | 11.79 | 12.23 | 12.47 |
| Commercial | OR | 8.86 | 8.91 | 8.85 | 9.00 | 9.11 | 9.35 | 9.92 | 10.11 | 10.56 |
| Industrial | US | 6.88 | 6.92 | 6.81 | 6.67 | 7.18 | 8.32 | 8.04 | 8.13 | 8.62 |
| Industrial | VA | 6.51 | 6.86 | 6.85 | 6.28 | 6.49 | 7.99 | 8.92 | 8.99 | 9.45 |
| Industrial | TX | 5.35 | 5.39 | 5.45 | 5.07 | 6.12 | 7.13 | 6.60 | 6.12 | 6.55 |
| Industrial | GA | 5.96 | 6.00 | 6.17 | 5.77 | 6.49 | 8.65 | 6.88 | 7.21 | 7.81 |
| Industrial | OH | 6.92 | 7.01 | 6.55 | 6.16 | 6.55 | 7.45 | 7.03 | 7.10 | 8.52 |
| Industrial | AZ | 6.45 | 6.55 | 6.28 | 6.07 | 6.79 | 7.86 | 8.11 | 7.90 | 8.10 |
| Industrial | OR | 5.98 | 5.86 | 5.86 | 5.70 | 5.97 | 6.81 | 7.52 | 8.05 | 8.28 |

January–July 2026 year-to-date: US commercial 13.97 and industrial 9.03; Virginia commercial 11.21; Ohio commercial 13.83 and industrial 10.32.

### 3.4 On-site generation and its fuel

- **Announced vs operating.** Behind-the-meter capacity announced for US data centers is ≈90 GW (Cleanview; >25% of planned capacity), but only ≈2 GW (2.2%) was operating in 2026, rising to ~3 GW by end-2026.
  - EIP counts 74 plants and 143 GW of dedicated gas; GEM counts 189 GW of gas in development tied to data centers.
  - Almost all of it is **natural gas**: aeroderivative and industrial turbines, reciprocating engines, and some SOFC (Bloom).
  - IEA and EPRI publish no share of data-center electricity generated on site. Our estimate is that it is **<1–2% of 2025 data-center MWh**. We derive this from ~2 GW operating against 35–44 GW nominal IT; it is not directly measured.
- **Examples.**
  - Stargate Abilene: 360.5 MW permitted for 8,760 h (TCEQ).
  - xAI Colossus: 15 turbines permitted, up to 35 installed. Southaven: 1,240 MW permitted.
  - Williams for Meta Ohio: 400 MW, $1.6bn.
  - Oracle: VoltaGrid 2.3 GW of engines; Bloom 1.2–2.8 GW.
  - Meta Hyperion's 2.26 GW of Entergy CCGTs are *utility, grid-side*, not behind the meter.
- **Cost of on-site power.**

  | Option | $/MWh |
  |---|---|
  | CCGT at $3.5–5/MMBtu | 41–56 |
  | Engines or aeroderivatives | 71–86 |
  | Turnkey incl. pipelines | 86–99 |
  | Mobile rental | ≈110 all-in |

  Scale the capital component by 1.3–1.5× for N+1/N+2 redundancy. Schneider/Wärtsilä WP286 (Ireland, 2019): gas-engine capex is 47% above grid + diesel, and gas is 80% of opex.

### 3.5 Grid interconnection: costs and who pays

- **Rules.** The trend is that the large load pays, through CIAC, study fees and minimum bills.
  - Texas SB 6 (2025): $100k study fee for loads ≥75 MW, which must pay interconnection costs.
  - PG&E Rule 30: 100% advance of transmission-level service cost.
  - Georgia: data centers pay upstream costs during construction.
  - FERC's PJM co-location order, Dec 2025 (EL25-49).
- **Socialised costs.** JLARC: $3.5bn of PJM transmission for Virginia data centers. PJM IMM: $9.33bn (63.5%) of 2025/26 capacity cost attributable to data-center load. E3 for the Data Center Coalition: ≈50% of the capacity price rise.
- **$/kW.** No primary $/kW for substation or transmission upgrades was found. The one number is Epoch's $164M/GW (≈$0.16M/MW) for utility works, re-quoted from the MISO transmission cost guide. The single Dominion project cited ($23M, Harvard ELI) has no MW attached.
- **Recommendation (gap G6).** Put customer-side substations (≈$0.15–0.25M/MW) in AI_facilities. Put network upgrades in Utilities' investment, recovered through tariffs (CIAC is a transfer, not a purchase).

## 4. Electricity cost per MW of IT per year

| Archetype | u | PUE | MWh/MW-IT-yr | $/MWh | **$k per MW-IT-yr** | One-at-a-time range | Corner bounds |
|---|---|---|---|---|---|---|---|
| A0 | 0.50 | 1.70 | 7,446 | 110 | **819** | 573–1,005 | 404–1,419 |
| A1 | 0.65 | 1.15 | 6,548 | 75 | **491** | 360–622 | 286–780 |
| A2 | 0.70 | 1.25 | 7,665 | 80 | **613** | 460–766 | 332–1,042 |
| A3 | 0.75 | 1.15 | 7,556 | 85 | **642** | 453–831 | 341–1,024 |
| A4 | 0.80 | 1.10 | 7,709 | 85 | **655** | 424–925 | 329–1,135 |

- **Energy is flat across generations.** Energy per MW-IT is roughly flat from A1 to A4 (6.5–7.7 GWh), because rising utilisation offsets falling PUE. Cost differences come from price.
- **CNT cross-check.** CNT charge $105k per NVL72 rack-year. At A3 values, a 132 kW rack costs 0.132 × $642k ≈ **$85k**; CNT's figure implies u × price ≈ 25% higher. That is inside our range, but at the high end.
- **SemiAnalysis cross-check.** Their worked example (28.4 MW IT, u 0.80, PUE 1.25, $83/MWh) gives $729k per MW-IT, inside our A2 range.
- **Facility cost-share check (A3).**
  - Capital: electrical ≈$6M/MW ÷ 0.48 (T&T) ≈ $12.5M/MW of construction; at user cost r + δ ≈ 0.042 + 0.085 that is ≈ $1.6M/yr.
  - Electricity: $0.64M/yr. Other opex: ≈$0.3M/yr.
  - So electricity is ≈25% of facility cost, in line with the engineering notes' 25–30% (DCN:171) and Digital Realty's utilities ≈23% of revenue.

## 5. Cross-checks: independent sources for each number

| Number | Sources | Agree? | Why they differ |
|---|---|---|---|
| Electrical share of facility capex | T&T 2025: 54% air, 48% liquid (cost consultant). Schneider WP61: 40–50% excl. building (vendor). IMPLAN/JLARC-type splits in UP note. | Yes, once the building is added back | WP61 excludes the shell, so its 40–50% sits below T&T's shares, which include the shell. |
| Equipment vs installation within electrical | Schneider WP61 only: 50–60 / 25–35 / 15–20 | Single source | **Gap G1 now has one primary source.** Eaton's content per MW ($1.2M on ~$5M electrical ≈ 25–50% after gensets) is consistent. |
| Installed electrical $/MW | Bottom-up (Schneider unit costs × PPI): 4.3 (A1), 4.7 (A3). T&T × share: 5.1–7.2. Cushman $11.7M/MW (2025) and $17.6M (2026) × ~45%: 5.3–7.9. | Partly | Bottom-up is 15–25% low: PPI does not capture 2023–26 backlog premiums, expediting or wages. Best estimate splits the difference, weighted to top-down. |
| Eaton-scope electrical equipment | Bottom-up $1.22M/MW (A1) vs Eaton cloud $1.2M. Bottom-up $1.33M (A3) vs Eaton AI $2.4M. | A1 yes; A3 no | Eaton's AI figure may include IT-side power (power shelves, BBUs, sidecars) or reflect far more redundancy and busway per MW. Unresolved. The A3 range is widened upward. |
| Transformer price inflation since 2019 | BLS PPI 335311 +76% (2019→25). WoodMac +77% power transformers, +78–95% distribution transformers. NIAC +80%. NREL: distribution transformer prices 4–9× in 3 years (outlier; probably specific units). | Yes (PPI vs WoodMac/NIAC) | NREL's figure is for specific quotes, not an index. |
| Transformer import share | Comtrade/Census calculation: 26.5% (2017), 38.5% (2024, lower bound). BEA 2017: 29%. BIS 2019 LPT: 82% by units / 73% by value. WoodMac: 80% power transformers, 50% distribution transformers. DOE 2022: 82% (re-quotes BIS). | Yes by size class | All-size value shares (~25–40%) mix cheap distribution transformers made in the US with imported large units. WoodMac's 50% for distribution transformers vs BIS 18–21% (2019) is a real gap: different year (post-surge), basis unstated, possibly incl. dry-type and parts. |
| Switchgear import share | Our calculation: 9–15% (MV); 43–50% incl. LV boards and controls. BEA 2017: 26%. | Bracketed | BEA's commodity mixes voltage classes. HS6 cannot isolate LV switchgear. |
| Generator import share | Our calculation: ≤44% (2017, upper bound). BEA: 64%. | No | The domestic genset product line is undercounted in Census. Large data-center gensets are mostly US-assembled, but imports of >375 kVA gensets tripled in 2025. |
| Hyperscale PUE | Google 1.09, Meta 1.08, AWS 1.14–1.15, Microsoft 1.16–1.17 (operators). LBNL modelled 1.22. Uptime capacity-weighted 1.36. EPRI 1.32. | Operators agree with each other; the model and surveys are higher | Operators report mature owned sites on their own boundaries. Surveys include colo and enterprise. |
| AI facility PUE | LBNL 1.14 modelled. Digital Realty 1.20 design. SemiAnalysis <1.3 spec. Vertiv hybrid 1.34. | Loosely | **No measured PUE for any GB200-class site.** |
| Utilisation | Mature: EPRI 0.75 (>75 MW), Microsoft 65–80% of non-reserve power. Fleet: EPRI 0.4 (2024), LBNL 0.5, IEA ~0.47. AI: IEA 0.9, E3 0.86, SemiAnalysis 0.8. | Consistent once ramping is separated from mature sites | IEA's "84% training load factor citing LBNL" is not in LBNL. |
| Electricity $/MW-IT-yr | Our 491–655k (A1–A4). SemiAnalysis worked example 729k. CNT $105k per rack ≈ $795k/MW. Project's dc_cost_buildup uses 8.5¢. | Within range | CNT sits at the top: implies higher u × price. |
| Electricity share of facility cost | Our A3 calculation ≈25%. Engineering notes 25–30%. Digital Realty utilities 23% of revenue. Equinix 14–16%. | Yes | Equinix is retail colo with higher non-power revenue. |
| On-site generation capex | EIA/Sargent & Lundy 2024: aero $1,606/kW (2023$). AEO2026: $2,275 (2025$). Williams–Meta ≈$4,000 incl. pipelines. Solaris JV ≈$720 (equipment). | Wide | Scope differs: equipment only vs turnkey with pipelines, redundancy and 2025 turbine scarcity. |

## 6. Best estimates for the recipe (what to put in `ai_recipe.py`)

**Electrical plant (share of AI_facilities capex).**
- Share: 48–54% (T&T). Use 50% for AI (A2–A3 mix), with a 45–55% band.
- Split each $1 of electrical into:
  - equipment $0.55 (band 0.50–0.60);
  - installation $0.30 → Construction (238210 electrical contractors);
  - design $0.15 → Prof_Tech (541330).
- Within equipment (A3), by maker:

  | Maker | Share of equipment |
  |---|---|
  | Generators 335312 | 29% |
  | UPS, PDU, misc. 335999 | 22% |
  | Switchgear, boards, busway 335313 | 22% |
  | Transformers 335311 | 9% |
  | Cable 335929 | 7% |
  | Batteries 335911 | 6% |
  | Controls and other | 5% |

- These replace the unsourced 30/20/15/15/10/5/5 in `upstream_concentration.py`.

**Imports (if the baseline is opened, R5).**

| Equipment | Share imported, best (band) |
|---|---|
| Transformers | 0.40 (0.30–0.55) |
| Switchgear | 0.25 (0.15–0.45) |
| Gensets | 0.30 (0.20–0.50) |
| UPS | 0.50 |
| Batteries | 0.50 |

**Service lives.**

| Asset | Life | Basis |
|---|---|---|
| Electrical plant | ~15–20 years | Uptime 2007 used 15 years for all non-IT capital |
| UPS electronics | ~10 years | WP229 |
| VRLA batteries | 4 years | WP229 |
| Li-ion batteries | 12 years | WP229 |
| Gensets | ~20–25 years (engineering norm) | No source found in this pass: **UNVERIFIED** |

**Electricity input of AI_facilities.**
- Best $640k per MW-IT-year for A3 (A2–A3 mix: $610–640k); range $450–830k.
- Physical: ≈7.6 GWh per MW-IT-year, at u 0.75 and PUE 1.15.
- In the per-$ recipe, electricity ≈ 25% of AI_facilities' cost at A3.

**On-site generation.** Keep it out of AI_facilities' baseline column. If modelled, it is ≈$3M per MW-IT of turbines, engines or fuel cells (333611, 333618, 335999) plus gas purchases (211000 and 486000), i.e. utility-type capital.

**Grid.**
- Customer-side substation, ≈$0.15–0.25M per MW (inside the electrical plant above): AI_facilities.
- Network upgrades: Utilities' investment. No $/kW source yet.

## 7. Open gaps

1. **Itemised electrical BOM from a current source.** The only engineering $/kW table is Schneider WP61 (2015). The SemiAnalysis BOM, Dell'Oro segment data, and Cushman/T&T element detail are paywalled or not machine-readable. The Cushman 2025 flipbook is JavaScript-only, so its $11.7M/MW is marked UNVERIFIED in the CSV.
2. **Standby genset $/kW** (2–3 MW diesel): no free primary. Our $500/kW is derived from WP286. The Generac–Amazon supply deal (Sep 2026) could pin it down if its MW are disclosed; the page was not reachable.
3. **Eaton A3 content ($2.4M/MW) vs bottom-up ($1.3M):** unresolved scope question.
4. **800 VDC capex effect:** only vendor claims (NVIDIA: up to −30% TCO, −45% copper, +5 pp efficiency). NVIDIA's 2026 paper says the cost analyses are still to be done.
5. **Measured PUE and utilisation for GB200/GB300, xAI and Stargate-class sites:** none published.
6. **$/kW of utility network upgrades, and who owns them (G6):** tariffs show the direction (CIAC, minimum bills) but give no level. Dominion's GS-5 order (SCC PUR-2025-00058) itself was not retrieved (403). The AEP Ohio term details are UNVERIFIED.
7. **PPA price levels** (LevelTen $ levels are gated). The Microsoft–Crane ~$110–115/MWh figure is UNVERIFIED.
8. **HS10 detail for UPS (8504.40.95) and LV switchgear (8537.10.91):** needs a Census API key or a DataWeb login. There is also no 2025 domestic shipments series yet.
9. **Switchgear and generator lead times:** no primary. Transformer lead times are well sourced (WoodMac, NREL, DOE).
10. **Share of data-center MWh generated on site:** no official figure. Our "<1–2% in 2025" is inferred from Cleanview's ≈2 GW operating.

## 8. Sources (primary unless noted; full list with URLs in the CSV)

- **Vendor / engineering white papers (Schneider Electric Data Center Science Center):**
  - WP61 Rev 2 (2015), Electrical Distribution Equipment in Data Center Environments
  - WP228 (2016), OCP architectures
  - WP229 Rev 1 (2018), VRLA vs Li-ion
  - WP262 (2018), MV generator plants
  - WP282 (2020), liquid vs air capex
  - WP286 (2020, with Wärtsilä), gas-engine generation
  - WP37 (2012), oversizing
- **NVIDIA:** 800 VDC white papers (Oct 2025; 2026) and technical blog (May 2025).
- **OCP:** Diablo 400 spec. The PDF is behind a Cloudflare challenge, so it was not downloaded.
- **Standards bodies:** Uptime Institute (Koomey et al. 2007; Global Data Center Surveys 2018–2026); The Green Grid WP49.
- **National labs / agencies:**
  - LBNL 2024 energy report
  - EPRI Powering Intelligence 2024 and 2026
  - IEA Energy and AI 2025
  - EIA / Sargent & Lundy capital costs (2020, 2024); AEO2026 assumptions; EIA EPM and state profiles
  - DOE LPT (2014); DOE Grid Supply Chain Review (2022)
  - NREL distribution transformers (2024)
  - BIS Section 232 transformers (2020)
  - NIAC transformer draft (2024)
- **Official statistics:** BLS PPI (PCU335311/335312/335313/335999/333618); UN Comtrade (US-reported); Census EC 2017/2022, ASM, AIES.
- **Analysts:** Wood Mackenzie (2023–2026 notes); SemiAnalysis (free sections); Dell'Oro press releases; Cleanview; EIP; GEM; E3; Lazard LCOE+ v18.
- **Operators and filings:**
  - Google, Meta, AWS, Microsoft efficiency pages and reports; Equinix; Digital Realty
  - Microsoft Research: Flex (2021) and LLM power (2024)
  - Google, Fan et al. (2007)
  - Eaton Q3 2025 call (via Motley Fool transcript)
  - Talen, Williams and Solaris SEC filings
- **Regulators and market monitors:** PJM BRA reports; Monitoring Analytics; Potomac Economics; FERC EL25-49; Texas SB 6; PG&E Rule 30; Georgia PSC; JLARC.
- **Cost consultants:** Turner & Townsend DCCCI 2025; Cushman & Wakefield Development Cost Guide 2025/2026 (landing page).

