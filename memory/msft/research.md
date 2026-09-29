# Microsoft initiation research file

GF-MSFT-1 · as of 2026-09-29 · name id `msft`

Read numeric facts in [`register.md`](register.md); this file owns the driver structure and interpretation. No fact is intentionally duplicated here.

## 1. Business and reporting architecture

1. **[FACT] Reporting.** Microsoft reports PBP, IC, and MPC. Product disclosures cut across those segments and Microsoft Cloud is an overlapping KPI, not a fourth segment. See R1–R3.
2. **[FACT] PBP.** Microsoft 365, LinkedIn, and Dynamics monetize user seats, premium SKUs, consumption, advertising, recruiting/sales subscriptions, and business-app workflows. See R1.2.
3. **[FACT] IC.** Azure, GitHub, health/life-sciences cloud, server software, developer tools, and hybrid infrastructure monetize consumption, subscriptions, licenses, and support. See R1.3.
4. **[FACT] MPC.** Windows/Devices, XBOX, and Search advertising monetize OEM licenses, hardware, content/subscriptions, transactions, cloud gaming, and advertising. See R1.4.

## 2. Segment driver tree

### 2.1 Productivity and Business Processes

1. **[DEDUCTED] Microsoft 365 Commercial revenue bridge:** paid seats × revenue per paid seat, plus usage-based products and on-premises products. Seat growth, E5/E7/Copilot mix, price, FX, term/license mix, and in-period recognition drive reported growth.
2. **[FACT] Copilot direction:** paid seats and sequential additions are obtained, while standalone revenue, ARPU, usage revenue, gross profit, and churn are not. Use R4.4/R9.2; do not multiply seats by a public list price and call it revenue.
3. **[DEDUCTED] Microsoft 365 margin bridge:** price/mix and mature cloud scale less inference/hosting cost, model cost, product engineering, sales capacity, and datacenter depreciation allocated to first-party apps. Increased usage can grow revenue while compressing gross margin before efficiency catches up.
4. **[DEDUCTED] LinkedIn revenue bridge:** member engagement × monetized impressions and yield, plus recruiter/sales/premium seats × ARPU. Hiring demand, ad budgets, feed quality, member growth, and AI-seat adoption are the key external/operating variables.
5. **[DEDUCTED] Dynamics revenue bridge:** cloud seats and modules × ARPU plus usage/low-code consumption and declining on-premises revenue. ERP/CRM sales cycles, renewals, partner implementation capacity, and Power Platform attach determine growth.
6. **[FACT] Segment history and latest margin commentary live in R2; product dollars live in R3.**

### 2.2 Intelligent Cloud — Azure and AI

1. **[DEDUCTED] Azure revenue bridge:** deployed compute/storage/network capacity × utilization × realized price, plus platform/database/security/developer services and support. Capacity constrains recognized consumption when demand exceeds supply.
2. **[DEDUCTED] AI demand bridge:** active customers/workloads × tokens or compute consumed × realized price, with model choice and optimization changing compute per outcome. Exact token economics and standalone AI revenue are not obtained (R9.1).
3. **[FACT] Capacity is the immediate conversion bottleneck.** Management said demand exceeded supply and efficiency/process gains were monetized quickly. See R4.3 and R7.3.
4. **[DEDUCTED] IC gross-profit bridge:** consumption and price less CPU/GPU depreciation, energy, networking, datacenter operations, model/provider cost, support, and third-party traffic/content. Mix toward Azure and infrastructure deployed ahead of use can lower margin even when revenue growth accelerates.
5. **[DEDUCTED] IC operating-income bridge:** gross profit less cloud/AI engineering, model and silicon development, sales, security, and shared R&D. Efficiency must offset both depreciation and continued R&D to preserve segment operating margin.
6. **[DEDUCTED] Server/hybrid bridge:** installed base × renewal/upgrade/licensing value, offset by migration to cloud. Transaction timing can create in-period volatility and should not be extrapolated as Azure consumption.
7. **[DEDUCTED] GitHub bridge:** developers/organizations × paid seats and usage. The user KPI is obtained, but paid mix and standalone economics are not (R4.6/R9.3).

### 2.3 More Personal Computing

1. **[DEDUCTED] Windows OEM revenue bridge:** PC units × Windows attach × realized OEM license value. PC demand, device mix, channel inventory, component prices, Windows lifecycle, and OEM contract timing drive the line.
2. **[DEDUCTED] XBOX revenue bridge:** active users × subscriptions/ARPU + content units/in-game spend and platform take rate + hardware units/ASP + advertising/cloud services. Release slate and first-party content quality can dominate quarterly comparisons.
3. **[DEDUCTED] Search advertising bridge:** queries/engagement × ad load × click/conversion × revenue per monetized event, less traffic-acquisition effects. Bing/Edge share, query quality, advertiser demand, and third-party partnerships drive volume and yield.
4. **[FACT]** Latest Windows, XBOX, and Search directions are in R4.5 and management’s FY2027 headwinds are in R7.4.
5. **[DEDUCTED] MPC margin bridge:** high-margin licenses and advertising offset lower-margin hardware/content, acquired-content amortization, impairment, gaming development, and shared R&D.

### 2.4 Corporate cash and capital intensity

1. **[DEDUCTED] Cash conversion:** segment operating income after tax + noncash D&A/SBC − operating working-capital investment − capex. Segment cash-flow allocations are not obtained; the workbook models only consolidated cash flow.
2. **[FACT]** FY2026 cash flow, PP&E, debt, shareholder returns, and short-lived-asset capex commentary are in R6.
3. **[DEDUCTED] AI capital cycle:** bookings/RPO and demand signals lead capacity commitments; capacity installation enables revenue; utilization and price determine revenue per capital dollar; efficiency and useful lives determine margin timing; cash returns arrive after capex.
4. **[FACT]** The useful-life change affects depreciation timing and lease classification, but does not remove the economic capital commitment (R6.5).
5. **[VIEW]** Forecast capex, working-capital ratios, segment growth, and margins live only in [`models/msft/inputs.md`](../../models/msft/inputs.md), not in this research file.

## 3. Historical financial skeleton

| model block | periods | register pointer | disclosure status |
|---|---|---|---|
| Segment revenue, cost, opex, operating income | FY2024–FY2026 | R2 | obtained |
| Product/service revenue | FY2024–FY2026 | R3 | obtained; overlaps segment lines |
| Consolidated income statement | FY2024–FY2026 | R5 | obtained |
| Balance sheet | FY2025–FY2026 | R6.1 | obtained |
| Cash flow | FY2024–FY2026 | R6.2 | obtained |
| Segment balance sheet/cash flow/capex | through 2026-06-30 | R9.4 | **not obtained** |

## 4. Azure and AI economics

1. **[FACT]** Revenue growth, capacity commentary, Microsoft Cloud margin, RPO, and Azure’s broad annual threshold are in R4.
2. **[DEDUCTED]** RPO is evidence of contracted demand, not a forecast-period revenue plug. Contract duration, cancellation/adjustment terms, consumption timing, financing, and the OpenAI concentration matter.
3. **[DEDUCTED]** Supply constraint supports near-term revenue visibility but can hide the unconstrained demand curve. It also means new capacity may be monetized quickly while the company is constrained; that is not proof of steady-state returns after supply catches up.
4. **[DEDUCTED]** The underwriting question is not whether AI demand exists. It is whether revenue and operating profit grow fast enough to cover the cash capex, depreciation, energy, model, and R&D burden while sustaining a return above the discount rate.
5. **[FACT]** Exact AI revenue, gross profit, utilization, and ROIC are not obtained (R9.1/R9.5).

## 5. Microsoft 365, LinkedIn, and Dynamics

1. **[FACT]** Product composition is in R1.2, dollar revenue in R3, and current growth/seat data in R4.
2. **[DEDUCTED]** Copilot monetization has three observable stages: paid-seat expansion, premium-SKU/ARPU mix, then incremental consumption. The first is partly observed; the latter two lack standalone dollars.
3. **[DEDUCTED]** Microsoft 365 can be both a direct AI revenue pool and a utilization source for Microsoft’s infrastructure. Avoid double counting app revenue and Azure internal consumption as two external revenue streams.
4. **[DEDUCTED]** LinkedIn and Dynamics provide separate workflow/data surfaces for agents, but model only reported segment economics until product-level disclosure supports an incremental wedge.

## 6. Windows, Gaming, Search, and advertising

1. **[FACT]** Product revenue history is in R3 and latest growth is in R4.5.
2. **[DEDUCTED]** Windows and XBOX are near-term drags in management’s FY2027 frame, while Search is the measurable growth offset inside MPC.
3. **[DEDUCTED]** Search’s AI opportunity is economically relevant only through incremental users/queries, monetization, and cost per query. No standalone Copilot consumer P&L is obtained.
4. **[DEDUCTED]** Activision improves content breadth but introduces release-cycle, amortization, impairment, and integration effects; segment revenue alone does not isolate organic XBOX economics.

## 7. Node map

| node / flow | who pays whom | where value sits | what breaks it |
|---|---|---|---|
| Enterprise/SMB → Microsoft 365 **[FACT]/[DEDUCTED]** | per-seat licenses, premium SKUs, usage | installed base, workflow/data integration, distribution, switching costs | weak adoption, low usage, seat compression, inference cost, regulation |
| Enterprise/developer → Azure **[FACT]/[DEDUCTED]** | metered compute, storage, network, data/AI services, support | global capacity, software stack, model choice, sales channel | overbuild, capacity delays, power/chip shortages, price competition, workload optimization |
| Microsoft → chip/model/energy/datacenter suppliers **[DEDUCTED]** | equipment, leases, power, model/provider economics | scarce supply and technical capability; Microsoft orchestration and utilization | supply concentration, component inflation, energy limits, partner disputes |
| Developer/organization → GitHub **[FACT]/[DEDUCTED]** | seats and usage | code graph, workflow integration, Copilot distribution | model commoditization, security/IP concerns, weak paid conversion |
| Recruiter/advertiser/professional → LinkedIn **[FACT]** | subscriptions and advertising | professional graph, identity, engagement, workflow data | hiring cycle, ad slowdown, low-quality engagement, privacy rules |
| Business → Dynamics/Power Platform **[FACT]** | seats, modules, usage, services | embedded workflows, data, partner ecosystem | long sales cycles, implementation friction, CRM competition |
| OEM/device buyer → Windows/Devices **[FACT]/[DEDUCTED]** | OEM license or device purchase | installed base, compatibility, distribution | PC contraction, component inflation, platform substitution |
| Gamer/content buyer → XBOX **[FACT]/[DEDUCTED]** | hardware, subscriptions, content, in-game spend | content library, network, distribution | weak releases, engagement loss, high content cost, platform competition |
| Advertiser → Microsoft Search **[FACT]/[DEDUCTED]** | auction-priced advertising | query intent, Bing/Edge distribution, ad stack | query-share loss, lower yield, TAC/partnership changes, AI query cost |

**[VIEW] Value concentration.** Near-term incremental value is concentrated in Azure/AI capacity monetization and Microsoft 365 premium/usage adoption. The valuation should not assign a separate unreported “AI segment” on top of segment cash flows.

## 8. What would break the operating case

1. **[DEDUCTED]** IC revenue growth slows before capex and depreciation normalize.
2. **[DEDUCTED]** Microsoft Cloud or IC gross margin continues to fall without operating-expense leverage.
3. **[DEDUCTED]** RPO growth is concentrated in long-duration or related frontier-model commitments that do not convert into high-return cash revenue.
4. **[DEDUCTED]** Copilot seat growth fails to produce durable ARPU/usage expansion, or inference cost absorbs the uplift.
5. **[DEDUCTED]** Windows/XBOX weakness overwhelms Search growth and MPC margin.
6. **[DEDUCTED]** Regulation, cybersecurity failure, power constraints, chip supply, or OpenAI/partner economics reduce Microsoft’s control of the stack or increase required returns.

## 9. Numbers the model must take

Values live only in the register. “Take” means link the model assumption to the cited register item, preserving source date and classification.

| named input | take from | source / as-of | status |
|---|---|---|---|
| Segment revenue, cost, opex, operating income | R2 | S2 FY2024–FY2026 | obtained |
| Product/service revenue | R3 | S2 FY2024–FY2026 | obtained; overlapping |
| Azure/Microsoft Cloud growth and margin | R4.1–R4.3 | S3–S5, 2026-06-30 | obtained |
| Microsoft 365 seats/Copilot paid seats | R4.4 | S4/S5, 2026-06-30 | obtained |
| Copilot revenue, ARPU, margin, churn | R9.2 | through 2026-09-29 | **not obtained** |
| GitHub paid economics | R4.6/R9.3 | through 2026-09-29 | users obtained; economics **not obtained** |
| RPO and ex-OpenAI growth | R4.2 | S3/S5, 2026-06-30 | obtained; duration mix **not obtained** |
| Consolidated income statement | R5 | S2 FY2024–FY2026 | obtained |
| Balance sheet and shares | R6.1 | S2, 2026-06-30 | obtained |
| Cash flow, capex, D&A, SBC, returns | R6.2 | S2 FY2026 | obtained |
| FY2027 management operating bar | R7 | S5, 2026-07-29 | obtained |
| Segment assets/capex/cash flow | R9.4 | through 2026-09-29 | **not obtained** |
