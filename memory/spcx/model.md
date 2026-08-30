# SpaceX model pointer

Generator: `models/spcx/compute.py`

Workbook:

- Segments and forecast drivers: `models/spcx/segments.md`
- Consolidated income statement: `models/spcx/income.md`
- Balance sheet and share bridge: `models/spcx/balance.md`
- Cash flow and liquidity runway: `models/spcx/cashflow.md`
- Valuation and scenarios: `models/spcx/valuation.md`

Valuation source: `models/spcx/valuation.md` → `Price target` → `12-month base price target`.

Valuation uses the consolidated Revenue and Operating income / EBIT lines in `income.md`, Free cash flow in `cashflow.md`, and Cash, Marketable securities, Debt and finance leases, and ending basic shares in `balance.md`. Fully diluted shares remain `not obtained`. EchoStar is a scenario memo, not part of the base case.

Reconciliation notes:

- Consolidated revenue and EBIT are summed from the segment model.
- Forecast net income ties between the income statement and cash flow.
- Forecast ending cash ties between cash flow and the balance sheet.
- Each forecast balance sheet balances.
- Free cash flow equals operating cash flow less capex.
- FY2026E equals H1 actual plus H2 forecast.
- Internal Falcon and Starship launches are excluded from Launch Services revenue.

Run `python3 models/spcx/compute.py` to regenerate the workbook and execute the checks.
