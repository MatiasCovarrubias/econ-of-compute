# Data-center operations and resource use, by archetype

Status: research note, 28 Sep 2026. Input to `recipe_plan.md` Phase 1 steps 1–3 (f's operating column) and step 4 (δ_f).
Every number below has a row in `operations_obs.csv` (311 rows: source, page or table, primary or re-quote, and origin when it is a re-quote).
PDFs are in `References/engineering/operations/` (37 files).

**Units and conventions**
- **Per MW:** all "per MW" figures are per MW of IT (critical) load, per year, in 2025 USD, unless stated otherwise.
- **Utilisation (u):** the ratio of average IT draw to IT capacity.
  - A0 and A1: 0.7.
  - A2 to A4: 0.8. LBNL has training at 80% and inference at 40% of hours; Epoch uses 71% facility utilisation.
- **Electricity comparator:** $75–80 per MWh times PUE.
- **WUE:** litres of water per kWh of IT energy.
  - Consumption basis: Microsoft and LBNL.
  - Withdrawal basis: AWS and Meta.
  - Withdrawal ≈ consumption ÷ 0.75–0.79. The ratio is 0.79 at Google (2024) and 0.77 at Equinix, and Han et al. (2026) report 0.77–0.79.

**Archetypes**

| Code | Description | Specs |
|---|---|---|
| A0 | Legacy enterprise or retail colo | Pre-2015; 4–8 kW/rack; chillers, CRAH and cooling towers |
| A1 | Hyperscale cloud, air-cooled | 2015–22; 8–15 kW/rack; evaporative or adiabatic free cooling |
| A2 | AI air-cooled or hybrid | 2023–24; H100; 30–45 kW/rack |
| A3 | AI liquid-cooled | 2025–26; GB200/GB300 NVL72, ~130–142 kW/rack; direct-to-chip closed loop; dry coolers or chillers |
| A4 | Next generation | 2027+; ≥600 kW racks; immersion or two-phase; 800 VDC; heat reuse |

**Corrections to the indicative specs**
- **A0 rack density:** 4–8 kW is right for the stock. Uptime's 2025 survey gives an average modal density of 7.5 kW once ≥30 kW outliers are excluded, 4–6 kW is the most common value, and few sites exceed 30 kW.
- **A1 PUE:** 1.1–1.2 holds for the best hyperscalers (Google 1.09, Meta 1.08, Microsoft 1.16–1.17). LBNL's modelled hyperscale aggregate is 1.22.
- **A3 rack power:** a GB300 NVL72 is ~142 kW (Van Nieuwerburgh 2026, quoting NVIDIA), not 120.
- **A3 and water:** direct-to-chip does **not** by itself mean low water. With cooling towers, LBNL puts a liquid-cooled hall at 2.0 L/kWh. The water saving comes from warm-water dry heat rejection.

---

## 0. Headline table: best estimate [range] per MW-IT-year

| Line | A0 legacy | A1 hyperscale air | A2 AI hybrid | A3 AI liquid | A4 next-gen | Supplying industry |
|---|---|---|---|---|---|---|
| Site WUE, L/kWh IT (consumption) | 2.0 [1.3–3.7] | 0.30 [0.10–1.04] | 0.50 [0.20–1.04] | 0.05 [0–0.3]; 2.0 if towers | 0.02 [0–0.13] | — |
| Water & sewer $k | 26 [10–100] | 4 [1–28] | 7 [2–32] | 0.6 [0–7]; 62 if towers | 0.2 [0–3] | Utilities (221300) |
| Facility staff (FTE/MW, incl. contractors & security) | 5 [3–10] | 1.3 [0.9–1.7] per 30–40 MW hall; 0.6 [0.4–1.0] per campus | 0.7 [0.3–1.5] | 0.5 [0.3–1.0] | 0.3 [0.15–0.5] | Labour + Admin |
| Own staff payroll, loaded (excl. security & cleaning) $k | 400 [250–700] | 133 [80–180] | 90 [60–130] | 60 [40–130] | 40 [25–70] | Labour (VA) |
| M&E maintenance $k | 150 [90–300] | 70 [50–150] | 100 [65–170] | 120 [90–190] | 150 [90–250] | Construction (230301); some 811300 |
| Security $k | 150 [60–320] | 43 [25–85] | 30 [20–60] | 20 [10–45] | 15 [8–40] | Admin & support (5616) |
| Cleaning $k | 40 [20–75] | 13 [8–21] | 7 [4–12] | 5 [2–8] | 3 [1–6] | Admin & support (5617) |
| Insurance (facility) $k | 10 [5–30] | 10 [5–28] | 12 [6–30] | 15 [8–40] | 20 [10–50] | Finance & insurance (524) |
| Real-property tax (facility), after abatements $k | 80 [40–330] | 50 [20–120] | 70 [25–130] | 80 [30–150] | 95 [35–180] | Taxes on production (not a purchase) |
| Operator IT/network ops, software, DCIM $k | 100 [60–350] | 60 [30–65] | 50 [30–70] | 50 [30–80] | 55 [30–90] | Info (517, 513210/518) + 5415 |
| Other (generator fuel & testing, consumables, admin) $k | 40 | 25 | 25 | 30 [20–50] | 30 | 324110, 5416, misc. |
| **Total non-electric facility opex $k** | **~1,000 [600–1,600]** | **~410 [300–550]** | **~390 [300–520]** | **~380 [280–550]** | **~410 [300–600]** | |
| Electricity $k (u, PUE, $75–80/MWh) | ~760 (0.7, 1.65) | ~530 (0.7, 1.15) | ~680 (0.8, 1.30) | ~630 (0.8, 1.2) | ~580 (0.8, 1.10) | Utilities (2211) |
| Non-electric opex ÷ electricity | ~1.3 | ~0.75 | ~0.6 | ~0.6 | ~0.7 | |
| M&E plant life (years, physical) | 18 | 18–19 | 19–20 | 19 | ~19 (few data) | |
| Plant δ (BEA geometric 1.65/L) | 0.09 | 0.09 | 0.085 | 0.088 | 0.09 | |

**Not in the facility column**
- **IT personal-property tax:** falls on AI_compute (z). At Loudoun rates it is ≈1.24% of the IT purchase price a year, which is ~$280k/MW-yr for NVL72 IT at ~$21m per MW. Many localities abate it to near zero; the JLARC range is 0.05–1.44% a year.
- **Tenant connectivity:** also belongs to z. That is CNT's $20k per rack-year network line (~$150k/MW) and Equinix cross-connects.

**What this means for the recipe (A3, per $1 of electricity)**
- Non-electric opex is ≈ 0.60 per $1 of electricity. The purchases in it are:
  - Construction repairs: 0.19
  - Admin (security and cleaning): 0.04
  - Insurance: 0.024
  - Information/software: 0.08
  - Water: 0.001
  - Other: 0.05
- Own labour ≈ 0.10 and taxes ≈ 0.13 per $1 of electricity.
- **Converted to $1 of AI services:** with f's electricity at 0.080 per $1 of AI services (`ai_recipe.py`), this gives:
  - Repairs 0.015
  - Admin 0.003
  - Insurance 0.002
  - Information 0.006
  - Other 0.004
  - Water ≈0
  - Labour 0.008
  - Taxes 0.010
- **The 50/25/25 split in `ai_recipe.py` is contradicted.** Facility labour is ≈ 0.10–0.16 of non-electric opex, not 0.5. Professional/technical services are small and consist mostly of software.
- **CNT's Table A3 gives 0.81 per $1 of electricity** ($85k against $105k per rack-year). That is higher than here because it includes network, which belongs to z, and an unexplained "other" line of $40k.

---

## 1. Water

### 1a. Site WUE by cooling technology (LBNL 2024 simulations, 965 US weather stations)

Values are read from Fig. 4.4, p.46, and are accurate to about ±0.05.

| Cooling system | Scale | Site WUE, median [whiskers] | Simulated PUE | Archetype |
|---|---|---|---|---|
| Water-cooled chiller + tower, no economiser | small | 3.2 [2.4–4.1] | 1.70 | A0 |
| Water-cooled chiller + tower | midsize/colo | 2.9 [2.2–3.7] | 1.53 | A0 |
| Waterside economiser + water-cooled chiller | midsize | 2.5 [2.0–3.2] | 1.38 | A0 |
| Airside economiser + water-cooled chiller | midsize | 1.3 [0.3–2.35] | 1.45 | A0 |
| Air-cooled chiller / DX / dry cooler | midsize | ≈0.05 (humidification) | 1.84 / 1.87 / 1.60 | A0 |
| Waterside economiser + water-cooled chiller (towers) | large | 2.2 [1.75–2.75] | 1.12–1.13 | A1 (Google-type) |
| Airside economiser + adiabatic, water-cooled chiller trim | large | 0.45–0.5 [0–1.55] | 1.15 | A1 (≈43% of hyperscale, Fig 4.2) |
| Airside economiser + adiabatic, air-cooled chiller trim | large | ≈0.01* | 1.17 | A1 (≈42% of hyperscale) |
| Dry cooler with adiabatic assist | large | 0.25 [0–0.55] | 1.21 | A1/A2 |
| Liquid IT + waterside economiser + tower | large | 2.0 [1.65–2.45] | 1.14 | A3 with towers |
| Liquid IT + dry cooler with adiabatic assist | large | 0.13 [0–0.3] | 1.10 | A3 |
| Liquid IT + dry cooler (air-cooled chiller trim) | large | ≈0.0 | 1.10 | A3/A4 |

\* LBNL says this value is too low. Operators report 0.1–0.3 for similar systems, and at 0.2 the hyperscale aggregate would rise from 0.32 to 0.40 (p.47).

**Aggregates for 2023 (Fig. 4.5)**

| Segment | WUE | PUE |
|---|---|---|
| Small | 0.32 | 1.91 |
| Midsize/colo | 0.67 | 1.68 |
| Hyperscale | 0.32 | 1.22 |
| AI-specialised | 0.61 | 1.14 |

- The US average is 0.36, rising to 0.45–0.48 by 2028.
- Total US on-site consumption was 21.2 GL in 2014 and **66 GL in 2023**. Hyperscale and colo are 84% of the 2023 figure.

**Climate**
- Microsoft's own sites (Li et al., Table 1) range from **Arizona 1.63** and Washington 0.95 to Illinois 0.74, Texas 0.25, and **Virginia/Iowa 0.14**. New Nordic and Irish builds are at 0.01–0.02.
- Hot-arid summer peaks reach 9 L/kWh (Karimi 2022, via Li).
- Uptime: a large 25 MW site free-cools 90–95% of the year, against 30% for a small 8 MW open-system site.

### 1b. Operator fleet WUE by year

| Operator | Basis | Series |
|---|---|---|
| Microsoft | consumption | early 2000s 2.3 → 2021 0.49 → FY24 0.30 → FY25 0.27 (Americas 0.38 / 0.34); fleet PUE 1.16–1.17 |
| AWS | withdrawal | 2021 0.25 → 2022 ~0.19 → 2023 0.18 → 2024 0.15 → 2025 0.12; free air ~90% of hours, evaporative above ~85°F; 2.5 bn gal withdrawn in 2025 |
| Meta | withdrawal | 2017 0.24, 2018 0.27, 2019 0.27, 2020 0.30, 2021 0.26, 2022 0.20; PUE 1.08; 2024 ~0.18 (UNVERIFIED) |
| Google | derived from 2025 report | consumption ≈1.04, withdrawal ≈1.32 L/kWh IT; 7.8 bn gal consumed, 9.9 withdrawn (2024) |
| Equinix (retail colo, A0-like) | withdrawal (basis not stated) | portfolio 1.07 (2023) → 0.95 (2024); **evaporative sites only 1.63 → 1.55**; PUE 1.39 |
| Digital Realty | — | 0.59 (2025, −15.7% y/y); ~25% of sites evaporative (latter UNVERIFIED) |

Google says water-cooled plants use ~10% less energy than many air-cooled ones (Hoelzle 2022).

**Old vs new, according to the operators themselves**
- Microsoft went from 2.3 to 0.27, down about 90%.
- Equinix's evaporative legacy sites run at 1.55, against 0.12–0.30 for air-first hyperscale fleets.
- For AI builds:
  - Microsoft: every new design since August 2024 uses closed-loop chip-level cooling that consumes zero water for cooling. That avoids >125 ML per datacenter per year and costs a "nominal increase" in energy (no number given). The pilots are Phoenix and Mt Pleasant.
  - Fairwater, Mt Pleasant: water-free for >90% of hours.
  - Crusoe/Stargate Abilene: closed loop, initial fill 1.7 Mgal, recirculated for up to 15 years, annual use below 10 households.
  - Meta Hyperion: closed-loop glycol, dry cooling for most of the year.

### 1c. Site vs source water

**Power-plant water per kWh of electricity (consumption)**
- LBNL 2024: **4.52 for data centers** (4.35 US average, includes hydro reservoir evaporation). US data centers' indirect water was ~800 GL in 2023, **about 12× on-site water**.
- Other estimates: WRI via Li 3.14; Meta scope-2 3.7; Mytton 2.18.
- Thermoelectric only: Green Grid 1.8, from NREL 2003.
- Withdrawal is ~43.8.
- **Best: 4.4 [3.1–7.6] L/kWh.**

**Where the "industry average WUE 1.8 L/kWh" comes from:** it is LBNL 2016's *assumed on-site water per kWh of total site energy*. Siddik et al. 2021 reuse it, and vendor blogs then quote it as an average. It coincidentally equals the Green Grid thermoelectric factor. Per IT kWh it is ~2.9–3.1, which matches the legacy A0 figures (Uptime 2016: 6.75 Mgal per MW-yr ≈ 2.9; Mytton 25.5 ML per MW-yr). Do not cite 1.8 as a measured fleet average. Uptime's surveys publish no average WUE; only 47% of operators even collect water data (2025).

**Amazon's "industry average 0.84"** is constructed: 0.56 consumption (de Vries-Gao 2025) × 1.5 for three cycles of concentration.

### 1d. Price of water

**Loudoun Water, per 1,000 gal (rate study Oct 2024; rates page 2026)**

| Charge | 2024 | 2025 | 2026 | 2027 |
|---|---|---|---|---|
| Commercial Tier 1 | 3.86 | 4.13 | 4.42 | 4.73 |
| Commercial Tier 2 | 6.63 | 7.09 | 7.59 | 8.12 |
| Sewer | 5.76 | 6.16 | 6.59 | 7.05 |
| Reclaimed | 1.80 | 1.93 | 2.07 | 2.21 |

Rates rise ~7% a year.

**Other price evidence**
- **PNNL-34006, industrial rates by region (2021$):** water $2.74–5.63, wastewater $3.12–11.90. Real escalation is **3.0% a year for water and 3.2% for wastewater**.
- **Phoenix:** $6.59–12.30 per 1,000 gal for water alone, depending on season and on inside/outside the city. The high season coincides with evaporative peaks.

**All-in cost per 1,000 gal withdrawn**
- Towers discharge only blowdown (~25% of withdrawal), so sewer applies to that share.
- Loudoun: $5.67 (2025) to $6.07 (2026). Reclaimed ≈ $3.5 all-in.
- **Best: $6 [3.5–12.5].** The earlier note used $10 (FC), which is inside the range but high for Loudoun.

**Capacity charges.** Loudoun charges water-cooled data centers an availability charge of $15.62 per gallon-per-day of capacity. Sized on peak demand, that is roughly $0.2m one-time per MW for A1 (our derivation).
- Peak-day factors are 4.5–30 (Han et al. 2026). ICPRB finds summer months at ~3× the annual average and peak days up to 10×.
- The binding cost of water is therefore **peak capacity and permitting, not the annual bill**.

### 1e. Water cost per MW-year

Computation: IT MWh = 8,760 × u; × WUE (consumption) ÷ 0.75 → withdrawal; ÷ 3.785 → gallons; × $6 per 1,000 gal.

| Arch. | u | WUE | $/MW-yr [range] | Electricity $/MW-yr | Water ÷ electricity |
|---|---|---|---|---|---|
| A0 | 0.7 | 2.0 | 25,900 [9,800–99,900] | 758,800 (PUE 1.65) | 3.4% |
| A1 | 0.7 | 0.30 | 3,900 [800–28,100] | 528,900 (1.15) | 0.7% |
| A2 | 0.8 | 0.50 | 7,400 [1,700–32,100] | 683,300 (1.30) | 1.1% |
| A3 | 0.8 | 0.05 | 560 [0–6,900]; 62,000 if tower-rejected | 630,700 (1.20) | 0.1% |
| A4 | 0.8 | 0.02 | 220 [0–3,000] | 578,200 (1.10) | 0.04% |

**Cross-checks**
- Epoch's 1 GW AI campus: $6k per MW-yr, about 1% of opex.
- JLARC Virginia 2023: 2.1 bn gal on ~5,050 MW of facility demand ≈ 416k gal per MW-yr ≈ 0.26 L per facility kWh at u = 0.7, i.e. $2.5k/MW-yr at $6. That is an A1-heavy mix, one third of it reclaimed.
- ICPRB: 800 gal/day per MW of permitted capacity (site range 100–1,600) ≈ $1.8k/MW-yr.

### 1f. Water for electricity: the trade-off, old vs new

ΔPUE values are from LBNL Fig. 4.4. Dollars use u = 0.7, $75/MWh and $6 per 1,000 gal. Source water uses 4.4 L/kWh.

| Switch | ΔPUE | Extra electricity $/MW-yr | Site water saved | Extra source water | Private verdict |
|---|---|---|---|---|---|
| A0: water-cooled chiller + tower → air-cooled chiller | +0.30 | ~$138k | 2.9 L/kWh ≈ 17.8 ML (~$38k) | ~+1.3 L/kWh-IT (8 ML) | Towers pay; this is why legacy plants used them |
| A1: adiabatic with water-cooled trim → air-cooled trim | +0.02 | ~$9k | ~0.44 L/kWh ≈ 2.7 ML (~$6k) | small | ≈ break-even; capacity charges and permits tip it to dry |
| A1: tower-based (Google) → air-cooled | ≈+0.1 (Google: ~10%) | ~$50k | ~1 L/kWh (~$13k) | ~+0.4 L/kWh | Google keeps towers |
| A3: liquid + tower → liquid + dry cooler | **−0.04** | saves ~$15k | 2.0 L/kWh ≈ 12 ML (~$28k at u = 0.8 with withdrawal) | none | **No trade-off**: warm water (ASHRAE W32–W45) makes dry rejection free |

AWS states that chiller-based cooling uses 25–35% more cooling electricity than its evaporative design. Microsoft calls its zero-water penalty "nominal".

**Conclusion.** The move to low water happened in two steps:
1. **2010s hyperscale (A1).** Air-side economisers with occasional adiabatic assist cut water by ~5–10× relative to towers at almost no energy penalty, because they need few chiller hours.
2. **AI liquid (A3/A4).** Warm-water direct-to-chip loops let dry coolers carry the whole load at PUE ~1.1, so water goes to ~0 with *no* electricity cost.

On a site-plus-source basis, the total water footprint of every archetype is dominated by electricity (≈4.4 L/kWh × PUE, against 0–2 on site). The site saving is real, but it is small next to the power-plant water already embedded in the Utilities cell.

---

## 2. Staffing

### 2a. Staff per MW by archetype and scale

Figures are on-site facility staff, including full-time contractors and security.

| Archetype / scale | FTE per MW IT, best [range] | Evidence |
|---|---|---|
| A0 enterprise, 1–5 MW | 5 [3–10] | Koomey et al./Uptime 2007: 19 heads on 2.18 MW = **8.7/MW** (security 9 across 3 shifts, maintenance 4, facilities 3, IT 3); 24×7 floor of 8–15 staff per site regardless of size |
| A0 retail colo | ~22 engineering & ops staff per site | Equinix FY2025: 13,716 employees, 44% engineering/ops, 280 sites |
| A1 hall, 30–40 MW | 1.3 [0.9–1.7] | JLARC: ~50 full-time per 250,000 sq ft (≈37 MW), half contractors; KPMG US lines imply 1.0–1.6; Virginia statewide 8,000 jobs on 5,050 MW facility load = 1.6 per facility MW |
| A1 campus, 150–1,500 MW | 0.6 [0.4–1.0] | Meta Kuna 0.66, Temple 0.55; AWS Madison County 0.66 |
| A2 H100 campuses | 0.7 [0.3–1.5] | xAI Colossus 0.9–2.1 announced (but 44 pension-plan participants); AWS New Carlisle 0.4–1.0 |
| A3 GB200 campuses, 0.4–1.4 GW | 0.5 [0.3–1.0] | Crusoe Abilene 400 jobs / ~843 MW = 0.47; Fairwater WI 550 FTE → 0.87–1.49; Oracle fact sheet 1.1–1.2 (announcement); Epoch median over 17 AI campuses 0.68 |
| A4 multi-GW | 0.3 [0.15–0.5] | Meta Richland Parish 1,000 operational jobs at 5 GW = 0.20 (500 at ~2 GW in 2024); USC Zage 0.15–0.20 for automated hyperscale (UNVERIFIED, PDF blocked) |

### 2b. Wages and payroll

**Wages**
- JLARC: Virginia data-center staff and contractors average **~$100k**.
- OEWS May 2025, NAICS 5182 (UNVERIFIED this session; the agent read the local file because bls.gov blocks bots):
  - facilities managers $135.5k
  - network support $87.6k
  - maintenance and repair $69.8k
  - security guards $41–60k
- Electricians and HVAC mechanics at facilities contractors: $82.6k and $74.3k.
- Loaded cost is ≈ 1.3–1.4 × base, so **~$130k per FTE**.

**Payroll per MW-year**

| Archetype | Payroll | Source |
|---|---|---|
| A0 (2007 model) | ~$0.93m, ≈ $1.4m in 2025$ (including IT site staff and security) | Koomey et al. |
| A1 | KPMG labour $133k (engineering-only $39–47k) + security $43k + cleaning $13k = ~$190k | KPMG |
| A3 | $40k | Epoch 1 GW |
| A3 | ~$60k | ~0.47 FTE × $130k |

**How staff split by function**
- JLARC: about half are direct employees (managers, engineers, technicians) and half are full-time contractors (electricians, pipefitters, security).
- Koomey et al.: security 47% of heads, maintenance 21%, facility management 16%, IT 16%.
- **For the recipe:** 50–60% of "facility staff" is own labour (VA). The rest is purchases from Admin & support: 5612 facilities support, 5616 security, 5617 cleaning.

### 2c. How staffing scales

- **24×7 cover sets a floor.** One post takes 4.2–5 FTE; KPMG's interviewee put it as "one person on a shift requires 4 people". Uptime's Tier standard requires ≥1 qualified person per shift for Tier III and ≥2 for Tier IV.
- **Scale economies are modest and come in steps.**
  - KPMG: headcount grows only partly with MW; "30 to 80 MW within the same cost frame", then a step at 100 MW.
  - Security grows with the number of posts and buildings, not with MW.
- **Implied curve per MW IT:**
  - 1–5 MW: ≈5–10
  - 30–40 MW: ≈1.0–1.5
  - 100–300 MW campus: ≈0.6
  - 1 GW: ≈0.3–0.5
  - 5 GW: ≈0.2

  Announced job counts are political and often include contractors and community roles, so read them as an upper bound.
- **BLS NAICS 518210 is not a facility-staff measure.**
  - Loudoun County has 1,550–2,034 employees in 518210 across multiple GW, averaging $213k.
  - Facility trades are <0.5% of 5182 employment, and US 518210 average pay is $195–206k.
  - Most facility staff sit in the parent company's industry, in 5612, or in 5616; Loudoun has 2,032 jobs in 561612 security alone.

---

## 3. Maintenance and other operating costs

### 3a. Maintenance of electrical and mechanical plant

| Source | Archetype | $ per MW-yr | % of capex |
|---|---|---|---|
| KPMG 2026, US 30 MW cloud, facilities O&M (OEM + third-party, preventive + reactive) | A1 | **67k** ($2.0m / 30 MW; range ~1.3–3.0m) | ≈1.0% of M&E capex (≈0.54% of total) |
| A.CRE development model default (UNVERIFIED, page blocked) | A1 | 132k ($11/kW-month) | — |
| ITK / Thunder Said (100 MW US) | A1–A3 | 150k; 100–250k | — |
| Epoch 1 GW (source A.CRE lifecycle, checked against filings) | A3 | **120k** | ≈1.05% of facility capex |
| CNT Table A3, $25k per NVL72 rack-year at ~132 kW | A3 | ~190k | 1.7% of non-IT capex; 2.7% of electrical + cooling |
| Koomey et al. 2007, in-house maintenance staff only | A0 | 193k (2007$) | ~0.8% of $23.8k/kW site infrastructure |
| Schneider WP6 (small, oversized rooms), service contracts | A0 | — | 6.25% of power + cooling equipment a year; 15% of 10-yr TCO |

**Capitalised life-extending capex, on top of the expensed amounts above:** Equinix ~0.7–0.8% of gross PP&E a year; Digital Realty guides recurring capex at ~1.0% of gross real estate.

**Mix:** KPMG puts it at 60% preventive and 40% reactive. The big-ticket items are "batteries, UPSs, generators, chillers".

**Liquid cooling:** no quantified maintenance cost for CDUs, coolant or filters was found (gap). The qualitative evidence is that pumps and power supplies are replaced on run-hours, filters on a time schedule, and coolant chemistry is sampled.

**Verdict:** ~1% of M&E capex a year for large modern halls, and 1.5–3% (up to 6%) for small legacy rooms. **A3 best estimate $120k per MW-yr.** CNT's $190k is plausibly high because it may include IT hardware maintenance.

**Industry:** Construction (230301 nonresidential maintenance and repair), as in FC. OEM service on UPS, gensets and chillers could arguably be 811300 (commercial machinery repair); in the 2017 IO both sit in the same Other Services / Construction neighbourhood.

### 3b. Other lines

| Line | Evidence | Best (A1 → A3) | Industry |
|---|---|---|---|
| Security | KPMG US $1.3m per 30 MW = 43k; Koomey 2007 322k at 2.2 MW | 43k → 20k | Admin (561612) |
| Cleaning | KPMG US $0.38m = 12.7k; falls with density (floor area) | 13k → 5k | Admin (561720) |
| Insurance | KPMG "about 2% of opex"; Europe $0.16–0.83m per 30 MW; Digital Realty 0.33% of revenue, **0.047% of gross real estate** ($18.6m on $39.9bn); broker "$0.08–0.25 per $100 of insured value" (UNVERIFIED) | 10k → 15k | Finance & insurance (524) |
| Property tax (real) | KPMG US $1.3m = 43k; Digital Realty 3.4% of revenue, 0.50% of gross real estate; Loudoun real rate 0.805% of assessed value; Koomey 2007: 1% of non-IT capex | 50k → 80k | Taxes on production |
| Property tax (IT personal property) | Loudoun $4.15 per $100 → ≈1.24% of cost a year over a 5-yr refresh; JLARC Virginia range 0.05–1.44%; Loudoun FY27 budget: real $417m vs equipment $879m | falls on z | Taxes on production |
| Sales & use tax exemption | Virginia $928m in FY23; ~90% of the industry uses it; lowers IT capex, not opex | — | Tax expenditure |
| IT & network ops / software / DCIM (operator) | KPMG US $1.9m per 30 MW = 63k (includes tooling and NOC); ITK connectivity 20k + software 40k | 60k → 50k | Info (517), software (513210/518), 5415 |
| Tenant network (cross-connects, transit) | CNT $20k per rack-yr (~150k/MW); Equinix interconnection ~$5.7k per cabinet-yr; Koomey 2007 network $0.5m on 2.2 MW | z's cost | Info (517) |
| Other | Epoch recurring utility works ~20k; diesel fuel for testing ~3–5k (engineering estimate) | 25–30k | 324110, 5416, 5611 |

**Totals, non-electric (all per MW-yr):**

| Archetype | Source | Total | Notes |
|---|---|---|---|
| A1 | KPMG US | **$373k** | cloud greenfield; explicitly excludes AI/HPC |
| A1 | ITK | $320k | 100 MW |
| A1 | Digital Realty | ~$440–590k | rental property operating + tax + insurance; includes JVs so a lower bound per MW; H1-2025 ratios to utilities 0.78 / 0.15 / 0.014 |
| A3 | Epoch | **$329k** | includes all taxes |
| A3 | CNT | ~$644k | includes network and "other" |
| A0 | Koomey et al. 2007 | $1.57m (2007$) | includes IT staff and network |

- **Europe (KPMG):** non-electric opex is 10–18% of revenue.
- **Verdict:** A1–A3 cluster at **$0.33–0.41m per MW-yr**, ≈ 0.6–0.75 × the electricity bill. A0 is 2.5–4× higher per MW because of staff, security and property taxes on a small base.

---

## 4. Plant lifetimes

| Component | Best (yr) | Range | Sources |
|---|---|---|---|
| Shell (structure, envelope) | 40 | 25–60 | BEA office 36 (δ 0.0247), warehouses/communication 40; IRS 39-yr MACRS; Amazon buildings ≤40; Alphabet 7–40; Equinix 12–60; Meta 25–30 (UNVERIFIED) |
| MV/LV switchgear, transformers, busway | 30 | 22–40 | ASHRAE (Akalin) transformers 30; BEA electrical apparatus 33 (δ 0.050); IRS class 00.4: 22 class life, 15 GDS |
| Diesel generators | 25 | 20–30 | ASHRAE reciprocating engines 20 (analogue; standby duty is light) |
| UPS modules | 12 | 10–15 | Schneider WP229 "10 to 15 year typical UPS life"; WP214: replace/upgrade decision at "10 years or so"; OEM support ends ~10 yrs after a model is discontinued |
| UPS subassemblies (mid-life) | 5–7 | 5–15 | WP214: DC caps 5, fans 5–7, AC caps 7, PSUs 10, inverters/static switch 10–15 |
| VRLA batteries | 4 | 3–6 | WP229 service life 4 (calendar 5); Vertiv 3–5 at 20–25°C; replaced at years 4 and 8 of a UPS life |
| Li-ion UPS batteries | 10–12 | 7–15 | WP229 service 12 / calendar 17; Vertiv 10 at 25°C, 7 at 40°C |
| Centrifugal chillers | 23 | 18–25+ | ASHRAE survival curve >25 (Abramson 2005); Akalin 23; ASHRAE database 18 (biased down) |
| Cooling towers | 20 | 17.5–22+ | ASHRAE >22 (galvanised), Akalin 20, database 17.5; ceramic 34 |
| CRAH/CRAC (air handlers, DX) | 18 | 15–27 | ASHRAE DX >24; AHU 20–27; packaged DX 15–17 |
| Dry coolers / air-cooled condensers | 20 | 10–20 | Akalin air-cooled condenser 20; database 10 (n=13) |
| Pumps | 20 | 10–21 | ASHRAE database 18–21; pipe-mounted 10 |
| CDUs | 12 | 5–15 | Eaton/Boyd "5–10 years" (UNVERIFIED); ASHRAE analogues: pumps 20, shell-and-tube HX 24, electronic controls 15; closed-loop coolant up to 15 (Crusoe) |
| BMS/DCIM, controls | 10 | 7–15 | ASHRAE electronic controls >7 / 15 |
| Whole-plant conventions | 15–20 | 10–25 | Epoch 14; Koomey et al. 15; VN 20; KPMG "20-year lifecycle"; Amazon heavy equipment 10–13; CoreWeave ≤12; **Microsoft data-center buildings 15 → 25 years from FY2027** |

### Implied δ for the plant

**Element weights (T&T 2025)**
- Liquid-cooled: electrical 48 / mechanical 33 / shell 9.
- Air-cooled: 54 / 22 / 14.
- The splits within each block are our assumptions:
  - electrical: switchgear 45%, UPS 20%, Li-ion batteries 8%, generators 27%
  - mechanical: chillers/dry coolers 40%, CDUs 20%, pumps/piping 25%, CRAH/controls 15%

**Results**

| Scope | Straight-line life | Straight-line δ | Geometric δ (BEA 1.65/L) |
|---|---|---|---|
| Plant only | 18.7–19.1 yr | 0.052–0.054 | **0.086–0.088** |
| Plant + shell | — | 0.048–0.051 | **0.077–0.082** |

- The research agent's independent weights (from KPMG's bar chart) give plant L = 18.4–19.6 yr: 5.1–5.4% straight-line, 8.4–9.0% geometric.
- Equinix's implied depreciation rate is **6.05%** on depreciable PP&E (plant + shell mix).
- **Verdict:** δ_plant ≈ 0.085–0.09 (geometric) and δ_f ≈ 0.08. That confirms `recipe_plan.md`'s expected δ_f of 0.085–0.09, and rejects both 0.10 (JLL refresh) and 1/14 straight-line as central values.

**Archetype differences**
- **A0/A1:** VRLA batteries are replaced 2–3 times per UPS life.
- **A2/A3:** Li-ion removes that and lowers electrical δ by ~0.6 pp. CDUs and pumps add some back on the mechanical side.

**Mid-life practice**
- UPS capacitor and fan overhaul at 5–7 yrs; replace or upgrade at ~10 yrs. Service call-outs more than double after year 10 (WP214).
- Batteries on 4-yr (VRLA) or 10–12-yr (Li-ion) cycles.
- Equinix spends ~0.8% of gross PP&E a year on life-extending capex.
- Legacy sites keep running: 47% of Uptime respondents work in facilities >11 yrs old (2024), and 27.5% in facilities 16+ yrs old (2025).

**Obsolescence vs wear.** The risk for A2 air-cooled AI halls is economic obsolescence (liquid retrofits), not physical wear. Operator book lives for M&E (Amazon 10–13, CoreWeave ≤12) are shorter than ASHRAE physical lives (20–25). That argues for the upper end of δ for AI plant, but Microsoft's move to 25 years points the other way.

---

## 5. Efficiency trends other than PUE

| Metric | A0 | A1 | A2 | A3 | A4 |
|---|---|---|---|---|---|
| Server utilisation (LBNL) | internal 11% (2014) → 20% (2027); colo 21% → 35% | 45% → 50% | training 80% / inference 40% of hours; power 70% of rated; Llama 3 MFU 38–43% | same as A2; VN bills 80% of GPU-hours | — |
| Rack density | 4–8 kW (Uptime modal 7.5) | 8–15 | 30–45 (few sites >30 kW in surveys) | ~130–142 kW | 600 kW–1 MW; 800 VDC |
| PUE | 1.68–1.91 (LBNL); Uptime 1.54 all, 1.48 new, 1.44 ≥20 MW; EU 1.36 (1.64 at 500–1000 kW sites) | 1.08–1.22 | 1.2–1.3 | 1.10–1.14 | ≤1.2 required in Germany |
| UPS efficiency | 80–94% (legacy transformer units ~85% at half load) | 90–99% | 90–99% | 90–99% | up to +5% end-to-end with 800 VDC (NVIDIA) |
| Staff per MW | 5–9 | 1.3 hall / 0.6 campus | 0.7 | 0.5 | 0.2–0.3 |
| Heat reuse | EU average ~1.8% of heat reused; 67 sites report any | Meta Odense 165,000 MWh/yr to ~9,000 households (175 jobs) | — | — | Germany EnEfG: ERF ≥10% (sites from Jul 2026), 15% (2027), 20% (2028) |
| Facility size | 1–20 MW | 18–100 MW buildings | 100–300 MW | 0.4–1.4 GW campuses | multi-GW (Hyperion 5 GW) |

The EnEfG heat-reuse thresholds are conflicting:
- The law, as read by the lifetimes agent, gives 10/15/20%.
- A Columbia Climate Law blog gives 15% from 2026 and 20% from 2028.
- We use the statute; both rows are in the CSV.

**Implication for the model.** Moving from A0 to A3 raises the **capital intensity per MW** (IT and plant) far more than it lowers opex. Per MW of IT, non-electric opex falls from ~$1.0m to ~$0.38m and staff from ~5 to ~0.5 FTE. Water falls ~40× on site, but only ~35–40% on a site-plus-source basis (≈57–61 → ≈37 ML per MW-yr, consumption vs withdrawal on site). Electricity per MW rises with utilisation (0.55–0.7 → 0.8) even as PUE falls.

---

## 6. Old vs new design comparison

| Dimension | A0 legacy colo | A1 hyperscale air | A3 AI liquid | Change A0 → A3 |
|---|---|---|---|---|
| Heat rejection | chillers + CRAH + cooling towers | outside air + adiabatic/evaporative assist (or towers at Google) | warm-water DLC + dry coolers (chiller trim) | from evaporation to dry |
| Site WUE (L/kWh IT) | 2.0 [1.3–3.7]; Equinix evaporative sites 1.55; Microsoft early 2000s 2.3 | 0.30 [0.1–1.0]; Microsoft 0.27, Meta 0.20, AWS 0.12 | 0.05 [0–0.3] (2.0 if towers) | ÷ 40 |
| Site water (ML per MW-yr) | ~12–16 (withdrawal) | ~2.5 | ~0.4 | −97% |
| Source water (ML per MW-yr, 4.4 L/kWh × PUE × IT MWh) | ~45 | ~31 | ~37 (higher u) | −18% |
| PUE | 1.65–1.9 | 1.1–1.22 | 1.10–1.2 | −0.5 |
| Facility MWh per MW IT-yr | ~10,100 (u 0.7, PUE 1.65) | ~7,050 | ~8,400 (u 0.8, PUE 1.2) | −17% (higher utilisation offsets) |
| Water $ ÷ electricity $ | 3.4% | 0.7% | 0.1% | — |
| FTE per MW | 5 [3–10] | 1.3 hall / 0.6 campus | 0.5 [0.3–1.0] | ÷ 10 |
| Maintenance $k per MW-yr | 150 (1.5–3% of M&E capex) | 70 (~1%) | 120 (~1–1.5%) | −20%; rises from A1 to A3 with plant complexity |
| Non-electric opex $k per MW-yr | ~1,000 | ~410 | ~380 | −60% |
| Plant life / battery | 15–20; VRLA every 4 yrs | 18–19 | 19; Li-ion 10–12; CDUs ~12 | similar physical life; more obsolescence risk |
| Rack density (kW) | 4–8 | 8–15 | 130–142 | × 20 |
| Server utilisation | 11–35% | 45–50% | 80% training / 40% inference hours | × 3–5 |

---

## 7. Cross-checks, number by number

1. **A1 site WUE ≈ 0.3.** Four independent sources agree:
   - LBNL model 0.32
   - Microsoft 0.27–0.30 (consumption)
   - Meta 0.20 (withdrawal)
   - ICPRB/JLARC Virginia ≈0.2–0.3

   AWS is lower (0.12, withdrawal) and Google higher (~1.0), both by design: AWS runs evaporative only above 85°F, and Google uses towers for energy efficiency. **Agree, with the basis (consumption vs withdrawal) explaining ~1.3×.**
2. **A0 site WUE ≈ 2–3.** Four independent sources agree:
   - LBNL tower cases 2.5–3.2
   - Uptime 2016 engineering example 2.9
   - Microsoft early 2000s 2.3
   - Equinix evaporative sites 1.55

   Equinix is lower, plausibly because of economisers and reclaimed water. **Agree.** The quoted "1.8 average" is a mis-quote (see 1c).
3. **A3 site WUE ≈ 0.** Evidence: LBNL liquid + dry cooler; operator designs (Microsoft, Crusoe, Meta Hyperion). No operator has yet published a measured WUE for a GB200 fleet. **Agree on design, but not measured.** Liquid-cooled halls on towers reach 2.0 (LBNL), so the archetype needs to specify the heat-rejection method.
4. **Water price $6 per 1,000 gal.** Evidence: Loudoun rate study (primary), PNNL regional averages (water $2.7–5.6 + wastewater $3.1–11.9 on the discharged ~25%), Phoenix. **Agree.** The earlier $10 in FC is high for Loudoun but inside the range.
5. **Water cost per MW-yr is small.** Three independent sources agree: Epoch $6k, JLARC-derived $2.5k, and our A1 $3.9k. **Agree.**
6. **Staff per MW, 30 MW hall ≈ 1.3.** Three sources agree: JLARC (≈1.3–1.6), KPMG cost lines (1.0–1.6) and Koomey scaled. **Agree.**
7. **Staff per MW at GW scale.** Sources disagree:
   - Meta 0.2, Crusoe 0.47 and Epoch's labour line ($40k ≈ 0.3 FTE) are low.
   - Oracle/Stargate announcements (1.1–1.2) and Fairwater (0.9–1.5) are high.

   The high values mix construction-phase or announced numbers with contractors. **Partial agreement.** Use 0.5 [0.3–1.0] for A3.
8. **Maintenance ≈ $70–120k per MW-yr (≈1% of M&E capex).**
   - KPMG (primary, interviews) $67k.
   - Epoch $120k (A.CRE-based).
   - CNT $190k (unsourced).

   **Partial agreement.** A1 is lower because air-cooled plant is simpler (fewer pumps and CDUs) and KPMG covers stabilised cloud sites.
9. **Insurance.** Digital Realty's effective 0.047% of gross real estate is far below the "0.1–0.3% of insured value" rule, partly because tenants insure their own IT and blanket programmes are cheap. KPMG's "~2% of opex" ≈ $8k per MW. **Agree on small (<$20k per MW).**
10. **Property tax (facility).**
    - KPMG US $43k.
    - Digital Realty 0.50% of gross real estate (≈$68–91k per MW).
    - Loudoun statutory 0.805% × ~$11m per MW = $89k before abatements.
    - Epoch $143k includes IT personal property.

    **Agree at $50–90k** once IT tax is separated.
11. **Total non-electric opex.** Five sources in total. Four agree on A1–A3 ≈ $0.33–0.41m per MW-yr: KPMG $373k, ITK $320k, Epoch $329k and Digital Realty lower bound ~$440k. CNT ($644k) is the outlier, explained by network and "other". **Agree (excluding CNT).**
12. **Plant δ ≈ 0.085–0.09.**
    - ASHRAE/BEA/Schneider component lives weighted by T&T shares.
    - The research agent's KPMG weights.
    - Equinix's implied 6% straight-line on a plant + shell mix.

    **Agree.** Epoch's 14 yr (δ_SL 0.071) cites Koomey's 15 yr, which was a modelling convention, not a measurement.

---

## 8. Open gaps

- **Measured WUE for GB200/GB300 fleets.** No operator publishes WUE by hall type. Immersion or two-phase WUE (A4) is extrapolated.
- **Liquid-cooling maintenance.** No quantified cost for CDUs, coolant or filters; no vendor design life for CDUs (the Eaton "5–10 yr" is UNVERIFIED); nothing on immersion fluid replacement.
- **Insurance.** No Marsh, WTW or Aon rate data. The broker $0.08–0.25 per $100 of insured value is UNVERIFIED.
- **Facility wages.** OEWS by occupation for 518210 was read from a local file (bls.gov blocks fetches). The BCG headcount behind Epoch's labour line has not been seen.
- **Network ops.** No split of on-site IT/remote-hands vs central NOC staffing at hyperscalers.
- **Digital Realty per MW.** Digital Realty's MW denominator (consolidated vs JV) came from a secondary source, and SEC blocks direct fetches. Meta's building lives, 25–30 yrs, are UNVERIFIED.
- **Capacity charges.** Water availability/connection charges are sized on peak demand (≈$0.2m one-time per MW for A1 in Loudoun, illustrative). They belong in capex (grid/utility connection, gap G6), not in opex.
- **Consultant opex benchmarks.** No JLL, CBRE, Cushman or T&T opex benchmarks were found; KPMG is the only consultant opex source, and it excludes AI/HPC. The "JLL M&E refresh at year ~15" in the plan could not be sourced.
- **Staff counts.** Campus job counts are announcements. QCEW cannot identify facility staff because of the industry classification of parent companies.
- **Heat reuse.** The European Commission's COM(2026)500 gives the EU reuse share (~1.8%). There is no US data and no evidence that heat reuse generates revenue for US AI campuses.

## 9. Files

- **`operations_obs.csv`** (311 rows). 27 rows cite a source URL that could not be fetched this session because of 403 errors, blocked SEC pages or timeouts. Those rows say so in their notes as "UNVERIFIED" or "verification: UNVERIFIED".
- **PDFs** in `References/engineering/operations/`:
  - KPMG 2026, JLARC 2024, Uptime 2007/2021/2022/2024/2025, Green Grid WP35, Mytton 2021, Li et al., LBNL 2016
  - ICPRB 2026, Han et al. 2026, PNNL-34006, Loudoun Water rate study and presentation
  - Equinix / Google / Meta / Microsoft / Amazon sustainability documents
  - ASHRAE PHVAC9 LCC chapter, Schneider WP6/WP214/WP229, IRS Pub 946
  - Amazon / Alphabet / CoreWeave 10-Ks, EC COM(2026)500
  - Mangum 2020, Oxford Economics 2018, E3 for JLARC
  - Loudoun strategy paper
  - Oracle Stargate fact sheet: marked "Confidential – Oracle Internal", but publicly posted on house.gov by Rep. Arrington.
