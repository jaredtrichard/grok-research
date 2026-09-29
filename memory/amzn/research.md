# Amazon initiation research file

GF-AMZN-1 · as of 2026-09-29 · name id `amzn`

Read numeric facts in [`register.md`](register.md); this file owns driver structure and interpretation. No fact is intentionally duplicated here.

## 1. Business and reported segments

1. **[FACT] Reporting architecture.** Amazon reports North America, International and AWS. Product/service sales groups are an overlapping revenue disaggregation, not additional reportable segments. See R1.1–R1.3.
2. **[FACT] North America.** This segment combines first-party and marketplace retail economics, physical stores, advertising, subscriptions and other services through North America-focused stores. Export sales from those stores remain in North America. See R1.1.
3. **[FACT] International.** This segment has the analogous stores/service perimeter for internationally focused stores. Its export rules—not customer domicile alone—determine segment attribution. See R1.1 and R5.1.
4. **[FACT] AWS.** AWS is the only reportable segment whose perimeter also appears as a separately disclosed sales group. It sells compute, storage, database and other services globally. See R1.1–R1.2.
5. **[FACT] Measurement boundary.** Segment revenue, operating expense, operating income, assets, PPE additions and PPE D&A are disclosed. Segment gross profit and product-line profit are not. Amazon explicitly prefers operating income to gross profit as a performance measure. See R1.5, R2 and R8.2/R8.6.

## 2. Segment driver tree

### 2.1 North America retail and other

1. **[DEDUCTED] First-party revenue bridge:** paid first-party units × realized revenue per unit, plus transactional digital content and shipping revenue recorded gross. Neither unit count nor clean ASP is disclosed (R8.1).
2. **[DEDUCTED] Marketplace revenue bridge:** third-party gross merchandise sales × effective take rate, where take rate combines commissions, fulfillment/shipping fees and other seller services. Seller unit mix is observable; GMV and take-rate components are not (R3.2, R8.1).
3. **[DEDUCTED] Stores operating-income bridge:** first-party merchandise contribution + marketplace fees + advertising + subscriptions + Other − shipping − fulfillment − technology/infrastructure − marketing − G&A − other operating items.
4. **[FACT] Key volume drivers:** customer demand, selection, price, delivery speed, inventory availability, third-party seller participation and Prime engagement. Latest paid-unit, seller-mix and sales-group readings are in R3.
5. **[DEDUCTED] Key cost drivers:** product/content acquisition, inbound/outbound freight, sortation and last mile, fulfillment labor/depreciation/rent, payment processing, returns, customer service, technology and marketing. Cost classification and shipping disclosures are in R2.4 and R3.6.
6. **[DEDUCTED] Working-capital advantage:** first-party inventory and receivables consume cash, while seller/vendor payables and prepaid subscriptions can fund growth. The advantage depends on inventory turns, mix, seasonality and payment terms—not revenue growth alone.

### 2.2 International

1. **[DEDUCTED]** Use the same retail/marketplace/ad/subscription bridge as North America, then add country maturity, local selection, delivery density, payments, duties/tariffs, wage structure and FX.
2. **[FACT]** Revenue and profit attribution follow internationally focused stores and AWS selling entities rather than a simple buyer-location convention (R5.1).
3. **[DEDUCTED]** International margin convergence is not automatic: smaller local networks, price investment, cross-border logistics, regulation and country mix can offset scale.
4. **[FACT]** Current International sales and operating-income drivers and FX effects are in R2.3 and R5.2.

### 2.3 AWS

1. **[DEDUCTED] Revenue bridge:** average active paid workloads × compute/storage/database/other consumption × realized unit price, plus contractual minimums and support/professional services where applicable.
2. **[FACT]** Filing evidence supports usage as the primary current growth driver, partly offset by pricing changes associated with long-term contracts (R3.3).
3. **[DEDUCTED] Capacity bridge:** opening usable compute/storage/network capacity + commissioned capacity − retirements, constrained by data-center shells, power, chips, networking and deployment cadence. Regions/AZs measure geographic footprint, not available compute.
4. **[DEDUCTED] Operating-profit bridge:** revenue − power − server/network depreciation − data-center rent/operations − personnel/support − sales commissions − allocated shared costs. Segment PPE and D&A provide capital-intensity anchors, not a complete unit-cost curve (R4.3, R6.6).
5. **[DEDUCTED] Backlog bridge:** opening performance obligations + new/expanded commitments − revenue recognized − cancellations/price changes. RPO is not annual recurring revenue; usage and performance govern timing (R3.4).
6. **[FACT]** Customer counts, workload units, utilization, chip volumes, AI revenue dollars and clean gross margin are not obtained (R8.5).

### 2.4 Advertising

1. **[FACT] Revenue pool.** Sponsored, display and video advertising sold to sellers, vendors, publishers, authors and others is disclosed globally as a sales group but not as a reportable segment (R1.2–R1.3).
2. **[DEDUCTED] Revenue bridge:** monetizable traffic/impressions × ad load/fill × price per impression/click/conversion, plus video and off-Amazon inventory.
3. **[DEDUCTED] Value drivers:** high-intent commerce traffic, closed-loop attribution, seller competition, advertiser tooling, Prime Video inventory and third-party publisher reach.
4. **[DEDUCTED] Cost bridge:** serving/measurement infrastructure, sales/support, traffic or publisher consideration and content/inventory costs. Revenue growth alone cannot prove incremental margin because standalone costs and profit are not disclosed (R8.4).

### 2.5 Subscription services / Prime

1. **[FACT]** Subscription revenue includes Prime membership fees and non-AWS digital video, audiobook, music, e-book and other subscriptions (R1.3).
2. **[DEDUCTED] Revenue bridge:** average paid members × recognized membership ARPU + standalone digital subscriptions; geography, monthly/annual mix, promotions and FX alter realized ARPU.
3. **[DEDUCTED] Economic bridge:** fees plus induced retail/ad/marketplace activity − expedited shipping, content, payment and service costs. Prime’s value cannot be assessed from subscription revenue alone.
4. **[FACT]** Member count, churn, cohort retention and benefit cost are not obtained (R3.7, R8.3).

### 2.6 Third-party seller services

1. **[FACT]** Recognized revenue comprises commissions, related fulfillment/shipping fees and other seller services; Amazon is not seller of record for marketplace merchandise (R1.3–R1.4).
2. **[DEDUCTED] Revenue bridge:** third-party gross merchandise sales × all-in effective take rate, where the rate spans commissions, fulfillment/shipping and other seller-service fees.
3. **[DEDUCTED] Profit drivers:** marketplace density, seller service adoption, inventory placement, fulfillment utilization, payment cost, returns and customer guarantees.
4. **[FACT]** Unit mix is obtained; GMV, seller count, FBA penetration and take-rate decomposition are not (R3.2, R8.1).

### 2.7 Physical stores

1. **[FACT]** Physical-stores revenue counts items selected in-store; delivery or pickup orders placed online remain Online stores (R1.3).
2. **[DEDUCTED] Revenue bridge:** store count × selling area × sales density, adjusted for openings/closures, comparable traffic, basket and category mix.
3. **[DEDUCTED] Profit bridge:** merchandise margin − occupancy − labor − shrink/spoilage − local fulfillment and technology. Online attribution prevents a complete omnichannel store P&L.
4. **[FACT]** Store counts/footprint are in R4.1; same-store sales, sales density and standalone profit are not obtained (R8.2).

### 2.8 Devices and Other

1. **[FACT]** Devices are manufactured and sold but not separately quantified. “Other” includes shipping, healthcare, certain content licensing/distribution and co-branded credit-card agreements (R1.3).
2. **[DEDUCTED] Device economics:** units × hardware ASP + downstream engagement, less BOM, logistics, warranty and development. Hardware contribution may differ materially from ecosystem value.
3. **[DEDUCTED] Other revenue:** service volumes × fees, with credit-card economics also sensitive to spend, partner terms and credit quality.
4. **[FACT]** Device units/revenue/margin and the constituents of Other are not obtained separately (R8.2).

## 3. Historical financial skeleton

**[FACT]** Use the register once; do not recreate history elsewhere.

| model block | periods | register pointer | disclosure status |
|---|---|---|---|
| North America revenue / opex / operating income | FY2022–FY2025; Q2, 1H and TTM 2026 | R2 tables, R2.1 | obtained; TTM opex deduced |
| International revenue / opex / operating income | same | R2 tables, R2.1 | obtained; TTM opex deduced |
| AWS revenue / opex / operating income | same | R2 tables, R2.1 | obtained; TTM opex deduced |
| Sales groups | FY2022–FY2025; Q2 and TTM 2026 | R3 tables | obtained; most TTM groups deduced from reported quarters |
| Product-line gross profit / operating income | all periods | R8.2 | **not obtained** |
| Consolidated operating-expense lines | Q2/1H 2026 | R2.4 | obtained |

## 4. Operating footprint

1. **[FACT] Fulfillment / stores / data centers.** Property footprint by use and segment is in R4.1–R4.2. Mixed “fulfillment, data centers and other” square footage cannot be cleanly split into logistics versus cloud.
2. **[FACT] Segment capital base.** Latest PPE and 1H net additions are in R4.3; additions include non-cash activity and must not be substituted for cash capex.
3. **[FACT] AWS regions.** The current official Region/AZ count is in R4.4. It measures fault-domain and geographic reach, not data-center count, installed power or utilization.
4. **[DEDUCTED] Retail density loop.** Better inventory placement and denser delivery routes can reduce distance and cost while improving speed; the economic test is lower cost per fulfilled unit without excess inventory or underused facilities.
5. **[DEDUCTED] AWS capacity loop.** Capex creates sellable capacity only after power, chips, networking and data halls are commissioned. PPE additions can precede revenue and cash returns.
6. **[FACT]** Utilization, throughput, installed MW, accelerator fleet and precise site counts are not obtained (R4.5, R8.7).

## 5. Geography

1. **[FACT] Country revenue.** Use R5 for the U.S., Germany, U.K., Japan and rest of world. The basis is country-focused stores or AWS selling entity.
2. **[FACT] Segment geography.** Canada and Mexico sit in North America; International export rules can include sales to the U.S., Mexico and Canada. Do not map segment sales directly onto end-customer countries.
3. **[DEDUCTED] Revenue FX bridge:** local-currency growth plus translation into U.S. dollars. Intercompany remeasurement is a separate non-operating item. Use reported ex-FX growth for operating direction, not as a substitute for local unit economics.
4. **[FACT]** Quarterly country revenue and quantified AWS end-customer geography are not obtained.

## 6. Retail / marketplace economics

1. **[FACT] Gross-versus-net reporting.** First-party merchandise is generally gross revenue; marketplace service fees are net revenue (R1.4). **[DEDUCTED]** Reported sales growth can therefore lag underlying commerce growth as mix shifts to third parties.
2. **[DEDUCTED] First-party contribution:** gross revenue − product/content cost − inbound/outbound freight − fulfillment/payment/returns − allocated technology/marketing/overhead.
3. **[DEDUCTED] Marketplace contribution:** commissions/FBA/other fees − fulfillment and shipping − payment processing − seller support/guarantee − allocated technology/marketing.
4. **[DEDUCTED] Inventory/payables test:** improvement is durable only if faster turns, in-stock rates and vendor/seller terms support it; delayed inventory or payables timing can flatter cash conversion temporarily.
5. **[FACT]** Paid-unit growth, seller-unit mix and shipping cost are in R3.2/R3.6. GMV, ASP, take rate and FBA mix are not obtained (R8.1).
6. **[VIEW]** The key retail question is not only revenue growth; it is whether regionalized fulfillment and mix shift can sustain contribution after delivery-speed investment and price reinvestment.

## 7. AWS economics

1. **[FACT]** Historical/latest revenue, operating expense and operating income live in R2.
2. **[FACT]** Usage/price commentary and contractual obligations live in R3.3–R3.4.
3. **[FACT]** PPE, additions, D&A and Region/AZ footprint live in R4.3–R4.4 and R6.6.
4. **[DEDUCTED]** Incremental operating margin depends on utilization of commissioned capacity, workload mix, custom-versus-merchant chips, power, pricing commitments and depreciation—not revenue growth alone.
5. **[DEDUCTED]** Large AI commitments are demand evidence but also concentration, performance-obligation and capacity-funding risks; booked commitments cannot be treated as near-term revenue.
6. **[VIEW]** The central underwrite is whether faster AI-led revenue and custom-chip economics can outrun the depreciation, power and financing burden of the current capacity build.

## 8. Advertising and other high-margin lines

1. **[FACT] Advertising.** Revenue history and latest growth live in R3; standalone profit does not.
2. **[DEDUCTED]** Advertising likely benefits from commerce intent and existing traffic, but calling it a fixed incremental margin without traffic/content and infrastructure costs would overstate observability.
3. **[FACT] Subscriptions.** Revenue history is in R3; Prime member economics are absent (R8.3).
4. **[DEDUCTED]** Prime should be modeled as an ecosystem loop—membership revenue plus induced purchase frequency, seller demand and ad inventory—against shipping/content/service costs.
5. **[FACT] Other/devices.** Revenue constituents are known but not quantified separately (R1.3, R8.2).
6. **[VIEW]** Mix toward Advertising, seller services and subscriptions can lift Stores economics, but the model must not assign segment-like margins to these sales groups without explicit assumptions.

## 9. Balance sheet and cash-flow inputs

1. **[FACT] Liquidity/working capital.** Cash, investments, inventory, receivables, payables and unearned revenue are in R6.1.
2. **[FACT] Debt/leases.** Current/non-current debt, post-quarter issuance and lease liabilities/commitments are in R6.2–R6.3.
3. **[FACT] Shares.** Latest outstanding, stock-award and diluted share measures are in R6.4; use the denominator appropriate to valuation versus EPS.
4. **[FACT] Cash flow.** OCF, cash capex and FCF history/latest are in the R6 table.
5. **[FACT] Capex outlook.** The latest numerical annual outlook found is in R6.5. Do not read 1H segment PPE additions as cash capex.
6. **[FACT] Investments/non-operating marks.** Anthropic/OpenAI cash deployment and non-operating gains are in R7.1–R7.2; separate them from operating earnings and core capex.
7. **[FACT] Commitments/acquisition.** Contractual commitments and the pending Globalstar transaction are in R7.3–R7.4.

## 10. Node map: who pays whom, where value sits, what would break it

| node / flow | who pays whom | where value sits | what breaks it |
|---|---|---|---|
| Consumer → Amazon first-party **[DEDUCTED]** | product price, membership and service fees | selection, price, delivery speed, trust, inventory turns | weak demand, price competition, inventory errors, freight/returns/shrink |
| Consumer → third-party seller; seller → Amazon **[FACT]/[DEDUCTED]** | buyer pays seller; seller pays commission, fulfillment/shipping and other fees | marketplace density, FBA network, conversion and trust | seller disintermediation, fee/regulatory pressure, poor fulfillment economics |
| Advertiser → Amazon/publisher **[FACT]/[DEDUCTED]** | sponsored/display/video ad spend; potential publisher consideration | high-intent traffic, attribution, inventory, tools | traffic loss, low returns, ad-load limits, privacy/competition rules |
| Prime/digital subscriber → Amazon **[FACT]/[DEDUCTED]** | recurring membership/subscription fee | retention, purchase frequency, content and delivery bundle | churn, benefit-cost inflation, content weakness, regulatory limits |
| AWS customer → AWS **[FACT]/[DEDUCTED]** | usage, commitments and support/service payments | scale, breadth, reliability, chips, developer ecosystem | price/performance loss, outages, capacity/power constraints, customer concentration |
| Amazon → chip/power/data-center ecosystem **[DEDUCTED]** | accelerators, CPUs, networking, construction, leases, electricity | scarce compute and power; Amazon custom silicon/software | supply delays, power/permitting limits, capex overbuild, rapid obsolescence |
| Amazon → vendors/carriers/labor **[FACT]/[DEDUCTED]** | merchandise, freight, delivery, wages and benefits | procurement, route density, automation and throughput | labor disruption, tariffs, fuel/freight inflation, supplier concentration |
| Amazon → content creators/rights holders **[DEDUCTED]** | licensing and production spend | engagement, subscription retention and ad inventory | cost inflation, weak viewing, rights loss |
| Amazon ↔ strategic AI investees **[FACT]/[DEDUCTED]** | equity capital from Amazon; large AWS commitments from investees | model access, demand for AWS chips/compute, investment upside | circular demand, concentration, funding need, valuation reversals |
| Governments/regulators ↔ Amazon **[FACT]/[DEDUCTED]** | taxes, fines, procurement and remedies | market access and licenses | antitrust/marketplace remedies, privacy rules, tax, cloud procurement limits |

**[VIEW] Value concentration.** AWS operating income is directly observable; Stores’ marketplace, ad and subscription mix is economically important but not separately profitable in disclosure. Strategic-investment marks can dominate GAAP net income without improving operating cash generation.

## 11. Competitive and regulatory frame

1. **[FACT] Retail/marketplace competition.** Amazon identifies physical, e-commerce and omnichannel retail, e-commerce services and logistics among intensely competitive markets (R7.7).
2. **[FACT] AWS competition.** Web/infrastructure computing and AI services face established and new competitors; semiconductor availability can constrain AI infrastructure (R7.7).
3. **[FACT] Advertising/content/devices.** Amazon identifies digital advertising, digital content and electronic devices among its competitive markets (R7.7).
4. **[FACT] Regulation.** The filing identifies competition/antitrust, marketplace, advertising, privacy/data, consumer-protection, labor, tax, AI, communications and cloud-service rules. See R7.7; material proceedings are in R7.5.
5. **[DEDUCTED]** Marketplace remedies can affect both seller-service revenue and retail selection; privacy/ad rules can affect measurement and monetization; cloud remedies/procurement restrictions can affect AWS sales or bundling.
6. **[DEDUCTED]** Model litigation cash costs only when a sourced accrual, settlement or scenario exists. Do not convert unquantified claims into a point estimate.

## 12. Numbers the model must take

Values live only in the register. “Take” means preserve the source date, classification and reporting boundary.

| named input | take from | source / as-of | status |
|---|---|---|---|
| Segment revenue / operating expense / operating income | R2 tables | S1/S2/S3/S4; through 2026-06-30 | obtained; TTM opex deduced |
| Segment operating margins | R2.2 and named R2 inputs | S3/S4 Q2 2026 | deduced |
| Product/service sales groups | R3 tables | S1/S2/S3/S4; through 2026-06-30 | obtained; TTM mostly deduced |
| Paid-unit growth / seller unit mix | R3.2 | S4 Q2 2026 | obtained |
| First-party units/ASP; marketplace GMV/take rate | R8.1 | through 2026-09-29 | **not obtained** |
| Prime members / ARPU / churn / benefit cost | R3.7, R8.3 | through 2026-09-29 | **not obtained** |
| Advertising impressions/pricing/margin | R8.4 | through 2026-09-29 | **not obtained** |
| AWS usage direction and RPO | R3.3–R3.4 | S3 2026-06-30 | obtained; annual conversion **not obtained** |
| AWS workload units/utilization/customer concentration/gross margin | R5.3, R8.5 | through 2026-09-29 | **not obtained** |
| Segment PPE / additions / D&A | R4.3, R6.6 | S3 2026-06-30 | obtained; additions not cash capex |
| Fulfillment/AWS footprint | R4.1–R4.4 | S1 2025-12-31; S6 accessed 2026-09-29 | obtained at disclosed aggregation |
| Facility throughput/utilization; AWS installed MW/chips | R4.5, R8.7 | through 2026-09-29 | **not obtained** |
| Country revenue / FX exposure | R5 | S1 FY2025; S3 Q2 2026 | obtained |
| Cash, investments, working capital | R6.1 | S3 2026-06-30 | obtained |
| Debt / leases / commitments | R6.2–R6.3, R7.3 | S3 2026-06-30 and subsequent event | obtained |
| Outstanding / diluted shares | R6.4 | S3/S4 Q2 2026 and 2026-07-22 | obtained |
| OCF / cash capex / FCF | R6 table | S1/S3/S4; through 2026-06-30 | obtained / deduced as labeled |
| 2026 capex outlook | R6.5 | S5 2026-02-05; checked against S3/S4 | obtained; no revised Q2 figure found |
| Strategic investments / non-operating marks | R7.1–R7.2 | S3 2026-06-30 and subsequent event | obtained |
| Product-line profit; complete segment cash flow | R8.2, R8.6 | through 2026-09-29 | **not obtained** |
