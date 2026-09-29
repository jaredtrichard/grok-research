# Oracle working thesis

GF-ORCL-1 · as of 2026-09-29 · name id `orcl`

Numbers live in the workbook. This file owns the claim, the mechanism, and the killing conditions. Official 12-month price target: [`models/orcl/valuation.md`](../../models/orcl/valuation.md). Do not treat a restated dollar target here as a second source of truth.

## Claim

Oracle’s equity should be valued on **segment-built operating income** as OCI scales—not on headline RPO, not on prepay-boosted operating cash flow, and not on a product-level OCI margin that filings do not provide. The initiation model says cloud infrastructure revenue rises from **$18,101m** (FY2026A) to **$45,931m** (FY2028E) on `[VIEW]` growth in [`inputs.md`](../../models/orcl/inputs.md), cloud-and-software **reported segment margin** glides from **58.9%** to **53.5%** over the same span, and consolidated **operating income** reaches **$31,521m** (FY2028E) in [`income.md`](../../models/orcl/income.md) with no segment-to-OI residual plug in forecast years. [`valuation.md`](../../models/orcl/valuation.md) applies a `[VIEW]` forward **EV/EBIT** on that FY2028E line, nets **FY2027E** modeled net debt from [`balance.md`](../../models/orcl/balance.md), and divides by **R5.5** shares—without capitalizing undisclosed RPO quality (R8.2) or mandatory-convert dilution (R5.7).

The investment idea in one line: **the market already prices a strong OCI earnings ramp at roughly the same forward EBIT the model uses; the official frame adds a modest multiple premium for delivery and margin holding, not a second full RPO lottery ticket.**

If the model does not say it, it is not this thesis.

## Why this view is right

1. **Revenue and margin are tied to reported segments, not narrative RPO.** Product lines in [`segments.md`](../../models/orcl/segments.md) sum to consolidated revenue; three segment margins sum to total reported segment margin (R1.4). Operating income is rebuilt from that margin less filed-style corporate exclusions in [`income.md`](../../models/orcl/income.md). Historical years tie register R2; forecast years use explicit `[VIEW]` OCI and applications growth and margin %—not RPO ÷ years.
2. **OCI acceleration is already in the filings and the base path.** Q1 FY2027 cloud infrastructure revenue was **$7,388m** (+121% YoY [FACT] R3.2); FY2026A OCI was **$18,101m** (R3). The model’s FY2027–FY2028 OCI path (**$31,677m** / **$45,931m**) decelerates from that burst but still implies ~**59%** two-year CAGR [DEDUCTED] from FY2026A—consistent with capacity delivery (850 MW incremental in Q1 [FACT] R3.6) without assuming every RPO dollar converts on schedule.
3. **Margin pressure is explicit, not hidden.** Cloud-and-software infrastructure expense rose ~**$2,800m** YoY in Q1 FY2027 with a lower segment-margin rate (R3.3). The model mirrors that with a **54.5% → 53.5%** cloud-and-software margin `[VIEW]` glide—more conservative than FY2024–FY2026 history but above a collapse scenario.
4. **Cash economics are split correctly for the claim.** Core free cash flow stays **negative** through FY2028E (**$(9,128)m** in [`cashflow.md`](../../models/orcl/cashflow.md)) while reported OCF includes `[VIEW]` customer prepayment financing (R5.2). The thesis and official valuation anchor on **operating income**, not on prepay-inflated OCF or a negative core-FCF DCF check in `valuation.md`.
5. **The tape comparison is narrow, not heroic.** [`valuation.md`](../../models/orcl/valuation.md) [DEDUCTED] implies the last close embeds ~**16×** modeled FY2028E operating income with Q1 FY2027 net debt (R5.1). The official method uses **[VIEW] 17.5×** on the same income line—a gap of mechanism (multiple), not a greenfield OCI story.

## What others miss or get wrong

1. **RPO as revenue or simple NPV.** RPO was **$664,000m** at 2026-08-31 with **~13%** expected in the next twelve months [FACT] R3.4—but customer, margin, funding and cancellation detail is **not obtained** (R8.2). Treating headline RPO as near-term sales or as fully valued optionality double-counts what the segment model already loads into recognized cloud revenue.
2. **Segment margin equals OCI margin.** Only cloud-and-software **aggregate** margin is reported (R1.4, R8.3). Applications, license, and support can offset or mask infrastructure drag; inferring unit economics on GPU contracts from segment margin alone is unsupported.
3. **Reported OCF equals quality earnings.** Q1 FY2027 operating cash flow included **$11,363m** of customer prepayments with a significant financing component [FACT] R5.2. Equating OCF to recurring cash generation ignores the financing bridge the model separates in [`cashflow.md`](../../models/orcl/cashflow.md).
4. **Negative free cash flow means “no earnings power.”** FY2026A capex was **$55,663m** [FACT] R2; `[VIEW]` capex stays elevated in the forecast. Capital intensity is the debate; **operating income** still rises on the modeled path if segment margin and OCI revenue hold.
5. **Balance-sheet risk is only on-balance-sheet debt.** **$260,000m** of mostly data-center lease commitments not on the balance sheet and large power/purchase obligations [FACT] R5.4 are not fully in [`balance.md`](../../models/orcl/balance.md); ignoring them understates fixed-charge risk if utilization or renewals disappoint (research §2.7).

## Mechanism and magnitude

- **Mechanism:** OCI and applications growth (`inputs.md`) → product revenue (`segments.md`) → reported segment margins → operating income after R&D, G&A, amortization, restructuring, and SBC (`income.md`). Valuation is **operating EV = [VIEW] multiple × FY2028E operating income**; equity subtracts modeled **FY2027E** net debt; per-share result only in [`valuation.md`](../../models/orcl/valuation.md).
- **Magnitude:** FY2028E operating income **$31,521m**; FY2029E **$38,471m**; total revenue **$99,542m** / **$115,462m** (`income.md`). OCI **$45,931m** / **$59,711m** (`segments.md`). Core FCF **$(21,563)m** / **$(9,128)m** / **$(1,019)m** FY2027–FY2029 (`cashflow.md`). Official PT, bear/bull multiples, tape-implied EV/EBIT, and core-FCF DCF check: **`valuation.md` only**.

## Killing conditions

Statuses reflect evidence through 2026-09-29. Recheck on official prints and filing tables, not slide adjectives alone.

| kill | status | what would do it / what remains | when to check |
|---|---|---|---|
| OCI revenue path breaks | **LIVE WATCH** | Reported cloud infrastructure / IaaS revenue run-rate materially below [`segments.md`](../../models/orcl/segments.md) FY2027E **$31,677m** or FY2028E **$45,931m** after FX adjustment | Q2–Q4 FY2027 earnings releases and 10-Q MD&A (R3) |
| Capacity does not convert to recognized revenue | **LIVE WATCH** | RPO or bookings grow but incremental MW/GPU delivery, utilization, or recognized OCI revenue fails to follow (research §8.1) | Q2–Q4 FY2027 capacity KPIs (R3.6); annual 10-K |
| Cloud-and-software margin collapses below model | Open | Reported cloud-and-software segment margin sustained below **[VIEW] 54.5%** (FY2027E) or **53.5%** (FY2028E) without a modeled offset in other segments | Each quarterly segment table (R2); Q1 FY2027 was **54.5%** [FACT] |
| Operating income bridge breaks | Open | Consolidated operating income materially below [`income.md`](../../models/orcl/income.md) while segments look intact—e.g. corporate exclusions or restructuring step up beyond `[VIEW]` | Quarterly 10-Q; FY2027 10-K |
| Funding / core FCF stress | Open | Core FCF (prepay excluded) worse than **`cashflow.md`** plus net debt rising faster than modeled **FY2027E** bridge without disclosed contract economics to justify it | Quarterly cash flow; debt footnotes (R5); covenant language in 10-Q/10-K |
| RPO quality disappoints (cannot be modeled yet) | Open | Disclosed cancellations, concentration, or margin on AI contracts that contradict “maintaining and improving” contract-margin language without numeric proof [FACT] R3.6 | Risk factors and contract notes; any customer-10% revenue breach (R3.7) |
| Dilution beyond R5.5 share count | Open | Mandatory convertible preferred conversion or large issuance above **3,023,736,000** shares (R5.5–R5.7) not in [`inputs.md`](../../models/orcl/inputs.md) | 10-Q share count; Note 10 |
| Product-level margin disclosure refutes infra story | Open | Oracle begins reporting OCI or GPU margins that show uneconomic unit economics (R8.3)—would force model and valuation rework | Future 10-K/MD&A if disclosed |

A last-close move alone does not kill the thesis. Headline RPO growth alone does not validate it. Do not retune the official PT in this file.

## What this file is not

This file assigns no recommendation and no long/short/pass label. Tape versus official target is discussed in [`valuation.md`](../../models/orcl/valuation.md), not here.
