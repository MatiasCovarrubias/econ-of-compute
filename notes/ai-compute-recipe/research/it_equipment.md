# IT equipment of AI_compute: bill of materials, costs, lives, supply chain, operating inputs

Research note, 28 Sep 2026. Scope: the capital that AI_compute (z) owns (servers, GPUs, networking,
storage) and the compute layer's non-space operating inputs, by archetype A0/A1 (CPU cloud), A2
(HGX H100), A3 (GB200/GB300 NVL72), A4 (Vera Rubin, Rubin Ultra/Kyber).

- **Observations:** `it_equipment_obs.csv` (289 rows, one per observation, with URL, page and
  verification status). The helper files `sec_useful_lives*.{md,csv}`, `gpu_rental*.{md,csv}` and
  `gpu_failure_priceperf*.{md,csv}` in this folder are merged into it.
- **PDFs:** `References/engineering/it_equipment/` (33 files: NVIDIA datasheets and user guides,
  the CoreWeave 10-K, the Nebius Q4 letter, BEA methodology, reliability papers, CRS, the Federal
  Register 232 notices).
- **Verification:** every number below was verified at its URL or in a local PDF unless it is
  marked UNVERIFIED. "Arithmetic" means our own calculation from verified inputs.
- **Primary vs re-quote:** Section 10 traces the most-cited re-quotes to their origins.

## 0. Bottom line for the recipe

1. **The IT rack alone is not the IT capital.** The Bank of Italy $3.0m per NVL72 (CNT Table A1)
   is the rack only. It matches SemiAnalysis's $3.1m GB200 rack "for a typical hyperscaler".
   - SemiAnalysis's all-in cost is $3.9m per rack, so scale-out networking, storage and other
     items add about **20–25% on top** (they are 17–21% of IT capex).
   - With them, IT is about **72% of campus capex** (CNT rack + $0.8m against CNT's non-IT $1.5m).
     Van Nieuwerburgh (VN) gets 68% and Epoch 69%. The current recipe uses 67% and leaves
     networking out.
2. **Composition of IT capex (A3, share of all-in cluster IT capex):**

   | Item | Central | Range |
   |---|---|---|
   | GPU modules incl. HBM | 55% | 50–60% |
   | Rest of compute tray (Grace CPU, LPDDR, NICs, boards) | 14% | 12–17% |
   | NVLink switch trays and rack infrastructure (power shelves, busbar, cold plates, cabling) | 10% | 8–12% |
   | Scale-out network | 14% | 8–19% |
   | Storage | 4% | 2–6% |
   | Integration and commissioning | 3% | 2–5% |

   About **55–60% of the cluster's IT capex is NVIDIA gross profit**. NVIDIA content is more than
   92% of the rack, at a 71–75% gross margin.
3. **Cost per MW of IT load (all-in, $m):**
   - A0/A1: about 15 (10–22), low confidence.
   - A2: 24 (21–28).
   - A3 GB200: 27 (26–30).
   - A3 GB300: 37 (31–42).
   - A4 Vera Rubin: about 50 (35–65), low confidence.

   Cost per rack rose about 15× from CPU to GB200. Cost per MW rose only about 2×, because rack
   power rose about 12×.
4. **δ_IT.**
   - Geometric δ for GPU servers is about **0.27 (0.20–0.33)**; for networking about 0.20
     (0.15–0.28); for storage about 0.30.
   - Blended, that is **δ_IT ≈ 0.26 (0.20–0.32)**. The recipe's 0.25 is inside the band, and the
     plan's proposed 0.30 sits at its upper end.
   - Physical failure contributes about 1 point; obsolescence does the rest.
5. **Investment column of z, at purchasers' value.** Central (range):
   - Computers 3341: 0.77.
   - Communications equipment 3342: 0.13.
   - Computer systems design 541512 (integration): 0.03 (0.02–0.05).
   - Wholesale: 0.06 (0.03–0.10).
   - Transport: 0.01 (0.005–0.015).
   - Retail: 0.

   This replaces the PEQ average-buyer margins (wholesale 0.19, retail 0.14 for 334111).
   Import shares: servers 0.85–0.95, networking 0.80–0.95, storage 0.60–0.80.
6. **Non-space, non-power purchases of the compute layer: about 0.06–0.08 per $ of GPU-cloud
   revenue.**
   - Software 0.02, telecom/transit 0.01, maintenance and spares 0.015, purchased S&M and G&A
     services 0.02–0.03.
   - Labour (excluding the labs) is 0.06–0.12.
   - CNT's per-rack opex (network $20k, maintenance $25k, other $40k) is 2–4% of *realised*
     revenue per rack, not the 0.3–0.6% that list prices imply.

## 1. Archetype specifications (corrected against sources)

| | A0/A1 CPU cloud | A2 HGX/DGX H100 | A3 GB200 NVL72 | A3 GB300 NVL72 | A4 Vera Rubin NVL72 / Rubin Ultra (Kyber) |
|---|---|---|---|---|---|
| Years | 2015–22 | 2023–24 | 2025 | 2025–26 | 2026–28 |
| Unit | 2-socket server, ~0.3–0.8 kW | 8-GPU server, 10.2 kW max (DGX H100) | 72 GPU + 36 CPU rack | same | 72 packages (144 dies); Kyber 576 dies |
| kW per rack | mean 8.4 (Uptime 2020); modal <10, drifting to ~10 by 2025; ≤12 (SemiAnalysis) | ~40 operating (4 DGX per rack, NVIDIA RA; SemiAnalysis). TrendForce 60–80 kW is the TDP of dense HGX H200/B200 racks | ~120 operating (NVIDIA user guide); 123.6–132 (SemiAnalysis); 140 TDP (TrendForce, Meta Catalina) | 130–140 (TrendForce); 142 (VN citing NVIDIA RA, cluster-equivalent) | ~150–180 per NVL72 at facility level (NVIDIA: 40k GPUs per 100 MW; arithmetic); Kyber 600 kW, 800 VDC, up to 1 MW |
| Cooling | air | air | liquid (cold plates, CDU) | liquid | 100% liquid, 45°C inlet |
| Scale-out NIC | 10–25 GbE, later 100G | 8× CX-7 400G per server | 4× CX-7 + 2× BF-3 per 4-GPU tray | 4× CX-8 800G + 2× BF-3 | CX-9 1.6T; co-packaged optics switches (Quantum-X 2025, Spectrum-X 2026) |

Corrections to the indicative specs:
- **A2 is ~40 kW**, not 60–80.
- **A3 spans 120–142 kW** depending on GB200 vs GB300 and on operating draw vs TDP.
- **"NVL144" was renamed Vera Rubin NVL72.** NVIDIA now counts packages, not dies.
- **Rubin Ultra NVL576 (Kyber) is ~600 kW** and targeted at 2027.
- **A100 (2020–22) sits between A1 and A2.**

## 2. Bill of materials per generation

Shares are of all-in cluster IT capex unless stated. "Rack/server" means the compute system as
sold.

| Component | A0/A1 CPU cloud | A2 H100 | A3 GB200 / GB300 | A4 Vera Rubin |
|---|---|---|---|---|
| Accelerator dies + HBM | n/a | GPU+NVSwitch baseboard 72% of DGX ($195k of $269k); ~55–66% of cluster | GPU modules ~68% of GB300 rack (~$3.4m of ~$5.0m); ~55% of cluster | similar; HBM4 288 GB per package |
| HBM within the GPU's *manufacturing* cost | n/a | ~40% (UNVERIFIED) | B200: HBM3E $2.9k of ~$6.3k (46%); HBM + CoWoS ~2/3 | higher (HBM4/4e) |
| CPUs | large share of CPU+board+PSU+chassis ≈45% of server | ~2% of cluster (blog model) | Grace inside compute tray; rest of tray ~17–20% of rack | Vera |
| DRAM | ~40% of a 1 TB 2-socket server | <5% of AI server | LPDDR5X in tray | |
| Local NAND | 14.7% of server BOM | small | 4× 3.84 TB E1.S per tray | ~$1m 3D NAND per rack (press, UNVERIFIED) |
| NVLink switching / scale-up | n/a | in baseboard | NVLink trays ~5% of rack (by subtraction); copper spine (cost paywalled) | same; optical scale-up would add >$5.6m per NVL576 |
| Rack infrastructure (power shelves, busbar, cold plates, manifolds, steel, cabling, integration) | small | small | <8% of rack; liquid cooling $42k (GB200) / $50k (GB300), ~1–1.5% | ~$56k cooling |
| Scale-out network (NICs outside the tray, switches, optics, cables) | 10–15% central, up to 25–30% | 15% (9–20) | 14% (8–19) | 12% (8–18), CPO lowers optics |
| Storage | 15% (8–25), low confidence | 4% (2–8) | 4% (2–6) | 5–15% if NAND moves into the rack |
| Integration / ODM margin | OEM margin 10–20% (Supermicro 11–18%, Dell 20% consolidated) | ~5–10% | ODM L10–L11 margin under 10% on non-NVIDIA content; 2–5% of rack | <5% |
| NVIDIA gross profit in price | n/a | ~70% of DGX price ($190k of $270k); ~55% of cluster | 71–75% corporate GM × >92% NVIDIA content → 65–70% of rack, 55–60% of cluster | 70–75% |

Main sources: SemiAnalysis (AI Server Cost Analysis 2023; Neocloud Playbook 2024; GB200 Hardware
Architecture 2024; H100 vs GB200 benchmarks 2025), Epoch (ml_hardware.csv, B200 cost breakdown,
1 GW cost breakdown), Data Gravity (GB300 purchase orders), NVIDIA DGX and GB user guides, NVIDIA
10-K and CFO commentary.

## 3. Cost per rack, per GPU and per MW of IT load

| | Rack or server price | All-in per rack-equivalent (incl. network and storage) | All-in per GPU | $m per MW of IT | kW per rack |
|---|---|---|---|---|---|
| A0/A1 | $7.4k per server (IDC 2019 average); $10.4k 2-socket 1 TB (SemiAnalysis 2023); $3k (Greenberg 2008) | $0.2–0.3m per 8–12 kW rack (arithmetic) | n/a | **15 (10–22)**; Greenberg $3k/180 W → $17m per MW of average draw | 8–12 |
| A2 | $190k (2025) – $270k (2023–24) per 8-GPU server | $1.0–1.3m per 4-server rack | **$35k (31–42)**. SemiAnalysis $31.3k (2025), $35.4–39.8k (2024, ex-storage); Epoch Colossus $35k | **24 (21–28)** at 1.4–1.5 kW all-in per GPU (SemiAnalysis 150 MW / 100k GPU; CoreWeave 360 MW / 250k GPU) | ~40 |
| A3 GB200 | **$3.1m** (SemiAnalysis); $3.0m (CNT); $2.8–3.4m (press); ~$3m (Barron's via Data Gravity) | **$3.9m** (SemiAnalysis) | **$54k** (all-in); $43k rack only | **27 (26–30)**. Epoch $26.1m (1 GW IT); $3.9m / 132–145 kW = $27–30m | 120–140 |
| A3 GB300 | **$4.5m (4.0–5.0)**. VN $4.0m (assumption, unsourced); purchase orders "just under $5.0m" (Data Gravity); press $6–6.5m; Loop Capital $3.7–4.0m (UNVERIFIED) | $5.5m (4.8–6.0) | **$76k (67–83)** | **37 (31–42)**. VN $34m (142 kW cluster-equivalent) | 135–142 |
| A4 Vera Rubin NVL72 | $5–7m (press); TrendForce "~2× GB300 ASP" → $8–10m; central $7m | $8.5m (6–12) | ~$115k (85–165) | **~50 (35–65)**, low confidence | ~150–180 (NVL72); 600 (Kyber) |

Reading:
- **Per GPU**, all-in capex rises about 1.6–1.7× from H100 to GB200 (SemiAnalysis). TCO rises
  about 1.6×.
- **Per MW**, the rise is small from A0 to A3 GB200, because CPU servers were also about $20m
  per MW of nameplate. GB300 and Rubin add HBM and price per watt.
- **Stock check:** CoreWeave's gross technology equipment was $20.9bn plus $9.4bn construction in
  progress, against 850 MW active at end-2025. That is about $25–35m per MW, in line with the table.

## 4. Networking and storage shares: cross-check

| Source | Archetype | Network | Storage | Non-rack total | Type |
|---|---|---|---|---|---|
| SemiAnalysis 2025 (H100 $190k vs $250k all-in) | A2 | — | — | 24% | analyst, primary |
| SemiAnalysis Neocloud 2024 (SuperPOD reference architecture / optimised 2:1) | A2 | 15.1% / 9.4% (ex-storage) | excluded | — | analyst, primary |
| Cottier et al. (Kostovic, from the H100 SuperPOD reference architecture) | A2 | 19% (20% for ≥4096 GPUs) | — | 19% | academic; the origin is an unpublished note |
| Pytorch-to-Atoms, Meta 24k H100 cluster | A2 | 18.4% | — | — | blog, low quality |
| SemiAnalysis 2025 (GB200 $3.1m vs $3.9m) | A3 | — | — | 20.5% | analyst, primary |
| Epoch 2026, 1 GW GB200 ($21.2bn servers, $4.9bn network) | A3 | 18.9% (all non-server) | inside network | 18.9% | analyst; re-quotes SemiAnalysis |
| Van Nieuwerburgh 2026 (allowances) | A3 GB300 | 8.3% | 4.2% | 16.7% (with 4.2% integration) | academic, unsourced allowance |
| CNT 2026 | A3 | not in the $3.0m; the $0.24m "Other" possibly | — | — | academic |
| NVIDIA networking share of data-center revenue | A2 / A3 | 11.3% (FY25) / 16.2% (FY26, incl. NVLink) | — | — | seller view |
| Greenberg 2009 (Microsoft) | A0 | ≤25% of servers+network (includes WAN) | — | — | academic |
| BEA 5140: EP20 share of IT-equipment investment, 2024 | A1/A2 | 30% | EP1G 1.7% | — | official; industry-wide LAN/WAN, not only fabric |

**Verdict.**
- **Agreement:** the independent A2/A3 analyst sources (SemiAnalysis's two articles, Cottier via
  Kostovic, Epoch via SemiAnalysis) agree that non-rack IT is **17–24%** of cluster IT capex.
  That is networking at about 13–19% plus storage at about 3–5%. VN's 12.5% for network plus
  storage is at the low end and is an unsourced allowance.
- **Epoch and SemiAnalysis are not independent:** Epoch's server and network prices come from
  SemiAnalysis.
- **Topology moves the share by up to 6 points:** oversubscription, InfiniBand vs Ethernet, and
  a third switch tier.
- **Recommended:** network 14% (8–19), storage 4% (2–6), integration 3% (2–5).
- **The BEA share is not comparable:** its 30% EP20 share is an industry-wide asset share, not
  cluster fabric.

## 5. Vendor and integrator margins

- **NVIDIA:**
  - GAAP gross margin was 75.0% in FY25, 71.1% in FY26 (H20 charge; 75.0% in Q4 FY26).
  - Chip level: SemiAnalysis puts the DGX H100 gross profit at about $190k of a $270k price (70%).
    Epoch puts the B200 at about 82% at the chip and about 73% realised on Blackwell bundles.
  - Rack level: NVIDIA content is more than 92% of GB300 rack value (Data Gravity), so NVIDIA
    gross profit is about **65–70% of the rack** and about **55–60% of cluster IT capex**.
- **ODM/OEM:** ODMs find it hard to keep a 10% margin on NVIDIA-supplied L10 trays, which are about
  90% of server cost (DigiTimes via Tom's Hardware).
  - Supermicro gross margin: 18.0% (FY23), 13.8% (FY24), 11.1% (FY25), 10.8% (FY26).
  - Dell consolidated: 20%.
  - Integrator value added on an NVL72 is **2–5% of rack price**.
- **Distribution:** TD SYNNEX gross margin is 7.0% (FY25); its Hyve unit sells direct to
  hyperscalers. Arrow and Avnet are 10–11%, but they distribute components.

## 6. Service lives and depreciation

**Accounting lives** (SEC filings, verified; details in `sec_useful_lives.md`):

| Company | Life |
|---|---|
| Amazon | 5–6 years (a subset cut 6→5 in 2025, citing AI/ML) |
| Microsoft | 2–6 |
| Alphabet | 6 |
| Meta | 5–5.5 |
| Oracle | 6 |
| CoreWeave ("technology equipment", 5→6 in 2023) | 6 |
| Nebius | GPUs 4; servers and network 5 from 2026 |
| IREN, WhiteFiber | 5 |
| Nscale | 5–6 |

Networking is grouped with servers everywhere (Amazon moved network 5→6 in 2022).

**BEA:**
- **Communications equipment:** geometric 0.15 (11 years) in rental/leasing and computer
  systems design; 0.11 (15 years) elsewhere. Declining-balance rate 1.65.
- **Computers:** empirical age–price profiles, not a single rate. Mainframes (1980–94 vintages)
  keep 0.30 of value at age 4 and 0.17 at age 5, which implies δ ≈ 0.30–0.35. PCs keep 0.17 at
  age 4 (δ ≈ 0.44); storage 0.32 at age 4 (δ ≈ 0.28–0.35).
- **Hosting (5140):** the implied δ on computers is about 0.33 (dc_it_stock.tex).
- **Software:** prepackaged 0.55, custom 0.33.

**Market evidence** (`gpu_rental.md`, `gpu_failure_priceperf.md`):
- **H100 rental, time series:** SemiAnalysis index $6.62 (2H23) → $2.79 (Jul 2025), about
  −0.48 log/yr, which includes the unwinding of a scarcity premium. From mid-2025 the path is flat
  or rising: Silicon Data $2.16 (Sep 2025) → $2.70 (Sep 2026); SemiAnalysis 1-year contracts
  $1.70 → $2.35.
- **Vintage cross-section, Sep 2026:** A100 $1.57, H100 $2.70, B200 $5.87, B300 $6.80. The slope
  is about +0.27 log per year of vintage, so δ ≈ 0.24.
- **Resale:** an H100 fetches about 57% of new after 3 years (δ ≈ 0.17) and about 25% after 5 or
  more years (δ ≈ 0.24–0.28). A100s are still rented; AWS has "never retired an A100".
- **Price-performance:** 0.28–0.36 log/yr (Epoch 2022–24), and 0.40 for chips bought in 2023–25.
  That is an obsolescence ceiling of δ ≈ 0.25–0.33.
- **Failures:** GPUs actually replaced run at 0.4%/yr (A100) and 0.8%/yr (H100) (NCSA). The
  quoted "9% H100 failure rate" is Tom's Hardware's arithmetic on Llama 3 job interruptions
  (148 faulty GPU + 72 HBM3 in 54 days on 16,384 GPUs), mostly cleared by reset. Warranties run
  3 years, extendable to 5. A spare pool of about 5% is needed for 99.9% job availability. This
  adds about 1 point to δ.

**Reconciliation.**
- **Accounting to geometric:** BEA's convention δ = DB/L with DB = 1.65 turns 5–6-year accounting
  lives into δ = 0.27–0.33.
- **Market evidence:** vintage gradients and resale point to 0.17–0.28.
- **Price-performance** caps obsolescence at about 0.25–0.33.
- **Recommended δ:**

  | Asset | δ | Range |
  |---|---|---|
  | GPU servers | **0.27** | 0.20–0.33 |
  | Networking | **0.20** | 0.15–0.28 (between BEA 0.15 and generation-tied refresh) |
  | Storage | **0.30** | |
  | **Blended IT** (80/15/5 weights) | **0.26** | 0.20–0.32 |

## 7. Supply chain, imports, margins and BEA classification

**Where things are made.**
- **Chips:** GPU logic dies come from TSMC Taiwan, packaged with CoWoS. The first Blackwell wafer
  came out of TSMC Arizona in Oct 2025; Arizona packaging (Amkor, TSMC, SPIL) is not yet in
  volume. HBM comes from SK hynix, Samsung and Micron; SK hynix's Indiana HBM packaging plant is
  due in 2H 2028.
- **Trays and racks:** Foxconn, Quanta and Wistron/Wiwynn build them in Taiwan and Mexico.
  Foxconn is building the "world's largest AI server factory" in Guadalajara and claims more than
  40% of AI servers. There is US assembly too (Foxconn Houston and Wisconsin, Wistron Fort Worth,
  Supermicro San Jose), and NVIDIA announced $500bn of "American-made" AI supercomputers in
  April 2025.
- **Networking gear** comes from Vietnam, Thailand, Mexico and Taiwan.

**US imports, $bn** (UN Comtrade US-reported customs value; Census end-use):

| Code | 2022 | 2023 | 2024 | 2025 | 2025 partners |
|---|---|---|---|---|---|
| HS 847150 servers | 42.5 | 36.9 | 61.8 | 163.6 | Mexico 49%, Taiwan 42% |
| HS 847330 parts incl. GPU trays | 32.9 | — | 53.9 | 88.5 | Taiwan 52% |
| HS 851762 switches/routers | 50.6 | — | 55.8 | 84.0 | Vietnam 28%, Thailand 22% |
| HS 847170 storage | 11.0 | 7.5 | 9.6 | 13.9 | Thailand 54% |
| HS 854231 processors | 24.4 | — | 28.3 | 32.5 | US is a net exporter |
| End-use 21300 computers | 102.3 | 88.5 | 116.8 | 218.2 | Mexico 84.6, Taiwan 72.3 |

- **Re-exports:** 58% of 2025 server exports were re-exports. GPUs and boards go out and come back
  as servers from Mexico.
- **The Census trade API now needs a key** (UNVERIFIED path), so the HS detail uses Comtrade.

**Import shares.**

| Item | Estimate | Basis |
|---|---|---|
| Servers | 0.81 (2023), 0.86 (2024) | Absorption: HS 847150/80 net of re-exports against NAICS 334111 shipments ($22.6bn in 2024) |
| Servers | 0.72–0.95 (2022–25) | NIPA net imports over PFI computers |
| Servers | 0.949 | 2017 BEA import matrix, equipment-investment column, 334111 |
| **Servers, recommended** | **0.85–0.95** | |
| Networking | 0.64 (334210), 0.84 (334220) | 2017 import matrix |
| Networking | ~1 | 2024 trade: HS 851762 net imports exceed 3342-router shipments |
| **Networking, recommended** | **0.80–0.95** | |
| **Storage, recommended** | **0.60–0.80** | 2017 BEA: 0.61 (import matrix), 0.56 (supply) |
| Semiconductors (334413) | 0 in PFI | BEA allocates them to intermediate use. GPUs reach investment only inside imported 334111 servers and 8473.30 parts |
| Fed FEDS 2025-109 | 80% | High-tech equipment overall |

**Margins.**
- **The PEQ 2017 margins describe the average buyer, not hyperscalers:**

  | Commodity | Producers' value | Transport | Wholesale | Retail |
  |---|---|---|---|---|
  | 334111 | 0.667 | 0.007 | 0.186 | 0.141 |
  | 3342 | 0.632 | 0.006 | 0.354 | 0.008 |

  The 2012 benchmark put the 334111 wholesale margin at 0.244.
- **Hyperscalers and neoclouds buy direct from ODMs or NVIDIA-certified OEMs**, or through thin
  intermediaries (Hyve; TD SYNNEX GM 7%).
- **Freight is small:** the CIF/FOB gap is 0.3–0.6% (servers) and 1.1% (switches), in line with
  PEQ transport of 0.7%.
- **Recommendation:** wholesale 0.06 (0.03–0.10), transport 0.01, retail 0.

**BEA classification.**
- **Servers, storage, integration, networking:** servers fall in EP1A mainframes (and EP1H system
  integrators), storage in EP1G, integration services (541512) in EP1H, networking in EP20.
- **Integration is capitalised with the hardware:** in the PEQ, 541512 is 36% of the computers
  line (line 4), and it corresponds to EP1H.
- **Tariffs:**
  - Servers (8471), trays (8473.30), switches (8517.62) and chips (8542) were excluded from the
    2025 reciprocal tariffs, and their MFN duty is zero.
  - The 2026 Section 232 proclamation puts 25% on a narrow class of advanced chips, but exempts
    US data-center use.
- **NVIDIA's markup:** its design value sits inside the import price and is not recorded as a US
  export. Epoch estimates this at about 0.3 pp of GDP growth (Juniewicz et al. 2026).

**Recommended investment column for z** (purchasers' value, sums to 1):

| Item | Central | Range |
|---|---|---|
| Computers (334111/2/8) | 0.77 | 0.72–0.82 |
| Communications equipment (3342, incl. optics) | 0.13 | 0.08–0.18 |
| Computer systems design (541512, integration) | 0.03 | 0.02–0.05 |
| Wholesale | 0.06 | 0.03–0.10 |
| Transport | 0.01 | 0.005–0.015 |

Import shares per cell are as above. Under the VLW grouping, Computers + Communications
equipment ≈ 0.90.

## 8. Operating inputs of the compute layer (beyond power and space)

The main evidence is CoreWeave (10-K FY2025, Q2 2026), Nebius (20-F 2025), IREN (AI Cloud
segment), Epoch's 1 GW TCO, the Census SAS/AIES for NAICS 518 and the BEA 2017 use table.

| Per $1 of GPU-cloud revenue | Best | Range | Evidence | Maps to |
|---|---|---|---|---|
| IT depreciation (memo) | 0.46 | 0.45–0.79 | CoreWeave 45–48% (FY25), 54% (Q2 2026); Nebius 79% (4-yr life, ramp-up) | capital services |
| Space / colocation rent | 0.20 | 0.14–0.22 | CoreWeave total lease cost 22% (~$156/kW-month); Nebius 14% | AI_facilities |
| Power | 0.05 | 0.035–0.06 | CoreWeave ≥5.5% (derived); IREN 3.5% | Utilities (or via f) |
| Labour (all functions) | 0.09 | 0.06–0.12 excl. IPO stock comp | CoreWeave 2.6 FTE per active MW; IREN direct 6.6%; CPU cloud 0.27–0.34 (Census) | labour |
| Software | 0.02 | 0.01–0.04 | CoreWeave support+software residual ~4% incl. maintenance; NVAIE list $4,500 per GPU-yr ≈ 8% of H100 on-demand revenue (upper bound, rarely paid); Census 518 software 3.1% | Info (5112/5415) |
| Telecom / transit | 0.01 | 0.005–0.02 | CNT $20k per rack-yr; BEA 518200 telecom 1.9%; Koomey 8.5% of opex (2007); CoreWeave charges no egress | Info (517) |
| Maintenance and spares | 0.015 | 0.01–0.03 | CNT $25k per rack-yr (0.8% of rack capex per yr); ~5% spare pool; 3-year warranties | Repairs (811) / Computers |
| Purchased S&M + G&A services | 0.025 | 0.02–0.05 | CoreWeave S&M 2.3–2.8%, professional services +$117m | Prof_Tech / Admin |
| Property tax and insurance | 0.01 | 0.005–0.015 | Epoch $0.143m per MW-yr; Virginia BPP tax 0.05–1.4% of equipment per yr; insurance: no data | taxes on production (not a purchase) |

**Cross-check against CNT Table A3.**
- CoreWeave's realised revenue is $8.5m per average active MW-yr, which is about $1.1m per
  132 kW rack-year (fleet-weighted, mostly H100).
- On that base, CNT's network $20k, maintenance $25k and other $40k are 1.8%, 2.2% and 3.6% of
  revenue. That agrees with the table above.
- CNT's on-demand list rents ($6.6–10.1m per NVL72 per year) are 4–6× realised revenue. Use them
  for payback arithmetic, not for cost shares.

**Staffing per MW:**

| Source | FTE per MW |
|---|---|
| CoreWeave (all functions) | 2.6 |
| Nebius (group-wide) | 8.8 |
| Virginia site staff (JLARC) | 1.6 |
| Meta Richland Parish (on-site jobs) | 0.2–0.5 |
| Epoch (site labour, $0.04m per MW-yr) | ~0.3–0.4 |

## 9. Best estimate and range per generation

| | A0/A1 | A2 | A3 GB200 | A3 GB300 | A4 |
|---|---|---|---|---|---|
| kW per rack | 8–12 | 40 | 120–140 | 135–142 | 150–180 (Kyber 600) |
| Rack/server price | $7.5–10k per server | $190–270k per server | $3.1m (2.8–3.4) | $4.5m (4.0–5.0) | $7m (5–10) |
| All-in per GPU | — | $35k (31–42) | $54k (50–58) | $76k (67–83) | ~$115k (85–165) |
| $m per MW IT | 15 (10–22) | 24 (21–28) | 27 (26–30) | 37 (31–42) | ~50 (35–65) |
| Compute system share of IT | ~70–80% | 76–85% | ~80% | ~80% | ~75–85% |
| Network share | 15% (10–30) | 15% (9–20) | 14% (8–19) | 13% (8–18) | 12% (8–18) |
| Storage share | 15% (8–25) | 4% (2–8) | 4% (2–6) | 4% (2–6) | 5–15% |
| Integration share | ~3% | ~3% | 3% (2–5) | 3% (2–5) | 2–4% |
| NVIDIA gross profit / IT capex | — | ~55% | 55–60% | 55–60% | ~55–60% |
| δ (geometric) | 0.30 (BEA profiles) | 0.27 (0.20–0.33) | 0.27 | 0.27 | 0.27–0.33 |
| Accounting life | 4–6 years | 5–6 (Nebius 4) | 5–6 | 5–6 | n/a |
| Import share | 0.85–0.95 | 0.85–0.95 | 0.85–0.95 | 0.85–0.95 | 0.80–0.95 (US assembly rising) |

Confidence is highest for A2 and A3 GB200: several primary analyst sources, vendor specs and
filings. It is medium for GB300: purchase orders from one blog, unsourced BPEA assumptions and
press. It is low for A0/A1 $/MW and storage, and for all of A4, which rests on press and our
arithmetic.

## 10. Cross-check verdicts per number, and re-quote traces

- **GB200 rack $3.0–3.1m.** CNT (averaged from Savills, C&W, Dgtl Infra, DCD and Anastasi) and
  SemiAnalysis (primary) are independent and agree within 3%. The Barron's/Tae Kim ~$3m is
  consistent. Verdict: **agree.**
- **GB300 rack price.** VN's $4.0m has no source. Data Gravity's ~$5.0m comes from unnamed
  purchase orders. Press has $6–6.5m, and Loop Capital $3.7–4.0m (UNVERIFIED). Verdict:
  **disagree by ±25%**. The sources differ on whether the price is an ODM, purchase-order or list
  price, and on whether the CDU, network and warranty are included. Use $4.5m (4.0–5.0).
- **Non-rack share 17–24%.** SemiAnalysis (two articles) and Cottier/Kostovic agree, and Epoch
  (a SemiAnalysis re-quote) matches. VN's 12.5% for network plus storage is low. Verdict: **agree,
  except VN.**
- **IT share of campus capex, 68–72%.** VN 68%, Epoch 69%, CNT + SemiAnalysis add-on 72%, the Fed
  30/70 structures/equipment split, and Alphabet 60/40 (servers and network vs buildings). Verdict:
  **agree.** Alphabet is lower because its figure is a gross stock with older CPU fleets.
- **$/MW A3 about $26–30m.** Epoch $26.1m (SemiAnalysis inputs) against SemiAnalysis's $3.9m per
  132–145 kW. VN's $34m is for GB300. Verdict: **agree.**
- **H100 all-in $31–42k per GPU.** SemiAnalysis (2024 and 2025), Epoch Colossus, and Cottier's
  server route (DGX price/8 = $33.6k × 1.23 = $41k) agree. Cottier's chip route (1.64 × 1.23
  applied to a $25–30k chip) gives $50–60k, which is too high. Verdict: **agree, except for the
  chip route.** Its 1.64 comes from P100–A100 list prices; the H100 BOM implies about 1.4.
- **Rack power.** NVIDIA 120 kW (operating) against TrendForce and Meta 140 kW (TDP/capability).
  Verdict: **consistent once you separate operating draw from TDP.**
- **δ.** Accounting lives (BEA convention), rental vintage slope, resale and price-performance
  overlap at 0.24–0.30. Verdict: **agree.** The H100 time series of 2023–25 (−0.48 log/yr)
  overstates δ because it includes the end of a scarcity premium.
- **Import share 0.80–0.95.** Fed 80%, absorption 0.81–0.86, the 2017 import matrix 0.95, and
  NIPA net imports over PFI 0.72–0.95. Verdict: **agree on 0.85 ± 0.1.**
- **Wholesale margin.** PEQ gives 0.19–0.24 for the average buyer, against 0.03–0.10 implied by
  direct ODM channels and distributor gross margins of 7–11%. Verdict: **disagree.** Use the
  channel evidence for hyperscalers and neoclouds, and state the departure from PEQ.

**Re-quote traces:**
- Cottier's 19% interconnect share → Kostovic (unpublished) → NVIDIA H100 SuperPOD reference
  architecture.
- Epoch's 1 GW server and network prices → SemiAnalysis public estimates.
- The "9% H100 annual failure rate" → Tom's Hardware arithmetic on Llama 3 Table 5
  (interruptions, not replacements).
- The "GPUs last 1–3 years" claim → an anonymous X post via TrendForce/Tom's Hardware (not
  usable).
- Liquid-cooling content per rack → Morgan Stanley via Data Gravity (UNVERIFIED origin).
- H100 manufacturing cost $3,320 → Raymond James via The Decoder (UNVERIFIED origin).
- VN's 142 kW → NVIDIA NVL72 enterprise reference architecture (not fetched).
- The Fed's 80% → BEA/Census 2024 imports and investment.

## 11. Implications for `ai_recipe.py` (for the authors; nothing was edited)

1. **Add networking, storage and integration to the IT capex.**
   - Using the CNT rack, use rack × 1.25 (1.2–1.3), or VN's itemisation.
   - This raises the IT share of capex from 67% to about 72%. K_IT rises with it, and the
     investment column gains 3342 and 541512.
2. **δ_IT = 0.26 (0.20–0.32).** The current 0.25 can stay; 0.30 is the upper case, not the
   central one.
3. **Investment margins:** wholesale 0.06, transport 0.01, retail 0 (the current 0.22 wholesale is
   too high). Report import shares per cell.
4. **z's other purchases:** about 0.06–0.08 of compute revenue. Software 0.02 and telecom 0.01 go
   to Info, maintenance 0.015 to Repairs/Computers, and 0.025 to Prof_Tech/Admin. Keep property
   tax as a production tax.
5. **The NVIDIA margin** (55–60% of IT capex) is what makes the import treatment matter. In a
   closed baseline it becomes value added of Computers.

## 12. Open gaps

- **No verified source for:**
  - an ODM-direct share of hyperscaler server purchases (IDC ODM Direct share: page returned 403);
  - GB200 air-freight cost;
  - insurance on IT equipment;
  - the SemiAnalysis item-level BOM tables (paywalled);
  - the Dell'Oro network share of capex (not in the free releases).
- **Rack prices:** the GB300 and Vera Rubin prices rest on press and one blog of purchase orders.
  The Kyber/NVL576 price is unknown.
- **Storage share:** it is weakly sourced everywhere. For A4, check the claim of ~$1m of NAND per
  rack.
- **Conventional-cloud $/MW:** no direct source. Our 10–22 range is our own arithmetic.
- **NVIDIA's industry classification** as a factoryless goods producer, and where BEA records its
  margin: only Epoch's argument, no BEA statement.
- **The Census trade API** now needs a key. HS detail comes from UN Comtrade (US-reported).
  Re-pull from USA Trade Online if an account is available.
- **Two derived numbers could not be settled:** the Pytorch-to-Atoms Meta cluster total
  ($1.047bn vs $0.913bn on two fetches), and Epoch's power multiplier (1.82 vs 2.03 across its
  own documents).
- **Oracle's 14% GPU-rental gross margin** is behind The Information's paywall (UNVERIFIED).
