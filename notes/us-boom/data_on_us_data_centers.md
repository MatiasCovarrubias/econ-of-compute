# Data on US Data Centers

Landscape note across official statistics, regulatory filings, and the private vendors that sell project-level data. Three questions in turn: aggregate pipeline, financing, and phases/durations. For each, what is official, what you have to buy, and what the numbers currently say.

---

## The single most useful starting point

The Fed Board published exactly the paper you'd want: Brandsaas, Garcia, Kurtzman, Nichols and Zytek, "Estimating Aggregate Data Center Investment with Project-level Data," FEDS 2025-109 (December 2025). It uses Dodge Construction Network microdata to nowcast aggregate investment, and it answers two of your three questions with estimated parameters. Their headline: investment rises from roughly $60bn annualized in 2024Q4 to $180bn in 2025Q4, reaching about $370bn by 2026Q2 in the mean simulation, with 2027 ranging from $360bn to $930bn depending on assumed plan inflows. Read it first; it will save you weeks.

---

## 1. Aggregate pipeline

**Official**

- **Census, Value of Construction Put in Place (C30).** Data centers were carved out as a standalone line inside private office in July 2024 after lobbying by the AGC. April 2026 came in at $50.7bn SAAR, up 28.1% from $39.6bn a year earlier, about 2.3% of all US construction and roughly 52% of private office. Full-year 2024 was $28.33bn. Monthly, seasonally and non-seasonally adjusted, with a historical VIP file and geographic detail for private nonresidential. One measurement wrinkle worth knowing: Census counts racks and servers installed at the site as part of value put in place, so VIP is not purely a structures measure.
- **BEA / NIPAs.** Since the September 2025 annual update, BEA publishes data centers separately from "general, financial and other" offices within private fixed investment in nonresidential structures, deflated by a new composite index that equally weights the BLS PPIs for industrial buildings and warehouses rather than the office PPI. Structures detail sits in the Table 5.4.5 family plus the underlying detail tables; stocks in the Fixed Assets tables. The gap: equipment is not broken out. GPUs and servers sit inside "computers and peripheral equipment." The Fed paper's workaround is to detrend that series on a 2015–2022 trend and treat the residual as data center equipment, then add structures. On that basis nominal structures spending went from about $10bn in 2021 to about $40bn annualized in the first half of 2025.
- **FERC State of the Markets (March 2026)** puts operating IT load at roughly 50 GW at end-2025, derived from interconnection data, with the average facility entering service in 2025 at about 80 MW against 25 MW in 2020. ISO/RTO large-load queues (ERCOT, PJM, MISO) and utility IRPs and rate filings are the richest official project-level source, though badly contaminated by duplicate filings.

**Private project-level**

- **Dodge Construction Network, Real Estate Analyzer.** This is the one to buy. Dodge has been the Census Bureau's preferred construction data provider for over 55 years, so it is the input to the official statistics rather than a competing estimate. Coverage runs 2003 to present with property type, square footage, location, project value and eight phases (pre-planning, planning, final planning, bidding, underway, completed, abandoned, deferred), plus a master-to-child report crosswalk for phased campuses. Values appear to reflect total project cost including equipment, not just the structure. The descriptive statistics alone are striking: new plans totalled almost $300bn in 2024 and over $900bn through September 2025, with the stock of plans exceeding $1tn. From 2019–2022 there were 278 data center plans averaging $114m (median $26m); in 2025 through September there were 521 plans averaging just under $2bn (median $216m).
- **Dodge Momentum Index** is the free monthly leading indicator built on the same planning data, with a data center component. Commercial planning fell 6.9% from May to June 2026 on a dip in data center filings.
- **ConstructConnect** and **Industrial Info Resources** are the alternatives, more bid-oriented and less used by statistical agencies.
- **Capacity trackers (MW rather than dollars):** DC Byte, datacenterHawk, Baxtel, Cloudscene, Synergy Research (hyperscale facility counts), Structure Research, S&P Global Market Intelligence (formerly 451). Baxtel sells both one-off snapshot exports and refreshed subscriptions with location, operator, operational status and current/planned power capacity, verified site by site, which makes it the cheapest way to get a usable site-level panel. DC Byte tracks projects from early-stage planning and land-banked sites through committed and operational capacity.
- **Brokers:** CBRE, JLL, Cushman & Wakefield, Newmark publish free semiannual summaries and sell the underlying data.
- **Wood Mackenzie US data center pipeline**, quarterly, is the best aggregate capacity tracker. Cumulative disclosed US capacity is 331 GW, about 40% under active development. Q1 2026 additions of 36 GW were down 19% quarter-on-quarter, a third consecutive decline from a peak above 60 GW in Q3 2025. Texas leads with nearly 100 GW cumulative planned. 53% of projects have cleared permitting but represent only 32% of pipeline capacity, and 195 GW has signed construction or electricity supply agreements, equal to 26% of 2025 US peak load.
- **SemiAnalysis Datacenter Model**, **Epoch AI** (free Stargate and Fairwater trackers), **Sightline Climate** for the delay/cancellation view.

**The definitional trap.** Every "under construction" number means something different. A useful reconciliation from an ITK Research compilation: CBRE reports 5,994 MW because it counts wholesale colocation in eight primary metros only; Cushman & Wakefield and datacenterHawk report 25.3 GW across all asset types in primary, secondary and tertiary North American markets including hyperscaler-owned and behind-the-meter sites; JLL reports 35 GW because it includes projects starting within 24 months. A defensible working figure for load physically under construction in May 2026 is 22–26 GW, roughly 89–92% pre-committed. Same caution on facility counts: 580 hyperscale-owned facilities (Synergy) versus 4,700–5,400 in the broad directories. Never add across trackers.

---

## 2. Financing

**Official and regulatory**

- **SEC EDGAR** is more useful than it sounds. 10-K/10-Q capex and, critically, the ASC 842 disclosure of operating leases signed but not yet commenced, which is where the forward hyperscaler obligation shows up. VIE and unconsolidated-affiliate footnotes are where the SPVs surface. 424B2 and 8-K filings give deal terms.
- **BDC and fund filings.** Blue Owl, Blackstone and Apollo vehicles file schedules of investments at position level in N-PORT and 10-Ks. This is free, granular private-credit data and badly underused.
- **Supervisory data.** FR Y-14Q (Schedule H corporate and CRE, loan level) is the ideal source and available to central bank researchers through the usual channels; Call Reports and the Shared National Credit program give the coarser public view. The Chicago Fed's February 2026 note estimates bank exposure to AI-adjacent industries at about 0.8% of total assets on average, with large bank C&I commitments around $450bn late 2025 of which $150bn was drawn, against JPMorgan's estimate of roughly $1.2tn in AI-company debt. MSCI Real Capital Analytics put bank lending to data centers at $14.9bn over the year through 2025Q3.
- **Central bank and international work.** BIS Bulletin 120 (Aldasoro, Doerr, Rees) is the closest to your institutional register: private credit outstanding to AI-related companies grew from near zero to over $200bn, with more than $40bn originated in 2025 against about $3bn in 2010. The Bank of England's July 2026 FSR traces AI infrastructure financing across public debt, private credit, leveraged finance, structured finance and SPVs, and reports private credit's share of AI investment financing rising from 9% in 2024 to 34% in 2025. The FSB's May 2026 private credit report sizes the sector at $1.5–2.0tn and documents roughly $220bn of drawn and undrawn bank credit lines to private credit funds, against commercial estimates of $270–500bn. It also flags that AI firms accounted for more than a third of 2025 private credit deals, up from 17% over the prior five years.

**Market data**

- **Securitization** is the best-measured channel. KBRA counts $48.69bn across 88 US transactions since 2018: ABS 70.8% (75 deals, $459.7m average) and CMBS 29.2% (13 deals, $1.09bn average). Barclays puts outstanding issuance at $61bn year-to-date 2026, up from $4bn in 2020, roughly 12% of the esoteric ABS market. As of late February 2026, ABS outstanding was about $40.5bn and CMBS about $18.0bn; combined annual issuance went from $0.9bn in 2018 to roughly $26bn in 2025. Almost all deals are 144A, so the data lives in Finsight, Intex, Trepp, Bloomberg and CREFC, and rating agency pre-sale reports (KBRA, Moody's, Fitch, Morningstar DBRS) are free and give deal-level lease terms, tenant identity and capacity. Note the July 29, 2026 SEC interpretive guidance placing qualifying data center securitizations outside Exchange Act ABS treatment, which exempts them from Regulation RR risk retention and Exchange Act reporting while leaving single-asset CMBS on the same collateral fully regulated. That asymmetry will shape structuring choices and therefore your data availability.
- **Corporate bonds.** Hyperscalers issued roughly $121bn in 2025, more than four times the five-year average, with AI-related investment accounting for about 30% of net US dollar IG issuance and total data center debt issuance nearly doubling to $182bn. Morgan Stanley projects global AI-related issuance near $570bn in 2026.
- **SPVs and private credit.** Blue Owl and JPMorgan put roughly $13bn ($10bn as debt) into the SPV owning the Abilene facility, alongside a $38bn debt package elsewhere. In the Meta Hyperion structure, PIMCO holds senior debt and Blue Owl the equity, while Meta retains the four-year renewal option and provides a residual value guarantee. Morgan Stanley estimates private credit could supply over half of the $1.5tn needed through 2028, an $800bn opportunity.
- **Deal databases:** PitchBook, Preqin, Infralogic, LSEG/Dealogic, MSCI Real Capital Analytics, Green Street.

Practically, the financing question has five archetypes worth separating in any aggregation: hyperscaler balance-sheet self-build; SPV/JV with private credit and a lease-back; wholesale developer build-to-suit funded by construction loan then refinanced into ABS or CMBS at stabilization; neocloud high-yield and GPU-collateralized debt; and utility-financed generation recovered through rate base. Only the third is cleanly measured.

---

## 3. Phases and durations

**The rigorous numbers, all from the Fed paper's Dodge estimation sample (about 1,700 projects, 2003–2025):**

Abandonment out of planning is 0.33, lower than the 0.46 Glancy, Kurtzman and Loewenstein (2025) find for commercial generally. Mean time from plan to start is 11.1 months (median 6, p90 26). Mean start to completion is 9.4 months (median 9, p90 17). For large projects above $250m, roughly the top decile: abandonment 0.30, plan to start 15 months, start to completion 19.8 months (median 18, p90 35). They fit T = 19.15 + 2.15·log(V), implying about 19 months start-to-completion for a $1bn project. Around 95% of projects that ever start do so within four years.

**Spending phasing.** The Census "Length of Total Time" supplement to C30 gives average start-to-completion months by construction type and value category, plus tables showing the share of value put in place in each month of construction. For projects above $100m running more than three years, Census finds roughly 50% of value phased in during the first year and 90% by the end of the second. These tables cover privately-owned nonresidential, state and local, and private multifamily, in two-year completion cohorts back to 2000–01, and were last refreshed on 3 August 2026 under Historical Construction Spending Data. Also see Millar, Oliner and Sichel (2016, RSUE) on time-to-plan lags.

**The phase taxonomy itself** is only softly measured. Industry practitioner sources converge on: site selection and land control, design and engineering, permitting and zoning, utility interconnection, site prep and civils, shell, MEP fit-out, network and security, commissioning, then IT install and ramp. Typical quoted figures are 18–30 months for construction, 3–6 years for the full development lifecycle, with commissioning 3–6 months and hyperscale builds 24–36 months. Others put the construction phase at 18–30 months with the full lifecycle spanning several years depending on permitting, power access and equipment lead times. Treat these as trade estimates rather than measured distributions.

One conceptual point that matters for your aggregation: Dodge "completion" means the structure, while energization and IT ramp come afterward. So Dodge start-to-completion of 9–20 months is much shorter than announcement-to-first-power, which is where the interconnection queue and long-lead electrical equipment bind. That gap is currently the whole story on the supply side.

---

## Energy, briefly

LBNL's 2024 report (Shehabi et al., LBNL-2001637) is the congressionally mandated baseline: 176 TWh in 2023, 4.4% of US consumption, with a scenario range to 2028. The 2025 Update revises to 11.8% of US electricity by 2030, range 9.5–15.3%, against the earlier 6.7–12.0% by 2028. EIA has no data center breakout in Forms 861 or 861M, so the official series stop at commercial and industrial retail sales. FERC's State of the Markets, ISO large-load queues and utility IRPs fill the gap. The phantom-load problem is severe: ERCOT's large-load queue went from 63 GW at end-2024 to 226 GW by October 2025 with only 1.8% operational, and Dominion reports 47.2 GW of contracted pipeline against forecast peak data center demand of about 9 GW in ten years. A 30–50% discount on utility-stated demand is a defensible adjustment.

---

## Two practical recommendations

If you can make one purchase, make it Dodge REA. It is the input to the official statistics, it carries dollar values rather than megawatts, and it gives you the phase transitions you need for the duration question. Baxtel snapshot exports are the cheap complement for site-level power capacity.

For financing, resist the temptation to build one aggregate. The channels are measured with wildly different precision: securitization is well documented deal by deal, corporate bonds are clean, bank exposure requires supervisory data, and the SPV and private credit layer is only visible through fund filings and litigation disclosure. Also note the import adjustment if you want GDP contributions: the Fed paper assumes 30% structures and 70% high-tech equipment with an 80% import share on the latter, implying only 44% of data center investment is domestic.

A deeper investigation could pin down subscription terms and coverage overlap across the eight or so commercial trackers, and reconcile their capacity definitions against the Dodge dollar series project by project.
