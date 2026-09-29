# TSMC model

GF-TSM-1 gate 2 · as of 2026-09-29 · name id `tsm`

## Workbook location

| artifact | path |
|---|---|
| Assumptions and register pointers | [`models/tsm/inputs.md`](../../models/tsm/inputs.md) |
| Segment build (single foundry segment) | [`models/tsm/segments.md`](../../models/tsm/segments.md) |
| Income statement | [`models/tsm/income.md`](../../models/tsm/income.md) |
| Balance sheet | [`models/tsm/balance.md`](../../models/tsm/balance.md) |
| Cash-flow statement | [`models/tsm/cashflow.md`](../../models/tsm/cashflow.md) |
| Valuation | [`models/tsm/valuation.md`](../../models/tsm/valuation.md) |
| Engine | [`models/tsm/compute.py`](../../models/tsm/compute.py) |

Regenerate outputs after assumption changes:

```bash
python3 models/tsm/compute.py
```

## Accounting basis

- **Annual history (FY2023A–FY2025A):** IASB-IFRS per Form 20-F ([register R2](../../memory/tsm/register.md#r2--historical-financial-skeleton), S1).
- **Interim actual (`1H2026A`):** TIFRS quarterly filings summed (R2 latest-quarter table); labeled separately in the model tables.
- **Forecast (FY2026E–FY2028E):** company-level build on IASB-style lines; all growth, margin, mix and capex assumptions are `[VIEW]` unless tied to a register fact.

Do not splice TIFRS quarterly earnings into IASB annual series without an obtained bridge (R2.3A, R10.13).

## Modeling choices

1. **One segment.** Foundry revenue equals company revenue (R1.2). Node and platform tables are mix lenses only—no node P&Ls (R10.4).
2. **VIS gain.** Q2 2026 Vanguard International Semiconductor disposal/mark-to-market is separated from recurring earnings (R2.4A); forecast assumes zero repeat `[VIEW]`.
3. **Packaging.** Advanced packaging is a disclosed capacity constraint (R4.7), not a modeled P&L (R10.3).
4. **Quotient.** NT$bn revenue divided by wafer equivalents is a cross-check, not ASP (R3.3).
5. **Units.** NT$ billions are primary throughout the workbook.

Numeric facts remain in [`register.md`](register.md); narrative drivers in [`research.md`](research.md).
