# Microsoft valuation

The official DCF values the filed three-segment business without a separate unreported “AI” wedge. The operating statement is that Azure/AI and Microsoft 365 monetization sustain double-digit company growth while FY2027 operating margin declines by less than one point and cash capex remains elevated.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | 2026-09-29 |
| Last close | $509.22 on 2026-09-28 |
| Last-price source | [Microsoft IR stock lookup](https://www.microsoft.com/en-us/investor/stock-lookup) |
| Method | Enterprise DCF; three explicit forecast years + terminal value |
| WACC | 8.5% |
| Terminal growth | 4.0% |
| PT denominator | 7,427m FY2026 shares outstanding |

## Unlevered free cash flow

| period | Operating income | NOPAT | D&A | Cash capex | Cash effect of Δ operating capital | FCFF |
|---|---|---|---|---|---|---|
| FY2027E | 178,509.0 | 142,807.2 | 46,760.5 | (140,000.0) | 15,958.8 | 65,526.5 |
| FY2028E | 210,826.3 | 168,661.1 | 59,057.3 | (155,000.0) | 17,569.7 | 90,288.1 |
| FY2029E | 247,655.1 | 198,124.0 | 70,463.4 | (150,000.0) | 16,766.6 | 135,354.1 |

FCFF is `NOPAT + D&A − cash capex − change in operating capital`. SBC is not added back in valuation because it is treated as an economic cost. No OpenAI mark is forecast.

## Official price-target bridge

| item | basis | $m except per share |
|---|---|---|
| PV FY2027E–FY2029E FCFF | Explicit period | 248,011.1 |
| FY2029E terminal value | FY2029E FCFF × (1+g) ÷ (WACC−g) | 3,128,183.0 |
| PV terminal value | Discounted to valuation date | 2,498,843.4 |
| Enterprise value | Explicit PV + terminal PV | 2,746,854.5 |
| FY2026 net cash | Cash + short investments − debt | 36,549.0 |
| Equity value | Enterprise value + net cash | 2,783,403.5 |
| Shares outstanding (m) | FY2026 filing | 7,427.0 |
| Official 12-month price target / share | Equity value ÷ shares | $374.77 |

**Official price-target line:** **$374.77 per share.** This is the DCF output from the operating assumptions in [`inputs.md`](inputs.md); it is not fitted to the last close.

The target requires the following segment and cash milestones:

| period | PBP revenue | IC revenue | MPC revenue | Operating income | Operating margin | Cash capex | Equity FCF |
|---|---|---|---|---|---|---|---|
| FY2027E | 158,195.5 | 179,128.3 | 49,727.8 | 178,509.0 | 46.1% | 140,000.0 | 79,527.4 |
| FY2028E | 180,342.8 | 222,119.1 | 50,225.1 | 210,826.3 | 46.6% | 155,000.0 | 106,264.8 |
| FY2029E | 203,787.4 | 266,542.9 | 51,731.9 | 247,655.1 | 47.4% | 150,000.0 | 153,306.3 |

“Equity FCF” in the milestone table is consolidated OCF less cash capex from [`cashflow.md`](cashflow.md); the DCF uses the unlevered FCFF table above.

## What the last close already requires

| item | formula | value |
|---|---|---|
| Market capitalization | Last close × FY2026 shares | 3,781,976.9 |
| Market enterprise value | Market cap − FY2026 net cash | 3,745,427.9 |
| EV / FY2026A revenue | Market EV ÷ revenue | 11.3x |
| EV / FY2026A operating income | Market EV ÷ operating income | 24.1x |
| Price / FY2026A diluted EPS | Last close ÷ diluted EPS | 28.4x |
| EV / FY2027E revenue | Market EV ÷ modeled revenue | 9.7x |
| EV / FY2027E operating income | Market EV ÷ modeled operating income | 21.0x |
| Market-implied terminal growth | Solve DCF to last close, hold explicit FCFF/WACC | 5.2% |

**[DEDUCTED] Signed target spread:** `$374.77 − $509.22 = $-134.45` per share. The market-implied terminal growth solves only one variable while holding the explicit operating path and 8.5% WACC fixed; it is not a claim that the market literally uses that terminal rate.

## Sensitivity — diagnostics, not additional official targets

| WACC / terminal growth | 3.5% | 4.0% | 4.5% |
|---|---|---|---|
| 8.0% | $377.74 | $421.97 | $478.84 |
| 8.5% | $339.67 | $374.77 | $418.64 |
| 9.0% | $308.53 | $337.02 | $371.84 |

The terminal value is 91.0% of enterprise value. That concentration makes IC growth, steady-state AI/cloud margins, capex normalization, and the discount rate the primary valuation risks.

## What would move the official value

- Segment growth or margin that changes consolidated operating income and FCFF.
- Cash capex, useful-life economics, or working-capital conversion.
- WACC or terminal growth.
- A sourced standalone AI/Copilot P&L that changes—not double counts—the reported segment cash flows.
