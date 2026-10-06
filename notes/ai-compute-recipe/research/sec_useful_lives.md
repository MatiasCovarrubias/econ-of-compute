# Useful lives of servers, network equipment and GPUs in SEC filings

Pulled on 28 Sep 2026 from 31 filings (10-K, 10-Q, 20-F, 6-K, S-1, 424B4) of 11 companies. Every
number was verified in the text fetched from sec.gov.

| Company | Life now | History, and depreciation or net-income effect |
|---|---|---|
| Amazon | 5–6 yrs (a subset cut 6→5 from 2025) | 3→4 (2020, −$2.7B); servers 4→5 and network 5→6 (2022, −$3.6B); 5→6 (2024, −$3.2B); subset 6→5 (2025, +$1.4B, citing AI/ML pace); early-retirement charges ~$0.92B (Q4 2024) and ~$0.6B (2025) |
| Microsoft | 2–6 yrs | 3→4 (FY21, est. +$2.7B operating income); 4→6 (FY23, est. +$3.7B); no change FY24–26 |
| Alphabet | 6 yrs | 3→4 (2021, −$2.6B); 4→6 (2023, −$3.9B); no change to Q2 2026 |
| Meta | 5–5.5 yrs | →4 (2021, −$0.62B); →5 (2022, −$0.86B); →5.5 (2025, −$2.92B) |
| Oracle | 6 yrs | 4→5 (FY23, −$434M operating expenses); 5→6 (FY25, −$733M) |
| CoreWeave | 6 yrs (technology equipment) | 5→6 (2023, −$20M) |
| Nebius | GPUs 4 yrs; servers and network 5 from 2026 | 4→5 (2026, −$86.1M in H1) |
| IREN | HPC hardware 5 yrs | |
| WhiteFiber | Cloud equipment 5 yrs | 3→5 (2025) |
| Nscale (S-1, Sep 2026) | GPUs and related infrastructure 5–6 yrs | |

Caveats:
- Asset classes differ. Amazon's 2020 change covers servers only, and Meta's changes cover
  "selected cohorts". Oracle's line mixes in machinery. CoreWeave's "technology equipment" is not
  defined as GPUs.
- Effects are measured on different bases. Microsoft gave only ex-ante estimates.
- Lambda and Crusoe have no S-1 on EDGAR. Applied Digital reports only a 3–5 year networking and
  electrical line.

Full row-level observations with quotes: `sec_useful_lives_obs.csv`.
