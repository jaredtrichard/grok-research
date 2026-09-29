# NVIDIA initiation research file

GF-NVDA-1 · as of 2026-09-29 · name id `nvda`

Read numeric facts in [`register.md`](register.md); this file owns driver structure and interpretation. No fact is intentionally duplicated here. It contains no rating, thesis or price target.

## 1. Business and reported segments

1. **[FACT] Reportable segments.** NVIDIA reports two segments: Compute & Networking and Graphics. Compute & Networking includes Data Center compute/networking, AI software and Automotive; Graphics includes GeForce gaming/PC GPUs and enterprise-workstation graphics. See R1.1.
2. **[FACT] Current market platforms.** The latest quarterly presentation is Data Center and Edge Computing, with Data Center split into Hyperscale and ACIE. These are market platforms, not reportable segments. See R1.2.
3. **[FACT] Taxonomy break.** Data Center compute/networking, Gaming, Professional Visualization, Automotive and OEM/Other remain available as FY2026 history, but NVIDIA stopped presenting those six lines in the latest quarter. Do not splice them into FY2027 without marking the missing split. See R1.3 and R9.1.
4. **[FACT] Full-stack scope.** The Data Center offer spans accelerators, CPUs, DPUs, NVLink, InfiniBand/Ethernet, rack-scale systems, software and services. CUDA is the common programming platform; paid software is not separately quantified. See R1.4 and R3.3.

## 2. Segment and market-platform driver trees

### 2.1 Data Center compute

1. **[DEDUCTED] Revenue bridge:** deployed systems/racks × accelerators per system × realized accelerator content, plus CPU/DPU/system content, software/support and services. Unit counts and ASPs are not obtained (R3.4/R9.2), so the model must begin with reported Data Center revenue rather than a fabricated unit bridge.
2. **[FACT] Demand pools:** Hyperscale and ACIE are the current disclosed customer groupings. ACIE includes AI clouds, industrial and enterprise demand; sovereign and AI-native demand are discussed inside this pool. See R1.2 and R2.
3. **[DEDUCTED] Mix drivers:** architecture generation; training versus inference; rack-scale systems versus modules; GPU/CPU/DPU content; memory capacity; liquid cooling; software/support; direct versus channel route; geography; and customer-specific terms.
4. **[DEDUCTED] Gross-profit bridge:** system revenue less wafers, HBM/other memory, advanced packaging, boards, assembly/test, networking, freight/tariffs, warranty and inventory provisions. Fixed-price/mix effects and supply charges can dominate an apparent semiconductor-ASP bridge; use R2.1 and R8.3.
5. **[FACT] Architecture and deployment constraints:** Blackwell remained the majority of shipments, Rubin had begun production shipments, and supply, land, power, shell, cooling and customer capital could gate deployment. See R1.5 and R5.3.

### 2.2 Data Center networking

1. **[DEDUCTED] Revenue bridge:** AI-cluster nodes × network attach per node × ports/adapters/switches/cables × realized content, split among NVLink scale-up and InfiniBand/Ethernet scale-out.
2. **[FACT] Historical anchor:** exact Data Center networking revenue exists through FY2026; current-quarter absolute revenue does not. Management supplied current growth direction only. See R3.1–R3.2 and R9.1.
3. **[DEDUCTED] Mix/attach drivers:** rack architecture, cluster size, NVLink fabric content, InfiniBand versus Spectrum-X Ethernet, optical/copper content, switch generations and customer-built networking.
4. **[DEDUCTED] Failure modes:** customers unbundle the stack, choose lower-cost Ethernet/custom fabrics, delay cluster buildouts, or cannot source optics, switches, packaging, memory, power or cooling.

### 2.3 CUDA, enterprise software and services

1. **[FACT] Products:** CUDA/CUDA-X, AI Enterprise, vGPU, APIs/SDKs, models and domain stacks such as DRIVE and Omniverse support hardware adoption. The developer count is obtained; standalone economics are not (R3.3/R9.3).
2. **[DEDUCTED] Revenue bridge:** paid seats/instances × price × term, plus support and development arrangements. Do not infer paid seats from total developers.
3. **[DEDUCTED] Economic role:** software can increase hardware utilization, shorten deployment and raise switching friction even when its standalone revenue is not disclosed. That mechanism must not be converted into an invented software margin.
4. **[DEDUCTED] Watchpoint:** framework portability, open standards, custom accelerators and competitor software maturity can reduce CUDA's workload lock-in without immediately reducing installed hardware.

### 2.4 Edge Computing and legacy end markets

1. **[FACT] Current aggregate.** Edge Computing is the only current non-Data-Center market-platform line. The latest commentary ties it to Blackwell workstations and consumer PCs; Gaming, Professional Visualization, Automotive and OEM/Other are not separately quantified in FY2027. See R2.3 and R9.1.
2. **[DEDUCTED] Gaming bridge:** GeForce desktop/laptop GPU units × realized board/GPU content, plus console SoCs and cloud gaming. Drivers are installed-base upgrade cadence, game releases, RTX/DLSS adoption, channel inventory, memory/system prices and crypto-independent demand.
3. **[DEDUCTED] Professional Visualization bridge:** workstation units × GPU/system content, plus vGPU/software; drivers are design/content workloads, enterprise refresh, AI workstations and channel mix.
4. **[DEDUCTED] Automotive/robotics bridge:** design-win production units × SoC/system content, plus development, software and support. Design-win announcements are not revenue, and production timing follows OEM programs.
5. **[DEDUCTED] OEM/other bridge:** OEM/embedded volume × realized content; retain only as historical disclosure until NVIDIA restores a current split.

### 2.5 Corporate operating items

1. **[DEDUCTED] R&D:** architecture and chip design, systems/networking, software/models, compute infrastructure, compensation/SBC and product validation.
2. **[DEDUCTED] SG&A:** field sales, developer/partner support, corporate functions, legal/regulatory and compensation/SBC.
3. **[FACT]** Consolidated R&D, SG&A and SBC are disclosed. Segment operating income is disclosed on NVIDIA's CODM basis, but functional opex by segment is not (R2 and R9.6).
4. **[DEDUCTED] Inventory/warranty:** rapid architecture transitions, export controls, yield and demand forecast error can create provisions; provision releases can also lift margin. Use filed charges rather than normalizing silently.

## 3. Historical financial skeleton

| model block | periods | register pointer | disclosure status |
|---|---|---|---|
| Company revenue through net income | FY2024–FY2026; Q2/1H FY2027 | R2 company table | obtained |
| Compute & Networking / Graphics revenue and operating income | FY2024–FY2026; Q2/1H FY2027 | R2 segment table | obtained |
| Data Center / Hyperscale / ACIE / Edge Computing | Q2/1H FY2026 recast; Q2/1H FY2027 | R2 current-platform table | obtained |
| Data Center compute/networking; Gaming; Pro Viz; Automotive; OEM/Other | FY2024–FY2026 | R3 annual table | obtained through FY2026 only |
| Current legacy-market split | FY2027 | R9.1 | **not obtained** |
| Segment gross profit, assets and capex | all periods | R9.6 | **not obtained** |

## 4. Units, ASP and mix discipline

1. **[FACT]** Units and ASP are not disclosed for GPUs, CPUs, DPUs, rack systems, networking, HBM or the legacy end markets (R3.4/R9.2).
2. **[DEDUCTED]** Revenue divided by an external shipment estimate is not a company ASP and does not isolate system, networking, software, support or customer-program effects.
3. **[FACT]** Current exact networking dollars are not disclosed; use FY2026 history and current growth commentary separately (R3.1–R3.2).
4. **[DEDUCTED]** Keep architecture mix explicit: Hopper, Blackwell/Blackwell Ultra and Rubin have different system content, memory, networking and cost structures. A single GPU-equivalent unit risks hiding the full-stack shift.
5. **[FACT]** Backlog, RPO, utilization, channel inventory and architecture-specific orders are not obtained (R9.4).

## 5. Geography, foundry, packaging and capacity

1. **[FACT] Geography.** Reported geography is direct-customer headquarters, not end demand. Use R4 and retain the Taiwan attribution caveat in R4.1.
2. **[FACT] Customer concentration.** Revenue and receivables are concentrated, while customer identities and end-user purchases are not disclosed (R4.2–R4.3/R9.5).
3. **[FACT] Manufacturing chain.** TSMC/Samsung fabricate wafers; SK hynix/Micron/Samsung supply memory; CoWoS is used for packaging; Hon Hai/Wistron/Fabrinet are named downstream partners. See R5.1.
4. **[FACT] Capacity commitments.** Supply, cloud, lease, investment and capex commitments are in R5.2/R5.4. Commitments are not revenue, backlog, expense or installed capacity.
5. **[FACT] Missing capacity data.** Foundry share, wafer starts, node mix, CoWoS capacity, HBM content/pricing, yield and utilization are not obtained (R5.6).
6. **[DEDUCTED] Constraint order:** wafer/process capacity → HBM and other components → advanced packaging/yield → board/rack integration → networking → customer land/power/cooling → financing and deployment. A break at any node can defer NVIDIA revenue.

## 6. Balance sheet and cash-flow inputs

1. **[FACT] Liquidity/working capital/debt.** Use R6.1; keep marketable equity securities separate from cash and debt securities.
2. **[FACT] Cash conversion.** Use R6.2–R6.3 for operating cash flow, capex/intangibles, D&A, SBC and company-defined free cash flow.
3. **[FACT] Shares.** Use R6.4 for diluted weighted-average and outstanding shares.
4. **[FACT] Contract/current liabilities.** Deferred revenue, customer advances, warranty and excess-purchase obligations are in R6.5.
5. **[DEDUCTED] Working-capital watch:** extended customer terms, large system deliveries, inventory builds and advance supply commitments can make cash conversion diverge from revenue and operating income.
6. **[FACT] Ecosystem exposure.** Guarantees and other long-dated commitments belong in a separate risk schedule; do not add maximum exposure directly to debt or capex. See R5.4–R5.5.

## 7. Node map

| node / flow | who pays whom | where value sits | what breaks it |
|---|---|---|---|
| Hyperscaler/CSP → NVIDIA or channel **[FACT]** | direct purchases or purchases through OEMs, ODMs, integrators and distributors | full-stack performance, deployment speed, common architecture and CUDA ecosystem | custom ASICs, AMD/other accelerators, capex/power limits, customer concentration, price pressure |
| AI cloud / model maker / enterprise → NVIDIA ecosystem **[FACT]** | infrastructure purchase, often through partners; some arrangements include NVIDIA cloud commitments or guarantees | access to complete systems and deployable capacity | weak tenant demand, financing/default risk, lower utilization/pricing, NVIDIA purchase obligations |
| OEM/ODM/system integrator → NVIDIA **[FACT]** | buys chips/modules/systems for resale or integration | integration, credit and route to end customer | cancellation, working-capital limits, integration delays, customer insourcing |
| NVIDIA → TSMC/Samsung **[FACT]** | wafer fabrication and capacity commitments | advanced process execution and scarce capacity | yield/node delay, geographic disruption, competing demand |
| NVIDIA → SK hynix/Micron/Samsung **[FACT]** | HBM/memory purchases and commitments | bandwidth/capacity required by AI systems | scarcity, price inflation, qualification or yield failure |
| NVIDIA → packaging/assembly partners **[FACT]** | CoWoS and downstream assembly/test/packaging | turning dies, memory and networking into shippable systems | package capacity/yield, component mismatch, logistics |
| NVIDIA → networking/optics ecosystem **[DEDUCTED]** | switches, adapters, cables/optics and integration inputs | NVLink plus InfiniBand/Ethernet attach expands content per cluster | Ethernet/custom-fabric substitution, optics/switch shortage, unbundling |
| Developer/enterprise → NVIDIA or cloud **[DEDUCTED]** | software/support license or cloud consumption; hardware may be indirect | CUDA libraries, models, tools and installed developer base | portability, open standards, competitor software, low paid conversion |
| Gamer/creator → board/OEM/cloud channel **[DEDUCTED]** | PC/workstation GPU, system or service purchase | RTX/DLSS and creator/workstation stack | slow refresh, channel inventory, memory/system prices, competitor performance/price |
| Auto/robotics OEM → NVIDIA/partner **[DEDUCTED]** | development platform, SoC/system, software and support | DRIVE/robotics hardware-software stack and design wins | delayed programs, OEM insourcing/custom SoCs, regulation and safety validation |

**[DEDUCTED] Value concentration.** Current reported economics are concentrated in Data Center and Compute & Networking. CUDA and networking can increase platform value, but standalone software economics and current networking dollars are not separately observable.

## 8. Competitive and regulatory frame

1. **[FACT] Accelerators/CPUs.** AMD, Intel and Huawei are named competitors; cloud customers including Alphabet/Google, Amazon and Microsoft design internal AI hardware/software. See R8.1.
2. **[FACT] Networking.** Named competitors include AMD, Arista, Broadcom, Cisco, HPE, Huawei, Intel, Lumentum and Marvell, plus internal cloud/system-vendor teams (R8.1).
3. **[DEDUCTED] Custom ASIC mechanism.** Custom accelerators can take workload-specific volume or cap merchant pricing; NVIDIA's counter is a fungible full-stack platform across models and workloads. The filings do not quantify share lost to custom silicon.
4. **[FACT] China/export controls.** Current H200 economics, charges and effective Data Center exclusion are in R8.3; Q3 guidance excludes China Data Center compute (R2.4).
5. **[FACT] Antitrust.** Multi-jurisdiction information requests and named French/China matters are in R8.4. No remedy or loss amount was obtained.
6. **[DEDUCTED] Regulatory transmission:** controls can remove addressable demand, strand inventory/purchase commitments, add tariffs/compliance, disrupt networking attach and accelerate non-U.S. alternatives.

## 9. Numbers the model must take

Values live only in the register. “Take” means link the assumption to the cited register row while preserving date and classification.

| named input | take from | source / as-of | status |
|---|---|---|---|
| Company P&L | R2 company table | S1 FY2024–FY2026; S2 Q2/1H FY2027 | obtained |
| Reportable-segment revenue / operating income | R2 segment table | S1/S2 | obtained |
| Current Data Center / Hyperscale / ACIE / Edge revenue | R2 current-platform table | S2 2026-07-26 | obtained |
| Historical compute/networking and legacy end markets | R3 annual table | S1 through FY2026 | obtained; not current taxonomy |
| Current compute vs networking and legacy-market split | R9.1 | through 2026-09-29 | **not obtained** |
| Units, ASP, HBM content, product cost/margin | R3.4, R9.2 | through 2026-09-29 | **not obtained** |
| Software/support economics | R3.3, R9.3 | through 2026-09-29 | developer count obtained; economics **not obtained** |
| Geography and customer concentration | R4 | S1/S2 | obtained with headquarters caveat |
| Foundry/memory/packaging chain | R5.1 | S1 FY2026 | named suppliers obtained |
| Supply/capacity commitments | R5.2, R5.4 | S2 2026-07-26 | obtained; not backlog/capacity |
| Foundry/CoWoS/HBM capacity and utilization | R5.6 | through 2026-09-29 | **not obtained** |
| Cash, securities, receivables, inventory, payables, debt | R6.1 | S2 2026-07-26 | obtained |
| OCF, capex/intangibles, D&A, SBC, FCF | R6.2–R6.3 | S2/S4 Q2/1H FY2027 | obtained |
| Diluted and outstanding shares | R6.4 | S2 | obtained |
| Deferred revenue, advances, warranty, purchase obligations | R6.5 | S2 2026-07-26 | obtained |
| Q3 FY2027 guide | R2.4 | S3 2026-08-26 | management guidance |
| Segment gross profit/assets/capex | R9.6 | through 2026-09-29 | **not obtained** |
| Related-party transaction amounts | R7.1 | through 2026-09-29 | **not obtained** |
