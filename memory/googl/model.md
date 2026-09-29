# Alphabet model

The Gate 2 segment three-statement model and Gate 3 valuation live in [`models/googl/`](../../models/googl/).

Workbook: [`inputs`](../../models/googl/inputs.md) · [`segments`](../../models/googl/segments.md) · [`income`](../../models/googl/income.md) · [`balance`](../../models/googl/balance.md) · [`cash flow`](../../models/googl/cashflow.md) · [`valuation`](../../models/googl/valuation.md) · [`compute`](../../models/googl/compute.py).

Use [`research.md`](research.md) for the driver map and [`register.md`](register.md) for sourced historical inputs. Forecast assumptions are labeled `[VIEW]`; script-derived reconciliations are `[DEDUCTED]`.

Reconciliation:

- Product revenue sums to Google Services, reported segments and consolidated revenue.
- Reported-segment operating income sums to consolidated operating income.
- Consolidated cost of revenue reconciles segment operating income to explicit functional-opex assumptions because segment/product COGS is `not obtained`.
- PP&E, retained earnings, APIC and liquidity roll through the cash flow; every forecast balance sheet and cash bridge ties in `compute.py`.
- Equity-investment remeasurement is separated from recurring earnings and removed from operating cash flow.
- Valuation uses unlevered FCF from the operating path, an EBIT exit terminal, and a separate net-cash plus non-marketable bridge; see [`valuation.md`](../../models/googl/valuation.md).
- Working thesis and killing conditions live in [`thesis.md`](thesis.md); consensus framing in [`consensus.md`](consensus.md).

Gate 4 adds the working thesis and consensus home; no rating.
