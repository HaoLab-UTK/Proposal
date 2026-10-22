# NSF ENG/CBET Energy, Water, and Resource Engineering (EWRE), NSF 26-518: Proposal Idea Screening for Hao Lab

Current as of 2026-10-22. "Why us" claims come only from `talent-pool/labs/hao-lab.md` (cited as [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)). Web pages were fetched with curl. NSF award data come from the NSF Award Search API (api.nsf.gov). Literature metadata (titles, authors, dates, abstracts) was checked with the arXiv API.

## Q0. EWRE scope, exclusions, award size, and review criteria (applies to all ideas)

### Takeaway
EWRE funds "foundational engineering research to manage energy, water, minerals, and material resources." That includes AI modeling, life cycle assessment, and closing energy and water loops. It sends Earth-system science to GEO and "buildings and cities" to CMMI. Proposals are accepted anytime. No award size is stated. Recent EWRE-coded standard grants have a median of about $390K. A data center energy-water decision problem fits if it is framed as resource-management engineering (design and operation under uncertainty), not as policy analysis or facility HVAC.

### Cited Findings
- Program synopsis: EWRE "supports fundamental research to advance energy, water, and resource management". It "supports studies on advanced manufacturing that increase the re-use of potentially valuable secondary products by closing energy, water and resource loops" and "studies on life cycle assessment, materials flow analysis, and AI modeling that incorporate novel metrics to advance the circular economy and bioeconomy." — [EWRE program page](https://www.nsf.gov/funding/opportunities/energy-water-resource-engineering)
- Exclusions: "Proposals with a main goal of understanding earth systems are more appropriate for the NSF Directorate for Geosciences. Proposals that focus on buildings and cities are a better fit for the NSF Division of Civil, Mechanical, and Manufacturing Innovation." — [EWRE program page](https://www.nsf.gov/funding/opportunities/energy-water-resource-engineering)
- Contact: EWRE Program Team, cbet-ewre@nsf.gov. Due date: "Full proposal accepted anytime." — [EWRE program page](https://www.nsf.gov/funding/opportunities/energy-water-resource-engineering)
- NSF 26-518 was posted August 17, 2026 and covers CPS, EBBS, EWRE, and TP. It anticipates 225-275 awards and $100,000,000 in total across all four CBET programs. Award type is a standard or continuing grant. Voluntary committed cost sharing is prohibited. There are no limits on proposals per PI or organization. — [NSF 26-518 solicitation](https://www.nsf.gov/funding/opportunities/engineering-eng-chemical-bioengineering-energy-transport/nsf26-518/solicitation)
- The solicitation states no average award size for EWRE. It says "Estimated program budget, number of awards and average award size/duration are subject to the availability of funds." It encourages "proposals requesting up to five years of support" and the use of Planning, RAPID, EAGER, and RAISE mechanisms for exploratory work. — [NSF 26-518](https://www.nsf.gov/funding/opportunities/engineering-eng-chemical-bioengineering-energy-transport/nsf26-518/solicitation)
- NSF priorities in the solicitation:
  - "work that creates opportunities for exceptional early-career investigators"
  - proposals that "leverage emerging technologies, including AI ... The use of these tools should be scientifically justified rather than incidental"
  - "strongly encourages proposals that forge novel connections across scientific domains"
  - Source: [NSF 26-518](https://www.nsf.gov/funding/opportunities/engineering-eng-chemical-bioengineering-energy-transport/nsf26-518/solicitation)
- Review: the standard NSB criteria (Intellectual Merit, Broader Impacts) apply. "In most cases, three or more external experts" review each proposal. "All else being equal after merit review, NSF may give preference to institutions with lower indirect cost rates" (EO 14332). Awards "may include termination for convenience provisions." — [NSF 26-518](https://www.nsf.gov/funding/opportunities/engineering-eng-chemical-bioengineering-energy-transport/nsf26-518/solicitation)
- Measures of success that proposals should advance: publications, data sets established or expanded, patents, new technologies or techniques, students and postdocs supported, and students trained in a critical area. — [NSF 26-518](https://www.nsf.gov/funding/opportunities/engineering-eng-chemical-bioengineering-energy-transport/nsf26-518/solicitation)
- "Proposers are strongly encouraged to email a one-page project summary to the Cognizant Program Director(s) before submitting a full proposal." — [NSF 26-518](https://www.nsf.gov/funding/opportunities/engineering-eng-chemical-bioengineering-energy-transport/nsf26-518/solicitation)
- Award size from my NSF API sample: I took 80 awards starting 2024 or later that carry the legacy fund code "EnvS-Environmental Sustainability", which still appears on EWRE awards in 2026. After excluding CAREER, EAGER, RAPID, and conference awards, 41 standard awards remain. Their median estimated total is about $393K, with an interquartile range of about $260K-$450K. — [NSF Award Search API](https://api.nsf.gov/services/v1/awards.json?keyword=optimization&fundProgramName=EnvS-Environmtl%20Sustainability&dateStart=01/01/2024)
- Examples of systems, optimization, and AI-modeling work funded under the EnvS/EWRE code, showing that decision-science framings are fundable there:
  - [2510781 GOALI: "Synergizing Advanced Optimization Models, Innovative Designs, and Life Cycle Assessment..." (Mahmoudi, Michigan State, $500K, 2025)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2510781)
  - [2618864 CAREER: "Forecast-informed Flexible Reservoir System Modeling Enabled by Artificial Intelligence..." (Yang, Michigan, $510K, 2026)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2618864)
  - [2429082 "Advancing Flood Analytics and Forecasting through Flood Computing and Engineered System (FloodEngine)" (Samadi, Clemson, $400K, 2025)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2429082)
  - [2515144/2515145 "CAS: Examining carbon emission implications of the impact of extreme weather conditions..." (Dixit/Wang, ~$450K total, 2025)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2515145)
- In my API search, no award coded EnvS/EWRE mentioned data centers. The data center water award found (2324915/2324916) sits in CISE "Sustainability in Computing" (DESC). — [NSF Award 2324916](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2324916)

### Inferences
- EWRE appears to have an open niche for data center energy-water work: computing-side water work is funded through CISE DESC, and no EWRE award was found. "Novel metrics" plus "AI modeling" plus "closing energy, water loops" is the language to mirror.
- A proposal centered on facility cooling hardware or HVAC risks being redirected. The "buildings" exclusion points to CMMI, and thermal hardware points to CBET Transport Phenomena / Thermal Transport Processes. The framing should be resource-system engineering: allocation, design, and operation of water and energy resources under hydro-climate uncertainty.
- A pure Earth-system or hydrologic-assessment framing risks redirection to GEO. Hydro-climate science should serve as the uncertainty model inside an engineering decision framework.
- The early-career emphasis favors Hao (Assistant Professor since 08/2026, per [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)). A 3-year, ~$350K-$450K single-institution budget matches the observed EWRE norm.

### Gaps
- The EWRE-specific typical award size and success rate are not published. My median comes from an API sample filtered by the legacy "EnvS" fund code and may include co-funded awards.
- I could not confirm whether new FY2027 EWRE awards use a new fund-program name. A search for "EWRE" as a program name returned nothing distinct.

## Q1. Idea 1: Joint energy-water optimization of AI data center cooling choice and siting under water stress and drought risk (robust optimization)

### Takeaway
Fundable and the strongest fit with Hao Lab. Prior work either optimizes siting deterministically with a static water-scarcity penalty, or assesses cooling trade-offs without optimizing them. No paper found combines siting and cooling co-design with drought and heatwave uncertainty and grid-attributed water. **Verdict: Pursue, as the lead idea after merging with Idea 4 (and Idea 3 as the operational layer).**

### Cited Findings
- Closest siting model: Vabson, Zater, Sajadi, Baker, Hodge, "Optimal County-Level Siting of Data Centers in the United States" (arXiv, 2026-01-22). It covers grid, telecom, climate, water use, and collocated generation. Its test cases focus on carbon-free generation collocation, and it finds "capital costs are the biggest driver." The abstract describes a deterministic "base model" with no robust or stochastic treatment of drought. — [arXiv 2601.16315](https://arxiv.org/abs/2601.16315)
- National scenario analysis: Xiao, You, et al., "Environmental impact and net-zero pathways for sustainable artificial intelligence servers in the USA," *Nature Sustainability* (Dec 2025).
  - Estimates the US AI-server water footprint at 731-1,125 million m3/yr for 2024-2030.
  - Best practices could cut the water footprint by up to 86%.
  - Server location drives "deep uncertainties."
  - This is scenario analysis, not site-level optimization.
  - Sources: [Nature Sustainability PDF (institutional repository)](https://re.public.polimi.it/retrieve/536a055b-d8ab-4b86-bd4d-88facfaaf2ae/s41893-025-01681-y.pdf); [Oxford ECI summary](https://www.eci.ox.ac.uk/news/ai-could-consume-10-us-electricity-2030-researchers-outline-path-sustainable-growth)
- Stress-adjusted assessment: Talukder, Rahim, Sen Gupta, Ren, Islam, "Balancing Bits and Drops" (arXiv, June 2026). It uses AWARE-US county-month water stress, includes off-site electricity water, and evaluates dry cooling and rainwater harvesting. This is an evaluation study, not a siting or design optimization under drought uncertainty. — [arXiv 2607.22617](https://arxiv.org/abs/2607.22617)
- Cooling trade-off evidence: an engrXiv preprint compares dry and adiabatic cooling at 12 U.S. sites under ASHRAE design conditions. Adiabatic cooling cut heat-rejection electricity by a median of ~30%, at 30-210 L of on-site water per kWh saved (preprint; date not confirmed). — [engrXiv 7795](https://engrxiv.org/preprint/view/7795)
- Practitioner reporting: water and wastewater capacity are now a gating factor in siting. — [Data Center Knowledge](https://www.datacenterknowledge.com/infrastructure/breaking-points-the-ai-boom-is-colliding-with-water-infrastructure)
- MSCI states that about one-quarter of current facilities, and nearly one-third of those under construction, are in regions expected to face greater water scarcity by 2050. This is an industry analysis, not peer reviewed. — [MSCI](https://www.msci.com/research-and-insights/blog-post/when-ai-meets-water-scarcity-data-centers-in-a-thirsty-world)
- Other work is MCDA or GIS screening, not robust optimization: a GeoAI and MCDA siting pipeline for the Guadalupe River Basin, Texas ([Research Square](https://www.researchsquare.com/article/rs-10595173/latest)), and an MIT J-WAFS groundwater network-planning project for India ([J-WAFS](https://jwafs.mit.edu/projects/2026/protecting-community-groundwater-security-network-based-planning-data-centers-water)).
- NSF: no NSF award found for robust or stochastic data center siting under water or drought uncertainty. The phrase "data center siting" returned 0 awards. — [NSF API query](https://api.nsf.gov/services/v1/awards.json?keyword=%22data%20center%20siting%22)
- Hao Lab assets:
  - Ongoing paper "Robust Data Center Siting under Interconnection-Queue Uncertainty" (Gao & Hao).
  - Ongoing paper "Siting Under Moving Rules: A Tariff- and Moratorium-Aware Optimization Model ... Tennessee Valley" (Jin & Hao).
  - PI expertise in flash drought, heatwaves, ET, remote sensing, and drought indices.
  - ISSE grant "The Local Footprint of AI Data Centers: Noise, Water, and Land-Market Tradeoffs in Tennessee" (PI, 2026).
  - USGS 104b TDEC decision-support grant on freshwater withdrawals and thermal discharges from data centers and SMRs (PI, 2027).
  - A submitted paper on water use tied to data center electricity demand.
  - Source: [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)

### Inferences
- **Gap:** existing siting models treat water as a static cost or penalty, or as an average scarcity factor. Existing water assessments do not optimize decisions. None treats cooling technology as a decision that moves water use between the site and the grid, under compound flash-drought and heatwave scenarios. Such scenarios hit cooling demand, water availability, and grid thermoelectric water intensity at the same time.
- **Novel engineering contribution:** a two-stage (or multistage) distributionally robust model.
  - Stage 1: site, capacity, cooling technology mix (evaporative, hybrid/adiabatic, dry, liquid), and water source.
  - Stage 2: hourly operational recourse (wet/dry switching, load curtailment or shifting).
  - Ambiguity sets are built from hydro-climate extremes (flash-drought onset, heatwave wet-bulb).
  - Decision-dependent uncertainty: the cooling choice changes grid dispatch and thus indirect water.
  - Outputs: new metrics such as drought-conditioned, stress-weighted total water, which aligns with EWRE's "novel metrics" language.
- **Why us:** Two pieces are uncommon together. One is the PI's flash-drought and heatwave science, the uncertainty model. The other is the lab's existing robust-siting models for the Tennessee Valley (Gao, Jin), the decision model. The ISSE and USGS 104b projects give data access and a stakeholder (TDEC) for broader impacts.
- **Risks:**
  - Reviewers may see it as "operations research applied to data centers" (CMMI) rather than water-resource engineering. Mitigate by putting water-resource engineering (withdrawal and consumption limits, basin depletion, thermal limits) at the core.
  - The Vabson/Hodge (NREL-affiliated authors) and Ren/Islam groups could extend into this space soon.
  - Facility-level cooling performance curves need credible engineering models. The lab profile lists no HVAC or thermal engineer, so consider a Co-PI (not named in hao-lab.md).

### Gaps
- I did not read full texts of Vabson et al. or Xiao et al. They may contain stochastic elements not visible in the abstracts.
- Scopus and Google Scholar were not queried directly. A targeted "chance-constrained" / "distributionally robust" + "data center" + "water" search should be done before writing.

## Q2. Idea 2: Thermal discharge and freshwater withdrawal management for data centers co-located with SMRs

### Takeaway
Real and under-studied. Published SMR-data center work covers economics and grid stability, not receiving-water thermal limits or withdrawals. The topic matches Hao Lab's USGS 104b TDEC grant directly. But the core physics (reactor heat rejection, river thermal plumes) is outside the lab's listed expertise. **Verdict: Revise.** Make it a module of the lead idea, or a second proposal with a nuclear or thermal Co-PI. Frame it as joint water-thermal resource management of the site under river-temperature extremes.

### Cited Findings
- Li, She, Zhang, "Techno-Economic Boundary Analysis of Small Modular Reactor Cogeneration for Hyperscale Data Center IT and Cooling Loads" (arXiv, Aug 2026). The study:
  - Co-optimizes reactor dispatch, steam extraction for absorption chillers, and grid exchange hourly for a 200 MWe ERCOT data center.
  - Finds nuclear configurations cost 49-62% more than grid supply at 2023 mid-range capital, with absorption cooling supplying 38% of annual cooling.
  - Does not cover water withdrawal or discharge in the abstract.
  - Source: [arXiv 2608.10999](https://arxiv.org/abs/2608.10999)
- Badakhshan et al. (Jie Zhang group, UT Dallas), "Dynamic Stability Assessment of Grid-Connected Data Centers Powered by Small Modular Reactors" (arXiv, Mar 2026). It covers PSSE grid stability and includes a coupled computational-thermal load model, but no water component. — [arXiv 2603.09110](https://arxiv.org/abs/2603.09110)
- The same group lists "The Role of Small Modular Reactors in Powering Data Centers for a Sustainable Digital Economy" as under review. — [UT Dallas publications](https://personal.utdallas.edu/~jiezhang/publications.html)
- ASCE: closed-loop cooling minimizes withdrawals, but blowdown still needs discharge permits. The heat sink may be a tower, hybrid system, dry array, or natural water body. — [ASCE Civil Engineering Source](https://www.asce.org/publications-and-news/civil-engineering-source/article/2025/12/17/demand-for-data-centers-soars-could-small-modular-reactors-meet-the-need)
- Tennessee Valley thermal-limit precedent: TVA derated or shut down Browns Ferry units when Tennessee River water exceeded a 90 F 24-hour average (2007, 2010, 2011). The 2010 event was reported to cost nearly $50M. — [APR 2007](https://www.apr.org/2007-08-17/heat-and-drought-shut-down-tva-reactor); [SEJ](https://www.em.sej.org/headlines/hot-river-forces-costly-cutback-tva); [CleanTechnica 2011](https://cleantechnica.com/2011/08/09/90-degree-river-shuts-tennessee-nuclear-plant-for-second-time/amp)
- NSF: the phrase "small modular reactors" returned 5 awards since 2018, none on data centers or water. — [NSF API query](https://api.nsf.gov/services/v1/awards.json?keyword=%22small%20modular%20reactors%22)
- Hao Lab asset: the USGS 104b PI grant "Decision Support for TDEC to Reduce Freshwater Withdrawals and Thermal Discharges from Data Centers and SMRs in Tennessee" (2027-01, 1 yr, $84K). Research direction 2.1 explicitly lists "data centers co-located with small modular reactors (SMRs)." — [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)

### Inferences
- **Gap:** no peer-reviewed or preprint work found that co-designs SMR plus data center heat rejection (once-through, tower, hybrid, dry, absorption-chiller use of steam) against receiving-water temperature limits and withdrawal caps under heatwave and low-flow scenarios. The TVA precedent shows the constraint is binding in this region. That makes a strong, regionally grounded engineering motivation.
- **Why us:** The lab already holds the only decision-support grant found that targets this exact combination (data centers + SMRs + thermal discharge + withdrawals, for TDEC). The PI's heatwave and drought expertise supplies the low-flow, high-temperature scenarios.
- **Risks:**
  - No river thermal-plume, reactor thermal-hydraulics, or heat-exchanger expertise is listed in hao-lab.md. Reviewers will expect it, so a Co-PI is needed. UT Knoxville has nuclear engineering, but that is not in hao-lab.md; verify.
  - No SMR is operating yet, so the work is design-stage, scenario-based.
  - NRC and NPDES permitting specifics were not verified (see Gaps).
  - It could drift into a "power plant cooling" topic better suited to CBET Thermal Transport.
  - The USGS 104b grant is only 1 year and $84K. The proposal must show NSF funds foundational methods beyond that deliverable, not duplicate it.

### Gaps
- Current TVA or TDEC NPDES thermal limits for specific Tennessee River and Clinch River reaches were not found. Planned SMR sites in Tennessee (e.g., TVA Clinch River) and any co-located data center plans were not verified in this research.

## Q3. Idea 3: Water-stress-aware scheduling of geo-distributed AI workloads

### Takeaway
Heavily occupied. The Ren/Islam groups have an NSF DESC award on user-interactive data center water management. In June 2026 they posted a stress-adjusted water framework that includes stress-aware workload scheduling. WaterWise, the equity-aware GLB work, and Attenni et al. cover carbon-water spatio-temporal shifting. It is also a computing-systems topic (CISE), not EWRE. **Verdict: Drop as a standalone EWRE idea.** Keep it only as the operational-recourse layer inside the lead idea.

### Cited Findings
- NSF DESC award, "Collaborative Research: DESC: Type I: A User-Interactive Approach to Water Management for Sustainable Data Centers: From Water Efficiency to Self-Sufficiency": Mohammad Islam (UT Arlington, #2324915, $299,957) and Shaolei Ren (UC Riverside, #2324916, $300,000), starting 2023-09-15, program Sustainability in Computing. Aims: user- and facility-level water accounting, user-interactive scheduling for water sustainability, and an online algorithm for water self-sufficiency. — [NSF 2324916](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2324916); [NSF 2324915](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2324915)
- Talukder, Rahim, Sen Gupta, Ren, Islam, "Balancing Bits and Drops: Stress-Adjusted Water Management for Data Centers" (arXiv, 2026-06). It uses AWARE-US county-month stress and off-site electricity water, and studies "workload scheduling policies that jointly optimize water and carbon efficiency." A search summary states up to 25% stress-adjusted reduction; that figure is not verified in the abstract. — [arXiv 2607.22617](https://arxiv.org/abs/2607.22617)
- Li, Yang, Wierman, Ren, "Towards Environmentally Equitable AI via Geographical Load Balancing" (ACM e-Energy 2024). Equity-aware GLB over carbon and water footprints across 10 data centers. — [arXiv 2307.05494](https://arxiv.org/abs/2307.05494); [DOI](https://dx.doi.org/10.1145/3632775.3661938)
- Li, Yang, Islam, Ren, "Making AI Less 'Thirsty'" (arXiv 2023; foundational AI water-footprint methodology, spatial-temporal water efficiency). — [arXiv 2304.03271](https://arxiv.org/abs/2304.03271)
- Jiang, Basu Roy, Kanakagiri, Tiwari, "WaterWise: Co-optimizing Carbon- and Water-Footprint..." (arXiv 2025). A job scheduler for geo-distributed data centers. — [arXiv 2501.17944](https://arxiv.org/abs/2501.17944)
- Attenni, Moawad, Bartolini, Thamsen, "Spatio-Temporal Shifting to Reduce Carbon, Water, and Land-Use Footprints of Cloud Workloads" (arXiv 2025). Reports up to ~50% water savings for FaaS. — [arXiv 2512.08725](https://arxiv.org/abs/2512.08725)
- Other NSF awards on the computing side: [2450515 DESC "Water- and Carbon-Aware Design of Chiplet-based Systems ... for AI in Datacenters" (Arora, ASU, $600K, 2025)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2450515); [2202126 CPS "Demand Response & Workload Management for Data Centers..." (UC Davis, 2021)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2202126)
- Hao Lab asset: Yifan Gao lists "geo-distributed AI workload scheduling" and "distributed computing, AI workload scheduling" as interests, but no publications or projects on it. — [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)

### Inferences
- The stress-weighted scheduling novelty has already been claimed, by the group that holds the NSF award. Hao Lab has an interest, not a track record, here, so "why us" is weak.
- The residual angle that only Hao Lab plausibly has is drought-forecast-informed scheduling: using flash-drought onset forecasts rather than static AWARE factors. That is incremental on its own, so use it inside Idea 1 as second-stage recourse.

### Gaps
- I did not verify the full text of 2607.22617 for whether it uses forecasts or dynamic drought indices. If it already does, the residual angle shrinks further.

## Q4. Idea 4: Integrated water-energy model of how cooling choices shift water use across the grid

### Takeaway
Pre-empted as an assessment model. Alston, Love, Haider (arXiv, Sept 2026) built exactly this: hourly dispatch, generator-level water, and subbasin depletion. Guidi and Dominici (June 2026) mapped both pathways for 472 US hyperscale sites. **Verdict: Drop as standalone.** Reuse the concept as the grid-water attribution submodel inside Idea 1. The new part would be making it decision-relevant and drought-conditioned for the TVA/SERC system.

### Cited Findings
- Alston, Love, Haider, "Data center cooling choices shift water impacts across the grid: An integrated water-energy model for sustainable data center development" (arXiv, 2026-09-21). The model links facility cooling and electricity demand with hourly economic dispatch, generator-level water consumption, and monthly subbasin depletion. It attributes indirect water to responding generators, not to the facility location. Michigan case study: air cooling halves total water consumption relative to evaporative cooling but raises indirect water consumption by one-third. — [arXiv 2609.25437](https://arxiv.org/abs/2609.25437)
- Guidi and Dominici, "The Hidden Water Geography of U.S. Hyperscale Data Centers in the AI Era" (arXiv, 2026-06). The study covers 472 facilities.
  - Total water: ~300 GL/yr (range 205-451).
  - Electricity-related water is about three-quarters of the total.
  - 3 of 24 balancing authorities account for 59% of electricity-related water.
  - Source: [arXiv 2607.02531](https://arxiv.org/abs/2607.02531)
- Bolaños-Zuñiga and Lamadrid, "Environmental and Economic Implications of AI Data Centers in the United States" (arXiv, Aug 2026). Impacts depend on marginal generation mixes, transmission, and the spatial-temporal distribution of demand. — [arXiv 2608.09882](https://arxiv.org/abs/2608.09882)
- Akinade, Amanambu, Frame, Ren, "AI Data Centers and the Water Use Feedback Loop" (arXiv, June 2026). A review that introduces a Water Consumption Impact index; community burden at ten US sites ranges from 0.2% to 134% of host capacity. — [arXiv 2606.21760](https://arxiv.org/abs/2606.21760)
- Hao Lab asset: a submitted paper on "water use tied to data-center electricity demand" (title and venue not given). — [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)

### Inferences
- The Alston et al. abstract describes a deterministic assessment over cooling configurations. It does not optimize siting or cooling, does not treat drought or heatwave uncertainty, and studies Michigan, not the Southeast or TVA. Remaining novelty for Hao Lab:
  - embedding generator-level attribution in an optimization (decision-dependent indirect water);
  - drought- and heatwave-conditioned thermoelectric water intensity and derating (see the TVA precedent in Q2);
  - the Tennessee Valley system.
  - These are improvements, not a new paradigm, so this is not a standalone proposal.
- Hao Lab's submitted paper may overlap with Alston et al. The proposal must cite both and state the difference clearly.

### Gaps
- I could not check whether Alston et al. is under journal review or has an NSF acknowledgment. The full text was not read.

## Q5. Idea 5: Data center waste heat and water reuse pathways in the Tennessee Valley

### Takeaway
As stated, it is weak for Hao Lab. Waste-heat reuse is a thermal-engineering and heat-pump topic with existing ORNL work and limited heating demand in this region, and the lab lists no thermal-engineering expertise. The water-reuse half is stronger and fits EWRE's "closing energy, water and resource loops" language. The Memphis (xAI) wastewater-reuse case makes it concrete in Tennessee. **Verdict: Revise.** Drop waste heat as the core and recast the idea as optimal design of reclaimed and alternative water-source networks for data center clusters under drought.

### Cited Findings
- ORNL case study: recovering waste heat from the Frontier supercomputer with high-temperature heat pumps for campus district heating. R1234ze(Z) and R600a were identified as the most promising refrigerants. — [ORNL Impact](https://impact.ornl.gov/en/publications/district-heating-utilizing-waste-heat-of-a-data-center-high-tempe/); [Energy and Buildings (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0378778824004432)
- Data center heat is low-grade and needs heat pumps and district networks. NYSERDA's February 2026 "DATA HEAT" report covers sector coupling of data centers with district heating. — [NYSERDA DATA HEAT](https://www.nyserda.ny.gov/-/media/Project/Nyserda/Files/Programs/Large-Scale-Thermal/DATA-HEAT---Sector-Coupling-Data-Centers-and-District-Energy.pdf); [ReImagine Appalachia, "Catching Heat" (Feb 2026)](https://reimagineappalachia.org/wp-content/uploads/2026/02/Catching-Heat_Using-Waste-Heat-Generated-from-Data-Centers.pdf)
- Memphis xAI water reuse:
  - Scope: an $80M, 13-acre wastewater recycling plant designed for 13 million gallons/day, meant to stop Colossus from drawing on the Memphis Aquifer.
  - Status as of April 2026: xAI is "prioritizing other projects," so construction is effectively paused.
  - Distance: Colossus 2 sits about 8.5 miles away, which complicates piping.
  - Nucor Steel declined to be an end user.
  - Sources: [WVLT, 2026-04-09](https://www.wvlt.tv/2026/04/09/alarming-xai-is-prioritizing-other-projects-water-plant-is-still-planned/); [Planetizen, 2026-03](https://www.planetizen.com/news/2026/03/137151-memphis-data-center-will-harness-wastewater-cooling); [DCD](https://datacenterdynamics.com/en/news/elon-musk-xai-memphis-supercomputer-wastewater-treatment)
- NSF: exact-phrase searches for "data center waste heat," "waste heat from data centers," and "data center heat reuse" returned 0 awards. — [NSF API](https://api.nsf.gov/services/v1/awards.json?keyword=%22data%20center%20waste%20heat%22)
- Hao Lab assets: research direction 2.1 covers freshwater withdrawals and local footprint (ISSE grant), plus the TDEC decision-support grant. No heat-pump, HVAC, or wastewater-treatment expertise is listed. — [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)

### Inferences
- Waste heat: low novelty for this team, a region with limited heating demand (inference, not verified with degree-day data), and ORNL already works on it locally. Drop as the core.
- Water reuse network design: the Memphis case shows the engineering problem. It means matching multiple data center sites to reclaimed-water sources under distance and piping costs, treatment capacity, aquifer protection, and drought-driven supply variability. This is a facility-location and network-design problem under uncertainty, which is Hao Lab's strength. It also mirrors EWRE's "closing ... water ... loops."
- **Risk:** the lab has no wastewater-treatment engineering in its profile. Treatment-quality constraints (scaling, blowdown chemistry) need an environmental-engineering Co-PI or a simplified treatment model. A single private developer's paused plant is a fragile case. Use a multi-site, multi-source Tennessee framing (Memphis, Nashville, Knoxville/Oak Ridge corridor).

### Gaps
- I did not find Tennessee data on municipal effluent volumes, existing reclaimed-water infrastructure, or district-energy systems taking data center heat. A search summary mentioned the Metro Nashville District Energy System, but no data center link was found.

## Q6. Final recommended ideas (3-5) with verdicts

### Takeaway
Advance three ideas, with one optional fourth that needs a novelty check. Lead with Idea A, which merges original Ideas 1, 4, and 3. It is the clearest gap, the strongest "why us," and the cleanest EWRE fit. Ideas B and C need Co-PIs for thermal, nuclear, or treatment depth.

### Cited Findings
- Supporting evidence for each recommendation is cited in Q0-Q5 above. Key differentiators:
  - deterministic siting ([arXiv 2601.16315](https://arxiv.org/abs/2601.16315));
  - assessment-only grid-water model ([arXiv 2609.25437](https://arxiv.org/abs/2609.25437));
  - stress-aware scheduling already done ([arXiv 2607.22617](https://arxiv.org/abs/2607.22617); [NSF 2324916](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2324916));
  - SMR-data center work without water ([arXiv 2608.10999](https://arxiv.org/abs/2608.10999); [arXiv 2603.09110](https://arxiv.org/abs/2603.09110));
  - no EWRE-coded data center award found ([NSF API](https://api.nsf.gov/services/v1/awards.json?keyword=%22data%20center%20water%22)).

### Inferences

**A. PURSUE (lead).** *Drought- and heat-robust co-design of data center siting, cooling technology, and water sourcing with grid-attributed water accounting* (merges Ideas 1 + 4, with Idea 3 as recourse).
- Engineering core: a two-stage distributionally robust optimization.
  - First stage: site, capacity, cooling-technology portfolio, and water source.
  - Second stage: hourly wet/dry switching and workload or load flexibility.
  - Ambiguity sets come from compound flash-drought and heatwave scenarios.
  - Decision-dependent indirect water uses generator-level attribution (in the style of Alston et al.) for the TVA/SERC fleet, including thermoelectric derating at river-temperature limits.
- New metric: drought-conditioned, stress-weighted total (direct + indirect) water.
- Why us: PI flash-drought and heatwave science, the Gao/Jin robust and tariff-aware siting models, the ISSE footprint grant, the USGS 104b TDEC grant, and the submitted data-center electricity-water paper (all from [hao-lab.md](../../../../talent-pool/labs/hao-lab.md)).
- Size: 3 years, ~$400K, single PI, early-career framing.
- Risks: being seen as OR or CMMI work; credible cooling-performance curves are needed.
- Action: email a one-page summary to cbet-ewre@nsf.gov stressing water-resource management.

**B. REVISE.** *Joint withdrawal and thermal-discharge management for SMR-co-located data center campuses under river-temperature extremes* (Idea 2).
- Engineering core: co-optimize heat-rejection configuration (tower, hybrid, dry, absorption chilling with extracted steam) and operations against withdrawal caps and receiving-water temperature limits (TVA's 90 F precedent) under low-flow and heatwave scenarios.
- Why us: the only matching decision-support grant found (USGS 104b, TDEC, data centers + SMRs), plus the PI's heatwave and drought expertise.
- Required change: add a nuclear or thermal-hydraulics Co-PI (none in hao-lab.md). Position it as foundational methods beyond the 1-year TDEC deliverable.
- Alternatively, fold it into A as a case-study module.

**C. REVISE.** *Circular water sourcing for data center clusters: optimal design of reclaimed-water and alternative-source networks under drought in Tennessee* (Idea 5, reshaped; waste heat dropped).
- Engineering core: multi-site, multi-source network design (municipal effluent, aquifer, surface water, harvested water) with treatment-capacity and drought-supply uncertainty.
- Fits EWRE's "closing energy, water and resource loops."
- Motivating case: Memphis xAI reuse plant (paused April 2026; distance limits Colossus 2).
- Why us: siting and network optimization plus the hydrology of drought supply. Needs an environmental-engineering Co-PI for treatment and water-quality constraints.

**D. OPTIONAL, novelty check required.** *AI- and remote-sensing-based observation of data center cooling water consumption.* This is an inference, not researched in depth.
- Concept: computer vision for cooling-tower and plume detection plus thermal and ET-based estimation, producing an observed dataset to feed A.
- Why us: Shi Jin's computer vision and infrared + LiDAR fusion experience, plus the PI's ET and remote-sensing expertise ([hao-lab.md](../../../../talent-pool/labs/hao-lab.md)). This is the rarest skill combination in the lab.
- EWRE fit is less certain because it is measurement or Earth-observation heavy (GEO risk). It also overlaps the USGS 104g FY2026 topic noted in [funding/2026-10-21.md](../../../2026-10-21.md).
- Prior art was not searched. Do so before adopting.

**Dropped:** Idea 3 (pre-empted by Ren/Islam's NSF DESC award and 2026 preprint; a CISE topic) and Idea 4 (pre-empted by Alston et al. 2026 and Guidi and Dominici 2026). Both are reused as submodules of A.

### Gaps
- No program-director feedback yet. EWRE versus CMMI or CBET-Thermal Transport placement should be confirmed with a one-page summary.
- Google Scholar, ES&T, Nature Sustainability, and e-Energy proceedings were covered only through web search snippets and arXiv. A Scopus check for 2022-2026 "robust optimization" + "data center" + "water" is recommended before finalizing Idea A.
- Co-PI candidates for B and C are not identified in hao-lab.md; only Mingzhou Jin (UT ISE/ISSE, optimization) is listed as a UT collaborator.
