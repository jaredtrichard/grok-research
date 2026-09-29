# Alphabet valuation

At the $340.92 Class A last close, the official operating DCF values recurring cash generation and a FY2028 operating-income exit multiple, then adds filing-balance net liquidity and non-marketable investments at modeled carrying value. The R4.1 equity-security remeasurement is excluded from unlevered free cash flow and from the operating-income path used for terminal value.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | 2026-09-29 |
| Last close (Class A) | $340.92 on 2026-09-29 |
| Class C reference close | $337.32 on 2026-09-29 |
| Last-price source | [Yahoo Finance historical](https://finance.yahoo.com/quote/GOOGL/history/) |
| PT denominator | 12,230.000 million shares outstanding (R5.3, 2026-07-15) |
| Model diluted WAS FY2028E | 12,750.0 million (reference only) |
| Method | Unlevered FCF DCF (FY2026E–FY2028E) + FY2028E EBIT exit multiple |

## Key `[VIEW]` assumptions

| assumption | value | brief justification |
|---|---|---|
| WACC | 9.5% | Mega-cap platform with net liquidity; beta near market; no operating leverage from the Q2 equity mark. |
| Terminal value | 20.0× FY2028E operating income | Premium to current tape-implied operating EV / FY2028E OI (~17.7×) but below peak AI rerating; anchors on recurring segment earnings. |
| Gordon cross-check | 2.5% perpetual growth on FY2028E UFCF | Sanity check only; capex-heavy years make Gordon unreliable as the primary terminal. |
| Investment marks | Zero remeasurement FY2027E–FY2028E | Matches income.md; R4.1 treated as non-operating. |
| Non-marketable securities | Modeled flat at R2 filing carrying value | Separates operating DCF from equity stakes; not marked up again in the DCF. |

## What the tape must be paying for

| item | formula | $m or multiple |
|---|---|---|
| Last-price market capitalization | Last close × R5.3 shares | 4,169,451.6 |
| 2026-06-30 net cash | Cash + marketable − debt (R2) | 142,310.0 |
| Non-marketable securities (carrying) | R2 balance sheet | 131,461.0 |
| Last-price operating EV | Market cap − net cash − non-marketable | 3,895,680.6 |
| Operating EV / FY2026E revenue | Tape operating EV ÷ model revenue | 8.0× |
| Operating EV / FY2028E revenue | Tape operating EV ÷ model revenue | 5.9× |
| Operating EV / FY2028E operating income | Tape operating EV ÷ model OI | 17.7× |
| Operating EV / FY2028E recurring net income | Tape operating EV ÷ recurring NI | 21.3× |

The tape’s operating EV embeds faster capex normalization and/or a higher terminal multiple than the base DCF: FY2026–FY2027 model unlevered FCF is deeply negative while Search and Cloud operating income still compound. The Q2 equity mark inflates reported net income but is stripped from operating cash flow in `cashflow.md` and from this DCF.

## Unlevered FCF bridge

Unlevered FCF = operating income × (1 − forecast cash tax rate) + D&A − capex − Δ operating NWC. Tax is applied to operating income only, not to R4.1 remeasurement.

| period | operating income | cash tax rate | [VIEW] UFCF | mid-year t | PV @ WACC |
|---|---|---|---|---|---|
| FY2026E | 161,277.4 | 19.1% | (39,863.0) | 0.5 | (38,094.6) |
| FY2027E | 188,260.1 | 17.0% | (26,110.3) | 1.5 | (22,787.2) |
| FY2028E | 219,613.7 | 17.0% | 26,750.3 | 2.5 | 21,320.3 |

## Operating DCF and equity bridge

| item | basis | $m except per share |
|---|---|---|
| PV explicit FY2026E–FY2028E UFCF | Mid-year discount at 9.5% | (39,561.5) |
| FY2028E operating income | income.md recurring path | 219,613.7 |
| Terminal EV / EBIT | [VIEW] | 20.0× |
| Terminal value | FY2028E OI × multiple | 4,392,273.3 |
| PV terminal (t = 2.5y) | Discounted at WACC | 3,500,693.3 |
| **Operating enterprise value** | PV explicit + PV terminal | **3,461,131.8** |
| Plus FY2028E net cash | cash + marketable − debt | 122,928.0 |
| Plus FY2028E non-marketable securities | Balance sheet carrying value | 131,461.0 |
| **Official equity value** | Operating EV + net cash + investments | **3,715,520.8** |
| Shares outstanding (m) | R5.3 | 12,230.000 |
| **Official 12-month PT / share** | Equity value ÷ R5.3 shares | **$303.80** |

Preferred stock (R5.4) is reflected in the balance sheet and dividends but mandatory-convertible conversion terms into common are **not obtained**; the PT denominator uses filed common shares outstanding, not fully converted preferred. Model diluted WAS (12,750.0m FY2028E) is shown for comparison.

## Gordon terminal cross-check (non-official)

| item | value |
|---|---|
| FY2028E UFCF | 26,750.3 |
| [VIEW] perpetual growth | 2.5% |
| Implied Gordon equity value | 527,018.1 |
| Implied Gordon PT / share | $43.09 |

Low near-term UFCF makes Gordon understate a capex cycle; the official terminal remains the EBIT exit multiple.

## Checks — not additional official targets

| check | method | value / share |
|---|---|---|
| Bear | WACC 10.5% + 16× FY2028E OI | $241.41 |
| Bull | WACC 8.5% + 23× FY2028E OI | $354.38 |
| Gordon cross-check | 2.5% on FY2028E UFCF | $43.09 |

**[DEDUCTED] Tape residual per share:** `$340.92 − official DCF = $37.12`. Positive residual means the last price exceeds the base operating DCF on these `[VIEW]`s; it is not an instruction to raise or lower the model.

## Killing sensitivities

### WACC vs FY2028E EBIT exit multiple

| WACC \\ multiple | 16× | 18× | 20× | 22× | 24× |
|---|---|---|---|---|---|
| 8.5% | $251.87 | $281.16 | $310.45 | $339.73 | $369.02 |
| 9.0% | $249.19 | $278.14 | $307.10 | $336.05 | $365.00 |
| 9.5% | $246.56 | $275.18 | $303.80 | $332.43 | $361.05 |
| 10.0% | $243.96 | $272.26 | $300.56 | $328.86 | $357.16 |
| 10.5% | $241.41 | $269.39 | $297.37 | $325.35 | $353.33 |

### Search growth (all forecast years)

| case | official PT / share |
|---|---|
| Base search growth | $303.80 |
| Search growth −200 bps | $293.55 |
| Search growth +200 bps | $314.41 |

### Cloud segment margin (all forecast years)

| case | official PT / share |
|---|---|
| Base cloud margin | $303.80 |
| Cloud margin −300 bps | $295.20 |
| Cloud margin +300 bps | $312.41 |

### Capex (all forecast years)

| case | official PT / share |
|---|---|
| Base capex | $303.80 |
| Capex +10% all years | $294.02 |
| Capex −10% all years | $313.58 |

## Comparable-company snapshot (check only)

Trailing EV/Sales from third-party screens; prices on 2026-09-29 from Yahoo except where noted. GOOGL model-implied FY2028E operating EV / revenue = 5.2×; operating EV / FY2028E OI = 15.8×.

| company | last close | EV / Sales | EV / FY2028E model OI | as-of | source |
|---|---|---|---|---|---|
| GOOGL | $340.92 | 8.93x | 17.7x | 2026-09-29 | https://finance.yahoo.com/quote/GOOGL/history/ |
| GOOG | $337.32 | not obtained | not obtained | 2026-09-29 | https://finance.yahoo.com/quote/GOOG/history/ |
| META | $738.79 | 6.59x | not obtained | 2026-09-29 | https://www.financecharts.com/compare/META,GOOGL,MSFT,AAPL/value/ev-to-sales |
| MSFT | $508.96 | 11.55x | not obtained | 2026-08-07 | https://tgmcharts.com/stocks/MSFT/ev-sales |
| AMZN | $246.67 | 4.05x | not obtained | 2026-08-07 | https://tgmcharts.com/stocks/MSFT/ev-sales |
| AAPL | $329.40 | 10.00x | not obtained | 2026-08-07 | https://tgmcharts.com/stocks/MSFT/ev-sales |

Peer multiples mix trailing revenue with different fiscal calendars and include non-ad businesses; use as a framing check only.

## What would move the official value

- A sourced change to FY2026–FY2028 Search, YouTube, Cloud or capex `[VIEW]` paths in `inputs.md`.
- A change to WACC or the FY2028E EBIT exit multiple.
- A change to net cash or non-marketable carrying values on the forecast balance sheet.
- Preferred conversion terms (R5.4) that shift the share denominator materially.

## Blockers

- Mandatory-convertible preferred conversion ratio and fully diluted share count at conversion are **not obtained** in the register (R5.4); PT uses R5.3 outstanding shares with disclosure only.
- Peer EV/EBIT is **not obtained** on a consistent basis across the comp set; EV/Sales is shown where sourced.
