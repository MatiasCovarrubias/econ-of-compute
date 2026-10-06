# Facility capex by archetype: shell, mechanical, electrical, site

Research note for the AI_facilities recipe. Written 28 Sep 2026. Every observation is in
`facility_capex_obs.csv` (173 rows). The CSV records the source, the source type, whether the
number is primary or a re-quote, the URL, and whether it was verified. PDFs are in
`PandP/References/engineering/facility_capex/`.

**Conventions.**
- All $/MW figures are per MW of IT (critical) load unless stated. To convert to per MW of utility
  load, divide by the design PUE: about 1.2–1.4 for air-cooled and 1.1–1.2 for liquid-cooled.
  Only Van Nieuwerburgh's figure is per MW of total facility power.
- Dollars are nominal in the year of the data.
- **Hard cost** means Turner & Townsend's (T&T) scope: shell and core, architectural finishes,
  mechanical and electrical (M&E) fit-out, M&E equipment including tax, duty and freight, and
  general-contractor (GC) preliminaries, margin and contingency. It excludes land, site works,
  utility works, professional fees, client direct costs and IT.
- **All-in** means hard cost plus land, site works, on-site utility works, soft costs, owner
  contingency and white-space fit-out, still excluding IT.

**Search limits in this pass.**
- The session's web-search budget ran out partway through. After that, sources were reached
  through known URLs, links inside fetched pages, and SEC EDGAR full-text search.
- census.gov did not resolve on 28 Sep 2026.
- The full Cushman & Wakefield (C&W) guides are gated flipbooks with no text layer.
- SemiAnalysis and Dell'Oro are paywalled.
- Not reached: RLB, Linesight, Currie & Brown, Gleeds, RSMeans, and the LBNL, NREL and EPRI cost
  pages. They may have usable material.

---

## 1. Headline: best estimate and range by archetype

US data, per MW of IT load. "Hard" uses T&T scope. "All-in" is the facility total, excluding IT.

| Archetype | Year of cost | Hard cost $m/MW: best (range) | All-in $m/MW: best (range) | Main anchors |
|---|---|---|---|---|
| A0 legacy enterprise/retail colo, 4–8 kW/rack, chillers + CRAH | 2010–15 | 9 (6–13) | 11 (8–30) | Schneider WP75 Tier III $7.9–9.8m/MW; WP218 $10.2/W for a 440 kW site; Uptime 2007 Tier III enterprise, 2.2 MW: $30m/MW all-in. T&T: colo/enterprise ±15% vs hyperscale |
| A1 hyperscale air-cooled, 8–15 kW/rack | 2019 / 2022 | 8.5 / 9.8 (7–11.5) | 10 / 11.5 (8–13) | T&T NoVA 8.0 (2019), 9.8 (2022); 8-market US mean 9.8 (2022); JLL global 7.7 (2020); Schneider WP282 $7.0/W (2 MW, 2N); Digital Realty (DLR) NoVA all-in 8.2 (2018), 9.8 (2022) |
| A2 AI air/hybrid, 30–45 kW/rack, rear-door heat exchangers | 2023–24 | 10.6 (9–13) | 12 (10–14) | T&T 8-market mean 10.2 (2023), 10.6 (2024); NoVA 10.2–10.5; KPMG US base build + OFCI (owner-furnished equipment) 12.4 (2025 pricing); DLR Americas all-in 10.6 (Q4 2024); C&W 2025: 11.7 (UNVERIFIED) |
| A3 AI liquid-cooled, GB200/GB300 NVL72, 120–140 kW/rack | 2025–26 | 12 (10.5–14) | 15 (12–18) | T&T 2025 8-market mean 11.06 × 1.07–1.10 = 11.8–12.2; JLL NoVA 11–12 × 1.10; Epoch 11.43/W (T&T-based); operators' landlord cost 8–13 (Cipher, TeraWulf, CleanSpark, Galaxy); DLR Americas all-in 14.1 (Q2 2026); C&W all-in 17.6; Meta Hyperion ≈15 incl. power infrastructure |
| A4 next generation, about 600 kW racks, 800 V DC, on-site power | 2027+ | 13–16 (projection) | 16–22 excl. on-site generation; +2–4 with generation owned | No cost-consultant benchmark exists. Extrapolates A3 at 5–7%/yr escalation plus spec change. NVIDIA claims 45% less copper and up to 30% lower TCO with 800 V DC. On-site generation is a separate asset (Section 5.6) |

**Element shares of hard cost.** Best estimate first, with the range and main source after it.

| Element | A0 | A1 | A2 | A3 | A4 (proj.) |
|---|---|---|---|---|---|
| Electrical, incl. equipment | 45% (40–55) | 54% (T&T air) | 52% (48–54) | 48% (T&T liquid) | 45–55%; power electronics replace transformers and UPS |
| Mechanical, incl. equipment | 25% (15–30) | 22% (T&T air) | 25% (22–30) | 33% (T&T liquid) | 30–35% |
| Shell, core, architectural | 20% (15–30) | 14% | 12% | 9% | 7–9% |
| GC preliminaries and fees | 10% | 10% | 10% | 10% | 8–10% |

**Items outside the hard cost, as a share of all-in.** Best estimates for A3. A1 is similar, with
land lower.

| Item | Share of all-in | $m per MW IT | Anchor |
|---|---|---|---|
| Land (powered land) | 3–5% (best 4%) | 0.2–0.9 (best 0.6) | C&W 2026: $584k/MW in primary markets; Epoch $172k/MW; Carpinelli, Natoli & Taboga (CNT) $0.9m/MW; C&W "site acquisition" 7% of all-in |
| Site works and civil (abnormal ground, roads, drainage) | 3–6% | 0.5–0.9 | Scope gap between T&T (excludes) and KPMG CSA (includes; US CSA ≈ $3.2m/MW in GC scope). Order of magnitude only |
| On-site utility works (customer substation) | 1–3% | 0.15–0.4 | Epoch $164k/MW (Dominion sizing, MISO unit costs); xAI Memphis substation ≈$0.16m/MW (press). Network upgrades are separate: Van Nieuwerburgh (VN) allows $2m/MW of total power as an allowance |
| Professional fees: design, engineering, PM, commissioning, permits | 5–8% | 0.8–1.2 | Uptime/Koomey 2008: A&E = 5% of infrastructure. C&W lists design/soft costs separately. Commissioning is not separately sourced |
| Owner contingency and escalation | 3–8% | 0.5–1.2 | C&W 2026: contingency is the 2nd-largest category, 16% of all-in, which overlaps the GC contingency already in T&T |
| Interest during construction | 3–6% | not a produced input | Uptime 2008: 6.1%. Leave it out of the investment column |

---

## 2. Main evidence

### 2.1 Turner & Townsend Data Centre Construction Cost Index (cost consultant, primary)

Market values come from the chart data behind each edition's "index scores and US$ per watt"
figure. Earlier editions come from the 2022–2024 report pages.

| US market ($/W IT) | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Silicon Valley | 9.4 | 9.8 | 10.3 | 11.49 | 12.15 | 12.8 | 13.31 |
| New Jersey | | | 10.3 | 11.44 | 11.92 | 12.4 | 12.90 |
| Chicago | | | 9.0 | 10.02 | 10.44 | 10.8 | 11.23 |
| Northern Virginia | 8.0 | 8.4 | 9.0 | 9.79 | 10.2 | 10.5 | 10.92 |
| Portland | | | 9.2 | 10.12 | 10.54 | 10.5 | 10.87 |
| Atlanta | | | 7.8 | 8.48 | 8.83 | 9.3 | 9.90 |
| Phoenix | 7.1 | 7.6 | 8.0 | 8.69 | 9.05 | 9.4 | 9.82 |
| Columbus | | | | 8.6 | 8.96 | 9.4 | 9.79 |
| Dallas | | | 7.8 | 8.45 | 8.8 | 9.0 | 9.54 |
| Charlotte | | | | | | | 9.50 |
| Mean of 8 markets (SV, NJ, CHI, NoVA, POR, PHX, ATL, DAL) | | | 8.93 | 9.81 | 10.24 | 10.59 | 11.06 |

- **Escalation.** The US mean grew +9.9% (2022), +4.4%, +3.4% and +4.5% (2025): a CAGR of 5.5% over
  2021–25. NoVA grew 5.3% a year over 2019–25, Silicon Valley 6.0% and Phoenix 5.6%. The global
  index moved +6% (2023), +9% (2024) and +5.5% (2025).
- **Scale drift.** The reference facility grew from 8–32 MW (2022) to 12–40 MW (2024) and 30–50 MW
  (2025). Scale economies therefore bias measured escalation down a little.
- **Liquid-cooling premium.** Liquid-cooled halls cost 7–10% more than air-cooled halls of similar
  IT capacity, from T&T's US Hive database.
- **Element shares.** Air-cooled: 54% electrical, 22% mechanical, 14% shell, 10% GC. Liquid-cooled:
  48/33/9/10.
- **Redundancy.** T&T notes that AI halls can carry less backup power and redundancy, which offsets
  part of the premium. Enterprise or multi-tenant colo can differ from build-to-suit by up to 15%
  (2022 methodology).

### 2.2 JLL 2026 Global Data Center Outlook (cost consultant, primary, local PDF p.24–25)

- **Scope.** "Shell and core" of a single-tenant 50 MW air-cooled hall, excluding land and IT.
  At about $11m/MW this scope must include the base-build M&E plant. It is comparable to T&T scope.
- **Market costs, 2026.** Chicago 12–14, N. Virginia 11–12, Phoenix, Dallas and Atlanta 10–11
  ($m/MW).
- **Global average.** $7.7m (2020) to $10.7m (2025), a 7% CAGR. The 2026 forecast is $11.3m (+6%).
- **Adjustments.** Liquid-cooled +10%; multistorey in the Americas +20%.
- **Tenant fit-out.** "Can cost as much as $25 million per MW for AI infrastructure." The scope is
  ambiguous and likely includes tenant-side systems. Do not add it to the facility cost.
- **Build and lead times.**
  - Average build for a 50 MW hall: 18 months.
  - US equipment lead time: 42 weeks, 83% above 2019.
  - 57% of 2025 projects were delayed by 3 months or more.

### 2.3 KPMG (2026) Data Centre Benchmarking Index (cost consultant, primary, PDF p.6)

Cloud-only greenfield base build at 2025 pricing, excluding white-space fit-out, substations and
fibre. It gives two separate benchmarks, and the second is the only published split of
owner-furnished contractor-installed (OFCI) equipment. USA values below are read from the charts
(±0.1).

| USA, $m/MW | Mechanical | Electrical | CSA (civil, structural, architectural) | GC prelims | Total |
|---|---|---|---|---|---|
| GC scope (construction) | 1.55 | 2.45 | 3.15 | 1.40 | 8.55 |
| OFCI equipment | 1.42 | 0.98 | 1.15 (legend as printed) | 0.30 | 3.85 |
| Sum | 2.97 | 3.43 | 4.30 | 1.70 | 12.4 |

- OFCI equipment is 31% of the total.
- KPMG: "mechanical and electrical plant costs are largely globalised." OFCI spans only $3.5–3.8m
  across Europe, while construction varies 26% (Spain 6.7, UK 8.5).
- The USA is the joint-highest market for construction.

### 2.4 Cushman & Wakefield Data Center Development Cost Guide (cost consultant)

The full guide is gated. Numbers come from the press release (verified) and press re-quotes.

- **2026 guide, released 3 Sep 2026.**
  - All-in greenfield averages $17.6m/MW "for the most modern facilities, excluding chips and
    GPUs" (VERIFIED).
  - That is +21% since Q4 2024, mixing price and specification.
  - Range $8.9–23.3m/MW. Texas is cheapest; Silicon Valley, Chicago, NY, NNJ, Toronto and LA are
    dearest (verified only at CRE Daily).
  - Power infrastructure is the largest category, at 21% (VERIFIED). Contingency is second.
  - Core-and-shell plus sitework is 17% and site acquisition 7% (CRE Daily only).
  - Powered land in primary markets is $584k/MW, +51% year on year (VERIFIED).
  - Equipment prices, Dec 2021 to early 2026: switchgear +60%, copper +46%, generators +33%,
    cooling +32%, transformers +29% (CRE Daily only).
  - MEP trade wages rose 5% a year over 2021–24 (VERIFIED).
- **2025 guide (Q4 2024 data).**
  - Average $11.7m/MW of critical load across 19 markets, from San Antonio 9.3 to Reno 15.0.
  - The snippet also says the construction analysis excluded OFCI, tenant costs, land,
    design/soft costs and owner contingency.
  - All of this is **UNVERIFIED**: it comes only from a search-engine snippet of the flipbook. The
    stated exclusions conflict with the $11.7m being an all-in figure.

### 2.5 Operator filings (primary)

**Digital Realty, "Development Lifecycle" tables.** Total investment per MW of IT capacity. From
2024 the tables state that the total includes a pro-rata share of acquisition, shell and
infrastructure plus the data-center fit-out, so it is all-in excluding IT.

| DLR | 2018Q4 | 2020Q4 | 2022Q4 | 2024Q4 | 2026Q2 |
|---|---|---|---|---|---|
| North America / Americas | 9.04 (60 MW) | 12.87 (62 MW) | 11.68 (153 MW) | 10.63 (318 MW) | 14.10 (1,140 MW) |
| Northern Virginia | 8.24 | 6.68 | 9.81 | 9.99 | 12.76 |
| Other | | | Portland 10.3; Dallas 20.2 (16 MW, outlier) | Chicago 12.0; Dallas 10.8 | Charlotte 15.9; Atlanta 16.8 |

**AI-lease landlords, per MW of critical IT, landlord scope.**

| Operator and project | Year | $m/MW | Notes |
|---|---|---|---|
| Cipher (Barber Lake, Fluidstack/Google) | 2025 | 9–11 | |
| TeraWulf CB-5 | 2025 | 8–10 | Brownfield powered site |
| TeraWulf CB-1/2 | 2025 | 7.2 | $6.0m per gross MW |
| Galaxy Helios Phase I (CoreWeave) | 2025 | about 13 | Total $1.75bn |
| CleanSpark | 2026 | 10–12 | |
| Riot retrofit | 2026 | 3.6 | Retrofit |
| Core Scientific | 2026 | 1.5 | Powered shell only; tenant funds the rest |
| Csquare expansions in existing buildings | 2026 | 4–8 | |

Retrofits and powered-shell deals are not greenfield comparables.

### 2.6 Engineering, standards and vendor sources (mostly A0/A1)

- **Uptime Institute.**
  - Turner & Seader (2006) Tier III: $23,801 per kW of IT plus $262/sq ft (2005$). Via the
    Koomey et al. (2008) True TCO model.
  - That model's 2.2 MW Tier III enterprise site is $65.4m, or **$30m per IT MW**. Of this, M&E
    is 79%, building 8%, interest during construction 6%, A&E 4.4%, fire 1.5% and land 0.8%.
  - Tier cost per kW: I $11.5k, II $12.5k, III $23k, IV $25k, ±30%. This is a re-quote via
    InfoWorld 2008; the original Uptime PDF was not retrieved.
- **Schneider Electric Data Center Science Center.**
  - WP75 rev 4 (2016): complete physical infrastructure per rack at 2.3–3.8 kW/rack. Tier I
    $13.5–18k, II $18–24k, III $24–30k, IV $36–42k. At 3.05 kW/rack that is 4.4–5.9, 5.9–7.9,
    7.9–9.8 and 11.8–13.8 $m/MW.
  - WP218 (2015): a 440 kW stick-built hall costs $5.51m ($12.5/W; $10.2/W excluding IT-room
    racks, PDUs and containment).
  - WP282 (2019/20): a 2 MW, 2N, air-cooled chiller hall costs $7.02/W. Chillers plus CRAH are
    $0.91/W (13%). CDUs add $0.10–0.20/W.
- **Modine (vendor):** heat-rejection equipment content is about $0.6m/MW.
- **NVIDIA (vendor):** 800 V DC cuts copper 45% and TCO up to 30%. Racks will range from 100 kW to
  over 1 MW from 2027.

### 2.7 Economists and analysts (secondary; recorded for tracing)

- **Epoch AI (May 2026).** Facility $11.43/W for a 1 GW campus. This is a re-quote: T&T 2025
  MW-weighted US average plus the 7–10% liquid premium. Land $172k/MW (C&W land price × acres/MW).
  Utility works $164k/MW. Facility life 14 years.
- **Van Nieuwerburgh (2026).** $11m per MW of *total* power (JLL 2026 applied to the wrong
  denominator; $13.2m per IT MW at PUE 1.2), plus $2m/MW for the grid. Meta Hyperion SPV about
  $15m/MW including power infrastructure.
- **CNT (2026).** Non-server capex per NVL72 rack is $1.51m, or $11.4m/MW at 132 kW. Shares: land
  8%, building 16%, electrical 35%, cooling 25%, other 16%. This re-quotes Savills, C&W, Dgtl
  Infra, DCD and a YouTube channel, with unspecified "correction factors".

---

## 3. Cross-checks: where sources agree and disagree, and why

1. **A1/A2 hard cost ($9.5–11m/MW, 2022–25): agree.**
   - T&T NoVA 9.8–10.9, JLL NoVA 11–12 (2026), KPMG US GC scope 8.55 (excluding OFCI), and
     Schneider WP282 7.0 (2019, 2 MW).
   - JLL runs 5–10% above T&T. Its figure is a year later (2026 vs 2025 pricing) and its
     reference is 50 MW single-tenant.
   - KPMG GC-only plus OFCI (12.4) sits above T&T. KPMG's CSA includes civil and site work, which
     T&T excludes.
   - Verdict: consistent once scope and year are aligned.
2. **A3 all-in ($12–18m/MW): the dispersion is real and scope-driven.**
   - Low end, 8–13: landlords (Cipher, TeraWulf, CleanSpark, Galaxy). Many sites are brownfield
     bitcoin sites with existing substations and powered land, and tenants may furnish some
     cooling and electrical items.
   - Middle, 12.8–14.1: DLR NoVA and Americas 2026, including land and fit-out.
   - High end, 17.6: C&W "most modern facilities", including land, soft costs and a large
     contingency; plus DLR Charlotte and Atlanta at 15.9–16.8 (new campuses).
   - VN's Hyperion figure (about 15) includes power infrastructure.
   - Verdict: the best estimate is 15, with 12–18 as the range. The consultant hard cost (T&T/JLL
     about 12) is the more reliable anchor for the produced-capital column. Add explicit
     allowances for land, site works, fees and contingency rather than taking C&W's total.
3. **Shell share: disagree.**
   - T&T: 14% air, 9% liquid. JLL note: multistorey +20%.
   - CNT: building 16% of facility. Schneider WP218: space/building/civil 30% (small 440 kW,
     2015). Uptime 2008: building 8%.
   - KPMG CSA: 35% of base build plus OFCI. C&W: core-and-shell plus sitework 17% of all-in.
   - Reasons: (i) whether civil and site work is inside "shell"; (ii) scale, since small enterprise
     halls carry far more building per kW; (iii) density, since liquid cooling shrinks the
     footprint.
   - Verdict: shell is 9–14% of hard cost for hyperscale. Add 3–6% for site and civil work when
     moving to all-in. CNT's 16% "building" plus 16% "other" is plausible as shell plus site. The
     recipe's current 33% shell (CNT building + other) is too high for A3.
4. **Electrical vs mechanical.**
   - T&T air 54/22 and liquid 48/33. CNT 35/25 of facility including land (38/27 excluding land).
   - KPMG US 28/24 of base build plus OFCI (its large CSA compresses both).
   - C&W: power infrastructure 21% of all-in, a narrower "power infrastructure" definition.
   - All agree that electrical exceeds mechanical, and that liquid cooling moves about 6–11 points
     from electrical and shell to mechanical.
5. **Liquid-cooling premium.**
   - T&T +7–10% (US projects, 2025). JLL +10%.
   - Schneider WP282: about 0% at equal density (immersion, 2 MW); −10% and −14% with 2× and 4×
     compaction.
   - These are consistent: the premium per IT MW is small because chiller and CRAH savings
     ($0.91/W) offset CDUs, manifolds and dry coolers, and footprint falls.
   - Verdict: +8% on hard cost (range 0–12%), with a composition shift toward Machinery.
6. **Redundancy tier.**
   - Uptime (2006/08): Tier III is 1.84× Tier II per kW; Tier IV is 1.09× Tier III.
   - Schneider WP75: Tier III is about 1.29× Tier II (midpoints); Tier IV is about 1.44× Tier III;
     Tier IV is about 2.5× Tier I.
   - The sources disagree on where the step comes, but agree that 2N electrical costs about 1.4–1.8×
     N/N+1 for the kW-related part.
   - T&T 2025 and industry commentary: AI training halls relax redundancy (fewer UPS and gensets,
     N+1 or no-UPS on part of the load). This partly offsets liquid-cooling costs.
   - No post-2020 hyperscale-scale tier differential was found. **Gap.**
7. **Escalation, 2020–26.**
   - T&T US +5.5%/yr (2021–25). JLL global +7%/yr (2020–25).
   - DLR all-in NoVA: 8.2 (2018) to 12.8 (2026), about 5.7%/yr, but with a spec change.
   - C&W: +21% from Q4 2024 to 2026, about 13%/yr. This mixes specification (the AI build) with
     price. Its component PPIs (+29% to +60% over 4 years) show equipment inflating faster than
     the index. The T&T index is dampened by growing reference size and the air-cooled fixed spec.
   - Verdict: like-for-like hard-cost inflation is 5–6%/yr in 2021–25 (about 10% in 2022). Moving
     from A1 to A3 adds another 15–25% through specification.
8. **Regional variation.**
   - T&T 2025: 9.5 (Charlotte) to 13.3 (Silicon Valley), a ratio of 1.40. The main markets
     (NoVA, Dallas, Phoenix, Atlanta, Columbus) cluster within ±7% of 10.2.
   - JLL: Chicago is the priciest main market; Dallas, Phoenix and Atlanta the cheapest.
   - C&W: Texas cheapest.
   - DLR's regional differences mix project phases.
   - Verdict: a national benchmark ≈ NoVA × 0.97. Use the 8-market mean, not NoVA, for a national
     cell.
9. **Build time.**
   - JLL: 18 months for 50 MW.
   - Fed FEDS 2025-109 (Dodge data): mean 19.8 months from start to completion for projects over
     $250m (median 18, p90 35); plan-to-start 15 months; 30% of plans abandoned.
   - Agree: 18–20 months construction, plus about 12–15 months of planning. A3 speed builds
     (Abilene, Colossus) are outliers at 4–16 months per building (see the TTB note in
     `econ-of-ai/.../Time to Build/`).
10. **National aggregate sanity check (indicative).**
    - C30 data-center put-in-place was $49.7bn in 2025. JLL North America inventory rose by about
      8 GW (32 to 40 GW) in 2025.
    - At about $11m/MW hard cost, completions alone imply about $88bn, and with 66 GW under
      construction put-in-place should be larger still.
    - C30 therefore appears to capture about half or less. This is consistent with the sizing
      note's finding that C30 undercounts (owner-built campuses, OFCI and fit-out may be outside
      the reported project value). Timing and scope make this indicative only.

---

## 4. Equipment vs installation inside electrical and mechanical (gap G1)

| Source | Electrical: equipment share | Mechanical: equipment share | Notes |
|---|---|---|---|
| Schneider WP218 (2015, 440 kW, US labour rates; Schneider cost calculator) | 71% materials / 29% labour | 72% / 28% | "Materials" include bulk cable, pipe and panels, i.e. manufactured goods, not only major equipment |
| KPMG (2026) US: OFCI share of discipline total | ≥29% | ≥48% | Lower bounds. GC scope also buys contractor-furnished equipment (switchboards, busway, pumps, CRAHs) |
| Schneider WP282 (2019) | n/a | Chiller + CRAH = $0.91/W installed, of $7.02/W | |
| Modine (2026) | n/a | Heat rejection ≈ $0.6m/MW | About 15–20% of A3 mechanical ($4m/MW) |

**Best estimate.** Manufactured equipment and materials are about 60% of electrical (range
45–72%) and about 60% of mechanical (range 50–72%; about 65% for liquid-cooled, since CDUs, dry
coolers and chillers are factory-built). Installation labour, contractor overhead and profit are
the remaining about 40%.

The labour share is higher in large hyperscale builds than in WP218's small hall. KPMG shows
electrical construction (GC) at 2.5× OFCI electrical in the US. Wages grew 5%/yr (C&W) while
equipment PPIs grew faster, so the equipment share probably rose in 2022–25.

---

## 5. Mapping to producing industries and national-accounts treatment

### 5.1 Supply-chain column

For A3, per $15m/MW all-in. This is a proposed replacement for `FAC_COL` in `ai_recipe.py`.

| Element | $m/MW | Producing industry (model sector; BEA 2017 detail) |
|---|---|---|
| Shell, core, architecture (9% of hard) | 1.08 | Construction (2332A0) |
| GC preliminaries and fees (10%) | 1.20 | Construction |
| Electrical equipment (60% of 5.76) | 3.46 | Electrical: 335311 transformers, 335313 switchgear, 335312 generators (gensets partly 333611 engines), 335911 batteries, 335999 UPS, 335920 cable |
| Electrical installation (40%) | 2.30 | Construction (electrical contractors 23821 inside 2332A0) |
| Mechanical equipment (65% of 3.96) | 2.57 | Machinery: 333415 HVAC/chillers/CRAH/CDU, 333914 pumps, 333413 fans; some 332 fabricated metals (pipe, manifolds) |
| Mechanical installation (35%) | 1.39 | Construction |
| Site works and civil | 0.60 | Construction |
| On-site substation | 0.30 | about 50/50 Construction and Electrical (335311/335313). Ownership G6: often utility-owned and paid through contribution-in-aid-of-construction |
| Professional services: design, engineering, PM, commissioning | 0.90 | Prof_Tech (541300; 541330) |
| Owner contingency | 0.60 | Pro-rata across the rows above |
| Land | 0.60 | Not produced. Exclude from I_f; keep as a non-reproducible asset or ignore |
| **Produced total** | **14.4** | Construction ≈ 49%, Electrical ≈ 26%, Machinery ≈ 19%, Prof_Tech ≈ 6.5% (after pro-rating contingency). With 70% equipment shares: Construction ≈ 43%, Electrical ≈ 30%, Machinery ≈ 20%, Prof_Tech ≈ 6.5% |

The current recipe, 33/40/27 (CNT), overweights Electrical and Machinery relative to this
column. That is because CNT has no installation labour: CNT's rack table has no GC or installation
line and puts all electrical and cooling spend on equipment.

A1 with T&T air shares 54/22/14/10 and a 60% equipment share, plus site works 5, substation 2 and
fees 7 per 100 of hard cost, gives: Construction about 53%, Electrical about 29%, Machinery about
12%, Prof_Tech about 6%.

### 5.2 Depreciation implied

Long-lived parts (shell, site and civil) are about 15–20% of produced facility capex. Plant is
80–85%.

- Shell at 0.0247 (BEA offices) and plant at 0.10: δ_f ≈ 0.085–0.09, as the plan expects.
- Plant at 1/14–1/15 (Epoch; JLL shows refresh cycles, not replacement): δ_f ≈ 0.06–0.07.

### 5.3 How national accounts record it

- **Census C30.** Data centers are a line under private office. Value put in place *includes*
  M&E installations: plumbing, heating, electrical, central AC and emergency backup power. It
  *excludes* special-purpose equipment such as racks and servers. The text is as quoted in
  `dc_structures_sizing.tex`; it could not be re-verified today because census.gov was unreachable,
  so it is UNVERIFIED in this pass. Whether C30 value includes A&E fees and interest during
  construction, as the general C30 definitions are usually read, is also UNVERIFIED here. So in
  C30, integral plant, whether contractor- or owner-furnished, counts as structures if reported in
  the project value.
- **BEA NIPA 5.4/5.4U** (Sept 2025): a "Data centers" line under office structures. It is deflated
  by an equal-weight composite of the BLS industrial-building and warehouse PPIs (VERIFIED on the
  BEA page; the Census source is not stated there).
- **BEA investment.** All of it enters as a Construction (structures) commodity. The BEA
  Construction (2332A0) input column buys little switchgear or transformer output
  (`dc_upstream_plan.tex`). Transformers, switchgear and generators reach buyers mainly as
  equipment investment. This is the core of plan decision R4.
- **ONS (24 Aug 2026).** Building and *integral* systems (electrics, plumbing, heating,
  ventilation, water) go to "other buildings and structures". **Racks, cabinets, power
  distribution units, back-up generators and monitoring tools go to "other machinery and
  equipment".** Servers, storage and network equipment go to ICT. ONS does not itemise UPS,
  chillers, transformers or switchgear. The ONS split supports routing stand-alone generators and
  PDUs (and, by extension, OFCI equipment) directly to Electrical and Machinery, not through
  Construction.
- **Fed FEDS 2025-109.** Assumes 30% structures / 70% high-tech equipment for total data-center
  investment in 2024, with 80% of equipment imported. This is IT-inclusive, so it is not a
  facility split.

**Recommendation for R4.** Keep the supply-chain view (Section 5.1). Report a national-accounts
variant in which equipment and installation both go to Construction and the equipment then
appears in Construction's input column. The difference between the two routes is 45–55% of the
facility column.

### 5.4 Archetype spec corrections from the sources

- **A1.** PUE 1.1–1.2 is consistent with the sources. T&T's reference hall grew from 8–32 MW (2022)
  to 30–50 MW (2025).
- **A2.** Keep it. Note that T&T 2023–24 do not price it separately: they say liquid designs were
  excluded from the 2024 index.
- **A3.** GB300 NVL72 is about 142 kW per rack (NVIDIA via VN). CNT uses about 132 kW. Liquid
  closed loop with dry coolers is typical (WP282 design: 40°C water, 100% free cooling).
- **A4.** NVIDIA's Kyber, 2027, has 800 V DC and 1 MW racks. An industry forecast in an S-1
  (Accelevation, citing "BCE", the industry consultant that prospectus relies on) gives 250+ kW by
  2027–28, 600+ kW by 2028 and 1 MW niches by 2031. The 600 kW spec is plausible for 2028.

### 5.5 A4 notes

There are no benchmarks.

- **Expected shifts:**
  - Electrical moves from transformers, UPS and PDUs to solid-state transformers, rectifiers and
    DC busway: still Electrical, but more semiconductor-heavy.
  - Copper falls 45%.
  - Storage (BESS) is added to smooth load spikes.
  - Shell share falls further with density.
- **On-site generation** (gas turbines or reciprocating engines plus BESS) is a separate power
  asset. Treat it either as Utilities capital (Section 5.1, G6) or as an f-owned
  Machinery/Electrical asset worth about $2–4m per IT MW (turbine capex of about
  $2,000–2,500/kW × PUE × N+1). That capex range is **UNVERIFIED** in this pass; it is Goldman's
  $2,500/kW via the project notes, a re-quote.

---

## 6. Open gaps

1. **Equipment vs installation (G1).** Only one bottom-up engineering split was found (WP218,
   small, 2015) plus KPMG's OFCI lower bound. Next steps:
   - Schneider's Data Center Capital Cost Calculator (TradeOff Tool; login-free web tool, not
     scraped).
   - SemiAnalysis Datacenter Anatomy (paywalled).
   - Vertiv, Eaton and Schneider investor-day "content per MW". The decks were not reachable:
     Vertiv IR pages are JS-rendered, and EDGAR full-text search found no per-MW content statement
     from Vertiv or Eaton.
2. **C&W guides (2024, 2025, 2026).** The full element tables are gated. The $11.7m (2025) and its
   scope note are UNVERIFIED.
3. **Tier and redundancy differential at hyperscale scale after 2020.** Only 2006–2016 enterprise
   data exist (Uptime, Schneider).
4. **A4 costs.** There are no consultant benchmarks. 800 V DC and on-site generation costs are
   vendor claims or re-quotes.
5. **Soft costs and commissioning.** No current source splits design, commissioning and
   permitting. Uptime's 5% A&E (2007) is dated.
6. **Grid interconnection ownership and size (G6).** Epoch's $0.16m/MW (on-site substation) and
   VN's $2m/MW (network allowance) differ by 12×. They are different objects, and utility tariffs
   (contribution-in-aid-of-construction) decide who books them.
7. **Census C30 definitions** could not be re-verified today (DNS failure). Whether C30 includes
   OFCI equipment for owner-built hyperscale campuses is untested.
8. **Not reached** (web-search budget exhausted): RLB, Linesight, Currie & Brown, Gleeds, RSMeans,
   LBNL, NREL, EPRI, Omdia and Dell'Oro physical-infrastructure market sizes, and CBRE cost data.
   CBRE's 2025 Global Data Center Trends has no construction-cost figures (checked).
