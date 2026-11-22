# NSF ECCS EPCL (NSF 26-514): past winners, proposal ideas and screening

Research notes for the 2026-11-22 scan (Funding Idea Rule). Call: NSF ENG/ECCS
solicitation NSF 26-514, program "Energy, Power, Control, and Learning (EPCL)";
full proposals accepted anytime; contact eccs-epcl@nsf.gov (one-page summary
encouraged). Idea IDs use the prefix **P** (not used by any earlier scan).
Collaborators are in [eccs-epcl-collaborators.md](eccs-epcl-collaborators.md).

**Flag for the scan writer.** The October summary listed "NSF ECCS EPCL
(score 3)" under "Open but below the relevance bar"
([summaries/2026-10.md](../../summaries/2026-10.md), section 6). If this scan
now scores it 4, the call notes should say why (the program page's explicit
"growth in data centers" and "interplay of power system operation with
regulatory and economic structures" language, plus 2026 EPCL awards on large
loads, see Q1). They should also say that Hao Lab can lead only with a
power-systems co-PI, because the lab has no power or controls engineer.

## Q1. Past winners: what EPCL (and its predecessor EPCN) has funded on data centers, large loads, interconnection, planning under uncertainty, water-energy and SMRs

### Takeaway
EPCL started funding data-center/large-load grid integration in 2025-2026:
at least five new projects in 12 months, $200K-$585K each over 3-5 years.
All of them are led by power-systems or control faculty. They treat the data
center as a grid-side load. Their topics are converter and stability dynamics,
unit-commitment flexibility, and colocation economics. None treats
hydro-climate stress (heat, drought, cooling-water limits), planner-side
hosting capacity, or tariff and interconnection-rule design with
siting-responsive loads. No EPCL/EPCN award on water-energy or SMRs turned up.

### Cited Findings

**Program text (opened 2026-11-22).**
- EPCL supports "systems and control, learning, optimization, and networked multi-agent systems", including "higher-level decision making, dynamic resource allocation, risk management in the presence of uncertainty ... and game theory". On power systems it covers "generation, transmission, storage ... and the interplay of power system operation with regulatory and economic structures and consumer behavior". Projects "focus on fundamental advances in knowledge" but "should ideally provide a clear vision of how research can influence real-world applications" — [EPCL program page](https://www.nsf.gov/funding/opportunities/epcl-energy-power-control-learning)
- The page names a single contact, the "EPCL Program Team, eccs-epcl@nsf.gov", and says "Full proposal accepted anytime" (publication date April 16, 2026) — [EPCL program page](https://www.nsf.gov/funding/opportunities/epcl-energy-power-control-learning)

**Data center / large-load awards in EPCL (NSF Award API, queried 2026-11-22; amounts are estimated totals).**
- 2603293, "Integrating Large Load with Resource Colocation: Energy Management, Economic Analysis, and Policy Impacts". Lang Tong (PI) and Timothy D. Mount (co-PI), Cornell; 2026-07-15 to 2029-06-30; $583,747. Topics: stochastic and deterministic optimization for colocating large loads with generation and storage ("profit maximization, risk management, and grid reliability constraints"); techno-economic and empirical studies; "costs and effectiveness of incentive mechanisms for encouraging large-load resource colocation"; a cross-listed course that draws economics, CS and environmental engineering students — [NSF 2603293](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2603293)
- 2610262, "Stability at the Edge: Cyber-Physical Risks and Control of Hyperscale Data Centers in Future Inverter-Dominated Grids". Javad Khazaei (PI), Lehigh; co-PIs Shalinee Kishore and Faegheh K. Moazeni; 2026-07-15 to 2029-06-30; $518,881. Multi-timescale dynamic models of workloads, cooling, UPS and IBR; stability boundaries; load-altering attacks; "risk maps" that inform "future planning and interconnection decisions" — [NSF 2610262](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2610262)
- 2624228/2624229, "Collaborative Research: Unified Modeling of Grid-Data Center Power Electronics Interactions". Jungwon Choi with co-PI Baosen Zhang, University of Washington ($300,000), and Yang Weng, Arizona State ($200,000); from 2026-10-01 for 3 years. Reduced-order converter models, stochastic workload models, and stability analysis — [NSF 2624228](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2624228); [NSF 2624229](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2624229)
- 2541996, "CAREER: Optimal Integration of Flexible Data Centers in Power Systems via Quantum Dynamics". Lei Fan, University of Houston; 2026-05-01 to 2031-04-30; $500,018. MILP and convex models of "spatiotemporal flexibility of data centers within security-constrained unit commitment" plus hybrid quantum-classical decomposition — [NSF 2541996](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2541996)
- 2446781/2446782, "Collaborative Research: Novel Fault Detection and Diagnostics Approach for Robust Design and Reliable Operation of Critical Cooling Infrastructure in Data Centers". Ardeshir Moftakhari (Oklahoma State, $210,141) and Romulo Meira-Goes with co-PI Wangda Zuo (Penn State, $340,000); from 2025-10-01. Supervisory control of discrete-event systems for data center cooling faults — [NSF 2446782](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2446782)
- 2536040, "Travel Grant: The Compute/Energy Nexus Workshop". Rakesh Kumar, UIUC; $45,000; a workshop to draft "a national strategic roadmap" — [NSF 2536040](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2536040)
- Older EPCN data center awards are about power electronics: 1838241, Pilawa-Podgurski, "Power Electronics Architectures for Extreme Efficiency Data Centers" (2018, $353,135); 1810428/2006173, Dong Cao, "Ultra Efficient Composite Modularized Power Delivery Architecture for Solar Farm and Data Center" (2018-2019, EPSCoR co-funded) — [NSF Award API](https://api.nsf.gov/services/v1/awards.json?keyword=%22data%20center%22&fundProgramName=EPCN-Energy-Power-Ctrl-Netwrks)

**Adjacent non-EPCL NSF awards on large loads (for the gap).**
- CPS-FR 2551716/2551717/2551718, "Designing Network Infrastructures for Reliable Wide-Area Control of Power Systems with Emerging Large Loads". Aranya Chakrabortty (NC State), Anuradha Annaswamy (MIT), Alefiya Hussain (USC); 2026-08-15; $350K + $350K + $300K. Topics: wide-area oscillations coupled with load dynamics, and "how load flexibility can be used for finding stable equilibria" — [NSF 2551716](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2551716)
- CICI 2613408, "Towards Resilient AI Data Center Infrastructure with Power Safety". Haining Wang (Virginia Tech); $1.2M (NAIRR program); power vulnerabilities of AI data centers and their grid interactions — [NSF 2613408](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2613408)

**Planning, markets and uncertainty in EPCN/EPCL (method precedents).**
- Transmission planning CAREERs: Adam Birchfield, Texas A&M, "Spatial Complex Network Analysis of Bulk Electric Grids for Long-Term System Planning" (2442131, 2025, $500,000) — [NSF 2442131](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2442131); Rui Bo, Missouri S&T, economics-driven transmission planning (2339956, 2024, $500,000) — [NSF 2339956](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2339956); Mort Webster, Penn State, "Multi-Stage Transmission Expansion under Uncertainty" (1710974, 2017) — [NSF 1710974](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1710974); Ramteen Sioshansi, Ohio State, decomposition for electricity expansion (1808169, 2018) — [NSF 1808169](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1808169)
- Market and regulatory-design CAREERs: Subhonmesh Bose, "Risk-Sensitive Market Design" (2048065, 2021) — [NSF 2048065](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2048065); Chiara Lo Prete, "Capacity Adequacy Options for Electricity Markets ... Equilibrium Models and Laboratory Experiments" (1943992, 2020) — [NSF 1943992](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1943992); Mostafa Ardakani, "Deregulated Market for Flexible Transmission" (2146531, 2022, GOALI) — [NSF 2146531](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2146531); Wenyuan Tang, "Pricing Non-convexities" (2144904, 2022) — [NSF 2144904](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2144904)
- Decision-dependent uncertainty: Ruiwei Jiang, University of Michigan, "CAREER: Incorporating Decision-Dependent Uncertainty via Distributionally Robust Optimization" (1845980, 2019, $500,000; includes "a power system simulation game") — [NSF 1845980](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1845980); Payman Dehghanian with co-PI Miguel Lejeune, GWU, stochastic programming "under Decision-Dependent Uncertainties" for mobile resilience resources (2114100, 2021, GOALI) — [NSF 2114100](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2114100)
- Distributionally robust optimization: Hanasusanto (UIUC) and Cheng (Arizona), "Distributionally Robust Quadratic Optimization and Its Applications to Power Systems" (2404412/2404413, 2024, $300K each) — [NSF 2404413](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2404413); Soroosh Shafiee, Cornell, CAREER on optimal transport (2541066, 2026, $670,000) — [NSF 2541066](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2541066)
- Extreme events and risk: Daniel Molzahn, Georgia Tech, CAREER on extreme events (2145564, 2022) — [NSF 2145564](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2145564); Line Roald, Wisconsin, "CAREER: From Reactive to Proactive Distribution Grid Risk Management" (2045860, 2021) — [NSF 2045860](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2045860); Ian Dobson, Iowa State, utility-data statistics for resilience (2153163, 2022) — [NSF 2153163](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2153163)
- Wildfire-grid in EPCL: Anamitra Pal, ASU, ASCENT "Sensor-enabled Wildfire Awareness and Risk Management (WARM) for Electric Power Infrastructure" (2132904, 2021, $1.5M) — [NSF 2132904](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2132904); Villegas Pico, Iowa State, broken-conductor faults and wildfire ignition (2610703, 2026, $300,000) — [NSF 2610703](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2610703); RAPID OHANA, Hawaii risk-aware partial microgrid shutoff (2412418/2412419, 2024) — [NSF 2412418](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2412418)
- Tennessee EPCL/EPCN winners: Hector Pulgar, UT Knoxville, "CAREER: Towards Enhanced Grid Robustness: Augmenting Grid-Regulating Capabilities Through Discrete Controls on Emerging Power Technologies" (2044629, 2021, $500,000) — [NSF 2044629](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2044629); Ahmad Taha, Vanderbilt, "Controllability and Observability with Confidence" (2550934, 2026, $409,027) and robust control and state estimation of converter-based systems (2151571, 2021) — [NSF 2550934](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2550934)

**Water-energy and SMRs.** Queries ("water-energy", "energy-water",
"cooling water", "small modular", "nuclear", "drought", "hydropower";
EPCN/EPCL program, 2016-2026) returned no EPCN/EPCL award on water-energy
or SMR-data center integration. Nuclear hits were unrelated: Syed Bahauddin
Alam's CAREER (2543177, 2026) builds foundation-model virtual sensing for
dynamic energy systems — [NSF 2543177](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2543177).

### Inferences
- **Typical scale.** Single-PI or one-institution standard grants run $300K-$585K for 3 years. Two-institution collaboratives run $200K-$300K per side. CAREERs run about $500K-$590K for 5 years. A Hao Lab-led EPCL proposal should plan about $450K-$600K over 3 years with a power-systems co-PI.
- **Team makeup.** Every data center award is led by ECE power-systems or control faculty. The two with a policy or systems scope add a second discipline: an economist co-PI on Tong-Mount, and cyber and environmental/systems co-PIs on Khazaei. Hao Lab has neither a power-systems nor a controls record, so the proposal will be judged on whether a credible power co-PI shares the lead.
- **Framing that won.** (i) "Data centers are a structurally new class of load" (the phrasing recurs in 2610262 and 2624228). (ii) A named mathematical object: reduced-order impedance models, SCUC with spatiotemporal flexibility, stability boundaries, stochastic workload models, colocation energy management. (iii) A policy or real-world link stated as a consequence, not as the core: "incentive mechanisms" (Tong), "risk maps ... interconnection decisions" (Khazaei). (iv) Open tools and cross-listed courses as broader impacts.
- **Why they were likely selected.** Each award pairs a timely national need with a theory contribution EPCL reviewers recognize (stability, optimization, control) and a team with prior EPCL-type publications. The fast run of 2026 awards suggests program interest. It also means the device, stability and operations angles are now taken.
- **Open lanes, inferred from the absences above.** Planner- and regulator-side decisions under uncertainty: hosting capacity, queue and tariff rules, risk allocation. Hydro-climate-correlated supply and demand risk in a river-cooled grid. The game between rule-setters and siting-responsive loads. These match EPCL's "risk management in the presence of uncertainty", "game theory" and "interplay ... with regulatory and economic structures" language.

### Gaps
- The Award API matches keywords loosely, and its index may lag. EPCL awards made after early November 2026 may be missing. Older EPCN awards appear under the program name "EPCL: Energy, Power, Control," in the API, so the split between EPCN and EPCL was not verified.
- Panel summaries and success rates are not public. Why each award was selected is inferred from abstracts only.
- DOE/ARPA-E awards were checked only through news summaries (DOE GRIP round 3, about $1.9B for 31 grid projects to speed large-load connections; DOE REFLEX on large-load flexibility). Neither covers hydro-climate-conditioned hosting capacity or tariff design, as far as the summaries show — [Baxtel on DOE GRIP](https://baxtel.com/news/doe-selects-1-9b-in-grid-projects-to-unlock-23gw-of-capacity); [LBNL news](https://newscenter.lbl.gov/?p=57495). The primary DOE award lists were not opened.

## Q2. Candidate ideas led or co-led by Hao Lab, screening, and full evaluations

### Takeaway
Two ideas survive as EPCL leads. **P1** is planner-side large-load hosting
capacity and flexibility envelopes in a river-cooled grid under compound
heat-drought stress. **P2** is a Stackelberg design of large-load tariffs and
interconnection rules when data centers re-site in response. Both need a UT
power-systems co-PI and must be fenced off from the tracked ideas CAREER K1,
CMMI C1/C2, CBET E1, DOE B1, NOAA N1 and the funded USGS 104b project. P3
(speculative-load realization) and P4 (river-temperature-aware unit
commitment) are thrusts, not standalone proposals.

### Tracked ideas this call must not duplicate
From [summaries/2026-10.md](../../summaries/2026-10.md), [2026-11-19.md](../../2026-11-19.md) and [2026-11-20.md](../../2026-11-20.md):
- **K1** (CAREER, ENG/EBE): multi-decade siting and capacity planning of coupled compute-power-cooling-water systems under compound extremes. The developer or planner chooses sites. The closest overlap.
- **C1** (CMMI AMDO): siting when moratoria, tariffs and queues respond to the siting itself (decision-dependent feasible regions). **C3**: text-to-constraint uncertainty. **C2** (held): data center-grid-water system-of-systems resilience under heat-drought.
- **E1** (CBET EWRE): facility cooling-technology and water-source co-design at fixed sites. **E4**: water-stress-aware workload scheduling, dropped.
- **B1** (DOE BER): Earth-system predictability of sub-basin water availability for Tennessee Valley energy expansion.
- **N1** (NOAA SI/ML): interpretable thresholds for heat-driven cascades in the Tennessee Valley energy-water system.
- **U1-U4** (USGS 104g): estimating data center water use. **I3** (104b): drought-conditioned water availability for large-load growth. **CL4** (CLaSH): hazard exposure of power lines, substations and data center sites.
- Funded: USGS 104b TDEC decision support on withdrawals and thermal discharges from data centers and SMRs. UT ISSE local-footprint grant (noise, water, land markets).

**Partition rule proposed for EPCL.** The decision-maker is the **grid
planner, operator or regulator** (TVA-type utility, state commission). The
decision variables are **hosting limits, flexibility contracts, tariff and
queue rules, and unit commitment**. Data center sites appear only as
candidate buses or as a response model. The contribution is **power-system
optimization, control or game theory**. This separates EPCL from K1 (the
developer's long-run siting), C1 (the siting firm facing endogenous rules)
and E1 (the facility's cooling design).

### Short ideas and screening

| # | Idea (2-4 lines) | Angle (method / scale / user / discipline) | Screening result | Verdict |
|---|---|---|---|---|
| P1 | **Hydro-climate-conditioned large-load hosting capacity.** How much firm and how much flexible (pause/shift) data center load can each bus of a river-cooled grid host when compound flash drought-heatwave events raise demand and derate thermoelectric and hydro capacity at the same time? Distributionally robust hosting-capacity and flexibility-envelope design with regime-conditioned ambiguity sets. | Optimization + risk / regional bulk grid / planners, TVA, regulators / hydro-climate + power systems | Closest work (Kim, Dong, Xie 2026) has no weather or water stress. NERC names heat and drought hydro losses as threats but no quantified study combining them with data center load was found (sources in full evaluation). | **Pursue (lead)** |
| P2 | **Stackelberg design of large-load tariffs and interconnection rules.** A utility or regulator (leader) sets upfront charges, minimum take, flexibility requirements and queue-entry rules. Data center developers (followers) choose bus, size and flexibility. Goal: limit stranded-asset risk and cost shift to other ratepayers while keeping reliability. | Game theory / bilevel optimization / regional / utilities, commissions / economics + policy | Tong-Mount (2603293) studies incentives for colocation, not location-responsive tariff design. arXiv bilevel papers treat price-responsive operation, not tariff or rule design with siting response. TVA adopted a new data center rate in Aug 2026. | **Pursue (alternative)** |
| P3 | **Learning which large-load requests will materialize.** A Bayesian model of queue requests that fuses satellite or aerial signs of construction (computer vision), permit and filing text (NLP) and developer duplicates across utilities. Its output feeds chance-constrained planning. | Learning + observation / national to regional / planners / CV, NLP | Utilities report 5-10x more requests than builds; no validated realization-probability model was found. Overlaps U3/U4 data layers and C3. | **Revise: thrust of P1 or P2** |
| P4 | **River-temperature-aware unit commitment with flexible data centers.** SCUC with thermal-discharge and river-temperature constraints (heat-driven derates at once-through-cooled plants) where data center load shifting is a control input that relieves those constraints. | Control/optimization / operations, hours-days / TVA operators / hydro-thermal + power | No EPCL award on cooling-water constraints. Close to the funded 104b scope (thermal discharges) and to E2. | **Revise: operations thrust of P1** |
| P5 | Grid-aware geo-distributed AI workload scheduling (Gao's interest), with carbon, price and water signals | Scheduling / national / cloud operators / CS | Crowded: Fan CAREER 2541996 (spatiotemporal flexibility in SCUC); an NSF-funded UW-Madison/UChicago data center flexibility project (Roald, Zavala); arXiv 2604.10998 (strategic spatial load shifting). E4 already dropped for the water version. | **Drop** |
| P6 | SMR-data center islanded or co-located microgrid control (load-following of SMR output under AI training swings) | Control / site / developers / nuclear + power electronics | No nuclear or power-electronics expertise in the pool. Dynamics side covered by 2610262 and 2624228. SMR thermal discharge already in 104b. | **Drop** |
| P7 | **Wildfire-aware large-load interconnection and shutoff planning in the humid Southeast.** Use data center flexibility during public-safety power shutoffs and fire-risk-weighted hosting limits. | Risk / regional / utilities / fire science + power | Builds on the PI's RSER 2026 wildfire-power grid review (co-authored with Fangxing Fran Li) and the submitted Southeast fire review. EPCL wildfire awards are Western or Hawaii and sensor- or fault-focused. Southeast fire-grid event data are thin, and the data center link is weak. | **Revise: hold for a later EPCL round with Fran Li; or a P1 scenario** |
| P8 | LLM extraction of large-load tariffs, interconnection agreements and moratoria into machine-readable constraint sets for planning models | NLP / national / regulators, researchers / AI | LBNL already compiles 55 large-load tariffs. Overlaps C3 (text-to-constraint). Not foundational for EPCL alone. | **Revise: data thrust of P2** |
| P9 | Dynamic stability of hyperscale AI loads in low-inertia grids | Control / transmission / operators | Pre-empted by 2610262, 2624228/9 and CPS 2551716-8. No lab record. | **Drop** |
| P10 | Joint data center siting and transmission expansion under uncertainty | Optimization / regional | Overlaps K1 and the planner-initiated siting of Kim et al. 2026. TEP CAREERs (Birchfield, Bo) are strong competitors. | **Drop (absorbed into P1's planner framing)** |
| P11 | "Power systems for AI infrastructure" module in IE 465/565 and IE 591 using the project's open hosting-capacity tool | Education | Broader impacts only | **Drop as standalone; broader impacts of P1/P2** |

### P1. Hosting AI loads in a river-cooled grid: hydro-climate-conditioned hosting capacity and flexibility envelopes for large loads under compound heat-drought stress — Pursue (lead)

**Team (talent pool names only).** Yuefeng Hao (PI or co-lead: compound
extremes, ET and drought science, data center water); Yifan Gao (robust and
scenario optimization, queue uncertainty); Shi Jin (from Spring 2027:
optimization and the tariff and moratorium model; computer vision for the P3
thrust). A UT power-systems co-PI is required; candidates are in the
collaborators file, and none has been contacted or has agreed. Mingzhou Jin
(registry, past co-author) is a possible optimization collaborator.

**Research question and approach.** When a flash drought-heatwave hits a
grid whose thermoelectric and hydro fleet is cooled by one river system,
supply derates and demand rises together. How much firm and how much flexible
data center load can each bus safely host, and what flexibility envelope
should a planner require, with the stress level depending on the
hydro-climate regime?
- **Thrust 1 (uncertainty model).** Regime-conditioned, spatially correlated scenarios of load, river temperature and flow, and plant derates, built from observations and reanalysis using the PI's flash-drought and heatwave methods.
- **Thrust 2 (optimization theory).** Distributionally robust or chance-constrained hosting capacity. Ambiguity sets are indexed by the hydro-climate regime, and flexibility envelopes (firm, pause, shift) are decision variables. Products: tractable reformulations, a decomposition, and a bound on the value of regime-awareness versus weather-blind screening.
- **Thrust 3 (validation).** Validate on synthetic, TVA-like test systems (CEII data limits), and compare the results with a weather-blind planner-initiated screen.
- **Optional thrusts.** P3 (realization-probability learning) and P4 (river-temperature-aware unit commitment).

**Closest existing projects and papers, and the gap.**
- Kim, Dong and Xie (arXiv 2605.14714, accepted in *Nature Communications*) site data centers planner-first with "reliability-gated screening" and "standardized flexibility envelopes (firm, pause, and shift)" on a synthetic 2,000-bus Texas system. Hydro-climate stress, cooling-water limits and correlated supply derates are not modeled — [arXiv 2605.14714](https://arxiv.org/abs/2605.14714)
- Xie et al. frame large AI data centers by "forecast uncertainty in load realization and multi-scale temporal variation", across resource adequacy, expansion, security and market design. Weather- and water-driven supply risk is not part of the framework — [arXiv 2610.14264](https://arxiv.org/abs/2610.14264)
- EPCL data center awards: stability and dynamics (2610262, 2624228/9), SCUC flexibility (2541996), colocation (2603293). None includes hydro-climate or cooling-water constraints (Q1).
- Water-constrained capacity expansion exists without data centers: Liu et al. 2019 (*Nature Sustainability*); ERCOT water and climate long-term assessment (NREL/Sandia). Drought derating of Eastern U.S. thermoelectric plants has been studied, also without data centers. These were seen as search summaries only — [PNNL summary](https://www.pnnl.gov/publications/implications-water-constraints-electricity-capacity-expansion-united-states); [Sandia ERCOT](https://www.sandia.gov/research/publications/details/water-and-climate-impacts-on-ercot-long-term-systems-assessment-2021-12-31/)
- The NERC 2026 Summer Reliability Assessment, as summarized, lists extreme heat and drought-driven hydro losses as threats. Searches found no study that quantifies data center load coinciding with drought or heat derates, or hosting capacity under such stress — [Energy Central summary of NERC 2026 SRA](https://energycentral.com/energy-management/post/executive-summary----nerc-2026-summer-reliability-assessment-cl8wkhRf4ANF9ZO)
- Local relevance: Browns Ferry has cut output when the Tennessee River ran hot (2010 news). Its permit has a downstream temperature limit and a 10°F 24-hour average rise limit (TVA hydrothermal study filed with NRC, 2004-2005 era; current permit terms not checked) — [Times Free Press 2010](https://www.timesfreepress.com/news/news/story/2010/aug/23/hot-river-forces-costly-cutback-tva/27261/); [NRC ML0428](https://www.nrc.gov/docs/ML0428/ML042800096.pdf). TVA expects load of 9-33 GW by 2040, and data centers were 10% of TVA load last year per WPLN as cited by WUNC — [WUNC 2026-08-25](https://www.wunc.org/2026-08-25/tva-welcomes-data-centers-but-at-a-price) (another summary gives 18% of industrial load: [search summary of TVA coverage](https://www.publicpower.org/periodical/article/tva-board-moves-protect-customers-subsidizing-expenses-tied-growth-data-center-load), not opened).

**Novelty.** Hosting capacity for large flexible loads made conditional on
correlated hydro-climate regimes, with the flexibility envelope chosen by the
optimization rather than fixed. This is a new decision-under-uncertainty
problem, not a relabeling of weather-blind screening. It also answers EPCL's
"risk management in the presence of uncertainty" and "growth in data
centers".

**Why us (talent pool facts only).**
- PI's compound-extremes science: "Evaluating the effects of heatwave events on hydrological processes in the contiguous United States (2003-2022)" (*J. Hydrol.* 637, 2024); flash-drought WUE and recovery (*AFM* 378, 2026); drought indices and recovery time (*SERRA* 36, 2022).
- PI's data center water and energy work: PI of the USGS 104b TDEC grant on withdrawals and thermal discharges from data centers and SMRs in Tennessee (2027-01, $84K) and the UT ISSE local-footprint grant (2026-08, $60K); submitted paper "Regional screening of electricity-related water consumption for projected data-center load growth" (*Water Resources and Industry*, under review).
- Power-grid hazard link: co-author of "Wildfire-Power Grid Interactions" (*RSER* 232, 2026) with Fangxing Fran Li, Grant Buster and Mingzhou Jin.
- Students' models: Gao's "Robust Data Center Siting under Interconnection-Queue Uncertainty" and Jin's "Siting Under Moving Rules: A Tariff- and Moratorium-Aware Optimization Model for AI Data Center Location in the Tennessee Valley".
- ORNL E3SM collaboration (Mao, Shi, Wang, Ricciuto, Thornton, Hoffman), a possible source of future-climate regimes.

**Fundability against EPCL and NSF criteria.**
- Intellectual merit: a new problem class with theory deliverables (reformulations, value-of-regime-awareness bounds).
- Broader impacts: an open hosting-capacity tool for utilities and regulators, IE 465/565 and IE 591 modules, and Tennessee Valley relevance.
- Fits "dynamic resource allocation", "risk management in the presence of uncertainty" and "growth in data centers" on the program page.
- Budget about $450K-$600K over 3 years, which matches the observed EPCL norms.

**Risks.**
- EPCL panels are power and control theorists, and the lab has no record there. A power co-PI must co-lead, and the theory contribution must lead the narrative.
- Overlap with K1, C2, B1 and N1 (same theme). Keep siting choices out (candidate buses only), keep Earth-system modeling as an input, and list all pending proposals.
- Hydro-climate-to-derate models need plant cooling data. TVA grid data are CEII-restricted, so plan for synthetic grids.
- Fast-moving competition (Xie group, Tong group).

**Verdict: Pursue.** Before writing: (1) secure a UT power-systems co-PI
(Hector Pulgar or Fangxing Fran Li; neither has been contacted); (2) send a
one-page summary to eccs-epcl@nsf.gov stating the planner-side framing;
(3) decide K1 versus P1 timing. K1's CAREER deadline is 2027-07-28. If P1
is pending then, K1 must exclude hosting capacity and flexibility envelopes.

### P2. Pricing the rush: Stackelberg design of large-load tariffs and interconnection rules with siting-responsive data centers — Pursue (alternative)

**Team.** Shi Jin (tariff and moratorium model, lower level), Yifan Gao (queue
uncertainty and NLP extraction of tariff terms), Yuefeng Hao (PI or co-lead;
water and heat stress as a cost driver). A power-systems co-PI and an
energy-economics co-PI are needed; candidates are in the collaborators file,
and none has been contacted.

**Research question and approach.** A utility or regulator (leader) chooses
large-load tariff and queue terms: upfront charges, minimum demand and
contract length, collateral and exit fees, mandatory flexibility or
bring-your-own-generation, and queue-entry readiness tests. Developers
(followers) choose whether, where and how big to build and how flexible to
be. How should the leader design these terms to minimize stranded-asset risk
and cost shift to other customers subject to reliability, when followers
re-site across utilities?
- Method: a bilevel or MPEC model with a stochastic follower population.
- Theory: existence and computation of equilibria, and robustness of tariff rules to misspecified follower models.
- Empirics: 55 public tariffs (LBNL) and TVA's 2026 rate as cases; P8's extraction pipeline supplies the tariff data.

**Closest existing projects and papers, and the gap.**
- NSF 2603293 (Tong, Mount) studies colocation energy management and the "costs and effectiveness of incentive mechanisms for encouraging large-load resource colocation". It does not cover location-responsive tariff and queue-rule design — [NSF 2603293](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2603293)
- Bilevel data center papers address operation, not rule design. Strategic spatial load shifting under DC-OPF prices — [arXiv 2604.10998](https://arxiv.org/abs/2604.10998). A DLMP bilevel model with the data center aggregator as leader — [arXiv 2606.26328](https://arxiv.org/abs/2606.26328). Utility pricing for data center demand response (2015, IEEE TSG; search summary) — [arXiv 1511.00575](https://arxiv.org/abs/1511.00575)
- Practice sources describe tariff elements but optimize nothing: LBNL/Brattle analyzed 55 large-load tariffs — [LBNL brief](https://eta-publications.lbl.gov/sites/default/files/2026-08/rate_designs_large_loads_2026.08.10.pdf) (search summary; PDF not opened). EEI, as cited by the Sabin Center, counts 23 states with an approved large-load tariff as of May 2026 — [Sabin Center](https://blogs.law.columbia.edu/climatechange/2026/06/02/data-center-regulation-what-local-governments-should-know-about-large-load-tariffs-and-clean-transition-tariffs/)
- Speculative requests: utilities see "five to 10 times more interconnection requests than data centers actually being built" (Atkinson, quoted by Utility Dive). AEP Ohio's tariff cut its queue from 30 GW to 5.6 GW — [Utility Dive](https://www.utilitydive.com/news/efforts-to-curb-data-center-speculation-gain-ground-across-the-us/830495/) (search summary)
- TVA context: in August 2026 the TVA board adopted a data center rate effective 2026-10-01 that "includes a new upfront cost for large customers" — [WUNC](https://www.wunc.org/2026-08-25/tva-welcomes-data-centers-but-at-a-price). TVA may require some data centers to "bring their own generation or participate in demand response" (search summary of TVA coverage) — [Industrial Info](https://www.industrialinfo.com/news/article/us-tva-board-adopts-spending-plan-commits-to-shielding-smaller-customers-from-large-electric-users-c--361985)
- Method precedents: EPCN/EPCL market-design CAREERs (Bose 2048065, Lo Prete 1943992, Ardakani 2146531) and decision-dependent DRO (Jiang 1845980). None addresses large-load tariffs.

**Novelty.** Tariff and queue rules treated as control inputs in a leader-
follower game with spatially mobile, partly speculative large loads. This
fits EPCL's "game theory" and "interplay of power system operation with
regulatory and economic structures". The mobility of followers across
utilities is what is new compared with classic retail tariff design.

**Why us.** Jin's tariff- and moratorium-aware Tennessee Valley siting
model is the follower model, already in progress. Gao's queue-uncertainty
siting paper and NLP and information-extraction background (a planned
source-linked dataset of data center development requirements) supply the
data and the uncertainty model. The PI's ISSE grant (noise, water,
land-market tradeoffs) and 104b TDEC grant provide the local-cost and
state-agency context.

**Fundability.** EPCL language fits almost verbatim. The NSF-wide
broader-impact story is ratepayer protection and reliability. It needs
economics depth, and the Tong-Mount award shows EPCL funds an
engineer-economist team.

**Risks.**
- Close to CMMI **C1**, which mirrors the same setting from the developer's side. Both reuse Jin's model, so NSF could see them as substantially similar. Submit only one of P2 and C1 in a given cycle, or make C1's endogenous-hazard method and P2's leader-follower design clearly different.
- The Tong group is a direct competitor.
- Bilevel theory is demanding for a new team.
- Tariff data are public, but TVA-specific cost data may not be.

**Verdict: Pursue as the alternative to P1.** Choose P2 over P1 if a UT
energy economist joins and the AMDO program director declines C1. Do not
submit P2 and C1 at the same time.

### P3. Which data centers will actually show up? Learning realization probabilities of large-load requests for risk-aware planning — Revise (thrust of P1 or P2)

**Team.** Shi Jin (computer vision of construction and substation build-out;
350K-record ETL and retrieval platform experience), Yifan Gao (NLP of
filings), Yuefeng Hao (remote sensing, statistics).

**Approach.** Hierarchical Bayesian or survival model of request-to-
energization conversion. Features: site-control evidence, satellite
construction progress, permit text, and duplicate requests across utilities.
Posterior realization probabilities feed P1's chance constraints or P2's
follower population.

**Gap and sources.** No "firm, published conversion rate" or validated
probability model was found; sources give ranges and qualitative judgments
(EPRI survey: no utility expected its 5-year data center share above 35% of
peak even where requests exceeded 50%) — [Utility Dive](https://www.utilitydive.com/news/efforts-to-curb-data-center-speculation-gain-ground-across-the-us/830495/)
(search summary). Xie et al. name "forecast uncertainty in load realization"
as a defining property — [arXiv 2610.14264](https://arxiv.org/abs/2610.14264).

**Why us.** Shi Jin's YOLO/EfficientNet detection, infrared + LiDAR
registration, and the 350K-paper ETL platform; Gao's information extraction;
the PI's MODIS and multi-source remote sensing.

**Why not standalone.** As a learning problem alone it reads as forecasting,
not EPCL theory. Labeled outcomes (built or not) are scarce. It overlaps the
U3/U4 data layers in 104g. Keep it as one thrust that supplies the
uncertainty set.

### P4. River-temperature-aware unit commitment with data center flexibility as a control input — Revise (operations thrust of P1)

**Approach.** Couple a reduced river-temperature model (heat budget, flow)
with SCUC. Thermal-discharge limits become state constraints, and data
center pause and shift actions are control inputs that relieve derates
during heat-drought events. Theory: MPC or chance-constrained SCUC with
exogenous hydro-climate forcing.

**Gap.** Fan's CAREER (2541996) puts data center flexibility in SCUC with no
cooling-water constraints. No EPCN/EPCL award with river-temperature
constraints was found (Q1). Browns Ferry's heat-driven cutbacks show the
mechanism ([Times Free Press 2010](https://www.timesfreepress.com/news/news/story/2010/aug/23/hot-river-forces-costly-cutback-tva/27261/)).

**Why us.** 104b TDEC grant on thermal discharges from data centers and
SMRs; the PI's heatwave hydrology paper.

**Why not standalone.** It is too close to the funded 104b scope and CBET
**E2**. As P1's operations thrust it shows how flexibility envelopes are used.

### Overlap and hosting summary (for the Ideas Overview)
- **EPCL hosts one proposal: P1 (with P3 and P4 as thrusts), or P2 (with P8).** Not both at once, since they share team, students and testbed.
- **P1 vs CAREER K1:** the same theme. P1 = planner-side hosting limits and flexibility envelopes with sites as candidate buses. K1 = developer- or planner-side multi-decade siting and capacity of coupled compute-power-cooling-water systems. If both go forward, K1's research plan must not include hosting capacity or flexibility-envelope design. List P1 in K1's Current and Pending Support.
- **P1 vs CMMI C2 (held), DOE B1, NOAA N1:** C2 stays on hold. B1 supplies Earth-system regimes; P1 must not claim predictability science. N1's heat-cascade thresholds may serve as P1 inputs; keep the deliverables separate.
- **P2 vs CMMI C1 (and C3):** mirror images built on the same student model. Choose one per cycle (see P2 risks). P8 duplicates C3; keep it as a data task.
- **P4 vs USGS 104b (funded) and CBET E2:** keep TDEC decision tools and permit-compliance analysis in 104b, and keep facility cooling in E1/E2. P4 contributes only grid-operations theory.
- **P7** reuses the RSER wildfire-grid review with Fran Li; it is a future option and conflicts with no tracked idea.

### Gaps
- No team member has power-systems or control publications in the talent pool files. All power expertise must come from a co-PI who has not yet been contacted.
- Several literature items were seen only as search summaries: Liu et al. 2019; the ERCOT water study; the LBNL tariff brief PDF; the Utility Dive speculation article; the NERC 2026 SRA summary; arXiv 1511.00575. The current Browns Ferry permit terms were not checked.
- Google Scholar and Scopus were not queried directly. Targeted searches for "hosting capacity" + "data center" + drought or heat, and for "tariff design" + "bilevel" + "data center siting", turned up nothing matching (web search only). Run a Scopus check before writing.
- The NSF PAPPG wording on duplicate or substantially similar proposals was not reopened, so confirm it before deciding the P1/K1 and P2/C1 timing.
- No EPCL per-award budget guidance is stated; the budget ranges above come from award samples.

## Sources checked
- NSF EPCL program page (opened with curl, 2026-11-22): https://www.nsf.gov/funding/opportunities/epcl-energy-power-control-learning
- NSF Award API, queried 2026-11-22 with keywords "data center(s)", datacenter, "large load(s)", "flexible load(s)/demand", interconnection, "interconnection queue", "capacity expansion", "transmission/generation expansion" uncertainty, "water-energy", "energy-water", "small modular", nuclear, "electricity market", "computing workloads", wildfire, drought, "extreme heat", climate, hydropower, siting, Tennessee, tariff, "resource adequacy", "distributionally robust", "cooling water", "demand flexibility", workload; the EPCN/EPCL program filter for 2016-2026 plus an unfiltered 2023-2026 data center sweep (about 900 unique records). Example: https://api.nsf.gov/services/v1/awards.json?keyword=%22data%20center%22&fundProgramName=EPCN-Energy-Power-Ctrl-Netwrks
- arXiv abstracts opened: 2605.14714, 2610.14264, 2604.10998, 2606.26328.
- WUNC article on the TVA data center rate (opened).
- Web searches: data center siting and interconnection co-planning; heat-drought derating and data center flexibility; large-load tariff and bilevel design; speculative load requests; DOE/ARPA-E data center grid awards; ORNL data center institute; TVA demand response; water-constrained expansion; Browns Ferry derates; resource adequacy with data center load and climate.
- Could not open: the ORNL news page on the Next-Generation Data Centers Institute (returned a 40-byte stub to curl); the LBNL "Watt's Next" news page (no text extracted).
