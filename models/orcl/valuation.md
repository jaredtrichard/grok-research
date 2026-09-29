# Oracle valuation

**Official 12-month price target: $149.25** — modest constructive on Oracle: the segment model’s FY2028 operating income (~$31.5B) is worth [VIEW] 17.5× operating EV/EBIT, net of modeled FY2027 net debt, without capitalizing undisclosed RPO quality or mandatory-convert dilution. That is a **Hold / slight overweight** versus $137.79; the tape already embeds strong OCI growth and ~16.0× the same forward EBIT line.

## Official method and as-of

| item | value |
|---|---|
| Valuation as-of | 2026-09-29 |
| Last close | $137.79 on 2026-09-29 |
| Last-price source | [Yahoo Finance historical](https://finance.yahoo.com/quote/ORCL/history/) |
| PT denominator | 3,023,736,000 common shares on 2026-09-07 (R5.5) |
| Method | [VIEW] forward operating EV/EBIT on modeled segment-built OI; not RPO capitalization |
| Official 12-month PT / share | $149.25 |

**Why this method.** Oracle is priced on **earnings power through the OCI buildout**, not on near-term core free cash flow: modeled core FCF stays negative through FY2028 while reported operating cash flow is lifted by customer prepayments (R5.2). A prepay-excluded FCF DCF is shown as a **check only** and is not the official anchor. The official PT uses **[VIEW] 17.5×** on **FY2028E operating income** from the segment-built [`income.md`](income.md), less **FY2027E net debt** from [`balance.md`](balance.md), over **R5.5** shares. We do **not** add an RPO or GPU contract premium because RPO customer, margin and funding quality are **not obtained** (R8.2).

## What the tape must be paying for

| item | formula | $m or multiple |
|---|---|---|
| Last-price market capitalization | Last close × R5.5 shares | 416,640.6 |
| Q1 FY2027 net debt | Current + non-current borrowings − cash − marketable securities (R5.1) | 88,260.0 |
| Last-price operating EV | Market cap + net debt | 504,900.6 |
| EV / modeled FY2028E operating income | Tape operating EV ÷ income.md FY2028E OI | 16.0x |
| Official operating EV | 17.5× FY2028E OI | 551,621.2 |
| [DEDUCTED] EV gap vs tape | Official EV − tape EV | 46,720.6 |

At the last close, the market is already paying roughly **16.0×** the same FY2028E operating income the model derives from reported segment margins and `[VIEW]` OCI growth. The gap versus the official **17.5×** frame is therefore **not** “OCI from zero,” but incremental confidence that (1) **OCI revenue** scales on the modeled path, (2) **cloud-and-software segment margin** does not collapse beyond the `[VIEW]` glide, and (3) **financing and prepays** bridge capex without blowing up equity risk — none of which is guaranteed by headline RPO alone (R3.4–R3.7, R8.2).

## Official bridge

| item | basis | $m except per share |
|---|---|---|
| FY2028E operating income | income.md; segment margin bridge | 31,521.2 |
| Selected EV / EBIT | [VIEW] | 17.5x |
| Operating enterprise value | FY2028E OI × multiple | 551,621.2 |
| FY2027E net debt | balance.md cash + STI − debt | 100,320.8 |
| Official equity value | EV − net debt | 451,300.4 |
| Shares (m) | R5.5 | 3,023.736 |
| Official 12-month PT / share | Equity ÷ shares | $149.25 |

The multiple is a `[VIEW]` discount to mega-cap software peers for **capex intensity, leverage, and contract-duration mismatch** (research §2.7, R5.4, R7.3). It is a premium to a pure legacy software multiple because FY2028E operating income already embeds fast OCI growth from [`segments.md`](segments.md).

## Model paths that drive the PT

| driver | source | FY2028E anchor | class |
|---|---|---|---|
| OCI revenue FY2026A → FY2028E | segments.md; [VIEW] growth in inputs.md | 18,101 → 45,931 | [DEDUCTED] ~59% CAGR |
| Cloud & software margin FY2028E | segments.md | 53.5% | [VIEW] |
| FY2028E core free cash flow | cashflow.md (excludes prepay financing) | (9,128) | [VIEW] |
| FY2028E reported OCF | includes [VIEW] customer prepay | 58,872 | [VIEW] |
| FY2028E capex | inputs.md | 68,000 | [VIEW] |

Operating income is **not** a separate forecast plug: it flows from combined segment margin per R1.4, minus `[VIEW]` corporate lines in `inputs.md`. Changing OCI growth, cloud-and-software margin %, or capex/prepay assumptions in `inputs.md` moves FY2028E OI and therefore the PT linearly through the EBIT multiple.

## Core FCF DCF — check only (not official)

| item | basis | $m |
|---|---|---|
| PV FY2027–FY2029 core FCF | 9% WACC; prepays excluded | (29,268.7) |
| Terminal on core FCF | FY2029 FCF ≤ 0 → not obtained as anchor | not obtained |
| Core FCF equity (check) | PV − FY2027E net debt | (129,589.5) |
| Implied PT / share (check only) | Not official method | $-42.86 |

Core FCF excludes `[VIEW]` customer prepayment financing in [`cashflow.md`](cashflow.md). With FY2029 core FCF still negative on the base path, a Gordon terminal on core FCF is **not obtained**; the check illustrates why the official method is EBIT-based.

## Checks — not additional official targets

| check | method | value / share |
|---|---|---|
| Bear | 14.0× FY2028E OI − FY2027E net debt | $112.77 |
| Bull | 21.0× FY2028E OI − FY2027E net debt | $185.74 |
| 3-year / FY2029 exit | 16× FY2029E OI − FY2029E net debt | $167.03 |

## R8 and disclosure gaps vs uncertainty

| gap | why it matters | valuation treatment |
|---|---|---|
| R8.3 product-level OCI / app margin | Cannot split EBIT multiple between infra vs apps | Widens multiple uncertainty; no SOTP fill |
| R8.5 segment assets / FCF | Capex funded at corporate level only | Core FCF DCF is not a primary anchor |
| R8.2 RPO quality | RPO 664,000; ~13% in 12m schedule [FACT] | Tape may capitalize RPO; model does not |
| R5.7 preferred conversion | Conversion share count not obtained | PT uses 3023.736m basic; dilution unmodeled |
| R5.4 off-BS leases / power | 260,000+ lease commitments [FACT] | Net debt understates fixed charges |
| R8.7 FY2027 capex range | Written numerical range not obtained | Capex [VIEW] drives FCF checks |

## Comparable framing (not a separate comp target)

| company | EV / sales (approx.) | EV / EBIT (approx.) | as-of | note |
|---|---|---|---|---|
| MSFT | ~12x | ~28x | framing only | Large-cap software + cloud; not obtained in this run |
| CRM | ~6x | ~22x | framing only | SaaS comp; not obtained in this run |
| ORCL (tape) | 5.1x | 16.0x | 2026-09-29 | Model-implied on FY2028 revenue/OI |

Peer multiples are illustrative; live peer ratios were **not obtained** in this run except the tape-implied ORCL lines on modeled FY2028E.

**[DEDUCTED] Tape residual per share:** `$137.79 − official PT = $-11.46`. Negative residual means the official PT is above the last close; closing the gap requires a higher multiple, higher FY2028E operating income from the segment model, or lower net debt than modeled — not an undisclosed RPO add-on.

## What would move the official PT

- FY2028E operating income from [`income.md`](income.md) (OCI growth, segment margin %, corporate opex).
- The `[VIEW]` 17.5× EV/EBIT assumption.
- FY2027E net debt in [`balance.md`](balance.md) (debt issuance, cash, capex).
- R5.5 share count; R5.7 conversion would lower PT per share if dilution is added.
