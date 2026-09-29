# AMD model

Three-statement segment workbook: [`models/amd/`](../models/amd/).

| file | role |
| --- | --- |
| [`inputs.md`](../models/amd/inputs.md) | `[FACT]` / `[VIEW]` assumptions and register pointers |
| [`compute.py`](../models/amd/compute.py) | sole arithmetic; run to refresh tables |
| [`segments.md`](../models/amd/segments.md) | Data Center, Client, Gaming, Embedded revenue; Client+Gaming combined OI |
| [`income.md`](../models/amd/income.md) | consolidated IS built from segment operating income sum |
| [`balance.md`](../models/amd/balance.md) | balance sheet |
| [`cashflow.md`](../models/amd/cashflow.md) | cash flow and FCF bridge |
| [`valuation.md`](../models/amd/valuation.md) | DCF + segment SOTP price target (gate 3); regenerate via `compute.py` |

## Reconciliation

- Consolidated **revenue** = Data Center + Client + Gaming + Embedded (Client/Gaming OI is combined only; standalone Client or Gaming OI is not obtained).
- Consolidated **operating income** = segment operating incomes + All Other (same as filed segment bridge in R1.2 / R2).
- Historical amounts trace to [`register.md`](register.md) R2 and R6; forecast amounts are `[VIEW]` in `inputs.md`.
- World Labs (R1.9) is excluded until close and filing.
- Regenerate outputs: `python3 models/amd/compute.py` from repo root.
