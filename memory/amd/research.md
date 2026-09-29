# AMD initiation research file

GF-AMD-1 · as of 2026-09-29 · name id `amd`

Read numeric facts in [`register.md`](register.md); this file owns driver structure and interpretation. No material number is intentionally duplicated here. This is research scaffolding, not a thesis, valuation or recommendation.

## 1. Business overview

1. **[FACT] Portfolio.** AMD is a fabless semiconductor designer spanning server and client CPUs, AI/data-center and gaming GPUs, networking devices, FPGAs/adaptive SoCs, embedded processors, semi-custom SoCs, software and limited development/IP licensing. See R1.3–R1.5.
2. **[FACT] Customers.** The paying nodes include hyperscalers, OEMs, ODMs, system integrators, distributors, add-in-board partners, console makers and embedded-equipment manufacturers. The economic customer and billing-location customer can differ when an ODM or distributor sits between AMD and end deployment. See R1.6 and R8.3.
3. **[FACT] Route to revenue.** Standard products generally recognize revenue on shipment; qualifying custom products recognize over production; development and IP licensing follow performance-obligation transfer. This matters most for semi-custom cadence and for interpreting RPO. See R1.7 and R3.5.
4. **[DEDUCTED] Economic perimeter.** AMD monetizes architecture, silicon design, chiplets/advanced packaging, software enablement and customer co-design while foundries and packaging partners own most physical production. ZT design capabilities move AMD further into rack/system architecture, but the manufacturing operation was divested. See R1.8 and R4.

## 2. Segment map and historical financial skeleton

1. **[FACT] Current reporting.** AMD currently reports Data Center, Client and Gaming, and Embedded. Client and Gaming are separately disclosed revenue businesses inside one reportable segment; their standalone operating income is not reported. Prior periods were retrospectively recast when the combination took effect. See R1.1.
2. **[FACT] Profit reporting.** AMD reports segment revenue, combined segment cost of sales plus operating expenses, and segment operating income. It does not report segment gross profit. All Other removes major unallocated acquisition-intangible amortization, SBC and acquisition-related items from segment results. See R1.2 and R2.3.
3. **[DEDUCTED] Modeling consequence.** A model can preserve four revenue drivers—Data Center, Client, Gaming and Embedded—but must not present Client or Gaming standalone EBIT as reported. Build consolidated gross profit independently from product/mix assumptions, then reconcile to the three filed segment operating-income measures and All Other.

### Historical financial skeleton

**[FACT]** Values are stored once in R2:

| model block | periods | register pointer | disclosure status |
|---|---|---|---|
| Data Center revenue / operating income | FY2023–FY2025; Q1, Q2 and 1H 2026 | R2 annual/latest tables | obtained |
| Client revenue | FY2023–FY2025; Q1, Q2 and 1H 2026 | R2 annual/latest tables | obtained |
| Gaming revenue | FY2023–FY2025; Q1, Q2 and 1H 2026 | R2 annual/latest tables | obtained |
| Client and Gaming operating income | same periods | R2 annual/latest tables | obtained only on combined reportable-segment basis |
| Embedded revenue / operating income | same periods | R2 annual/latest tables | obtained |
| Segment gross profit / capex / balance sheet | same periods | R9.5 | **not obtained** |
| Consolidated revenue through EPS | FY2023–FY2025; Q1, Q2 and 1H 2026 | R2 consolidated table | obtained |

## 3. Segment driver trees

### 3.1 Data Center

1. **[DEDUCTED] Revenue bridge.** Model server CPUs, Instinct accelerators/rack content, Pensando/Solarflare networking, and adaptive/FPGAs separately: shipment units or deployed systems × realized AMD content per unit, plus development/IP/service revenue. Product-level units and ASPs are not obtained (R9.1).
2. **[FACT] Units and ASPs.** Absolute EPYC, Instinct, networking and adaptive-product units and realized ASPs are **not obtained**; announced deployment power is not a unit disclosure. See R9.1 and R9.10.
3. **[DEDUCTED] Mix.** CPU versus accelerator versus networking/adaptive mix; component versus rack content; training versus inference; current versus prior generation; and customer/geographic mix can move both revenue and margin.
4. **[FACT] CPU drivers.** EPYC demand depends on hyperscaler and enterprise platform qualification, server refresh, cloud instances, workload performance, performance per watt, total cost of ownership and Intel/Arm alternatives. Current filed demand direction is in R2.2 and product/customer scope in R1.3/R1.6.
5. **[FACT] Accelerator drivers.** Instinct demand depends on customer deployment schedules, model-training/inference demand, rack power and data-center readiness, memory/advanced packaging, ROCm/framework maturity, networking and competitive performance/economics versus Nvidia and custom accelerators. Export controls can strand inventory or constrain reachable demand. See R2.1, R3.8–R3.10, R4.5 and R8.4.
6. **[DEDUCTED] AI revenue bridge.** Available accelerator/rack supply × shippable customer deployments × AMD silicon/system content × realized price, adjusted for deployment timing, acceptance, export licenses, mix and customer incentives. Gigawatts announced by customers are not revenue, backlog, shipment units or recognized capacity.
7. **[FACT] Backlog/visibility.** OpenAI and Meta filings provide deployment/purchase milestones; Anthropic is an announced collaboration. Filed RPO captures only a narrow contract subset and excludes shorter-duration obligations. Use R3.5 and R3.8–R3.10; do not convert headline gigawatts into revenue without explicit `[VIEW]` inputs.
8. **[DEDUCTED] Margin bridge.** Product mix and realized price less wafers, HBM/memory, substrates, advanced packaging/test, boards/rack content, freight, warranty and customer-support cost; then subtract allocated R&D and go-to-market expense to reach reported segment operating income. The filed segment margin history is in R2.
9. **[FACT] Customer concentration.** AMD's consolidated annual revenue did not cross the named customer threshold in the latest two fiscal years, but filings still warn that a small number of customers account for a substantial share of business and receivables. Deployment agreements can increase economic concentration before annual disclosure identifies it; a Data Center-specific percentage is **not obtained**. See R3.7–R3.10 and R9.1.
10. **[FACT] Competitive position.** The relevant sets are Nvidia in AI/data-center GPUs and software, Intel and Arm alternatives in server CPUs, Altera in adaptive products, customer-designed accelerators, and smaller specialist silicon firms. AMD identifies software completeness, availability, energy efficiency and TCO alongside silicon performance. See R8.1–R8.2.
11. **[DEDUCTED] Break conditions to measure, not a thesis.** Product or software delays, weak qualification/conversion, insufficient foundry/packaging/memory supply, lower realized content, customer data-center delays, export restrictions, or opex scaling faster than gross profit would weaken the segment bridge.

### 3.2 Client

1. **[DEDUCTED] Revenue bridge.** Ryzen processor units × realized processor ASP + chipset and ancillary revenue, adjusted for OEM/distributor rebates, price protection, returns and channel inventory.
2. **[FACT] Volume drivers.** PC sell-through, OEM design wins, commercial refresh, notebook/desktop mix, distributor inventory, platform availability and AI-PC adoption. Filed period-over-period unit changes are in R3.1–R3.2; absolute units are not obtained.
3. **[FACT] ASP/mix drivers.** Desktop versus mobile, premium versus mainstream, consumer versus commercial, Ryzen AI/PRO/Threadripper mix, product transitions and competitive pricing against Intel and Arm-based PCs. Filed ASP direction is in R3.1–R3.2; dollar ASP is not obtained.
4. **[DEDUCTED] Gross-profit bridge.** Units × `(realized ASP − wafer/package/test and other unit cost)` less channel provisions and product-transition reserves. Client gross profit is not reported separately (R9.2).
5. **[FACT] Visibility.** Customer forecasts usually lack minimum purchase commitments and standard-product orders retain cancellation flexibility. Treat OEM design wins as opportunity, not backlog. See R3.6.
6. **[FACT] Customer concentration.** AMD does not disclose a current Client customer share; one Client and Gaming customer crossed the consolidated annual threshold in an older period. See R3.7 and R9.2.
7. **[FACT] Competitive position.** Intel is the named primary x86 competitor; Arm platforms are an architectural alternative. Integrated graphics can displace discrete GPUs at some price points. See R8.1.

### 3.3 Gaming

1. **[DEDUCTED] Revenue bridge.** Radeon discrete-GPU units × realized ASP + semi-custom SoC units × AMD content/price + development/NRE revenue recognized under contract accounting.
2. **[FACT] Units and ASPs.** Absolute Radeon and semi-custom units, dollar ASPs and AMD content per console are **not obtained**. See R9.3.
3. **[FACT] Semi-custom drivers.** Console installed-base cycle, Sony/Microsoft and other customer sell-through, content per device, production ramps, customer inventory and new design wins. Revenue follows customers' products and AMD does not control their marketing. See R1.4 and R3.3.
4. **[FACT] Discrete-GPU drivers.** Radeon product timing, gaming/creator demand, board-partner inventory, performance per dollar and software/driver quality matter. See R8.1–R8.2.
5. **[DEDUCTED] Mix/margin bridge.** Semi-custom versus discrete mix, current versus prior-generation mix and launch costs can move economics even if aggregate Gaming revenue rises. Standalone Gaming operating income and gross margin are not obtained (R9.3).
6. **[FACT] Backlog/visibility.** Custom-product orders may be non-cancellable and recognized over time, while channel graphics demand has shorter visibility and price-protection exposure. AMD does not disclose the required bridge by product (R1.7, R9.3).
7. **[FACT] Customer concentration.** Console and semi-custom economics are structurally customer-linked, but current Gaming revenue by customer is **not obtained**. See R1.4, R3.7 and R9.3.
8. **[FACT] Competitive position.** Nvidia is the named leader and primary discrete-GPU competitor; Intel also competes, while integrated graphics can substitute at some price points. See R8.1–R8.2.

### 3.4 Embedded

1. **[DEDUCTED] Revenue bridge.** Units × realized ASP across embedded CPUs/APUs, FPGAs, adaptive SoCs and SOMs, plus tools/development/IP where applicable.
2. **[FACT] Volume drivers.** Design wins, customer qualification and production ramps across industrial, aerospace/defense, automotive, communications, healthcare, test, broadcast and edge/data-center uses. Long product lifecycles can support durability, while customer inventory digestion can delay orders. See R1.5 and R3.4.
3. **[DEDUCTED] ASP/mix drivers.** FPGA/adaptive content, application complexity, high-end versus broad-market mix and end-market mix. Absolute units, ASP and end-market revenue are not obtained (R9.4).
4. **[DEDUCTED] Margin bridge.** Realized product mix and price less foundry/packaging/test and support cost, then allocated R&D and selling expense. Reported segment operating margin is available in R2; product-level gross margin is not.
5. **[FACT] Visibility.** AMD discloses direction across end markets but not Embedded backlog, book-to-bill or design-win conversion. Do not infer a quantified recovery from qualitative demand language (R3.4, R9.4).
6. **[FACT] Customer concentration.** Embedded customer and end-market concentration are **not obtained** beyond the company-level disclosure in R3.7. See R9.4.
7. **[FACT] Competitive position.** The set spans Altera, Lattice, Microsemi, ASIC/ASSP suppliers and Intel in embedded CPUs. Programmability, power, reliability, tools and time to market are key dimensions. See R8.1–R8.2.

### 3.5 Shared margin, opex and accounting

1. **[FACT]** Segment operating income includes allocated materials, external manufacturing, labor and marketing/advertising, while major SBC and acquired-intangible amortization sit in All Other. See R1.2 and R2.3.
2. **[DEDUCTED]** Reported segment operating leverage can therefore diverge from consolidated GAAP operating leverage. A model must carry All Other explicitly and not treat segment operating income as fully burdened GAAP EBIT.
3. **[DEDUCTED]** Company gross margin is primarily a mix/price/unit-cost outcome; reported-segment operating margin then adds allocation choices and segment opex. Segment gross-profit assumptions cannot be validated directly against a filed segment gross-profit line.

## 4. Cost structure and foundry/packaging exposure

1. **[FACT] Foundry map.** TSMC supplies leading-node microprocessor/GPU wafers; GlobalFoundries supplies older-node requirements under a capacity/pricing arrangement through the current year; TSMC, UMC and Samsung also support programmable logic. See R4.1.
2. **[FACT] Packaging map.** AMD outsources assembly, test, mark and packaging and says the Tongfu JVs provide the majority of those services; SPIL and KYEC are also named. Related-party purchases and payables are in R4.3.
3. **[DEDUCTED] Unit cost tree.** Wafer price/yield + memory/HBM + substrate/interposer + advanced package/test + board/system content + freight/warranty, divided by good units. Node transitions and chiplet/package complexity can move cost before pricing and mix absorb it.
4. **[FACT] Commitments.** The aggregate contractual schedule includes wafers, substrates, components, cloud compute, software and technology licenses; it is not a foundry-only purchase commitment. See R4.4.
5. **[DEDUCTED] Exposure.** AMD avoids fab ownership but concentrates execution in external leading-edge wafer and packaging capacity. TSMC, Taiwan, memory, substrate, ATMP and yield risks therefore affect units, working capital and margin simultaneously (R4.1–R4.5).

## 5. Capex, R&D and opex cadence

1. **[FACT] R&D.** The latest annual and interim expense cadence and management's AI-headcount attribution are in R5.1–R5.2. The work spans CPUs, GPUs, adaptive products, networking, software, chiplets, packaging and rack/system design.
2. **[DEDUCTED] R&D driver tree.** Engineering headcount and compensation/SBC + EDA/IP and prototype tape-outs + software/ROCm + systems/lab/compute expense + acquired-team integration. Roadmap breadth and annual accelerator cadence raise the fixed-cost base before related revenue.
3. **[FACT] MG&A.** The latest cadence and stated go-to-market driver are in R5.1–R5.2. Customer enablement, field engineering and system-level selling should be tracked with, but not assumed proportional to, Data Center revenue.
4. **[FACT] Capex.** AMD's reported PP&E purchases and construction-in-progress are in R5.3–R5.4. As a fabless company, AMD capex does not capture supplier wafer, packaging or memory capacity investment; purchase commitments and prepayments carry part of that economic exposure.
5. **[DEDUCTED] Cash-investment frame.** Track PP&E, supplier prepayments/working capital, cloud capacity, leases/guarantees, strategic investments and acquisitions separately. Capex alone understates the resources committed to the AI platform build-out. See R4.4 and R6.6–R6.7.

## 6. Balance sheet, FCF and capital return

1. **[FACT] Liquidity and debt.** Cash, short-term investments, receivables, inventory, payables and debt are in R6.1.
2. **[FACT] Cash conversion.** OCF, capex and FCF for the latest quarter/half and the deduced annual comparator are in R6.2–R6.3. Preserve AMD's continuing-operations FCF definition.
3. **[DEDUCTED] Working-capital watch.** Inventory and prepayments rise ahead of advanced-node and AI ramps, while accounts payable timing can temporarily support OCF. Compare cash conversion with shipment and deployment timing rather than treating one period's payable build as recurring.
4. **[FACT] Capital return.** Repurchases and remaining authority are in R6.4. The program is discretionary and should be evaluated against SBC issuance, acquisitions, strategic investments and deployment-related commitments.
5. **[FACT] Dilution/commitments.** Share counts and customer warrants are in R6.5; lease guarantees and committed leases are in R6.6. Unvested warrant maxima are not current diluted shares but are material scenario inputs if milestones become probable.

## 7. Recent print and guidance

1. **[FACT] Q1.** GAAP/non-GAAP results and the Q2 guide are stored in R7.1.
2. **[FACT] Q2.** GAAP/non-GAAP results are stored in R7.2; the segment bridge is in R2's latest table and R2.2.
3. **[DEDUCTED] Guide comparison.** Q2 revenue finished above the prior range; the exact comparison lives in R7.3. This establishes execution against that quarter's top-line guide, not future conversion or margin durability.
4. **[FACT] Current guide.** Q3 revenue, non-GAAP gross margin, opex, below-the-line, tax and share-count assumptions are stored in R7.4. AMD did not provide the full-year or segment guide listed in R9.7.
5. **[FACT] Management frame.** AMD expects second-half Data Center acceleration tied to EPYC, Instinct and Helios, but did not quantify segment revenue. See R7.5.

## 8. Node map

| node / flow | who pays whom | where value sits | what breaks it |
|---|---|---|---|
| Hyperscaler / AI lab → AMD **[FACT]** | accelerator, CPU, networking and rack-design content; sometimes milestone-linked deployments | silicon architecture, memory/package integration, ROCm, full-stack/rack co-design | customer capex/power delays, weak software, competitive systems, export controls, concentration (R1.3, R1.6, R3.8–R3.10) |
| Enterprise / cloud customer → OEM/ODM → AMD **[DEDUCTED]** | server/platform price flows through OEM/ODM procurement | EPYC performance/TCO, qualification, platform breadth | Intel/Arm competition, slow refresh, failed qualification, channel inventory |
| PC buyer → OEM/channel → AMD **[DEDUCTED]** | Ryzen/APU/chipset content | x86 performance, battery life, NPU/AI capability, OEM designs | PC cycle, price pressure, Intel/Arm, channel correction |
| Gamer / console buyer → console maker or AIB → AMD **[FACT]** | semi-custom SoC or Radeon content | custom design, graphics architecture, software and installed platforms | console maturity, Nvidia competition, integrated graphics, inventory (R1.4, R3.3) |
| Industrial/auto/communications customer → AMD/channel **[FACT]** | embedded CPU, FPGA, adaptive SoC or SOM | programmability, long qualification, tools, application fit | inventory digestion, design loss, ASIC/ASSP substitution, end-market cycles (R1.5, R3.4) |
| AMD → TSMC/GF/other foundries **[FACT]** | wafer purchases and capacity commitments | process technology, yield and capacity; AMD architecture/chiplets | node/yield delay, allocation, geopolitics, power/water event (R4.1, R4.4–R4.5) |
| AMD → ATMP/memory/substrate partners **[FACT]** | packaging, test, HBM/memory and materials | advanced package integration and scarce supply | memory/package constraints, cost inflation, quality/yield failure (R4.2–R4.5) |
| AMD → software/cloud/EDA ecosystem **[FACT]** | licenses, cloud capacity, engineering and ecosystem investment | developer adoption, ROCm/framework support, design productivity | ecosystem gaps, commitment under-use, proprietary-stack lock-in (R4.4, R5.1–R5.2) |
| AMD → customer via warrant/guarantee **[FACT]** | potential equity dilution and commercial support tied to deployment | alignment and deployment scale | milestones fail, economics disappoint, dilution or guarantee obligation rises (R3.8–R3.9, R6.5–R6.6) |

**[DEDUCTED] Value concentration.** Observable value is currently reported in product revenue and segment operating income. Announced deployment scale becomes economically measurable only when shipment timing, AMD content, realized price, margin and cash terms are disclosed or explicitly modeled as `[VIEW]`.

## 9. Explicit numbered not-obtained list

1. **[FACT] Data Center product economics — not obtained.** Scope and boundaries: R9.1.
2. **[FACT] Client absolute units, dollar ASP and product economics — not obtained.** Scope: R9.2.
3. **[FACT] Gaming product split and standalone profit — not obtained.** Scope: R9.3.
4. **[FACT] Embedded end-market bridge, backlog and product economics — not obtained.** Scope: R9.4.
5. **[FACT] Segment gross profit, capital and balance sheets — not obtained.** Scope: R9.5.
6. **[FACT] Foundry/node/package volume, price, allocation and yield — not obtained.** Scope: R9.6.
7. **[FACT] Full-year company/segment guidance — not obtained.** Scope: R9.7.
8. **[FACT] Official written recent call transcripts — not obtained.** Scope: R9.8.
9. **[FACT] Current company-compiled consensus and market-implied segment values — not obtained.** Scope: R9.9 and [`consensus.md`](consensus.md).
10. **[FACT] Contracted dollars and economics for headline AI deployments — not obtained.** Scope: R9.10.
