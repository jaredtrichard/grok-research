# Meta Platforms model

The combined-segment three-statement model and valuation belong in [`models/meta/`](../../models/meta/).

No workbook numbers are stored here. Use [`research.md`](research.md) for the driver map and [`register.md`](register.md) for sourced inputs.

Workbook: [`inputs`](../../models/meta/inputs.md) · [`segments`](../../models/meta/segments.md) · [`income`](../../models/meta/income.md) · [`balance`](../../models/meta/balance.md) · [`cash flow`](../../models/meta/cashflow.md) · [`valuation`](../../models/meta/valuation.md) · [`compute`](../../models/meta/compute.py).

## Reconciliation notes

- **[FACT]** Historical company operating income equals FoA operating income plus RL operating loss; there is no corporate operating-income plug.
- **[DEDUCTED]** Functional company expenses reconcile to the same operating income but cannot be allocated by function to the two segments from public disclosure.
- **[VIEW]** Forecast segment operating contribution is the controlling income-statement architecture. Forecast functional expenses are constrained to the identical company operating income.
- **[VIEW]** Balance-sheet residual lines aggregate items not forecast separately. Cash, marketable securities, debt, PP&E, equity, and ending cash are explicit and checked by `compute.py`.
