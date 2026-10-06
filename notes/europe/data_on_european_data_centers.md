# Data on European Data Centers

The structure is inverted relative to the US. Europe has a mandatory facility-level reporting regime that the US lacks entirely, and lacks the Census/Dodge combination that makes US aggregation tractable. Here's the map.

---

## 1. Aggregate pipeline

**The one official European source with no US analogue**

Article 12 of the recast Energy Efficiency Directive (2023/1791), implemented through Delegated Regulation (EU) 2024/1364, obliges every data centre in the EU with installed IT power demand of at least 500 kW to report annually to a European database. First report was due 15 September 2024 covering calendar 2023, then 15 May every year thereafter. Reporting runs through national schemes where they exist, otherwise direct to the Commission, and results are published aggregated at Member State and EU level with size categories.

The Commission released the first aggregate tranche in spring 2026, covering 2023 and 2024 across 18 countries: 776 data centres, total installed IT power demand of 6.4 GW, total consumption of 16.7 TWh, weighted average PUE 1.36. Large facilities were the dominant type at 224 (28%), very large at 52 (7.3%), with Germany the largest hub on both count and installed IT power.

Two caveats that matter enormously for your purposes. First, coverage is poor: 6.4 GW reported against JLL's 3.8 GW of live capacity in the five FLAP-D metros alone and roughly 12.5 GW of EMEA operational capacity in commercial trackers. Treat 6.4 GW as a floor, and expect the 2025 and 2026 vintages to jump partly from better compliance. Second, national thresholds differ from the EU floor — Germany applies 300 kW, France 100 kW — so cross-country comparability is compromised at the small end.

The second-phase delegated regulation establishing the rating scheme and electronic labels was registered on 26 March 2026 and amends 2024/1364. The Data Centre Energy Efficiency Package, containing the Commission's assessment of the submitted data plus work on minimum performance standards, was planned alongside the Strategic Roadmap for Digitalisation and AI in the Energy Sector and the Cloud and AI Development Act.

**National accounts and construction statistics: the gap**

There is no European equivalent of the Census data centre line in Value of Construction Put in Place, and no Eurostat or ESA 2010 breakout of data centre structures within GFCF. You are stuck with `nama_10_an6` and `nama_10_nfa_fl` cross-classifications by NACE and asset type, which will not isolate data centres.

The ECB has built the closest available proxy. The Economic Bulletin box "From bricks to clicks: an assessment of euro area digital investment" constructs a digital investment measure from four components: non-residential buildings and structures in the ICT sector, ICT equipment in the business economy, computer software and databases outside the ICT sector, and IPP investment by the ICT sector. It finds euro area digital investment up just over 60% between 2014 and 2025 while the US proxy more than doubled, with the US accelerating in 2025 on data centre investment. That box, plus the Lagarde speech "AI and the euro area economy" from March 2026, are your institutional starting points and both are directly extensible.

Given the absence of a Dodge-style plan-to-start dataset for Europe, the Brandsaas et al. methodology cannot be replicated as-is. The nearest substitute for a "planning stock" is TSO grid connection queue data, which carries a phantom-load problem at least as severe as ERCOT's (see the Spanish numbers below).

**Commercial pipeline data**

- **DC Byte** is UK-based with the strongest EMEA project-level coverage, tracking from early-stage planning and land-banked sites through committed and operational. For Europe it is the equivalent of what Dodge is for the US pipeline, though with megawatts rather than euros.
- **JLL EMEA Data Centre Report**, semiannual, is the most quoted. FLAP-D live capacity reached 3.8 GW by H1 2026, up from 1.8 GW in 2019, with 1.4 GW under construction and 2 GW planned. H1 2026 deliveries were 194 MW across the five metros: Paris 72.5 MW, London 49 MW, Frankfurt 45 MW, Amsterdam 16.3 MW, Dublin 11.4 MW. Full-year 2026 deliveries forecast at 453 MW, roughly three times the 2020 level. Vacancy is 6.4% across FLAP-D, Frankfurt at 3.1%, and 83% of the pipeline is pre-let. The structural shift worth flagging: greenfield rises from 8% to 39% of the 2026–28 pipeline, and hyperscale sites average 175 km from hub cities against 46 km previously.
- **Cushman & Wakefield EMEA Data Centre Update** puts the total EMEA development pipeline approaching 15 GW across 33 markets, with a 19% increase in live capacity and a clear shift away from FLAP-D toward secondary markets and the Nordics driven by grid congestion.
- **CBRE**, **Colliers** (strong on Iberia), **Newmark**, **Synergy Research**, **Baxtel**, **Cloudscene** cover the rest. Same definitional trap as the US: 3.8 GW (FLAP-D live), 12.5 GW (EMEA operational), 15 GW (EMEA pipeline) and 6.4 GW (EED reported) are four different universes.

One structural difference worth quantifying: EMEA and APAC together hold roughly 6.1 GW across 541 sites, so average site size is about a quarter of the US equivalent. Any per-project parameter you estimate on US data will be wrong for Europe.

---

## 2. Financing

**Your institutional advantage**

AnaCredit is the obvious instrument and has no US counterpart in accessibility. Loan-level, harmonised across the euro area, with debtor NACE codes (63.1, data processing, hosting and related activities, plus the construction and real estate codes for developers) and collateral detail. That gives you euro area bank exposure to data centre borrowers at a granularity the Fed can only approach through Y-14. Pair it with Securities Holdings Statistics and the CSDB for bond and structured-product exposures held by euro area banks, insurers and funds, and with the Register of Institutions and Affiliates Database for group structures where SPVs are involved. If you want to write something the ECB does not already have, this is the angle.

**Official and supervisory**

The ECB Financial Stability Review of May 2026 covers stress in global private credit markets and their implications for euro area stability, and flags that AI infrastructure and data centres are highly energy-intensive and sensitive to persistent energy cost shocks. The transmission channel the ECB emphasises is that direct bank losses stay small because senior loans to private credit funds rank high in the capital stack, while pension funds and insurers holding the equity and high-yield layers absorb revaluation losses. Euro area private credit funds sit around €100bn, well below US scale.

The March 2026 ECB analysis adds a useful cross-sectional fact: over the past three years more than half of euro area private credit volumes went to firms in IT and other media plus healthcare, against roughly 5% of bank lending to those sectors. That is drawn from PitchBook/Morningstar, so it is replicable.

For the UK side, the Bank of England FSR is ahead of the ECB in naming AI infrastructure explicitly, and the FSB's May 2026 private credit report gives you the global aggregates.

**Market data**

European data centre securitisation is small but now established, and every deal is well documented. Vantage completed the first EMEA data centre ABS in sterling at £600m in 2024, tapped it in January 2026 with £200m of additional Class A-2 notes plus a new £54m Class B tranche, backing part of its 148 MW Cardiff campus. It also completed the first euro-denominated data centre ABS at €640m in June 2025, refinancing four German facilities — two in Offenbach and two in Berlin — fully leased to hyperscalers, with Class A-2 rated A− and Class B rated BBB− by S&P and Scope. The presence of Scope and Morningstar DBRS alongside S&P means European pre-sale reports are as informative as US ones, and free.

Beyond that, the European financing stack is bank-heavy relative to the US: syndicated construction facilities from the large European and Japanese banks, infrastructure funds and pension money on the equity side, and corporate debt at the operator level. For deal-level coverage use Infralogic, PitchBook, Preqin, LSEG and MSCI Real Capital Analytics. Digital Realty's SEC filings are unusually useful for European exposure since they disclose the Paris and Frankfurt joint ventures with Blackstone alongside the US ones.

**Public financing, which matters far more in Europe than the US**

InvestAI targets mobilising €200bn, with €20bn ring-fenced for AI gigafactories. Under Council Regulation (EU) 2026/150 amending Regulation (EU) 2021/1173, the Union contribution can cover up to 17% of the capex of an AI gigafactory's overall computing infrastructure, with participating Member States required to at least match it. On 30 July 2026 the Commission launched a call for up to seven AI gigafactories, committing €10bn public against a €20bn private target for €30bn total, with bids closing 12 November 2026, awards expected early 2027 and construction the same year. The Cloud and AI Development Act aims to at least triple EU data centre capacity within five to seven years with simplified permitting conditional on energy and water efficiency requirements. Thirteen EuroHPC AI factories were already selected across seven countries in 2024–25.

For your purposes this means a non-trivial share of announced European capacity has a public co-financing component with published award terms, which is genuinely easier to track than private US deal flow.

---

## 3. Phases and durations

This is where European data is weakest, and where the binding constraint differs from the US.

There is no Dodge. The closest national analogues are Barbour ABI and Glenigan in the UK, and Eurostat's building permits index (`sts_cobp_a`) plus national permit registers elsewhere, none of which carry a data centre category. Spain's *visados de obra* have the same limitation. So plan-to-start and start-to-completion distributions of the kind the Fed estimated cannot currently be produced for Europe from any single source.

What you can measure instead is the grid connection lag, which in Europe dominates the construction lag entirely. JLL reports lead times of up to 10 years limiting new supply in primary markets. Frankfurt's interconnects are allocated years ahead. Ireland introduced a restrictive connection framework, published by the CRU in December 2025, after development had effectively stalled awaiting it. This is why the greenfield and secondary-market shift in the pipeline is happening: the construction phase is broadly comparable to the US, but the pre-construction phase is much longer and dominated by a regulated bottleneck that produces documentation.

Practical consequence: for Europe, model the phase sequence as land control → grid connection application → connection offer/grant → permitting → construction → energisation, and instrument the middle steps with TSO and regulator data rather than construction filings. National TSOs (Red Eléctrica, Amprion, TenneT, RTE, EirGrid, NESO) publish connection queue statistics of varying quality, and ENTSO-E's TYNDP aggregates. ENTSO-E published a warning in April 2026 reframing the concern from data centres being unable to get power to data centres consuming enough generation headroom to force renewable curtailment.

---

## 4. Energy

**Ireland's CSO is the single best official statistic on data centre electricity anywhere in the world**, and worth using as a validation benchmark for bottom-up methods. *Data Centres Metered Electricity Consumption*, built from ESB Networks meter data, published annually since 2020 with the analysis extending back further. In 2025 data centres consumed 7,663 GWh, 23% of total metered electricity, up from 6,973 GWh and 22% in 2024, and from 5% in 2015. The new quarterly series runs from 291 GWh in Q1 2015 to 1,991 GWh in Q4 2025, a 584% increase. Total metered consumption was just under 33,000 GWh in 2025 and rose 34% over the decade. Large energy users, which include significant data centres, accounted for 33% of consumption. No other country publishes anything comparable.

**JRC** is the EU-level analytical source. Kamiya and Bertoldi estimate combined EU data centre and telecommunication network energy use at 70–95 TWh in 2022, equivalent to 2.8–3.8% of regional electricity, with Germany, France, Italy and Spain accounting for about 60% of total digital consumption. The Commission's own framing when adopting the delegated regulation put data centres at close to 3% of EU electricity demand.

For forward projections, use IEA *Energy and AI*, EPRI, BNEF and the national TSO scenarios, with the same 30–50% haircut on announced load that the US queue data warrants.

---

## 5. Spain, since it is on your doorstep

The Spanish grid access numbers are the cleanest illustration in Europe of the phantom-load problem, and the policy response is live.

Red Eléctrica reported in February 2026 that the transmission grid alone had 11.8 GW of capacity granted to new demand not yet in service, on top of 7.1 GW already connected. More than 12 GW of grid access and connection rights have been granted to data centres since 2021. Against that, Spain's 2024 AI strategy anticipated roughly 2.5 GW of compute capacity by 2030, implying 3.5–4 GW of electricity demand, with sector and independent forecasts in similar or lower ranges. Vice-President Aagesen has publicly described the volume of requests as a bubble.

Actual installed capacity is far smaller. Spain DC and Pb7 Research reported installed IT power across commercial colocation and hyperscale facilities at 439 MW at end-2025, up from 355 MW in 2024, with potential of 2,537 MW by 2030. Colliers puts more than 600 MW IT into operation before 2027 within a long-term announced pipeline exceeding 7 GW, with Madrid leading at 244 MW scheduled over two years plus 1,028 MW announced, and notes that 85% of electricity distribution nodes are saturated. Spain DC forecasts €66.9bn of investment through 2030. The headline commitments are AWS at €15.7bn in Aragón and Microsoft at $7.16bn in Aragón plus $2.1bn in Madrid.

On 25 August 2026 the Council of Ministers authorised urgent processing of a draft royal decree that would require any facility with 1 MW or more of access capacity to demonstrate that at least 80% of the electricity it consumes in each hour is backed by renewable generation produced in that same hour, from plant commissioned no more than 18 months before the data centre began operating, with a maximum PUE of 1.15 and WUE of 0.1 pending the EU labelling scheme. The decree itself has not been approved. The ratio of granted access rights to plausible built capacity is the natural policy question, and you have the data to quantify it.

---

## What I would actually do

Start from the ECB's digital investment proxy and extend it, because it is already euro area-consistent and the data centre share can be bounded from the EED database and the commercial MW trackers. Use AnaCredit for the financing side, since that is where you can produce something new rather than replicating market commentary. Use Ireland's CSO series to validate any bottom-up energy method before applying it to countries without meter-level data. Buy DC Byte if you need project-level European coverage.

The honest summary: for the US you can build a defensible aggregate investment series from official statistics plus one commercial dataset. For Europe you cannot yet, and the reason is that no statistical agency publishes data centre construction or investment separately. That gap is itself a publishable observation, and it is the kind of thing a Eurosystem paper is well placed to say.
