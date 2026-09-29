# Amazon working thesis

GF-AMZN-1 · as of 2026-09-29 · name id `amzn`

Numbers live in the workbook. This file owns the claim, the mechanism, and the killing conditions. Official 12-month price target: [`models/amzn/valuation.md`](../../models/amzn/valuation.md). Do not treat a restated figure here as a second target.

If the model does not say it, it is not this thesis. Segment forecast cells are `[VIEW]` paths in [`inputs.md`](../../models/amzn/inputs.md); filing segment history is `[FACT]` in [`register.md`](register.md) (R2). Advertising, Prime and product-line margins are not modeled separately (R8.2–R8.4).

## Claim

The official price target is the operating sum-of-the-parts on **FY2027E reportable segment operating income**—AWS, North America and International only—with `[VIEW]` enterprise value multiples of **17.0×**, **12.0×** and **10.0×**, plus **FY2026E net cash** (cash and marketable securities minus debt and lease liabilities). Strategic-investment fair values and non-operating marks are **excluded** from that bridge. The script sums to operating enterprise value **$1,855,405m**, net cash **$(148,440)m**, operating equity **$1,706,965m**, and **$158.25** per share on **10,786,313,572** shares (R6.4)—all in [`valuation.md`](../../models/amzn/valuation.md). Consolidated operating income in the forecast is the sum of segment operating income (R1.5); FY2027E segment operating income is **$72,987m** AWS, **$44,381m** North America and **$8,205m** International ([`segments.md`](../../models/amzn/segments.md)).

That operating anchor is not built to match the tape. Last close **$246.67** on **2026-09-29** is a comparison in `valuation.md` only; the mechanical gap to the official operating SOTP is **+$88.42** per share (**$953,695m** of equity, **35.8%** of last-price market cap in the hole-anatomy table). Tracking what is already priced in reported AWS growth, Stores profitability and the **~$200bn** R6.5 capex outlook can still be a valid investment question—the thesis separates **what the workbook values on disclosed operating income** from **what the single stock price bundles together**.

## Price target

Source of truth for the official 12-month point target, sensitivity checks, tape-implied multiples and the operating-versus-market gap: **[`models/amzn/valuation.md`](../../models/amzn/valuation.md)** (valuation as-of **2026-09-29**).

For orientation only (not a second PT): official operating SOTP **$158.25** per share versus last close **$246.67** on **2026-09-29** ([Yahoo Finance historical](https://finance.yahoo.com/quote/AMZN/history/) as cited in `valuation.md`). Bear, bull, three-year exit and consolidated FCF DCF figures in `valuation.md` are **checks**, not additional official targets.

## Why this view is right

1. **Segment perimeter matches disclosure.** Amazon values performance at segment operating income, not gross profit or sales-group margins (R1.5). The model forecasts revenue growth and segment operating margins only—North America **13% / 11% / 10%** revenue growth and **8.0% → 8.5%** margins; International **15% / 13% / 11%** and **3.6% → 4.2%**; AWS **26% / 20% / 16%** and **37.0% → 38.0%** ([`inputs.md`](../../models/amzn/inputs.md))—so FY2027E consolidated operating income **$125,573m** is the sum of three segment lines, not a plug ([`segments.md`](../../models/amzn/segments.md)).
2. **AWS versus Stores in the SOTP.** At FY2027E segment operating income, AWS **$72,987m** at **17.0×** drives **$1,240,780m** of operating EV (**46.6%** of last-price market cap in the hole table); North America **$44,381m** at **12.0×** is **$532,576m** (**20.0%**); International **$8,205m** at **10.0×** is **$82,049m** (**3.1%**). Stores economics—including embedded advertising and subscriptions—sit inside NA/Intl segment operating income, not a standalone ad multiple (R1.2, R8.4).
3. **FCF and capex bridge discipline.** FY2026E free cash flow is **$(40,562)m** in [`cashflow.md`](../../models/amzn/cashflow.md): operating cash flow **$180,738m** minus **`[VIEW]` net cash capex $(200,000)m** mapped from R6.5’s ~**$200bn** outlook minus **`[VIEW]` $(21,300)m** remaining OpenAI preferred cash (R7.2). FY2027E and FY2028E FCF recover to **$58,995m** and **$106,974m** as modeled net capex steps down to **$(175,000)m** and **$(155,000)m**. Net cash for the official PT uses the **FY2026E** balance-sheet roll-forward **$(148,440)m**, not Q2 alone.
4. **Non-operating marks stay out of the official PT.** 1H 2026 other income **$69,062m** from observable-price adjustments (R7.1) flows through forecast net income but AWS segment operating income excludes those marks; the official method refuses to capitalize unstaked fair value (**not obtained** at balance-sheet FV in `valuation.md`).
5. **Checks bound the operating story without redefining the PT.** On the same FY2027E segment operating income paths: bear **$132.45** (**0.85×** multiples), bull **$186.84** (**1.15×** multiples plus **50%** of R7.2 named cash deployed), FY2028E exit **$199.32**, consolidated FCF DCF **$148.99**—all labeled non-official in `valuation.md`.

## What others miss or get wrong

Debates below come from [`consensus.md`](consensus.md); post-Q2 sell-side consensus and market-implied segment splits remain **not obtained** (R8.8), so “priced in” stays qualitative unless tied to workbook lines.

1. **[VIEW] AWS AI acceleration versus investment burden.** Bulls treat large commitments (R3.4) and usage growth as proof of durable AI-led AWS expansion; bears stress revenue recognition lag versus earlier power, chip and depreciation costs. **What may be missed:** RPO is not run-rate revenue, but current revenue also undercounts contracted demand—the model uses a **`[VIEW]` usage and margin path**, not a backlog multiple (`consensus.md` §3).
2. **[VIEW] Stores margin durability versus reinvestment.** Bulls cite regionalized inventory and mix toward seller services, ads and subscriptions; bears note delivery-speed and price investment can recycle productivity into customer benefits rather than reported segment margin. **What may be missed:** third-party **61%** of paid units (R3.2) does not reveal take rate or contribution; reported retail revenue understates marketplace GMV (R1.4).
3. **[VIEW] Advertising as a high-margin mix engine.** Bulls extrapolate from **26%** Q2 advertising growth (R3.1); bears cite ad load, measurement and content/infrastructure limits. **What may be missed:** assigning a pure-play ad margin to all Advertising revenue is unsupported (R8.4)—the official PT keeps ads inside NA/Intl segment operating income.
4. **[VIEW] Strategic AI investments and GAAP earnings quality.** Bulls tie Anthropic/OpenAI stakes to AWS demand and upside; bears separate non-cash marks from operating cash and worry about concentration and further funding (**$60,000m** named cash deployed per R7.2 in `valuation.md`). **What may be missed:** equity stakes and operating cloud relationships need separate treatment—neither reported net income nor AWS revenue alone captures both (`consensus.md` §3).
5. **[VIEW] Near-term bar already visible.** Q3 2026 guidance **[FACT]**: net sales **$197.0bn–$202.0bn**, operating income **$22.5bn–$26.5bn** (S4). A revenue beat without evidence on capacity monetization and cash returns does not settle the capex-versus-return debate (`consensus.md` §2). **Appears embedded qualitatively:** continued AWS and Advertising growth, profitable North America, positive International operating income and **~$200bn** 2026 infrastructure spending—already in filings and R6.5, not “hidden” in the model base case.

## Mechanism and magnitude

**Mechanism (official PT):**

| step | workbook line | $m |
|---|---|---:|
| AWS FY2027E operating income × **17.0×** | [`segments.md`](../../models/amzn/segments.md); [`valuation.md`](../../models/amzn/valuation.md) | 1,240,780 |
| North America FY2027E operating income × **12.0×** | same | 532,576 |
| International FY2027E operating income × **10.0×** | same | 82,049 |
| Operating enterprise value (sum) | same | 1,855,405 |
| Plus FY2026E net cash | [`balance.md`](../../models/amzn/balance.md) via `valuation.md` | (148,440) |
| Operating equity ÷ R6.4 shares | `valuation.md` | **$158.25** / share |

**Why $246.67 sits above $158.25:**

- Last-price market capitalization **$2,660,660m** minus official operating equity **$1,706,965m** leaves **[DEDUCTED] implied gap to tape** **$953,695m** (**35.8%** of market cap)—the “residual” row in hole anatomy (`valuation.md`). That residual is **not** allocated to AWS, Stores or stakes because R8.8 segment splits are **not obtained**; `valuation.md` states the tape embeds AWS AI optimism, Stores margin debate and strategic-investment marks in one price.
- Proxy last-price operating EV (**$2,779,667m** using Q2 net cash in the tape table) implies **26.4×** FY2026E consolidated operating income **$105,252m** and **19.1×** FY2028E **$145,598m**—above the **`[VIEW]`** segment multiples applied to FY2027E segment operating income in the official bridge.
- Strategic stakes: **$69,062m** 1H other income and **$60,000m** named strategic cash sit **outside** the official PT; balance-sheet fair value remains **not obtained**, so the thesis does not assert how much of the **$88.42** residual is marks versus higher implicit multiples on operating income.

**Magnitude summary:** Operating SOTP is dominated by AWS EV (**~67%** of operating EV before net cash). FY2026 is the bridge year where **`[VIEW]`** **$(200,000)m** net capex and strategic cash drive negative FCF before modeled recovery. The official PT was **not** solved to **$246.67**; changing multiples to chase the tape would violate gate 3 rules documented in `inputs.md`.

## Killing conditions

Statuses reflect evidence through **2026-09-29**. Recheck on official prints and register updates, not narrative alone. A last-close move alone does not kill the thesis; retuning the official PT to match the tape would.

| kill | status | what would do it / what remains | when to check |
|---|---|---|---|
| Q3 2026 operating income outside guide with no model update | **LIVE WATCH** | Consolidated operating income materially below **$22.5bn** or above **$26.5bn** without revising segment **`[VIEW]`** paths in `segments.md` / `inputs.md` | Q3 2026 earnings release (S4); [`register.md`](register.md) R2 |
| R6.5 capex outlook diverges from **`[VIEW]` $(200,000)m** FY2026E net capex | **LIVE WATCH** | Company revises **~$200bn** outlook or defines capex in a way that breaks the net-cash-capex mapping; TTM net cash capex was **$169,007m** through 2026-06-30 (R6) | FY2025/Q4 updates (R6.5); 10-Q cash-flow statement; [`cashflow.md`](../../models/amzn/cashflow.md) |
| AWS FY2027E operating income path breaks | **LIVE WATCH** | Reported AWS operating income growth or margin (R2, R2.3) inconsistent with **`[VIEW]`** **$60,012m → $72,987m** FY2026E–FY2027E and **37.0% → 37.5%** margin without workbook revision | Quarterly segment note (S3 Note 8); `segments.md` |
| Stores segment margin reinvestment | **LIVE WATCH** | North America or International segment operating margin falls materially below forecast **8.0% / 3.6%** FY2026E or fails to reach **`[VIEW]`** FY2027E **8.3% / 3.9%** while revenue meets plan | Same segment filings; shipping/fulfillment/tech cost commentary (R2.3) |
| FY2026E FCF bridge fails | **LIVE WATCH** | Full-year OCF, net capex or strategic investment cash (R7.2) implies FCF far from modeled **$(40,562)m** | FY2026 10-K / 10-Q cash flow; R6 table |
| Strategic marks dominate without operating follow-through | **LIVE WATCH** | Large new non-operating marks (R7.1) without AWS usage/margin evidence; or additional unstaked cash commitments | 10-Q other income and investing lines; R7.1–R7.2 |
| Product-line margin disclosure arrives | **Open** | Obtained sales-group operating income (R8.2) would force explicit ad/Prime/seller margins instead of segment-only SOTP | Future 10-K/10-Q |
| Post-Q2 consensus or R8.8 segment-implied values | **Open — not obtained** | Sourced FY2026–FY2030 segment consensus or defensible market-implied AWS/Stores split would change the priced-expectations frame, not automatically the **`[VIEW]`** multiples | When R8.8 is sourced; [`consensus.md`](consensus.md) §1 |

## What this file is not

This file assigns no recommendation and no LONG/SHORT/PASS label. The cover pull request is a later gate. Publication of `names.thesis_ref` is outside this workbook.
