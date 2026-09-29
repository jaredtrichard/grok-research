# NVIDIA working thesis

GF-NVDA-1 · as of 2026-09-29 · name id `nvda`

Numbers live in the workbook. This file owns the claim, mechanism, and killing conditions. Official price target: [`models/nvda/valuation.md`](../../models/nvda/valuation.md). Do not treat a restated figure here as a second target.

If the model does not say it, it is not this thesis.

## Claim

The initiation view is that NVIDIA’s FY2028E earnings power on the modeled Data Center–led path (company revenue `[VIEW]` $688.5B, diluted EPS `[VIEW]` $15.63 in [`income.md`](../../models/nvda/income.md)) is worth **$500.13/share** at a `[VIEW]` **32× FY2028E P/E** (`valuation.md`). Versus the `[FACT]` 2026-09-29 last close of **$227.21**, that target is about **+120%** (`valuation.md`). The tape’s implied **~14.5×** FY2028E EPS (`valuation.md` diagnostics) prices a far weaker earnings outcome or a structural derating the model does not assume.

## Mechanism and magnitude

- **Revenue path** embeds `[FACT]` 1H FY2027 + Q3 guide + `[VIEW]` Q4 into FY2027E **$405B**, then ~70% growth into FY2028E per management’s preliminary outlook ([`register.md`](register.md) R2.4–R2.5), with Data Center **~92–93.5%** of sales (Hyperscale + ACIE) — see [`segments.md`](../../models/nvda/segments.md).
- **Gross margin** holds `[VIEW]` **~72.5–73%** — above the late-FY2027 trough path management flagged (R2.5), consistent with mix/price after H20/H200 charges roll off (R8.3).
- **Operating income** FY2028E `[VIEW]` **~$448B**; Compute & Networking remains **≥95%** of CODM segment OI (`segments.md`).
- **Full-stack** (accelerators + networking + systems + CUDA ecosystem) sustains content per cluster; units/ASP remain `not obtained` (R9.2), so the model does not pretend a GPU-unit bridge.

Magnitude of the official target and cross-checks (22× EBIT → ~$410, 42× FY2027E → ~$369, bear **24×** / bull **40×** on FY2028E EPS) is entirely in `valuation.md`; cross-checks frame risk, they are not the PT.

## Why this view is right

- Built from primary filings (FY2026 10-K, Q2 FY2027 10-Q/PR/CFO/transcript) in [`register.md`](register.md) / [`research.md`](research.md), not media.
- Uses current **Data Center / Edge** taxonomy (R1.2); does not splice discontinued six-market lines into FY2027+ (R1.3, R9.1).
- Official PT works **backward from the target**: **32×** on modeled FY2028E EPS is the investment idea; the operating statements in `income.md` / `segments.md` are what must be true for that EPS, not a residual fitted to the tape.

## What others miss or get wrong

- Anchoring on China Data Center foreclosure / H200 charges (R8.3) as if they dominate the FY2028 path while Hyperscale+ACIE dollars are still compounding on the guide (R2.4–R2.5, `segments.md`).
- Treating custom ASIC (Google/Amazon/Microsoft/etc., R8.1) as an imminent replacement of the merchant full stack without evidence of share loss quantified in filings (`not obtained`).
- Using stale Gaming/ProViz/Auto splits as if they were still current quarterly drivers (R9.1).
- Applying peak-cycle multiples **or** crisis multiples; **32×** is intentional mid-path given growth vs ASIC/export/supply risk (`valuation.md` rationale).

## Killing conditions (and when to check)

1. **Supply fails:** CoWoS/HBM/foundry constraints (R5) keep shipments below the FY2028 revenue path for two consecutive prints — check each earnings release + CFO commentary.
2. **Margin break:** GAAP GM sustains below ~70% after the guided trough without a clear one-off charge — check each print vs R2.1/R2.5.
3. **Demand freeze:** Hyperscale+ACIE revenue decelerates sharply vs the model (e.g. sequential declines not explained by architecture transition) — check quarterly platform table in filings / `segments.md`.
4. **Custom ASIC share:** Credible primary evidence that merchant GPU content per incremental GW falls enough to break FY2028E EPS by **>20%** vs model — check 10-Q MD&A/competition (R8.1) + customer capex commentary.
5. **Export/regulatory shock:** Broadened controls or antitrust remedies that remove a material slice of addressable Data Center (R8.3–R8.4) — check filings/risk factors each quarter.
6. **Multiple regime:** If the right earnings path is intact but the market sustainably clears below **~24× FY2028E** (bear frame in `valuation.md`) on non-transitory derating, revisit the **32×** official method — check tape vs model EPS after each print.

A last-close move alone does not kill the thesis. Narrative without a modeled number does not kill it. Do not retune the official PT to the tape.

## Explicit non-claims

No LONG, SHORT, or PASS. No second price target. Software/networking standalone economics and unit ASP remain `not obtained` (R9.2–R9.3) and are not smuggled into the thesis as quantified wedges.

## What this file is not

This file assigns no recommendation. Publication of `names.thesis_ref` is Firstmate’s job after the captain merges the cover branch.
