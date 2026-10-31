# NOAA CPO FY2027 SI/ML Innovation (NOAA-OAR-CPO-2027-33392): idea screening for Hao Lab

Research date: 2026-10-31. Researcher notes for the report writer. Team facts come only from `talent-pool/labs/hao-lab.md` and `talent-pool/resources/hao-lab/*.md`. Call facts come from the NOFO PDF ([NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)), which was read in full.

Access notes: cpo.noaa.gov returns 403. utk.edu and ornl.gov pages returned a Cloudflare "Attention Required!" bot-check page, so the ORNL RiTHyMs and UT ReForM items below rely on search-result snippets and are marked unverified. I ran the NSF Award API with quoted phrases (unquoted keyword queries return noise). I found no list of NOAA CPO awards for FY2024–FY2026, so the NOAA side of the prior-award check is incomplete.

Ideas at the end (5): **N1 Pursue** (PA3a, Tennessee Valley heat thresholds for the energy-water system; this is the lead), **N2 Revise** (PA3a agriculture and rural water, folded into N1 as a module), **N3 Revise** (PA3b soil-moisture forecasts of opportunity; standalone only with an S2S co-PI), **N4 Drop** (PA2), **N5 Drop** (PA1b emulator).

## What does the NOFO require, and how is it scored?

### Takeaway
Technical merit carries 50% of the score. Every priority area requires physically interpretable SI/ML results, NOAA data, SI/ML-ready public data, NOAA partner engagement and letters of support. PA3 also requires engagement with NIHHIS partner agencies. The team-composition language favors teams that combine SI/ML and domain expertise and include end users.

### Cited Findings
- Up to 15 awards, most up to $250,000 per year, 1–3 years, no cost share. Institutions of higher education are eligible. LOIs are due by email by 11:59 p.m. PT on 2026-11-17 (strongly encouraged, max 2 pages); full applications are due 2027-02-09. CPO replies to LOIs within four weeks, encouraging or discouraging a full application. — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- PA3a: "identify extreme heat thresholds for hazards to people and property, and model the complex interactions unleashed by extreme heat across U.S. systems and infrastructure." Its examples include "soil moisture data, in combination with water scarcity, power outages, health and air quality indicators, and infrastructure stressors." Research "should focus on examining and modeling thresholds and interactions of relevance across health, built infrastructure, and agriculture." — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- PA3b: research on forecast-of-opportunity windows "must provide a physical interpretation regarding the sources of predictability" and "should include assessing whether NOAA models and forecasting systems (research or operational) capture such forecast opportunities." — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- PA3 proposals should "Apply relevant NOAA data (e.g., from NESDIS, NWS)" and "Engage with NIHHIS partner agencies to inform research and communicate findings." — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- PA1 requires M2D (2–10 year) predictions, benchmarking against conventional approaches, interpretability with process fidelity, and NOAA SPEAR/CMIP6 or comparable data. PA1b targets "SI/ML emulators of NOAA models." Teams "should demonstrate a clear understanding of NOAA's stakeholders predictive M2D needs." — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- PA2 must "apply socio-economic methodologies." Small and mid-sized communities and organizations are "of particular interest," and PIs are "strongly encouraged to collaborate with NOAA staff." — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- Requirements across all areas include interpretation in domain-science terms, public SI/ML-ready NOAA data, an optional NOAA Learning Journeys Python notebook, AI workforce development through students, partners such as state and local governments, team members from user communities, and letters of support from community and partner organizations. — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- Scoring weights: Importance/relevance 25% (this includes the PI's record of making data accessible and the data sharing plan), technical/scientific merit 50%, qualifications 15%, costs 10%. Proposals scoring below 3.0/5 are not considered. Selection factors include "Duplication of other projects funded or considered for funding by NOAA/Federal agencies." — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- Applicants need eRA Commons before submission. Organizations registering for the first time should allow 2–4 weeks, and a PD/PI account is required on the SF-424. "Double dipping" with other federally funded projects is not permitted. The start date is 2027-09-01. — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- PA3 program contacts: Barbara Boustead (NIHHIS), Dan Barrie (MAPP) and Andrea Miralles-Barboza (AdSci). PA1: Dan Barrie. PA2: Bhaskar Subramanian. — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)

### Inferences
- PA3a's wording ("soil moisture … water scarcity, power outages … infrastructure stressors … agriculture") reads almost like a description of the PI's established expertise plus the lab's energy-water thread. That is the strongest fit in this call.
- The two lowest-cost ways to meet the NIHHIS and letter-of-support requirements are a state agency (TDEC, already a 104b decision-support partner in the funded grant title) and a utility or regional partner. Every partner other than TDEC's role in the 104b grant title is unconfirmed.
- With 50% on technical merit, the ML design has to be credible. The lab has no ML-for-prediction publications; Shi Jin has ML engineering experience and Yifan Gao has an ML-for-optimization interest. A co-investigator with an S2S or ML-for-climate publication record would strengthen any proposal.

### Gaps
- I could not open cpo.noaa.gov (403), so I did not verify which MAPP, NIHHIS or AdSci SI/ML or heat projects were funded in FY2024–FY2026.
- I did not verify that UT Knoxville holds an institutional eRA Commons registration or that the PI has a PD/PI account (no talent-pool information).

## Idea N1 (from candidate 2): Heat thresholds and cascading interactions in the Tennessee Valley energy-water system — Pursue (lead)

### Takeaway
River-temperature ML for TVA already exists (ORNL RiTHyMs; UT ReForM). National ML outage-vulnerability indices also exist. I found no funded work or paper that uses interpretable ML to identify compound heat and flash-drought thresholds at which cooling-water limits, load peaks (including new data-center loads) and outages cascade. The fit to PA3a is strong, and Hao Lab's data-center water grants are concrete assets. The proposal has to stay clear of river-temperature forecasting and of the lab's own 104b scope.

### Cited Findings
- Browns Ferry (TVA) may not discharge water above 90°F under its ADEM NPDES permit. When the Tennessee River warms, TVA derates instead: a 2011 report says a heat wave forced a TVA nuclear plant to run at 50% for eight weeks at a cost of $50M, and one unit shut down in August 2007 because intake water was too hot. These are 2007–2011 news sources, and the current permit terms were not verified. — [Climate Central](https://climatecentral.org/news/in-tennessee-heat-waves-frustrate-nuclear-power); [Inside Climate News 2011](https://insideclimatenews.org/news/20110414/southeast-extreme-heat-growing-concern-nuclear-power-operators); [APR 2007](https://www.apr.org/2007-08-17/heat-and-drought-shut-down-tva-reactor); [NRC document](https://www.nrc.gov/docs/ML1828/ML18283B708.pdf)
- A news item reports that a heat wave caused problems for Tennessee data centers (archived; not opened). — [DCD](https://www.datacenterdynamics.com/en/news/heat-wave-causes-headache-for-tennessee-data-centers/)
- ORNL's RiTHyMs is an LSTM river-temperature model with an average absolute error of 1.1°C that stayed accurate during hot events. It is reportedly being applied to TVA's managed rivers and utility operations. ORNL's Sean Turner uses deep learning to predict how rising water temperatures could affect TVA hydropower and nuclear operations. These come from search snippets only; the pages were behind a Cloudflare check. — [ORNL news](https://www.ornl.gov/news/ai-model-delivers-river-temperature-insights-strengthening-us-energy-security); [HPCwire 2026-01-15](https://www.hpcwire.com/aiwire/2026/01/15/ornls-sean-turner-on-using-ai-to-bridge-river-models-power-grid-operations/)
- UT Knoxville (Khojandi and Hathaway group) built ReForM, a hybrid physics plus sensor-data river-temperature forecasting model for TVA. This also comes from a search snippet; the page was behind a Cloudflare check. — [UT CEE](https://cee.utk.edu/tce-group-develops-novel-forecasting-model-to-predict-river-temperature/)
- Ma, Li, Omitaomu and Mostafavi (Applied Energy, 2025) built a county-level Power System Vulnerability Index from about 179M outage records (2014–2023) using interpretable ML. It is not specific to heat thresholds. — [IDEAS/RePEc](https://ideas.repec.org/a/eee/appene/v397y2025ics0306261925010906.html); [ORNL record](https://www.ornl.gov/publications/establishing-nationwide-power-system-vulnerability-index-across-us-counties-using-interpretable-machine-learning-2/)
- NSF Award API: quoted-phrase searches for "power outage" "heat", "extreme heat" "threshold", "thermoelectric" "water temperature" and "data center" "extreme heat" returned 0 awards. — [NSF API example](https://api.nsf.gov/services/v1/awards.json?keyword=%22data%20center%22%20%22extreme%20heat%22)
- Hao Lab assets (talent pool): the PI's USGS 104b grant "Decision Support for TDEC to Reduce Freshwater Withdrawals and Thermal Discharges from Data Centers and SMRs in Tennessee" ($84K, 2027-01, PI); the ISSE grant "Local Footprint of AI Data Centers: Noise, Water, and Land-Market Tradeoffs in Tennessee" ($60K, 2026-08, PI); Hao et al. 2024, "Evaluating the effects of heatwave events on hydrological processes in the contiguous United States (2003–2022)" (J. Hydrol. 637); the submitted K. Jin & Hao paper, "Regional screening of electricity-related water consumption for projected data-center load growth"; Mao, Hao et al. 2026, "Wildfire–Power Grid Interactions" (RSER 232); Shi Jin's paper in progress on tariff- and moratorium-aware data center siting in the Tennessee Valley; Yifan Gao's work on robust siting under interconnection-queue uncertainty; and Shi Jin's YOLO/EfficientNet and infrared+LiDAR substation inspection experience. — `talent-pool/labs/hao-lab.md`; `resources/hao-lab/Yuefeng_Hao_CV.md`; `resources/hao-lab/Shi_Jin.md`

### Inferences
- **Sharpened idea.** Interpretable ML (gradient boosting with SHAP, or monotone or threshold-detecting models, benchmarked against logistic and segmented regression) learns joint air-temperature × soil-moisture/flash-drought × river-temperature × load thresholds for three outcomes: (a) thermoelectric derates and curtailments, (b) heat-driven load peaks and outages, and (c) water-supply stress. The inputs are NOAA nClimGrid, URMA/RTMA, NWS heat products, NESDIS/SMAP-era soil moisture, USGS stream temperature, EIA-923/860 plant data and EIA/DOE outage records. The project then maps how projected data-center load growth shifts those thresholds. Outputs are an SI/ML-ready threshold dataset and a Learning Journeys notebook.
- **Gap.** Prior work forecasts river temperature (ORNL, UT) or ranks general outage vulnerability (Ma et al.). The open space is threshold identification across the coupled heat, drought, cooling-water, load and outage chain, with data-center growth as a new stressor, and NOAA heat information as the trigger. The novelty looks real, provided the project uses RiTHyMs or ReForM outputs, or simple physics, as inputs rather than reinventing them.
- **Why us.** Hao Lab is the only team I found that combines funded Tennessee data-center water and thermal-discharge decision support (104b with TDEC, plus ISSE), PI heatwave-hydrology and flash-drought research, and two students building Tennessee Valley siting models. Missing pieces: a power-systems or grid-data co-investigator, TVA or utility data access, a health component (PA3a lists health, but it is optional), a NOAA collaborator and a NIHHIS partner engagement. All partners are unconfirmed. UT's ReForM group and ORNL are natural partners, but neither appears in the talent pool, so they cannot be cited as team assets.
- **Overlap and duplication.** (1) The funded 104b grant covers withdrawals and thermal discharges for TDEC decision support. N1 must frame 104b as preliminary work and data access and must not repeat its deliverables, because the NOFO bars double-dipping. (2) In the 2026-10-21 scan, idea B1 (DOE BER: Tennessee Valley water availability under compound flash drought-heat, AI-enhanced E3SM-RRM) and C2 (CMMI-EBE, held) are close. Keep B1 as Earth-system predictability with E3SM, and keep N1 as observation-driven ML thresholds and NOAA heat information. List both in Current and Pending. E2 (EWRE, SMR thermal discharge module) also touches this space; keep facility design out of N1.
- **Budget fit.** Three years at about $200–250K/yr would fund 1–2 students (Shi Jin for the ML pipeline, Yifan Gao for scenario and load analysis) plus PI summer salary and a small partner subaward. That is commensurate with the call.
- **Risks.** The LOI is due in 17 days. A first application to NOAA needs eRA Commons. No NOAA or NIHHIS partner is confirmed. Outage data at the needed resolution (EIA OE-417 or EAGLE-I) may be coarse. Reviewers may see the project as energy-sector work rather than heat-health; keep heat thresholds for people (outage-driven loss of cooling) in the framing.

### Gaps
- I could not open the ORNL or UT pages (bot check), so the scope of RiTHyMs and ReForM is unverified. Confirm before the LOI.
- I found no 2024–2026 confirmation of TVA derate events or the current permit limit.

## Idea N2 (from candidate 1): Compound heat and flash-drought thresholds for Southeastern agriculture and rural water supply — Revise (module of N1)

### Takeaway
Flash-drought AI is a crowded and recently funded field (NSF CAIG at UCLA/Ohio State in 2026, an NSF EAGER, an Auburn CAREER). Heat-specific thresholds conditioned on soil moisture for humid Southeastern crops and small water systems are less covered. Even so, the idea overlaps the PI's FFAR grant and the earlier USDA A1712 idea, and it is weaker than N1 as a standalone NOAA proposal.

### Cited Findings
- NSF 2616278/2616279, "Collaborative Research: CAIG: Leveraging Artificial Intelligence for understanding and forecasting flash drought development and propagation" (Liu, UCLA; Zhang, Ohio State; start 2026-08-15; $502,520 + $390,000). It builds an "interpretable, multi-modal, multi-task" deep learning framework for flash-drought prediction that uses vegetation, soil moisture and heat. — [NSF API 2616278](https://api.nsf.gov/services/v1/awards/2616278.json?printFields=id,title,abstractText)
- Other NSF flash-drought awards: EAGER CHIRRP 2435046 (Mishra, TEES, 2024; community tools for agriculture); CAREER 2144293 (Tian, Auburn, 2022; agricultural flash droughts); 2414601 (Chen, UNL, 2024; land-atmosphere interactions in flash drought); 2303457/2303458 (Otkin/Gerken, 2023; land-atmosphere feedbacks); CAS-Climate 2406295/2445027 (Mishra; compound extremes in breadbaskets). — [NSF API "flash drought"](https://api.nsf.gov/services/v1/awards.json?keyword=%22flash%20drought%22)
- Bogenreuther et al. (Agric. For. Meteorol. 2025) found that compound heat-drought events matter more than single events for grain maize, and that absolute thresholds explain yield variability better than relative ones (region not verified; likely Europe). — [Bayreuth PDF](https://epub.uni-bayreuth.de/8863/1/1-s2.0-S0168192325004551-main.pdf)
- An EGU24 abstract (Sohoulande and Khedun) used random forests with SPEI to relate drought to corn, cotton, peanut and soybean yields in North Carolina, South Carolina and Georgia. It did not cover heat. — [EGU24-2908](https://meetingorganizer.copernicus.org/EGU24/EGU24-2908.html)
- Hao Lab assets: the FFAR grant "Multi-source remote sensing framework and decision-support tool for flash droughts and floods" (Co-PI, $434K, 2024-04, 3 years); the irrigation decision-support paper in progress (Xi, Hao, Leib, Jin); the unfunded SE CASC proposal "Building Resilience to Compound Drought and Heat Extremes … Southeastern Agroecosystems" (shows prior framing, not a funded asset); and ET/BMA and soil-moisture papers. — `resources/hao-lab/Yuefeng_Hao_CV.md`

### Inferences
- The gap is narrower than it looks: flash-drought prediction with AI is funded. What remains is heat-impact thresholds for agriculture and rural water conditioned on soil moisture, using NOAA heat products. That fits PA3a ("agriculture") but needs crop or livestock and water-system outcome data and an agricultural partner, none of which is confirmed.
- Overlap risk with the FFAR grant (same flash-drought decision-support theme) and with R1 in the 2026-10-25 scan (USDA A1712, flash-drought forage and stock water for Tennessee cattle producers).
- Verdict: **Revise.** Fold it into N1 as an agricultural and water-supply outcome module (same threshold engine, a second sector), which also strengthens the "across health, built infrastructure, and agriculture" language. Do not submit it as a separate NOAA proposal.

### Gaps
- I did not find a Southeast-specific ML study of compound heat-flash drought yield thresholds; the gap claim rests on the searches above.

## Idea N3 (from candidate 3): Forecasts of opportunity for U.S. extreme heat preconditioned by soil-moisture deficits — Revise

### Takeaway
The scientific gap is plausible: published ML forecast-of-opportunity work centers on Europe, the tropics as the predictability source, or stratospheric coupling, not U.S. heat driven by soil moisture with NOAA-system evaluation. But PA3b is scored mostly on S2S prediction expertise, which the talent pool does not document. Pursue it only as an aim of N1 or with a confirmed S2S or ML co-PI.

### Cited Findings
- NSF 2616256/2616257, "CAIG: Predictability from Stratosphere-Troposphere Coupling Using Physics-Informed AI Emulators" (SUNY Albany, Penn State, 2026), aims "to uncover critical 'forecasts of opportunity'." Only 3 NSF awards mention "forecasts of opportunity." — [NSF API](https://api.nsf.gov/services/v1/awards.json?keyword=%22forecasts%20of%20opportunity%22); [NSF API 2616257](https://api.nsf.gov/services/v1/awards/2616257.json?printFields=id,title,abstractText)
- NSF 2435262/2435263, "Role of Atmospheric Heat Transport, Radiation and Soil Moisture on Observed Heatwaves, Their Representation in Climate Models and Future Changes" (University of Washington and a University of California campus). This is process work on soil moisture and heatwaves, not ML forecasts of opportunity. — [NSF API "heatwave"](https://api.nsf.gov/services/v1/awards.json?keyword=%22heatwave%22)
- Neural-network forecasts-of-opportunity work by Mayer, Barnes and colleagues used CESM2-LE, with tropics-driven predictability (Arcodia et al. 2023). — [CSU thesis record](https://mountainscholar.org/items/161d2fe0-d221-4864-a065-847307ac8406); [Arcodia NOAA S2S webinar](https://www.weather.gov/media/climateservices/Arcodia-NOAA-S2S-APS-Webinar.pdf); [DOE EESM record](https://eesm.science.energy.gov/publications/assessing-decadal-variability-subseasonal-forecasts-opportunity-using-explainable-ai)
- European studies: van Straaten et al. (random forests with XAI; windows of opportunity for western and central European summer heat; predictability passes from land and SST into the atmosphere) and Weirich-Benet et al. (ML beats the ECMWF hindcast at 3+ weeks for central European heatwaves; soil moisture is an important predictor). — [PIK PDF](https://publications.pik-potsdam.de/pubman/item/item_28103_1/component/file_28111/28103oa.pdf); [WCE 2024 (DOAJ)](https://doaj.org/article/5d720f87d154453294b912e23d052a58)
- A subseasonal soil moisture and evaporative-demand study reports "skillful forecasts of opportunity" for 20–50% of forecasts in weeks 3–6. — [NSF PAR 10458479](https://par.nsf.gov/servlets/purl/10458479)
- An AI S2S preprint (TianXing-S2S) argues that skillful extreme-heat S2S forecasting requires land-atmosphere interactions. — [arXiv 2512.12545](https://arxiv.org/pdf/2512.12545)

### Inferences
- **Gap.** Interpretable ML identification of U.S. (especially Southeast and Central U.S.) heat forecast-of-opportunity windows tied to soil-moisture and flash-drought states, then a test of whether NOAA systems (GEFS, CFSv2, SPEAR seasonal) reproduce them. This matches the PA3b text, and I found no direct U.S. study. The novelty is moderate: the land-heat coupling mechanism is well known, and the new contribution is ML-diagnosed state dependence plus NOAA-system verification.
- **Why us (partial).** The PI's papers on heatwave hydrology (J. Hydrol. 2024), flash drought, soil-moisture controls (npj Clim. Atmos. Sci. 2025) and ET/BMA give physical interpretation. The PI was RUBISCO Soil Moisture Working Group topic lead. The talent pool shows no S2S forecasting or forecast-verification publications and no NOAA partner. Competing groups (for example CSU's forecasts-of-opportunity group) have stronger technical-merit credentials.
- **Verdict: Revise.** Either (a) make it a small aim of N1 (when do heat-plus-flash-drought threshold exceedances become predictable at weeks 2–4, so utilities get lead time), or (b) submit standalone only with a confirmed S2S/ML co-PI and a NOAA PSL, CPC or GFDL collaborator. Overlap: B3 in the 2026-10-21 scan (compound flash drought-heatwave predictability with E3SM-RRM, BER fallback). Keep NOAA systems and observations here and E3SM there.

### Gaps
- I did not find whether NOAA PSL or CPC has internal soil-moisture forecast-of-opportunity work on heat (cpo.noaa.gov blocked; NOAA PSL not searched).

## Idea N4 (from candidate 4): How small and mid-size utilities and water systems use SI/ML tools with NOAA heat and drought information — Drop

### Takeaway
PA2 requires socio-economic methods and NOAA-service collaboration. The talent pool has no social scientist, no survey or interview track record, and no utility partner, so Hao Lab could not lead.

### Cited Findings
- A survey of 49 large U.S. drinking-water utilities found that fewer than a quarter used AI, mostly experimentally. Barriers were AI expertise and return on investment. — [ASCE JWRMD](https://ascelibrary.com/doi/10.1061/JWRMD5.WRENG-5870); [BYU summary](https://cce.byu.edu/how-do-drinking-water-utilities-use-artificial-intelligence)
- aiWATERS (Virginia Tech) studied small, medium and large utilities; most were at an early stage, with concerns about black-box AI and trust. — [VTechWorks](https://vtechworks.lib.vt.edu/items/1eb809d6-947b-4e08-b91e-039380737f95)
- PA2 requires "socio-economic methodologies" and strongly encourages collaboration with NOAA staff. — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)

### Inferences
- A gap exists: I found no study of small utilities using SI/ML with NOAA heat and drought information. But Hao Lab would be a minor technical add-on. Yifan Gao's NLP experience could support qualitative-data processing (PA2a item 3), but that does not make the lab the lead.
- **Verdict: Drop** as standalone. Optionally keep a light stakeholder-interview task inside N1 (utility and TDEC decision needs), run with a partner.

### Gaps
- I found no small-system or heat- or drought-specific AI adoption study.

## Idea N5 (from candidate 5): SI/ML emulator of land and ecosystem drought response for multi-annual prediction — Drop

### Takeaway
PA1b asks for emulators of NOAA models (SPEAR) with demonstrated process fidelity at 2–10 year leads. The emulator field is led by GFDL and Ai2 (ACE, ACE2, SamudrACE). Hao Lab's modeling experience is with E3SM, not SPEAR, and it has no emulator or M2D prediction publications, so the team could not credibly lead.

### Cited Findings
- ACE and ACE2 (Ai2) emulate GFDL's atmospheric model and learn variability "from subseasonal to decadal" time scales. SamudrACE couples an ocean emulator. — [ACE arXiv 2310.02074](https://arxiv.org/pdf/2310.02074); [ACE2 arXiv 2411.11268](https://arxiv.org/pdf/2411.11268)
- SPEAR is GFDL's seasonal-to-multidecadal prediction system. — [Princeton AOS](https://aos.princeton.edu/news/spear-next-generation-gfdl-modeling-system-seasonal-multidecadal-prediction-and-projection)
- NSF 2616141, "CAIG: Advancing AI atmospheric emulators through rigorous theoretical evaluation and uncertainty quantification" (Chicago, start 2027-01-01). — [NSF API "heat wave forecast opportunity" results](https://api.nsf.gov/services/v1/awards.json?keyword=heat%20wave%20forecast%20opportunity)
- Talent pool: the PI co-authored the E3SMv3 RRM overview (JAMES, under review) and leads CIVE v1.0. The DOE/ORNL vulnerability grant is about E3SM/ELM. There are no SPEAR or emulator publications. — `resources/hao-lab/Yuefeng_Hao_CV.md`
- The 2026-10-21 scan already rated a related E3SM drought-recovery surrogate (B2) as "Revise" for DOE BER, because the lab has no emulator publications. — `funding/2026-10-21.md`

### Inferences
- A land drought emulator for SPEAR at M2D leads would be a different model, a different timescale and a different community from the lab's record. It would also duplicate the B2 direction. **Verdict: Drop.**

### Gaps
- I did not check whether GFDL already has a SPEAR land (LM4) emulator.

## Cross-cutting: overlap, risks, and recommended hosting

### Takeaway
Submit one NOAA proposal: N1 under PA3a, with N2 as an agriculture and water-supply module and, optionally, N3 as a weeks-2-to-4 predictability aim. Send the LOI by 2026-11-17 to Barbara Boustead (NIHHIS) with a copy to the MAPP and AdSci PA3 contacts, and use CPO's four-week LOI reply as the go/no-go.

### Cited Findings
- The selection factors include "Duplication of other projects funded or considered for funding by NOAA/Federal agencies," and double-dipping is barred. — [NOFO](https://files.simpler.grants.gov/opportunities/df29db0f-809b-40ad-9cbe-c7954b9e5cfd/attachments/2aa9ad30-0dde-4761-956c-9637c045a2c6/Foa_Content_of_NOAA-OAR-CPO-2027-33392.pdf)
- The 2026-10-21 scan's partition already assigns Tennessee Valley compound-extreme water availability to DOE BER (B1), facility cooling and SMR thermal discharge to EWRE (E1/E2), and data-center water estimation to USGS 104g (U1/U2). — `funding/2026-10-21.md`

### Inferences
- **Distinct question for NOAA:** "At what combined heat, soil-moisture and river-temperature levels do energy-water-outage cascades begin, and how does NOAA heat information signal them?" The NOAA proposal must not contain E3SM projections (B1), facility design (E1) or estimates of data-center water use as a deliverable (U1).
- **Open items before the LOI:** confirm UT's eRA Commons and the PI's PD/PI account; identify a NIHHIS-partner or NWS Morristown/Nashville or Southeast Regional Climate Center contact (none confirmed); ask TDEC (104b partner) for a letter; decide on a power-systems co-PI (for example, UT colleagues outside the talent pool, unconfirmed); and confirm the RiTHyMs and ReForM scope so N1 uses them as inputs rather than competing with them.

### Gaps
- No confirmed NOAA collaborator, NIHHIS partner, utility partner or S2S co-PI exists in the talent pool.
