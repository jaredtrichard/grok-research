# Alphabet working thesis

GF-GOOGL-1 · as of 2026-09-29 · name id `googl`

Numbers live in the workbook. This file owns the claim, the mechanism, and the killing conditions. Official 12-month price target: [`models/googl/valuation.md`](../../models/googl/valuation.md). Do not treat a restated figure here as a second target.

## Claim

The official PT is the unadjusted output of one operating DCF the model actually builds: unlevered free cash flow for FY2026E–FY2028E (mid-year discount at **[VIEW] 9.5% WACC**), plus a **[VIEW] 20.0× FY2028E operating income** terminal, then add FY2028E net cash and non-marketable securities at modeled balance-sheet carrying value. R4.1 equity-security remeasurement is excluded from UFCF and from the terminal operating-income path. The paths were set as segment and capex `[VIEW]`s in `inputs.md`; the script produced the number in `valuation.md`. Last close **$340.92** (2026-09-29) is a comparison there; the signed tape residual **+$37.12/sh** is whatever those paths produce versus the last sale—not an instruction to retune the model to the tape.

If the model does not say it, it is not this thesis. Forecast cells are `[VIEW]`; filings are `[FACT]` in the register.

## Why this view is right

1. **Consolidated economics are built bottom-up from reported segments, not from GAAP net income.** Google Services, Cloud, Other Bets and Alphabet-level activities sum to consolidated operating income in `segments.md` (FY2026E–FY2028E OI **$161.3bn / $188.3bn / $219.6bn** on revenue **$488.1bn / $577.2bn / $663.2bn**). The income statement is a reconciliation from that segment OI through explicit R&D, sales/marketing and G&A `[VIEW]`s—not a top-down EPS story.
2. **Search and Services still carry the revenue stack, with decelerating but double-digit Search growth.** `[VIEW]` Search growth steps down **16.0% → 13.0% → 11.0%** while Services OI margin holds **~41% → 40%** (`inputs.md`, R2.1–R2.2, R6.4). Network is modeled to shrink; subscriptions/platforms/devices grow but product split remains `not obtained` (R9.4).
3. **Cloud is the swing segment on both revenue and margin.** Cloud revenue is `[VIEW]` **$96.0bn / $139.2bn / $181.0bn** with segment OI margin **34.0% / 32.0% / 34.0%**, anchored to R6 backlog facts ($513.9bn Cloud backlog at 2026-06-30, R6.2) without inventing a GCP/Workspace/TPU split (R9.2). Cloud OI rises from **$32.6bn to $61.5bn** across the forecast in `segments.md`.
4. **The capex cycle dominates near-term cash, not the Q2 equity mark.** FY2026 capex is `[VIEW]` **$200bn** (midpoint of R5.8 **$195–205bn** guide), **$220bn** in FY2027E, **$210bn** in FY2028E. That drives model FCF **−$15.7bn / +$11.2bn / +$67.7bn** and unlevered FCF **−$39.9bn / −$26.1bn / +$26.8bn** in `valuation.md` even while operating income compounds. Operating cash flow in `cashflow.md` strips the **$135.9bn** 1H investment remeasurement (R4.1) from cash generation.
5. **Terminal value is on recurring operating income, not on marked equity stakes.** Non-marketable securities stay at **$131.5bn** carrying value through the forecast balance sheet; they are added once in the equity bridge, not capitalized into the DCF stream. Gordon on FY2028E UFCF is a cross-check only (~**$43/sh** in `valuation.md`) because low near-term UFCF makes perpetual growth misleading.
6. **20.0× FY2028E OI is a `[VIEW]` premium to tape-implied operating EV / FY2028E OI (~**17.7×** in `valuation.md`) but is not solved to match **$340.92**. The base PT sits below the last sale on these `[VIEW]`s; the tape embeds faster capex normalization and/or a higher terminal multiple than the base case.

## What others miss or get wrong

1. **Treating Q2 GAAP EPS ($9.11) or full-year net income with R4.1 as recurring earnings power.** The model’s recurring net income line excludes the equity mark; valuation uses operating income and UFCF, not marked other income.
2. **Pricing Cloud backlog or AI narrative without a capex and FCF path.** R6 backlog is a fact; converting it to margin and cash after **~$200bn+** annual capex is the modeled debate in `cashflow.md`, not a multiple on headline revenue alone.
3. **Ignoring the financing/dilution layer.** Q2 common and mandatory-convertible preferred issuance (R5.4) and zero buybacks in the forecast (R5.2 pause) are in the balance sheet and share `[VIEW]`s; preferred conversion terms into common are **not obtained**, so the PT denominator stays R5.3 outstanding shares with disclosure only.
4. **Street framing versus this workbook.** Pre-Q2 third-party Q2 consensus (~**$2.89** EPS, ~**$117bn** revenue) is summarized in `consensus.md`; post-Q2 refreshed multi-year Street models and a primary price-target compilation are **not obtained**. Secondary screens that mix equity marks into forward EPS or cite aggressive mean targets without a capex cycle are not substitutes for this segment model.
5. **Antitrust as a headline without a modeled TAC/remedy path.** Remedy facts live in R8.2–R8.3; Search growth and Services margin `[VIEW]`s embed deceleration risk but do not claim a quantified remedy settlement.

## Mechanism and magnitude

- **Mechanism:** Product revenue `[VIEW]`s → reported segment OI → consolidated opex reconciliation → operating cash flow (excluding investment marks) → unlevered FCF (NOPAT on operating income + D&A − capex − ΔNWC) → PV at WACC → terminal on FY2028E OI → add FY2028E net cash and non-marketable carrying value → divide by R5.3 shares.
- **Magnitude:** See the official PT, UFCF bridge, operating DCF, tape operating EV, signed residual, bear/bull checks, and killing sensitivities (Search growth, Cloud margin, capex, WACC, terminal multiple) in [`valuation.md`](../../models/googl/valuation.md). Search −200 bps and Cloud margin −300 bps are the largest segment levers in the script sensitivities; capex +10% is material but secondary to terminal OI on this horizon.

## Killing conditions

Statuses reflect evidence through **2026-09-29**. Recheck on official prints (10-Q/10-K, earnings release, register updates), not narrative alone.

| kill | status | what would do it / what remains | when to check |
|---|---|---|---|
| Search growth falls below the `[VIEW]` path | **Open** | Reported Search & other revenue growth materially below **16% / 13% / 11%** FY2026–FY2028 `[VIEW]`s for two consecutive quarters without a disclosed mix/FX explanation | Each quarterly product revenue table (S2/S3); vs `segments.md` |
| Cloud backlog fails to convert at modeled margin | **Open** | Cloud revenue growth or segment OI margin sustained materially below **`inputs.md`** (e.g., margin below **~29%** while revenue still guided to R6-scale growth), or backlog recognized without margin | Quarterly Cloud revenue and segment OI (Note 15); R6 backlog footnotes |
| Capex stays at or above the **$195–205bn** guide without FY2028 FCF recovery | **LIVE WATCH** | FY2026–FY2027 capex at/above R5.8 guide while model UFCF stays deeply negative into FY2028 (path: **−$40bn / −$26bn** then **+$27bn** UFCF) | Quarterly capex and OCF (R5.1, R5.8); vs `cashflow.md` |
| Antitrust remedies or TAC step-change hit Services economics | **Open** | Disclosed TAC rate or distribution/remedy economics move Services OI margin materially off **~41% → 40%** `[VIEW]` path, or a quantified revenue/TAC hit not already in Search growth `[VIEW]`s | 10-Q MD&A TAC (R7); R8.2 judgment implementation updates |
| Preferred / share denominator worse than modeled | **Open** | Mandatory-convertible conversion terms (R5.4) imply dilution beyond model diluted WAS **12.35 / 12.55 / 12.75bn** or PT denominator moves off R5.3 without a register update | 10-Q Note 11; any conversion disclosure |

A last-sale move alone does not kill the thesis. A new AI or Cloud narrative without a number in the model does not kill it. Do not retune the official PT to the tape.

## What this file is not

This file assigns no recommendation. The cover PR is the staged initiation thesis. Publication of `names.thesis_ref` is Firstmate’s job after the captain merges.
