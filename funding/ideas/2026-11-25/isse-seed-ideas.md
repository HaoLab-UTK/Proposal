# UT Knoxville ISSE 2027 Seed Grant: past winners and proposal ideas

Research notes for the 2026-11-25 scan (Funding Idea Rule). Call: University of
Tennessee, Knoxville, Institute for a Secure and Sustainable Environment (ISSE),
"Request for Proposals for 2027 Seed Grant Funding", due 2026-12-09 (time not
stated). Official pages: [ISSE Seed Grants page](https://isse.utk.edu/opportunities-for-faculty-students-partners/seed-grants/)
and [2027 RFP and cover sheet (PDF)](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf).
"Why us" statements use only facts in `talent-pool/labs/hao-lab.md` and
`talent-pool/resources/hao-lab/*.md`. Pages were opened with curl; pages that
could not be opened are named under Gaps.

## Key Question 1: Past winners of the ISSE seed program, and what they share

### Takeaway
ISSE seeds go to small UT Knoxville teams (a PI plus one to three co-PIs from
other departments, mostly Tickle College of Engineering, often CEE) on applied,
Tennessee-relevant topics that map to the RFP bullets. Several seeds have led to
external awards. The FY27 round funded only two projects, both about AI and
regional resilience: Hao's data center footprint seed and Haochen Li's
AI-augmented flood forecast "for energy and community resilience". So any Hao
flood or energy-water idea for 2027 has to build on Li's seed and must not
repeat it.

### Cited Findings
**FY27 winners (current awards, $60,000 each, 2026-08-15 to 2027-06-30)**
- PI Yuefeng Hao, "The Local Footprint of AI Data Centers: Noise, Water, and Land-Market Tradeoffs in Tennessee"; students listed: Yifan Gao (Ph.D. student) and Faith Keating (undergraduate researcher) — [ISSE Seed Grants page](https://isse.utk.edu/opportunities-for-faculty-students-partners/seed-grants/).
- Scope of the Hao seed: a scenario-based decision model for where future data centers may be located, covering land use, economic conditions, community factors, policy, climate, water resources and electricity infrastructure. The model is to become a web-based decision-support tool. Heat-wave electricity demand and cooling water are named as considerations — [ISSE news, Hao seed](https://isse.utk.edu/isse-seed-project-examines-local-impacts-of-ai-data-centers-in-tennessee/).
- PI Haochen Li, team Jon Hathaway, Kelsey Ellis and Nicholas Shanahan: "AI-augmented real-time flood forecast for energy and community resilience in Southern Appalachians" — [ISSE Seed Grants page](https://isse.utk.edu/opportunities-for-faculty-students-partners/seed-grants/).
- Scope of the Li seed: a prototype flood forecast for East Tennessee and western North Carolina at about 10 m resolution, updated about every six hours, to be made public. Named users are transportation agencies (about 3,000 bridges and culverts in the region) and regional planning and development organizations. The team's post-Helene analysis estimated that about 40% of flooded areas were outside FEMA flood-map coverage. Li notes that many mountain communities sit on streams that TVA dams do not regulate — [ISSE news, Li seed](https://isse.utk.edu/new-flood-forecasting-seed-project-targets-gaps-in-southern-appalachian-flood-risk-information/).
- Li's flood engine is a hydrodynamic solver for the whole roughly 19,980 km² watershed (202 million degrees of freedom on one GPU or TPU). It runs East Tennessee floods at 5 m resolution and was supported by UT ORIED's AI Tennessee Initiative. Earlier collaborators were Hathaway (CEE), Emine Fidan (Biosystems Engineering and Soil Science) and Ellis (Geography and Sustainability) — [UT CEE news, 2025-06-11](https://cee.utk.edu/li-develops-flood-hazard-forecasting-system).
- Paper from that line: Li, H., Hathaway, J., and Canestrelli, A., "Watershed-scale hydrodynamic modeling of Hurricane Helene flooding in Southern Appalachians", *Journal of Hydrology: Regional Studies* 64, 103167 (2026), listed in the [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf) (publications).

**Earlier awards (titles and PIs from the seed page; co-PIs and periods from annual reports)**
- 2022-2024 active seeds, with co-PIs: Jiangang Chen (PFAS in Tennessee surface water; co-PIs Jie Wu, Qiang He); Alison Buchan (bacterial PAH degradation; Qiang He); Baoshan Huang (waste plastics in asphalt; Qiang He, Brian Long, Pawel Polaczyk); Kai Sun ("Assessing the Implications of Large-Scale Hydrogen Production on Power Transmission Systems", 7/2023-6/2024; co-PI Feng Zhang); Anna Herring (mass transfer during underground hydrogen storage; co-PI Haochen Li); Tong Wang (sustainable aviation fuel and biofertilizer from black soldier fly) — [ISSE 2023-24 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2024/10/2023-24-THEC-report-FINAL-web.pdf), pp. 9-10.
- Seeds completed by 2024, with co-PIs: Khalid Alshibli (CO2-caprock interaction; Nicholas Dygert); Qiang He (personalized exposome monitoring; Cronley and Li); Kelsey Ellis ("Beat the Heat", adaptive capacity of vulnerable Knox County populations to urban heat; co-PIs First and Kintziger); Frank Loeffler (sulfonated PFAS degradation; Shawn Campagna); Jie Wu (arsenic in community water systems, field biosensors; Cronley and He); Chris Cherry (second-life micromobility batteries; Daniel Costinett) — [ISSE 2023-24 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2024/10/2023-24-THEC-report-FINAL-web.pdf), p. 10.
- Seeds completed by FY26: Anming Hu (porous carbon sorption plus TiO2 photocatalysis for micro/nanoplastics and PFAS, 7/2024-6/2026); Frank Loeffler (linked to ExxonMobil (EMBSI), 9/2024-6/2026); Philip Ye ("Decarbonization of nitrogen fertilizer for agriculture", 7/2024-6/2025) — [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf), p. 27.
- Other titles on the seed page: Peng Zhao (particle emission during battery thermal runaway and fires); Leon Tolbert (community EV charging with V2G for environmental and social justice); Eminé Fidan ("Environmental Justice in the City: Socio-Economic Dimensions of Urban Stream Health"); Chris Clark (organic waste diversion in Tennessee); Anahita Khojandi (multi-sensor, data-driven inspection and maintenance of green infrastructure); Steven Ripp (synthetic biology for plant phytosensing); Douglas Hayes (micro- and nanoplastics from biodegradable agroplastics); Scott Lenaghan (duckweed plastid-genome bioengineering); Terry Hazen (microbial-geochemical signatures for CO2 storage) — [ISSE Seed Grants page](https://isse.utk.edu/opportunities-for-faculty-students-partners/seed-grants/).
- At the 2026 ISSE Research Conference (2026-09-14), the Seed Project Showcase featured Anna Herring (subsurface fluid dynamics for sustainable energy), Feng-Yuan Zhang (bioelectrochemical nutrient recovery from waste), Emine Fidan ("Evaluating Water Availability and Sectoral Demand for Sustainable Allocation") and Haochen Li (hidden flood risks in the Southern Appalachians) — [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf), p. 35; [ISSE conference news](https://isse.utk.edu/5th-annual-isse-research-conference-brings-together-researchers-students-and-partners/).
- At the same conference, ORNL Associate Laboratory Director Kate Evans gave the featured talk "Tackling Southeast U.S. Resilience: Why now? Why us?", and Mark Finlay (Senior Energy Analyst, TDEC Office of Energy Programs) spoke on Tennessee energy priorities — [ISSE conference news](https://isse.utk.edu/5th-annual-isse-research-conference-brings-together-researchers-students-and-partners/).

**Seeds that led to external work**
- A 2023 ISSE seed on a PFAS sensor platform (PIs Jayne Wu, EECS, and Qiang He, CEE) led to a USGS 104g project — [ISSE 2023-24 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2024/10/2023-24-THEC-report-FINAL-web.pdf) (opening highlights list); [ISSE New Research Awards](https://isse.utk.edu/research-recognition/new-research-awards/).
- The Herring-Li seed was co-funded by UT's GE2 initiative and ISSE ($50,000). Herring planned to grow it into an underground hydrogen storage group co-led with Haochen Li — [UT CEE news](https://cee.utk.edu/herring-tackles-climate-change-with-multiphase-research/). A later ExxonMobil-sponsored project (PI Frank Loeffler, co-PIs Anna Herring and Haochen Li, 2026-05 to 2027-05) is listed in the [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf), p. 23.
- The Kai Sun seed paired grid simulation (Sun) with electrolyzer modeling (Zhang): electrolyzer cells respond to load changes within milliseconds, and the team built multi-timescale grid simulation methods — [ISSE 2023-24 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2024/10/2023-24-THEC-report-FINAL-web.pdf), p. 30.
- The Tong Wang seed report states that the seed data "will help better focus our USDA grant activities" — [ISSE 2023-24 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2024/10/2023-24-THEC-report-FINAL-web.pdf), p. 28.

### Inferences
- **Common pattern.** Winners pair one technical core (sensing, a process experiment, simulation or AI) with a second discipline from another department. Team sizes run from a PI alone to a PI with three co-PIs. Topics follow the RFP bullets: PFAS and microplastics (water pollutants), hydrogen, CO2 storage and the grid (energy), waste-to-value (circular economy), heat and exposome (environmental health), green infrastructure (built environment). The strongest have a Tennessee hook and a named external sponsor that later came through (USGS 104g, ExxonMobil, USDA).
- **Likely reasons for selection.** The RFP's review criteria reward fit with ISSE's mission, a feasible one-year plan, attractiveness to named funders, cross-unit collaboration, and a convincing external-proposal plan ([RFP](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf)). Past winners show concrete deliverables (a sensor, a model, a dataset) that become the preliminary results of an external proposal.
- **FY27 shift.** Both FY27 awards are AI plus Southeast resilience, and the 2027 RFP points applicants to ORNL's regional-resilience initiative. A 2027 Hao idea fits best if it is a resilience study of energy-water systems with ORNL involvement and an AI or optimization core.
- **Overlap with the Li seed.** Li's seed already owns real-time flood forecasting with an "energy" framing for East Tennessee and western North Carolina. A Hao flood idea can only add something that seed does not do, such as long-term mitigation decisions for energy-water assets using Li's outputs. It should be planned with Li's team, not in competition with it.
- **Template from the Kai Sun seed.** That seed asked how a new large flexible load (electrolyzers) affects transmission reliability. The same question for AI data center load under hydro-climate extremes is a direct analogue, and ISSE has already funded that kind of grid study once.

### Gaps
- The seed page lists PIs without years or amounts for the older awards. The year-by-year award count and dollar amounts for 2024-2026 could not be confirmed. FY27 had two awards, but how many were offered in the FY27 RFP is unknown.
- Nicholas Shanahan (on the Li team) could not be identified in a web search, so that person's role and department are unknown.
- No ISSE page states the success rate, review panel make-up or whether past PIs were funded twice in a row. Khalid Alshibli, Qiang He and Scott Lenaghan each appear twice on the seed page, but it is not clear whether those are repeat awards or duplicate listings.

## Key Question 2: Proposal ideas for the 2027 ISSE seed (led or co-led by Hao Lab)

### Takeaway
The safest plan is two proposals. **IS1** (Hao as PI, using the PI's one PI
slot): compound flash drought and heat stress on Tennessee Valley energy-water
systems, linked to ORNL's regional-resilience initiative. It seeds DOE BER
**B1** and USGS Powell **PC1**. **IS2** (Kai Sun of EECS/CURENT as PI, Hao as
co-PI): transmission reliability of AI large-load growth under hydro-climate
extremes. It seeds NSF ECCS EPCL **P1**, which already needs a power co-PI.
IS3 (flood mitigation for energy-water assets) should only go forward if Haochen
Li's team wants it and leads it. Every idea must exclude what the current Hao
ISSE seed covers (noise, land market, the siting decision tool) and what the
104b TDEC grant covers (withdrawal and thermal-discharge decision support).

### Cited Findings
**Call rules that shape the ideas**
- Up to five seed grants of at most $60,000. No F&A. The period runs 2027-01-01 to 2027-12-31. Funds may pay for faculty support, including teaching buyout, with the PI's department head's approval. Expenses that build collaborative networks are encouraged — [RFP](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf).
- Teams must have multiple investigators from multiple disciplines. PIs must be UT faculty or staff. UTIA faculty need at least one UTK co-PI. "Researchers may serve as the PI on only one proposal submission." The cover sheet must be signed by every team member and their department head — [RFP](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf).
- Funded teams commit to "one or more multi-investigator external follow-on funding proposals through ISSE" and one or more peer-reviewed articles. The UTK portion of any resulting external proposal must be routed through ISSE — [RFP cover sheet](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf).
- The three-page narrative must include at least two potential external programs or agencies, each with a targeted amount, plus a detailed plan and timeline. The review criterion asks for "planned visits to targeted programs" and "enough allocated faculty time to proposal development" — [RFP](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf).
- "Continued funding beyond 2027 will require the submission and approval of a new seed grant proposal in a subsequent funding cycle." The RFP neither allows nor bars a current awardee from reapplying. It says nothing on conflicts of interest or on who reviews. Packages go by email to the ISSE director, Dr. Mingzhou Jin, with a copy to Emily Hammerberg — [RFP](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf).
- Partners named in the RFP: ORNL, Y-12, TVA, Volkswagen, Denso, Eastman, the City of Knoxville, TDEC and ExxonMobil. The RFP also points to ORNL's new regional-resilience initiative ([ornl.gov/regional-resilience](https://www.ornl.gov/regional-resilience/); the page returned 403 to curl). Relevant topics: "Modeling and analysis of extreme hydrologic events, flood preparedness, and long-term mitigation strategies for resilient energy-water systems"; energy dominance and resilience; resilience modeling under environmental stressors; circular economy and bioeconomy — [RFP](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/2027-RFP-and-Cover.pdf).

**ORNL, TVA and TDEC context**
- ORNL's Southeast Resilience Accelerator (SERA), an LDRD initiative that grew out of the ARMADA modeling pilot, targets risks to critical energy and industrial infrastructure in the Southeast from flooding, heat waves, drought, population growth and aging systems. Named partners are Georgia Tech, AMD and TVA — search summaries of [ORNL Regional Resilience](https://www.ornl.gov/regional-resilience/) and [ORNL ARMADA project](https://www.ornl.gov/project/action-relevant-modeling-and-decision-analysis-armada). Neither page could be opened (403), so these details are unverified.
- TVA cut power output at Browns Ferry Nuclear Plant in 2007, 2010 and 2011 because river temperatures were too high to accept discharge water — [GAO-23-105375](https://www.gao.gov/products/gao-23-105375) (search summary). TVA's 2021 Climate Action Adaptation and Resiliency Plan names drought as a risk to river-cooled generation — search summary of [TVA 2022 CAP](https://www.sustainability.gov/pdfs/tva-2022-cap.pdf).
- TNWRRC (an ISSE center) holds a five-year, $1.25M TDEC Research Priorities grant ($250K per year), which can also serve as the 1:1 match for USGS 104(b) and 104(g). Its future priorities include "water and energy use from new data centers" and "the use of AI in water-resources management and modeling" — [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf), p. 9.
- A NERC incident review describes a July 2024 Northern Virginia event in which a 230 kV fault led to the simultaneous loss of about 1,500 MW of data center load that shifted to backup power. PJM reports similar later events. NERC and FERC have opened large-load reliability work — [NERC Incident Review: Large Load Loss](https://nerc.com/pa/rrm/ea/Documents/Incident_Review_Large_Load_Loss.pdf) (seen through search summaries; the PDF was not opened); [APPA article](https://www.publicpower.org/periodical/article/nerc-incident-review-examines-risks-challenges-tied-integration-large-loads).

**Funded-project and literature checks (closest existing work)**
- NSF Award API, "data center" AND flood: no relevant award. "flash drought" AND power, "thermoelectric" AND drought AND heat, "large load" AND "extreme weather", "Tennessee Valley" AND resilience: no awards returned — [NSF API query example](https://api.nsf.gov/services/v1/awards.json?keyword=%22data%20center%22%20AND%20flood).
- The closest NSF awards found:
  - NSF [2610262](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2610262) (Lehigh, 2026-07): "Stability at the Edge: Cyber-Physical Risks and Control of Hyperscale Data Centers in Future Inverter-Dominated Grids", $518,881. It studies data center grid stability but has no hydro-climate driver.
  - NSF [2324915](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2324915)/[2324916](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2324916) (DESC): facility-level water management for data centers.
  - NSF [2009726](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2009726) (UNC, 2020): drought and electricity systems in human exposure to air pollution. It covers drought and power, but not cooling-water constraints or large loads.
- Earlier EPCL large-load awards (Lang Tong [2603293](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2603293); Lei Fan [2541996](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2541996)) cover colocation energy management and flexible data centers in unit commitment. They are recorded in `talent-pool/collaborators.md` from the 2026-11-22 scan.
- UT CEE professor Joshua S. Fu, who also holds a joint ORNL appointment, lists "climate change impacts on energy infrastructure ... water availability, ... extreme events like heatwaves, floods, drought" as a research focus — [CEE profile](https://cee.utk.edu/people/joshua-s-fu/).
- Hongyu Zhou (CEE) leads "MATCH-TES: Multi-Stage Thermal Energy Storage System for Efficient Data Center-to-Industry Heat Reuse" (ThermPulse LLC, 2026-06 to 2029-05, co-PI Xiangyu Li) — [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf), p. 25.

**ISSE records that mention the PI but are not in the talent pool (flag, do not use as "why us")**
- The ISSE 2025-2026 Annual Report's "Sponsored Research" table (p. 24) lists:
  - "AI-Driven Coupled Surface-Groundwater Modeling for Water Availability and Flood Resilience in Energy-Supporting Watersheds" (DOE Office of Science; PI Qiang He; co-PIs John Schwartz, Haochen Li and Yuefeng Hao; 2026-07-01 to 2027-03-31);
  - "Uncertainty-Aware and Cross-scale Modeling using Bayesian Inference for Wildfire Risk and Infrastructure Resilience in the Wildland-Urban Interface" (NSF; PI Jiafu Mao; co-PI Yuefeng Hao; 2026-02-01 to 2029-01-31).

  Neither project appears in the PI CV or `hao-lab.md` — [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf), pp. 24-25.
- The same table lists four Hao-led projects with active periods that the PI CV records as "Not Funded": SE CASC compound drought-heat with cover crops; USDA NIFA topography and cover cropping; USDA NIFA "Digging Deeper"; BSF AI flash floods and flash droughts (co-PIs Bing Yao, Mingzhou Jin and Ioannis Sgouralis). The talent pool and the ISSE report conflict here — [ISSE 2025-2026 Annual Report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf), p. 24, versus `talent-pool/resources/hao-lab/Yuefeng_Hao_CV.md` (Not Funded items 9-12).

**Team facts used for "why us" (all from the talent pool files)**
- Funded: USGS 104b TDEC decision support for withdrawals and thermal discharges from data centers and SMRs (PI, $84K, 2027-01); ISSE local footprint of AI data centers (PI, $60K, 2026-08); FFAR multi-source remote sensing framework and decision-support tool for flash droughts and floods (Co-PI, $434,038, 2024-04); DOE/ORNL boreal and temperate ecosystem vulnerabilities (PI, $229,835, 2024-01) — `Yuefeng_Hao_CV.md`.
- Papers:
  - flash drought WUE and recovery (*AFM* 378, 2026);
  - heatwave effects on CONUS hydrology 2003-2022 (*J. Hydrol.* 637, 2024);
  - terrestrial water storage drivers (*J. Hydrol.* 635, 2024);
  - soil moisture controls on carbon and GHG (*npj CAS* 2025);
  - wildfire-power grid interactions (*RSER* 232, 2026);
  - submitted: electricity-related water consumption for projected data center load growth (*Water Resources and Industry*), CIVE v1.0, E3SMv3 RRM overview, and the humid-Southeast fire roadmap;
  - ongoing: irrigation decision support under flash drought and flood risk with remote sensing and stochastic optimization (with Mingzhou Jin and Brian Leib)

  — `Yuefeng_Hao_CV.md`.
- Students: Yifan Gao (robust data center siting under interconnection-queue uncertainty; ML for optimization; NLP; workload scheduling); Shi Jin (tariff- and moratorium-aware siting in the Tennessee Valley; YOLO/EfficientNet inspection; infrared + LiDAR substation digital twin; 350K-record ETL) — `Yifan_Gao.md`, `Shi_Jin.md`, `hao-lab.md`.
- ORNL collaborators: Jiafu Mao, Xiaoying Shi, Yaoping Wang, Daniel M. Ricciuto, Peter E. Thornton and Forrest M. Hoffman (E3SM-RRM, CIVE) — `hao-lab.md` section 6.

### Inferences

#### Short ideas and screening (12 candidates)

| # | Idea (2-4 lines) | Angle | Lead structure | Screen verdict |
|---|---|---|---|---|
| IS1 | **Compound flash drought and heat stress on Tennessee Valley energy-water systems.** Build a 1980-2026 event catalog of flash drought, heatwave and low-flow compound events, using ET and soil-moisture early indicators and terrestrial water storage, for the river reaches that cool TVA generation and supply large-load corridors. Test whether those indicators give weeks of lead time on known cooling-water stress (e.g., Browns Ferry 2007/2010/2011). Pair with ORNL SERA and E3SM-RRM projections. | Hydro-climate science plus early warning; ORNL regional resilience; RFP topics 2 and 3 | Hao PI; co-PIs Joshua S. Fu (CEE/ORNL), Emine Fidan (BESS, UTIA) | **Pursue** (full evaluation) |
| IS2 | **Grid reliability of AI large-load growth under hydro-climate extremes.** Place data center load clusters at candidate TVA-region sites (from the students' siting models) in a transmission model. Stress it with heat-wave demand, derated river-cooled generation and voltage-sensitive large-load ride-through events. Output: reliability limits and flexibility needs. The template is the Kai Sun hydrogen-grid seed. | Power systems plus siting plus hydro-climate; energy resilience | Kai Sun (EECS/CURENT) PI; Hao co-PI | **Pursue** (full evaluation) |
| IS3 | **Flood-aware long-term mitigation for energy-water assets in the Southern Appalachians.** Use the Li flood engine's Helene hindcast and design-storm ensembles to map exposure of substations, water and wastewater plants, and candidate large-load and SMR sites. Then find mitigation portfolios (elevate, harden, relocate, add redundancy) with robust optimization under deep uncertainty. | Flood preparedness plus optimization; RFP topic 3 | Jon Hathaway or Haochen Li PI; Hao co-PI | **Revise** (full evaluation) |
| IS4 | Power-line wildfire ignition risk under flash drought in the humid Southeast WUI, using the *RSER* 2026 review and the fire roadmap. | Wildfire-grid | Jiafu Mao or Hao | **Drop**: the ISSE report lists an NSF WUI wildfire-infrastructure project (PI Mao, co-PI Hao, 2026-2029) that would cover it; the status is unverified |
| IS5 | Precision poplar on fragipan and marginal soils as bioeconomy feedstock plus carbon (G×E×M), reusing the unfunded Allen Family proposal text. | Circular bioeconomy (RFP topic 4) | Hao PI or co-PI with a UTIA forestry partner | **Revise**: no UTIA poplar partner identified; Hao's PI slot is better spent on IS1; could be a 2028 seed |
| IS6 | Data center waste heat and water circularity: match data center heat to greenhouses and industry, and reclaimed water to cooling demand, by facility-location optimization. | Circular economy plus optimization | Hongyu Zhou PI; Hao co-PI | **Revise**: overlaps Zhou's MATCH-TES project and CBET **E3**; a data center focus also reads like the current Hao seed |
| IS7 | Computer-vision inventory of flood- and heat-exposed energy-water assets (substations, cooling towers, intakes) from aerial and satellite imagery, building on Shi Jin's substation inspection work. | AI data layer | module | **Revise**: use as a data task inside IS2 or IS3 (Shi Jin starts Spring 2027) |
| IS8 | Urban heat, cooling-driven electricity demand and stormwater evaporative cooling in Knoxville, with the City of Knoxville. | Built environment, environmental health | Hathaway or Ellis PI; Hao co-PI | **Drop for Hao**: Hao would be a minor add-on; overlaps the pending Schmidt Sciences buildings proposal and Hathaway's USACE evaporative-cooling award |
| IS9 | Agricultural flash-drought irrigation and its energy-water demand. | Agriculture | Hao | **Drop**: duplicates the FFAR grant (Co-PI) and CAREER **K3** / 104(b) **I1** |
| IS10 | NLP extraction of drought, flood and heat triggers and resilience commitments from TVA, LPC, TDEC and utility plans (Yifan Gao). | Policy text mining | module | **Revise**: a task inside IS1; overlaps the 104(b) student idea **I4** |
| IS11 | SMR siting under flood and drought hazards. | Nuclear | Jamie Coble PI; Hao co-PI | **Drop**: the 104b TDEC grant covers SMR water; Powe **PW1** covers SMR deployment |
| IS12 | Flash-drought and flood "whiplash" in TVA reservoir and hydropower operations. | Reservoir operations | Hao | **Revise**: fold into IS1 as an aim if TVA data can be had |

#### Full evaluation 1: IS1 (Pursue; Hao as PI)

**Title.** When rivers run low and hot: compound flash drought-heatwave stress on
Tennessee Valley energy-water systems.

**Team.** PI Yuefeng Hao (ISE). Co-PI Joshua S. Fu (CEE; joint appointment in
ORNL Computational Earth Sciences), for regional climate and extremes
projections and climate impacts on energy infrastructure
([profile](https://cee.utk.edu/people/joshua-s-fu/)). Co-PI Emine Fidan
(Biosystems Engineering and Soil Science, UTIA), for water availability, flood
risk and AI on landscapes; a past ISSE seed PI whose FY26 seed showcase was
"Evaluating Water Availability and Sectoral Demand for Sustainable Allocation"
([ISSE annual report](https://isse.utk.edu/wp-content/uploads/sites/5/2026/11/ISSE-2025-2026-Annual-Report-compressed-2.pdf);
[UTIA profile](https://utia.tennessee.edu/person?id=11763), search summary).
Student roles: Yifan Gao (IS10 text task) and, from Spring 2027, Shi Jin.
External partners to invite: the ORNL E3SM/ORNL team already in the PI's
collaborator list (Jiafu Mao, Xiaoying Shi, Yaoping Wang); ORNL SERA; TVA (river
temperature, flow and derate records, which would need a data request). No
partner has agreed to anything.

**Research question.** Do compound flash drought-heatwave events in the
Tennessee Valley give a detectable land-surface signal (ET deficit, soil
moisture drawdown, terrestrial water storage anomaly) weeks before the river
low-flow and high-temperature conditions that constrain river-cooled
generation? And how will the frequency of such events change under E3SM-RRM and
downscaled projections?

**Approach.** (1) An event catalog from multi-source remote sensing and drought
indices, with triple collocation for merging indicators. (2) Lagged links from
those indicators to USGS flow and temperature at intakes and to known TVA
curtailment periods. (3) A projection of event frequency with Fu's downscaled
climate and ORNL's E3SM-RRM. (4) A short screening of which corridors with
announced large-load growth face the highest compound risk, reported as a map,
not as a siting decision.

**Closest existing projects and papers, and the gap.** No NSF award matched
flash drought with power or thermoelectric drought-heat (NSF API checks above).
The closest NSF award, [2009726](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2009726),
links drought, electricity and air-pollution exposure, not cooling-water
constraints. The documented Browns Ferry derates
([GAO-23-105375](https://www.gao.gov/products/gao-23-105375)) and TVA's drought
risk statement ([TVA CAP](https://www.sustainability.gov/pdfs/tva-2022-cap.pdf))
show the hazard but not a land-surface early-warning signal. ORNL SERA works on
heat, drought and flood risk to Southeast energy infrastructure (search summary
only); its methods and outputs could not be read, so the IS1 gap claim against
SERA is provisional. The gap: flash-drought onset science, which is the PI's
specialty, has not been tied to energy-water operations in this basin.

**Novelty.** It moves flash-drought and heatwave hydrology from ecosystems and
agriculture to the thermal and low-flow limits of an energy system, and it
gives SERA a land-surface early-warning layer.

**Why us (talent pool facts only).**
- First-author papers on heatwave effects on CONUS hydrology (*J. Hydrol.* 637, 2024) and on flash-drought WUE and recovery (*AFM* 378, 2026).
- Triple-collocation drought-index integration (*SERRA* 2022), PT and BMA ET algorithms, and terrestrial water storage drivers (*J. Hydrol.* 635, 2024).
- Co-PI on the FFAR multi-source remote sensing flash drought and flood tool.
- E3SM-RRM co-authorship and a DOE/ORNL grant with ORNL modelers.
- A submitted paper on electricity-related water for data center load growth.

**Fundability against ISSE criteria.**
- Mission fit: RFP topics 2 and 3 (resilience modeling under stressors; extreme hydrologic events for energy-water systems).
- Originality and national priority: energy reliability and water.
- Feasible in one year: existing data only, plus ORNL outputs.
- Collaboration: CEE, UTIA, ISE, ORNL and TVA.
- External plan: see the targets below.

**Two external targets.**
- (1) DOE Office of Science BER via the FY2027 continuation solicitation DE-FOA-0003665, tracked idea **B1** (`funding/summaries/2026-10.md`). Award size per topic is not stated there, so the target amount must be set by the team after talking to the program manager. Submit before 2027-04-01 for FY2027, or use the seed results for FY2028. The tracked notes say odds are modest given the FY2027 budget request.
- (2) USGS Powell Center working group, tracked idea **PC1** (next annual call; the FY2028 call closes 2027-01-31, before the seed starts, so the FY2029 call fits the seed timeline). The award is travel for up to 15 participants plus an optional fellow up to $100K (`funding/2026-11-22.md`).
- A fallback multi-investigator target is NSF BIO **BE1** only if it is recast. Do not use CAREER **K1**: it is single-investigator, and the ISSE cover sheet requires multi-investigator follow-on proposals.

**Risks.**
- (a) Overlap with the current Hao ISSE seed, which names heat-wave electricity demand and water conditions. Keep IS1 free of siting, noise, land markets and the web tool, and state that in the narrative.
- (b) Overlap with the 104b TDEC grant (from 2027-01). No facility withdrawal or thermal-discharge decision support in IS1.
- (c) Overlap with the DOE-SC project listed by ISSE (Qiang He PI, Hao co-PI, "Water Availability and Flood Resilience in Energy-Supporting Watersheds"). Its status and scope must be confirmed. If it is active, IS1 must be framed as atmospheric and land-surface compound-event science, not surface-groundwater modeling, and listed as related support.
- (d) TVA data access is not secured.
- (e) Fourteen days to collect three CVs and all department-head signatures.
- (f) Hao's current seed runs to 2027-06-30, so the two seeds overlap for six months. The budget must show separate effort, and students on the current seed (Gao, Keating) need distinct tasks.

**Verdict: Pursue**, as the single proposal with Hao as PI.

#### Full evaluation 2: IS2 (Pursue; Kai Sun as PI, Hao as co-PI)

**Title.** Will the grid hold? Transmission reliability of AI large-load growth in
the Tennessee Valley under heat, drought and flood extremes.

**Team.** PI Kai Sun (Professor, EECS; CURENT member; former EPRI project
manager for grid operations and planning; research in power system stability,
control and optimization; [EECS profile](https://eecs.utk.edu/people/kai-sun/)).
Kai Sun led the ISSE seed on large-scale hydrogen production and transmission
systems ([ISSE 2023-24 report](https://isse.utk.edu/wp-content/uploads/sites/5/2024/10/2023-24-THEC-report-FINAL-web.pdf)).
Co-PI Yuefeng Hao (hydro-climate stress scenarios; siting inputs). Optional
co-PI from the registry: Leon M. Tolbert (CURENT; past ISSE seed PI;
SMR-centered microgrids for data centers) or Hector A. Pulgar (CURENT). Students:
Shi Jin (tariff- and moratorium-aware siting model gives candidate load
locations) and Yifan Gao (queue-uncertainty model). Partners to invite: TVA;
ORNL Next-Generation Data Centers Institute / GRID-C (in the registry). No one
has agreed.

**Research question.** How much AI data center load can the TVA-region
transmission system host at plausible sites while staying secure during compound
heat-wave demand peaks, derated river-cooled generation, and voltage
disturbances that make data center loads trip to backup power at once?

**Approach.**
- (1) Candidate load clusters from the students' siting models, plus announced projects.
- (2) Hydro-climate stress cases from the PI's heatwave and flash-drought definitions: concurrent demand, derating and outage cases.
- (3) Steady-state and dynamic studies on a synthetic or CURENT test-bed model of the region, using Kai Sun's multi-timescale simulation methods from the hydrogen seed.
- (4) Metrics: hosting limits, ride-through and flexibility needed.

**Closest existing projects and papers, and the gap.**
- NSF [2610262](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2610262) (hyperscale data centers in inverter-dominated grids; no climate stress).
- EPCL large-load awards [2603293](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2603293) and [2541996](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2541996) (colocation and flexible data centers in unit commitment).
- The NERC large-load-loss incident review (event analysis, not a hydro-climate study).

None of these combines load placement with compound hydro-climate stress on a
river-cooled fleet. That combination is the gap the tracked EPCL idea **P1**
also claims (`funding/2026-11-22.md`).

**Novelty.** Load location becomes a decision-relevant input to reliability
studies under hydro-climate stress. Hydro-climate stress is usually missing from
grid-side data center studies, and grid dynamics is usually missing from
hydro-climate studies.

**Why us (talent pool facts only).**
- The *RSER* 2026 review of wildfire-power grid interactions (with Fangxing Fran Li, Mingzhou Jin, Jiafu Mao).
- Heatwave and flash-drought papers.
- Two funded data center grants (ISSE footprint; 104b TDEC).
- The submitted electricity-related water paper.
- Shi Jin's Tennessee Valley siting model and substation digital-twin inspection experience; Yifan Gao's queue-uncertainty siting model.

Kai Sun's grid record is external (EECS profile and ISSE reports), not a talent
pool fact.

**Fundability against ISSE criteria.**
- Mission fit: "technologies related to energy dominance and resilience" plus energy-water extremes.
- Originality: ties into current NERC and FERC attention to large loads.
- Feasibility: test-bed models and existing load lists.
- Collaboration: EECS/CURENT, ISE, TVA and ORNL.
- External plan: the targets below.

The structure (a non-awardee PI) avoids the open question of whether a current
ISSE awardee may be PI again.

**Two external targets.**
- (1) NSF ECCS EPCL (NSF 26-514, rolling), tracked idea **P1**. Recent EPCL large-load awards ran $200K-$585K; a planning target of about $500K over 3 years is a team choice, not a sponsor figure.
- (2) NSF CMMI core (NSF 26-515, rolling; 225-275 awards, $100M total), using the held idea **C2** framing (data center-grid-water system-of-systems resilience). This target must follow the partition rule in `summaries/2026-10.md`: if **P1** or CAREER **K1** is pending, C2 cannot carry the same core.

A TVA- or EPRI-sponsored study is a possible third route but was not checked.

**Risks.**
- (a) P1 and K1 partitioning (see `2026-11-22.md`).
- (b) The grid model: TVA's real network data are restricted, so a synthetic grid may be needed (not checked).
- (c) The current Hao seed also names heat-wave electricity demand. IS2 must be about transmission reliability, not about where data centers should go.
- (d) Kai Sun's interest and availability are unknown.
- (e) The 14-day timeline.

**Verdict: Pursue**, with Kai Sun as PI. This is the safest structure.

#### Full evaluation 3: IS3 (Revise; only if Haochen Li's team leads)

**Title.** From forecast to mitigation: flood-robust protection and siting of
energy-water assets in the Southern Appalachians.

**Team.** PI Jon Hathaway (Professor, CEE; sustainable urban water and green
infrastructure; [CEE profile](https://cee.utk.edu/people/jon-hathaway/)).
Hathaway is a co-PI on the Li seed and led the UT team on a $4.3M urban-tree
project with the City of Knoxville
([ISSE news list](https://isse.utk.edu/news/)). Alternatively Haochen Li as PI,
if ISSE confirms a current awardee may apply. Co-PIs: Haochen Li (flood
engine); Yuefeng Hao (robust and stochastic optimization; flood and remote
sensing decision support); optionally Kelsey Ellis (registry; community
vulnerability). Partners: TVA, the City of Knoxville or KUB, TDEC.

**Research question.** Given high-resolution flood hazard ensembles, which
long-term mitigation portfolio for substations, water and wastewater plants, and
candidate large-load sites minimizes expected service loss under deep
uncertainty in storm frequency?

**Approach.** Exposure overlay on the Li engine's Helene hindcast and design
storms, then a two-stage robust or stochastic program for mitigation. Shi Jin's
computer vision (IS7) supplies the asset inventory.

**Closest existing projects and papers, and the gap.** The Li seed does
forecasting for transportation and planning users. The DOE-SC project listed by
ISSE (Qiang He PI) covers "Flood Resilience in Energy-Supporting Watersheds"
(scope not read). The search found no 2025 peer-reviewed exposure study of
Helene's effects on substations and water plants, only news and utility
accounts (e.g., [ENR on Asheville water repairs](https://www.enr.com/articles/59387-repairs-to-water-infrastructure-underway-after-hurricane-helene)).
The gap is the mitigation-decision layer. This is a thin claim: the literature
check was one search.

**Novelty.** The step from flood forecasts to optimized long-term mitigation of
energy-water assets.

**Why us (talent pool facts only).**
- Co-PI on the FFAR flash drought and flood decision-support tool.
- Ongoing stochastic optimization paper on irrigation under flash drought and flood risk.
- Robust siting models by both students.
- The USGS 104b TDEC decision-support grant.

**Fundability.** Direct hit on RFP topic 3 ("flood preparedness, and long-term
mitigation strategies for resilient energy-water systems"). But the reviewers
are funding the Li seed now, and a second proposal from much of the same team
could read as a continuation.

**Two external targets (if pursued).**
- (1) NSF CMMI core (NSF 26-515), a disaster-resilience framing; not yet tracked as its own idea; verify program fit.
- (2) The TNWRRC USGS 104(b) FY2028 round, which can use TDEC Research Priorities match. This is tracked as a program in `2026-11-19.md`, idea **I1**, but IS3 would be a new idea; keep it off data center water to protect the 104b TDEC grant.

**Risks.**
- (a) Overlap with the Li seed and with the DOE-SC project.
- (b) Hathaway and Li are already committed to the Li seed.
- (c) A third Hao-involved proposal spreads the lab thin.
- (d) The 14-day timeline.

**Verdict: Revise.** Raise it with Haochen Li and Jon Hathaway as a 2027 follow-on
that their team leads. If they prefer to keep their seed's scope clean, drop it
for 2027.

#### Structure, overlap and submission plan
- **Hao's PI slot.** The RFP allows one PI submission per researcher, so Hao can be PI on IS1 and co-PI on IS2 (and IS3). The RFP does not say whether a current awardee can be PI again. Its line that continuation "will require the submission and approval of a new seed grant proposal" suggests repeat proposals are expected, but that is an inference. Ask ISSE staff before 2026-12-09. If the answer is no, move IS1 to Joshua S. Fu as PI with Hao as co-PI.
- **Safest structure overall.** IS2 with Kai Sun as PI carries no reapplication risk. If only one proposal is feasible in 14 days, submit IS2.
- **Mingzhou Jin.** Jin is ISSE director and receives the proposals, and is a frequent co-author of the PI. The RFP says nothing about conflicts of interest or review. These notes make no assumption either way, and Jin is not listed as a team member in any idea.
- **External-target uniqueness.** IS1 seeds **B1** and **PC1**. IS2 seeds **P1** and CMMI **C2**. IS3 targets a new CMMI framing and 104(b). Keep **P1** (IS2) and **K1** apart as the 2026-11-22 notes require. CAREER K1 cannot be a named target: it is single-investigator, and ISSE requires multi-investigator follow-on proposals.
- **Current and pending support.** List the current ISSE seed, 104b TDEC, FFAR and DOE/ORNL in every proposal. Resolve the status of the two ISSE-listed projects (Qiang He DOE-SC; Mao NSF WUI) before writing support statements.

### Gaps
- The ORNL regional-resilience (SERA) and ARMADA pages returned 403 to curl. SERA details come only from search summaries, so SERA's methods, data and contacts are unverified.
- The status of the DOE-SC (Qiang He) and NSF (Jiafu Mao) projects that the ISSE annual report lists with Hao as co-PI, and of the four CV "Not Funded" items the report shows with active periods, could not be resolved. The user should check the resource files.
- The NERC incident review PDF, GAO-23-105375 and the TVA CAP were seen only through search summaries.
- The literature checks were limited: the NSF Award API (loose keyword matching) and a few web searches. Thermoelectric water-vulnerability literature (e.g., the van Vliet and Miara line of work) was not reopened, and Google Scholar, USAspending and DOE award lists were not queried for IS1 to IS3.
- The DOE BER per-topic award size and the EPCL per-award amount are not stated by the sponsors, so the targeted amounts in the narrative are planning choices.
- No ISSE guidance was found on whether a current awardee may be PI again, or on budget overlap between consecutive seeds.
- TVA and ORNL data and partnership availability, and the interest of every named UT faculty member, are unknown. No one has been contacted.
