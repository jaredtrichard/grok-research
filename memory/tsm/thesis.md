# TSMC working thesis

GF-TSM-1 · as of 2026-09-29 · name id `tsm`

Numbers live in the workbook. This file owns the claim, the mechanism, and the killing conditions. Official 12-month price target: [`models/tsm/valuation.md`](../../models/tsm/valuation.md). Do not treat a restated figure here as a second target.

## Claim

The official PT is a single-segment foundry equity bridge the model actually builds: **21.0× [VIEW] FY2027E recurring operating income** (ex VIS) **plus FY2027E net cash**, converted to ADR dollars at **1 ADR = 5 common shares** (R8.1) and **32 NT$/USD [VIEW]** (R2.5). That produces **$463.15 per ADR** (**NT$2,964.19 per common share**) as of 2026-09-29. Last close **$456.94** (Yahoo Finance TSM, 2026-09-29) is a comparison in `valuation.md`; the signed tape-vs-PT gap there is **−$6.21 (−1.3%)**, not an instruction to retune the path.

If the model does not say it, it is not this thesis. Node ASP, utilization, packaging P&L, and peer EV/EBIT remain `not obtained` (R10.1–R10.4, R10.8) and are not smuggled in as facts.

## Why this view is right

1. **The economics that are measurable sit in company foundry P&L, not invented node P&Ls.** TSMC reports one foundry segment (R1.2). The model takes IASB-IFRS revenue / GP / OI / parent NI for FY2023–FY2025 (R2) and builds FY2026E–FY2028E from disclosed drivers: advanced-node mix (Q2 2026: 7nm-and-below 77% of wafer revenue; 3nm 30%, 5nm 33%, 2nm 3% — R3), HPC platform share (66% of Q2 revenue — R3), N2 ramp margin dilution then maturation (R6.1), and overseas-fab dilution 2–4pp (R6.2). Packaging is modeled as a **capacity constraint** that supports frontend demand (R4.7), not a fake CoWoS P&L (R10.3).
2. **Near-term growth is anchored to management’s own USD outlook, then translated carefully.** Management expected FY2026 revenue growth slightly above 40% YoY in USD (R2.6). The `[VIEW]` revenue path is NT$5,360 / 6,120 / 6,680bn for FY2026E–FY2028E with gross margin 62.5% → 63.5% → 64.0%, embedding N2 dilution then recovery and overseas dilution. Recurring parent NI reaches NT$2,520 / 2,945 / 3,260bn. VIS disposal/MTM (NT$63.2bn in Q2 2026 — R2.4A) is separated and set to zero in the forecast.
3. **The official multiple sits on the tape, not on invented peers.** At last close, implied EV / FY2027E recurring EBIT is **21.3×** on the model path. Selecting **21.0×** is a `[VIEW]` that stays near that frame while leaving a thin discount for overseas dilution and concentration / Taiwan continuity risk (R5.1, R6.2, R9.5). Peer foundry EV/EBIT was **not obtained** (R10.8); the multiple is not a peer median.
4. **Cash conversion is real but capex-heavy.** FY2026 capex `[VIEW]` near the US$60–64bn guide (R7.3) produces strong OI and weaker near-term FCF. The DCF cross-check (WACC 9.5%, g 3%) lands at **$224.45/ADR** — below the official EV/EBIT PT — because the R7.3 capex path compresses FCF versus EBIT. That gap is a feature of the investment cycle, not a reason to abandon the EBIT bridge as the official method.
5. **Net cash and share count are model-tied.** FY2027E net cash NT$4,403.5bn and ~25,950m diluted WAS feed the equity bridge. Buybacks stay at 0 given R8.4; dividends rise with earnings as a `[VIEW]`.

## What others miss or get wrong

1. **Treating NT$/wafer as ASP.** The Q2 quotient (~NT$293k per 12-inch-equiv. shipment — R3.3) mixes packaging/testing and conversion effects. Exact node/customer ASP is `not obtained` (R10.1). Pricing power arguments that start from that quotient are wrong.
2. **Inventing a CoWoS profit center.** Advanced packaging is tight enough to limit customer growth (R4.7), which supports frontend wafer demand, but standalone packaging revenue/margin/capacity are `not obtained` (R10.3). Assigning a separate packaging multiple without disclosure is fiction.
3. **Splicing TIFRS into IASB without a bridge.** FY2025 parent NI differs TIFRS vs IASB-IFRS (R2.3). The model keeps annual history on IASB and labels 1H2026 as TIFRS (R2.3A). Mixing them creates a false trend.
4. **Assuming Street consensus is the base case.** Sell-side estimates and external PTs were `not obtained` (R10.9). Management guidance (R2.5–R2.6) is company outlook, not consensus. This thesis is the model path, not a fade-to-Street.
5. **Collapsing Taiwan risk, export controls, and overseas dilution into one haircut.** They have different timing and recovery paths (R9.3–R9.6, R6.2). One blended “geopolitics discount” hides which kill is firing.

## Mechanism and magnitude

- **Mechanism:** Company IS is one foundry segment. Official equity = (21.0× FY2027E recurring OI) + FY2027E net cash. ADR PT = common NT$ PT × 5 ÷ 32. Node and platform mixes are lenses on revenue, not separate P&Ls. Packaging enters as utilization / allocation constraint, not line-item profit.
- **Magnitude:** See official PT, tape comparison (−1.3% vs PT), EV/EBIT 21.3× at tape, and bear/bull checks ($400.78 / $463.15 / $525.53 per ADR at 18× / 21× / 24×) in `valuation.md`. DCF is a cross-check only.

## Killing conditions

Statuses reflect evidence through 2026-09-29. Recheck on official prints and IR packs, not narrative commentary.

| kill | status | what would do it / what remains | when to check |
|---|---|---|---|
| FY2026–FY2027 recurring OI path breaks | **LIVE WATCH** | Printed gross margin or OI far below `income.md` (N2 dilution worse than R6.1, overseas dilution >R6.2, or utilization shock) | Q3/Q4 2026 earnings; FY2026 20-F |
| Advanced-node mix stalls | **LIVE WATCH** | 2nm / 3nm / 5nm wafer-revenue shares far below the rising `[VIEW]` path in `inputs.md` / `segments.md` | each quarterly mix disclosure |
| Capex / cash conversion regime change | Open | Capex well below US$60–64bn without matching demand soft, or FCF collapse that forces a balance-sheet event | Q3/Q4 2026; FY2026 cash flow |
| Packaging bottleneck resolves without frontend support | Open | CoWoS / advanced packaging capacity eases **and** frontend wafer growth slows together in a way that breaks the demand bridge | quarterly call packaging commentary; any capacity KPI |
| Export-control / customer-eligibility shock | Open | License denial or customer demand cut that materially hits North America ~75–78% HQ mix (R5) | 20-F risk updates; material 6-K / IR |
| Taiwan production continuity event | Open | Earthquake, utility, or geopolitical interruption with lasting capacity loss beyond disclosed prior losses (R9.5) | immediate IR; next quarter |
| Accounting-basis confusion | Open | New disclosure that makes IASB/TIFRS splice mandatory without a bridge (R10.13) | FY2026 20-F / AR |

A last-sale move alone does not kill the thesis. A new narrative without a number does not kill it. Do not retune the official PT to the tape.

## What this file is not

This file assigns no recommendation. The cover PR is the staged thesis. Publication of `names.thesis_ref` is Firstmate’s job after the captain merges.
