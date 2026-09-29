# Oracle consensus — what is already priced

As of 2026-09-29. This home owns consensus and what-is-priced framing; company actuals remain in [`register.md`](register.md). Unless cited to a primary sell-side compilation, **sell-side consensus tables are not obtained** in GF-ORCL-1.

## 1. What the last close embeds (model-implied)

Source for price: [Yahoo Finance historical](https://finance.yahoo.com/quote/ORCL/history/), last close **$137.79** on **2026-09-29** [FACT] per [`valuation.md`](../../models/orcl/valuation.md). Share count **3,023,736,000** on **2026-09-07** [FACT] R5.5.

| item | basis | class |
|---|---|---|
| Market capitalization | last close × R5.5 shares | [DEDUCTED] in `valuation.md` |
| Q1 FY2027 net debt | R5.1 cash, securities, borrowings | [FACT] |
| Operating EV | market cap + net debt | [DEDUCTED] |
| EV ÷ modeled FY2028E operating income | `income.md` OI **$31,521m** | [DEDUCTED] ~**16×** in `valuation.md` |
| EV ÷ modeled FY2028E revenue | `income.md` revenue **$99,542m** | [DEDUCTED] ~**5.1×** |

- **[DEDUCTED]** The tape is **not** pricing Oracle as a low-growth support annuity: at the last close it already pays a mid-teens **forward EBIT multiple** on the **same** FY2028E operating income the segment model builds, before the official `[VIEW]` **17.5×** frame in `valuation.md`.
- **[DEDUCTED]** The gap between tape-implied and official EV/EBIT is **modest** (~1.5 turns on FY2028E OI in `valuation.md`)—a debate about **multiple and balance-sheet risk**, not whether OCI exists in the forecast.
- **[VIEW]** Much public commentary still anchors on **headline RPO** (**$664,000m** [FACT] R3.4) and AI contract headlines; the initiation model **does not** capitalize RPO because quality splits are **not obtained** (R8.2). Consensus narrative can therefore **overstate** what is already in recognized revenue and segment margin.

## 2. Filing facts the Street shares (whether or not models align)

| topic | latest obtained | register |
|---|---|---|
| RPO level and 12-month recognition % | **$664,000m**; **~13%** in next 12 months | R3.4 |
| Q1 FY2027 cloud infrastructure growth | **+121%** YoY; CPU/GPU infra **+151%** | R3.2 |
| Q1 FY2027 cloud-and-software segment margin | **54.5%** (55% rounded) | R2 |
| Capacity / utilization KPIs | **850 MW** incremental; **97.9%** AI-infra utilization | R3.6 |
| Customer prepay in OCF (financing) | **$11,363m** in Q1 FY2027 | R5.2 |
| ATM equity issuance | **141m** shares; program fully utilized | R5.5 |

- **[FACT]** These are widely visible in filings and the Q1 FY2027 earnings package (S2–S4).
- **[DEDUCTED]** Any sell-side model that flows **full RPO** into near-term revenue without delivery and margin constraints is **stricter** than this initiation workbook and **looser** than recognized revenue accounting (R1.3, R3.4).

## 3. Company-compiled or sell-side consensus tables

- **[FACT]** Oracle IR **does not** publish a Tesla-style delivery/earnings consensus page in the source set used for GF-ORCL-1 (S1–S12). A single official compilation of FY2027–FY2029 revenue, EPS, cloud infrastructure revenue, capex, or price targets: **not obtained**.
- **[FACT]** Post–Q1 FY2027 (2026-09-10) refreshed sell-side consensus averages, recommendation distribution, and price-target scatter: **not obtained** as of 2026-09-29.
- **[VIEW]** Until a dated primary compilation is added to the register, claims about “Street EPS” or “consensus PT” relative to [`income.md`](../../models/orcl/income.md) or [`valuation.md`](../../models/orcl/valuation.md) should be treated as **not obtained**, not inferred from press commentary.

## 4. Views commonly held around the name (not verified consensus)

Framing only—these are **market narratives**, not tabulated sell-side positions:

| view | what it prices | tension with initiation model |
|---|---|---|
| **RPO / AI contract bull** | Years of contracted cloud demand and winner-take-most AI infra | Model uses **recognized** OCI revenue and segment margin only; RPO NPV **not obtained** (R8.2) |
| **OCI hyper-growth bull** | Continuation of Q1 FY2027 **+121%** infra growth | Model **decelerates** OCI growth `[VIEW]` in `inputs.md` (75% / 45% / 30%) |
| **Legacy cash-cow** | Support and database durability | Model keeps support ~flat; bull case requires **OCI + margin** path in `segments.md` |
| **Capex / FCF bear** | FY2026A FCF **$(23,686)m** [DEDUCTED] R2 and rising debt | Aligns with `cashflow.md` core FCF negativity; official valuation **does not** use FCF DCF as anchor |
| **Leverage / lease bear** | Debt, converts, off–BS leases (R5.4, R5.7) | `balance.md` net debt is modeled; full fixed-commitment stack **not obtained** in BS |

- **[VIEW]** The initiation thesis is closest to: **“OCI earnings power is largely in the price; we need modestly better confidence on margin and financing than the tape implies.”** See [`thesis.md`](thesis.md).

## 5. What cannot yet be claimed as priced

- **[FACT]** Precise sell-side FY2028 cloud infrastructure revenue, cloud-and-software margin, capex, or EPS central tendency: **not obtained**.
- **[FACT]** Market-implied RPO discount rate, contract cancellation risk, or GPU-hour margin: **not obtained** (R8.1–R8.2).
- **[FACT]** Mandatory convertible preferred conversion share count: **not obtained** (R5.7).
- **[VIEW]** Without those, this file can describe **directional** what the tape embeds via `valuation.md`’s model-implied multiples, but cannot prove whether the market assigns a higher or lower RPO “option” than the official PT.
