# GPU failure rates versus price-performance (obsolescence)

Observations in `gpu_failure_priceperf_obs.csv`. PDFs are in
`References/engineering/it_equipment/`. Collected 28 Sep 2026.

**Physical failure is small.**
- GPUs actually replaced: 0.4%/yr for A100 and 0.8%/yr for H100 (NCSA Delta, tiny samples).
- The widely quoted "~9% H100 failure rate" comes from Tom's Hardware's arithmetic on Meta's
  Llama 3 Table 5. It counts job interruptions (mostly cleared by reset or remap), not dead GPUs.
- Warranty and RMA terms move failure cost to the vendor: a 3-year base warranty, extensions to
  4–5 years, and 5 years of NVIDIA service after end of sale.

**Obsolescence is large.** Price-performance improves by 0.28–0.36 log/yr (Epoch: doubling in
2.0–2.5 years; "30% cheaper each year"). The spending-weighted 2023–25 series gives 0.40 (90% CI
0.31–0.51).

**Implication.** Economic depreciation of GPUs is driven by obsolescence (roughly 25–40 points a
year), with physical failure adding at most about 1 point. This is consistent with the rental and
resale evidence (δ ≈ 0.20–0.30, `gpu_rental.md`).
