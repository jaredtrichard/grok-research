# NVIDIA consensus — what appears priced

As of 2026-09-29. This file contrasts the **tape-implied** frame with the initiation **official view** in [`valuation.md`](../../models/nvda/valuation.md). It does not restate model forecasts (those live in [`income.md`](../../models/nvda/income.md)) and assigns no rating.

## 1. Sell-side / company-compiled consensus

- **[FACT]** NVIDIA does not publish a company-compiled earnings or revenue consensus table comparable to Tesla’s IR polls.
- **[FACT]** Post–Q2 FY2027 refreshed Street revenue/EPS/PT compilations for FY2028: **`not obtained`** through 2026-09-29 (see [`research.md`](research.md) gap table).

Without a sourced sell-side FY2028 EPS poll, the only disciplined “consensus” observable here is what the **last sale** implies against the model’s FY2028E path.

## 2. Tape-implied vs official view (from `valuation.md` diagnostics)

Last close **`[FACT]` $227.21** on 2026-09-29 (Yahoo; R6.4 shares for market cap). Model FY2028E diluted EPS **`[VIEW]` $15.63** and operating income **`[VIEW]` ~$448B** (`income.md`). Official initiation PT **`[VIEW]` $500.13** = **32×** that EPS (`valuation.md`).

| frame | implied FY2028E P/E | implied FY2028E EV / EBIT | notes |
|---|---:|---:|---|
| **Tape** (last close ÷ model FY2028E EPS; tape EV ÷ model FY2028E OI) | **~14.5×** | **~12.2×** | `[DEDUCTED]` from `valuation.md` tape table; uses 1H FY2027 net cash for EV |
| **Official initiation** | **32.0×** | n/a (PT is EPS-based) | Only this row is the cover PT |
| **Cross-checks** (not PT) | 42× on FY2027E EPS → ~$369; bear **24×** / bull **40×** on FY2028E EPS | **22×** FY2028E EBIT → ~$410/sh | `[VIEW]` sensitivity in `valuation.md` |

## 3. What the gap means (interpretation, not a second target)

- **`[DEDUCTED]`** At **~14.5×** FY2028E EPS, the tape embeds either materially lower FY2028 earnings than the model’s **$15.63** path, a permanent multiple compression versus the **`[VIEW]` 32×** official method, or some combination. The initiation thesis argues the modeled Data Center–led path plus **32×** is the right anchor; see [`thesis.md`](thesis.md).
- **`[DEDUCTED]`** Tape **~12×** FY2028E EBIT vs a **22×** EBIT cross-check (~$410/sh) shows the same direction: the market is not paying the model’s operating-income power at mid-cycle software-semis multiples unless EPS or the multiple assumption is wrong.
- **`[DEDUCTED]`** Until a sourced FY2028 EPS consensus arrives, “Street vs model” cannot be quantified line-by-line; watch Q3 FY2027 guide actuals (R2.4) and subsequent estimate revisions after each print.

No LONG, SHORT, or PASS. No price target in this file.
