# Amazon valuation

At the $246.67 last close, the official 12-month price target values reportable **operating** segments at FY2027E operating income; the last close sits above the official operating SOTP. Strategic-investment marks (R7.1) and stake fair values are shown separately and are **not** in the official PT.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | 2026-09-29 |
| Last close | $246.67 on 2026-09-29 |
| Last-price source | [Yahoo Finance historical](https://finance.yahoo.com/quote/AMZN/history/) |
| PT denominator | 10,786,313,572 shares outstanding on 2026-07-22 (R6.4; 10-Q cover) |
| Method | Operating segment SOTP on FY2027E segment OI + FY2026E net cash; excludes strategic-investment marks |

## FY2026 capex outlook vs model cash capex

| item | basis | $m |
|---|---|---|
| R6.5 company outlook (FY2026) | [FACT] ~200,000; definition not tied to cash-flow line | 200,000 |
| Model FY2026E net cash capex | [VIEW] mapped to outlook; purchases − proceeds/incentives | [VIEW] 200,000 |
| Implied gross purchases (model) | Net ÷ (1 − FY2025 proceeds rate) | 205,453.6 |
| Implied proceeds/incentives (model) | Gross × FY2025 proceeds rate | 5,453.6 |
| TTM net cash capex (register R6) | [FACT] through 2026-06-30 | 169,007 |

The company’s ~$200bn R6.5 outlook is not defined as gross purchases, net cash capex or PPE additions. The model maps it to **net** cash capex (purchases of property and equipment less proceeds and incentives), consistent with register R6 and [`cashflow.md`](cashflow.md). Segment PPE additions in R4.3 are not interchangeable with this cash definition.

## Official operating SOTP bridge

| item | basis | $m except per share |
|---|---|---|
| 1. AWS FY2027E operating income | segments.md; operating only | 72,987.1 |
| AWS selected EV / segment OI | [VIEW] | 17.0x |
| AWS operating enterprise value | AWS OI × multiple | 1,240,780.3 |
| 2. North America FY2027E operating income | segments.md | 44,381.3 |
| NA selected EV / segment OI | [VIEW] | 12.0x |
| North America operating EV | NA OI × multiple | 532,575.5 |
| 3. International FY2027E operating income | segments.md | 8,204.9 |
| Intl selected EV / segment OI | [VIEW] | 10.0x |
| International operating EV | Intl OI × multiple | 82,048.7 |
| Operating enterprise value (1+2+3) | Sum of segment EVs | 1,855,404.5 |
| 4. FY2026E net cash | Cash + marketable securities − debt − lease liabilities | (148,439.8) |
| Strategic stakes (Anthropic/OpenAI marks) | R7.1–R7.2; excluded from official PT | not obtained at fair value |
| Official operating equity value | Operating EV + net cash | 1,706,964.7 |
| Shares outstanding (m) | R6.4 filing count | 10,786.314 |
| Official 12-month PT / share | Operating equity ÷ shares | $158.25 |

Segment operating income is the only segment P&L anchor disclosed (R1.5, R8.2). Advertising, Prime and seller-service economics are embedded in North America and International segments, not valued as standalone sales-group margins. AWS operating income excludes non-operating Anthropic/OpenAI marks in income.md.

## Strategic investments — separate from operating AWS

| item | basis | $m |
|---|---|---|
| 1H 2026 pre-tax other income (Anthropic marks, etc.) | R7.1; non-operating | 69,062 |
| Cash deployed — OpenAI preferred (1H + post-Q2) | R7.2 | 50,000 |
| Cash deployed — Anthropic preferred (Q2) | R7.2 | 10,000 |
| Total strategic cash deployed (named) | Sum of R7.2 items | 60,000 |
| Balance-sheet fair value of stakes | Separate line in other assets | not obtained |
| Official PT treatment | Segment OI multiples exclude marks; net cash excludes stake FV | Operating-only |

Q2 2026 net income and FY2026E net income are not suitable valuation anchors because 1H other income includes large observable-price adjustments (R7.1). The official PT uses segment operating income and cash only.

## What the tape implies

| item | formula | $m |
|---|---|---|
| Last-price market capitalization | Last close × R6.4 shares | 2,660,660.0 |
| 2026-06-30 net cash | Cash + STI − debt − leases | (119,007.0) |
| Last-price operating EV (proxy) | Market cap − Q2 net cash; marks remain inside EV | 2,779,667.0 |
| Official operating equity value | Accepted method | 1,706,964.7 |
| [DEDUCTED] Implied gap to tape | Market cap − official operating equity | 953,695.3 |

The tape embeds AWS AI optimism, Stores margin debate and strategic-investment marks in one price. R8.8 sell-side segment splits are **not obtained**, so this table is a mechanical gap check, not proof of what the market “should” pay for each segment.

## Consolidated FCF DCF — check only

| period | discount years | FCF | PV |
|---|---|---|---|
| FY2027E | 0.751 | 58,995.2 | 55,299.5 |
| FY2028E | 1.753 | 106,973.7 | 91,971.3 |
| Terminal (FY2028 FCF growing) | 1.753 | 110,182.9 | 1,578,840.9 |

PV of terminal uses FY2028E model FCF growing at 3% and 9% WACC, plus 2026-06-30 net cash. This path inherits consolidated FCF (including modeled FY2026E strategic cash outflows in the bridge year) and is **not** the official PT.

## Checks — not additional official targets

| check | method | value / share |
|---|---|---|
| 3-year / FY2028 segment exit | Same [VIEW] multiples on FY2028E segment OI + FY2028E net cash | $199.32 |
| Bear sensitivity | 0.85× segment multiples + FY2026E net cash | $132.45 |
| Bull sensitivity | 1.15× segment EV + net cash + 50%× R7.2 cash deployed | $186.84 |
| Consolidated FCF DCF (non-official) | PV FY2027–FY2028 FCF + terminal; 9% WACC; + Q2 net cash | $148.99 |

## Hole anatomy (operating SOTP vs market cap)

| piece | $m of last-price equity | % of market cap |
|---|---|---|
| 1. AWS operating EV | 1,240,780.3 | 46.6% |
| 2. North America operating EV | 532,575.5 | 20.0% |
| 3. International operating EV | 82,048.7 | 3.1% |
| 4. FY2026E net cash | (148,439.8) | -5.6% |
| [DEDUCTED] Residual vs official PT | 953,695.3 | 35.8% |

**[DEDUCTED] Tape residual per share:** `$246.67 − official PT = $88.42`. Positive means the market prices more than the operating segment SOTP plus modeled net cash; it does not identify which segment or stake the market is emphasizing (R8.8).

## Current market-implied multiples (proxy operating EV)

| item | multiple |
|---|---|
| EV / FY2026E revenue | 3.3x |
| EV / FY2028E revenue | 2.7x |
| EV / FY2026E operating income | 26.4x |
| EV / FY2028E operating income | 19.1x |

Proxy EV subtracts Q2 net cash from market cap and still includes unstaked mark-to-market and other assets inside the equity price.

## What would move the official value

- A sourced change in FY2027E segment operating income paths in [`segments.md`](segments.md).
- A change in any `[VIEW]` segment EV / operating-income multiple or in FY2026E net cash.
- A explicit, sourced fair value for Anthropic/OpenAI stakes that the user chooses to add to (or subtract from) operating equity.
- A revised mapping between R6.5 capex language and modeled net cash capex that alters FCF and net cash roll-forwards.
- Post-Q2 consensus or segment-level market data (R8.8) that would justify retuning multiples — still **not obtained**.
