# Alphabet model

The Gate 2 segment three-statement model lives in [`models/googl/`](../../models/googl/).

Workbook: [`inputs`](../../models/googl/inputs.md) · [`segments`](../../models/googl/segments.md) · [`income`](../../models/googl/income.md) · [`balance`](../../models/googl/balance.md) · [`cash flow`](../../models/googl/cashflow.md) · [`compute`](../../models/googl/compute.py).

Use [`research.md`](research.md) for the driver map and [`register.md`](register.md) for sourced historical inputs. Forecast assumptions are labeled `[VIEW]`; script-derived reconciliations are `[DEDUCTED]`.

Reconciliation:

- Product revenue sums to Google Services, reported segments and consolidated revenue.
- Reported-segment operating income sums to consolidated operating income.
- Consolidated cost of revenue reconciles segment operating income to explicit functional-opex assumptions because segment/product COGS is `not obtained`.
- PP&E, retained earnings, APIC and liquidity roll through the cash flow; every forecast balance sheet and cash bridge ties in `compute.py`.
- Equity-investment remeasurement is separated from recurring earnings and removed from operating cash flow.

Gate 2 contains no valuation, price target, thesis or rating.
