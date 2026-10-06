# GPU rental and resale prices: implied economic depreciation

Observations in `gpu_rental_obs.csv` (collected 28 Sep 2026).

Rates below are log changes per year, ln(P1/P0)/years.

**H100 time series (includes scarcity swings):**
- SemiAnalysis composite, 2H23 → Jul25: −0.48/yr.
- AWS P5 list: −0.30/yr, all in one cut in Jun 2025.
- From mid-2025 the path is flat or rising. Silicon Data went from 2.16 (Sep25) to 2.70 (Sep26). SemiAnalysis 1-year contracts went from 1.70 to 2.35.

**Cross-section by vintage** (Silicon Data neo-cloud indices, Sep 2026: A100 1.57, H100 2.70, B200 5.87, B300 6.80): the slope is about +0.27 log per year of vintage.

**Resale:** H100 at about 57% of new after 3 years gives −0.18/yr. A 25% floor after 5+ years gives about −0.28/yr.

**Epoch price-performance:** 0.32 log/yr (0.14 orders of magnitude).

**Implied geometric δ for GPUs: about 0.20–0.30** (economic life 3.5–5 years).
- The 2023–25 time-series decline includes the unwinding of a scarcity premium, so it overstates δ.
- The 2025–26 rebound reflects scarcity in the other direction.
- For δ, prefer the vintage gradient and resale age profiles.
