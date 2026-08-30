# Tesla valuation

At the $348.75 last close, the modeled-business official 12-month value in the bridge leaves most of the market price as unmodeled optionality rather than earnings included in this model.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | 2026-08-29 |
| Last close | $348.75 on 2026-08-28 |
| Last-price source | [Yahoo Finance historical](https://finance.yahoo.com/quote/TSLA/history/) |
| PT denominator | 3,949,547,394 shares outstanding on 2026-07-16 (R5.3) |
| Method | 20.0× FY2027E operating income + YE2026E net cash + SpaceX filing FV |

Robotaxi, incremental FSD and Optimus commercial revenue remain zero. No NPV for those businesses enters the official method.

## Official EV bridge

| item | basis | $m except per share |
|---|---|---|
| FY2027E operating income | income.md | 1,879.5 |
| Selected EV / EBIT | [VIEW] | 20.0x |
| Operating enterprise value | EBIT × multiple | 37,589.1 |
| YE2026E cash + short-term investments − debt | balance.md | 21,462.2 |
| Tesla-held SpaceX stake | R6.2; held at filing FV | 3,007.0 |
| Equity value | EV + net cash + stake | 62,058.3 |
| Shares outstanding (m) | R5.3; not diluted WAS | 3,949.547 |
| Official 12-month PT / share | Equity value ÷ shares | $15.71 |

The 20.0× FY2027E EBIT multiple is a `[VIEW]`: a premium to mature global auto framing, but not a software multiple. The modeled earned profit comes from Automotive, Energy and Services, while AI opex and capex compress FY2026–FY2027 EBIT and free cash flow.

## Checks — not additional official targets

| check | method | value / share |
|---|---|---|
| 3-year / FY2028 exit | 22.0× FY2028E EBIT + YE2028E net cash + stake | $23.97 |
| Bear | 10.0× FY2027E EBIT + YE2026E net cash + stake | $10.95 |
| Bull — modeled businesses only | 30.0× FY2028E EBIT + YE2028E net cash + stake | $31.24 |
| DCF | 10.0% WACC; 2.5% terminal growth | $7.99 |

The 3-year, bear and bull checks contain only the modeled businesses, net cash and Tesla-held SpaceX stake. They contain no autonomous-driving, FSD or Optimus NPV.

## DCF check

| period | FCF | after-tax interest expense | after-tax interest income | UFCF / terminal value | discount years | present value |
|---|---|---|---|---|---|---|
| FY2026E | (12,367.8) | 262.8 | (1,102.1) | (13,207.0) | 0.173 | (12,991.6) |
| FY2027E | (7,718.5) | 272.9 | (675.0) | (8,120.6) | 0.836 | (7,498.9) |
| FY2028E | (1,077.5) | 272.9 | (505.8) | (1,310.4) | 1.838 | (1,099.8) |
| Terminal | — | — | — | 35,838.7 | 2.342 | 28,667.6 |
| DCF enterprise value | — | — | — | — | — | 7,077.4 |
| DCF equity value | add YE2026E net cash + stake | — | — | — | — | 31,546.6 |

UFCF equals `FCF + after-tax interest expense − after-tax interest income`. FY2026 uses the midpoint of the remaining period after 2026-08-29; FY2027 and FY2028 use fiscal mid-year dates. Terminal value equals `FY2028E NOPAT × (1 + g) ÷ (WACC − g)`, where NOPAT uses the model’s FY2025 effective tax rate. Terminal value is 54.0% of the positive terminal/net-cash/stake components because every explicit-year UFCF is negative; the DCF is therefore terminal-dominated and does not replace the official method.

## Current market-implied checks

| item | formula | $m or multiple |
|---|---|---|
| Market capitalization | Last price × filing shares | 1,377,404.7 |
| 2026-06-30 net cash | Cash + STI − debt | 34,182.0 |
| SpaceX stake | R6.2 | 3,007.0 |
| Current operating EV | Market cap − net cash − stake | 1,340,215.7 |
| EV / FY2026E revenue | Current operating EV ÷ revenue | 13.0x |
| EV / FY2028E revenue | Current operating EV ÷ revenue | 10.7x |
| EV / FY2026E EBIT | Current operating EV ÷ operating income | 2370.6x |
| EV / FY2028E EBIT | Current operating EV ÷ operating income | 373.3x |
| EV / FY2026E common NI | Current operating EV ÷ common NI | 1060.0x |
| EV / FY2028E common NI | Current operating EV ÷ common NI | 469.4x |

**[DEDUCTED] Unmodeled residual per share:** `$348.75 − modeled official value = $333.04`. This is an arithmetic residual, not a Robotaxi valuation and not evidence that any specific optional business earns that amount.

## Comparable-company snapshot

| company | EV / Sales | EV / EBIT | as-of | market source |
|---|---|---|---|---|
| GM | 0.5x | 51.1x | 2026-08-07 | [ValueSense](https://valuesense.io/ticker/gm/intrinsic-value) |
| F | 1.0x | (26.7x) | 2026-08-25 | [ValueSense](https://valuesense.io/ticker/f/intrinsic-value) |
| TM | 1.34x | 18.95x | retrieved 2026-08-29 | [StockAnalysis](https://stockanalysis.com/stocks/tm/statistics/) |
| BYD (1211.HK) | 1.04x | 18.93x | retrieved 2026-08-29 | [StockAnalysis](https://stockanalysis.com/quote/hkg/1211/statistics/) |
| RIVN | 3.5x | (5.8x) | 2026-08-13 | [ValueSense](https://valuesense.io/ticker/rivn/intrinsic-value) |
| FLNC — storage | 0.80x | not obtained | 2026-08-28 | [StockAnalysis](https://stockanalysis.com/stocks/flnc/statistics/) |
| ENPH — solar/storage | 3.50x | 40.07x | 2026-08-28 | [StockAnalysis](https://stockanalysis.com/stocks/enph/statistics/) |

Negative peer EV/EBIT observations reflect negative trailing EBIT and are not economically meaningful positive valuation anchors. Fluence’s market page reports EV/EBIT as unavailable. The peer set is a framing check only; differing finance-company debt, leases, accounting, geography and business mix limit comparability.

## What would move the official value

- A sourced Robotaxi, FSD or Optimus P&L that can be added to the earned-profit model.
- A change in the FY2027E EBIT path generated by the segment and opex assumptions.
- A change in YE2026E cash, short-term investments or debt.
- A change in the selected 20.0× EBIT multiple.
