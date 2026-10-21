# Shi Jin (Chris) — CV & Research Interests

> Sources: `Shi_Jin_Resume_AI_Research_Engineering.tex` (primary), `Shi_Jin_Resume_SDE_Test_Engineering.tex`, `main.tex` (Chinese CV); research interests provided directly by Shi Jin. Converted to Markdown; original files not kept. Contact details and grades omitted.
> Lab: Hao Lab, University of Tennessee — PhD student (starting Spring 2027).
> Last reviewed: 2026-10-21.

- GitHub: [Chris-Jin02](https://github.com/Chris-Jin02)

## Research Interests

1. **Computer Vision** — any form of vision work (detection, classification, generative / diffusion models, multimodal sensing, medical and remote-sensing imagery).
2. **Optimization** — any form, from theory to application (e.g., optimization for AI models, infrastructure siting, real-world decision problems).
3. **AI Infrastructure** — systems that train and serve AI at scale: compute hardware, data centers, data pipelines, workload placement.
4. **Robotics & Embodied AI** — perception, mapping (SLAM), and decision-making for physical agents.
5. **AI for Understanding the Physical World** — world models, physics-aware learning, multi-sensor perception of real environments.
6. **AI Applied to the Real World, with an Environmental Focus** — Earth system models, environmental monitoring, and decision support (e.g., energy, water, and land impacts of infrastructure).

### How Past Work Connects

| Interest | Related experience |
|---|---|
| Computer vision | YOLO / EfficientNet detection and classification for substation inspection; CT preprocessing for diffusion-model workflows |
| Optimization | Ongoing lab paper on tariff- and moratorium-aware AI data center siting; Mathematical Contest in Modeling (MCM) |
| AI infrastructure | Server hardware/software test engineering at Quanta (server manufacturing); 350K-scale ETL and retrieval pipeline |
| Robotics & embodied AI | Robot surveying with SLAM-based infrared/LiDAR registration; 1st Prize, National Robot Championship (Intelligent Robot Innovation Design) |
| Understanding the physical world | Multi-sensor (infrared thermography + LiDAR) fusion and alignment for digital-twin substation monitoring |
| AI for environment / decision support | Hao Lab work on AI data center siting and its environmental footprint in the Tennessee Valley |

## Education

| Degree | Institution | Period |
|---|---|---|
| Ph.D. (incoming) | University of Tennessee, Knoxville — Hao Lab, Industrial and Systems Engineering | Starting Spring 2027 |
| M.S. in Computer Science | Stevens Institute of Technology, Hoboken, NJ, USA | Expected Dec 2026 |
| B.Eng. in Engineering (Joint Program) | Ulster University, Belfast, United Kingdom | 09/2020 – 06/2024 |
| B.Eng. in Computer Science and Technology | Shaanxi University of Science and Technology, Xi'an, China | 09/2020 – 06/2024 |

## Technical Skills

- **Languages:** Python, Java, C
- **AI / ML / CV / IR:** PyTorch; YOLO; EfficientNet; LSTM; OpenCV; PyDICOM; DICOM/CT processing; diffusion-model workflows; text mining and information retrieval
- **Backend / Web:** Django, Flask; REST-style APIs; AJAX; dashboard integration
- **Data / DB:** Web crawling; regex/ETL; data cleaning; validation/QC; MySQL; MongoDB
- **Systems / Test Engineering:** Server hardware/software diagnostics; component troubleshooting; test execution and retest; QMS documentation; defect reporting; root-cause analysis
- **Visualization:** ECharts, Matplotlib
- **Engineering Practices:** Debugging; data quality checks; reproducible workflows; parameter validation; privacy-aware data handling

## Research & Work Experience

### Hao Lab, University of Tennessee — PhD Student (incoming)
- Ongoing paper: "Siting Under Moving Rules: A Tariff- and Moratorium-Aware Optimization Model for AI Data Center Location in the Tennessee Valley" (with Y. Hao).

### Server Test Engineer Intern — Quanta Nashville, La Vergne, TN (06/2026 – 08/2026)
- Executed server-level hardware and software diagnostic workflows, interpreted test results, and isolated failures against product specifications and documented work instructions.
- Troubleshot failed servers and components, replaced or reassembled parts as required, and completed verification retests to confirm restored functionality and product quality.
- Recorded test, repair, and defect information in the QMS shop-floor system, maintaining traceable, analysis-ready data for engineering review and quality investigation.
- Documented failure symptoms and corrective actions, escalated recurring or quality-related issues to engineering, and supported data-driven root-cause analysis and continuous improvement.

### Research Developer (Medical Imaging / Diffusion Workflow) — Xi'an, China (07/2023 – 06/2024)
*Standardized Modeling of Sacrum Based on Diffusion Model; Supervisor: Prof. Yong Qi*
- Built a CT preprocessing pipeline for DICOM conversion and QC using Python, PyDICOM, and OpenCV, including missing-slice checks, noise handling, and pixel-anomaly handling.
- Hardened the experiment workflow with parameter validation and controlled preprocessing; evaluated augmentation and dimensionality-reduction techniques for stability-focused iterations.
- Collaborated with Xi'an Red Cross Hospital under privacy constraints, using anonymization and controlled data handling.

### Software Engineering Intern (Project-based) — Xi'an iSoftStone Network Technology Co., Ltd. (05/2023 – 06/2023)
- Built an end-to-end paper analysis system: ingestion → cleaning → storage → retrieval → visualization.
- Implemented a scalable crawler and cleaning pipeline in Python, collecting and normalizing 350K arXiv papers.
- Developed Django retrieval endpoints with AJAX-driven ECharts dashboards.
- Built an LSTM baseline in PyTorch with a standardized training/evaluation workflow.
- Introduced explicit data schemas and a serialization/conversion layer to fix format mismatches across ingestion, storage, and API responses.

### Research Assistant (Computer Vision / Robotics) — Xi'an, China (11/2021 – 02/2022)
*Digital Twin and Smart Substation; Supervisor: Prof. Yong Qi*
- Contributed to an inspection workflow integrating infrared thermography and LiDAR for substation monitoring, including robot surveying and field verification.
- Performed SLAM-based registration to align map, infrared, and LiDAR frames, improving cross-sensor consistency for downstream modeling.
- Produced training-ready labels with LabelMe (boxes, device types, temperature metadata) under consistent annotation conventions.
- Trained and iterated detection/classification baselines (YOLO, EfficientNet) with stable preprocessing and repeatable training runs.

## Selected Projects

- **Scholarly Data Platform (ETL + Retrieval + Dashboard)** — Python, Django, AJAX, MongoDB. Staged architecture with stage-wise data contracts at 350K scale; ingestion-time validation and schema checks.
- **Medical Imaging Pipeline (Preprocessing + Reproducible Experiments)** — PyDICOM, OpenCV. Reusable DICOM → CT conversion and QC components; reproducible comparisons across diffusion-model iterations.
- **Multi-Modal Inspection Data Workflow (Alignment + Annotation)** — Python, LabelMe. Infrared + LiDAR registration and standardized annotation outputs across collection sessions.

## Honors & Awards

- 1st Prize, China National College Computer Competition (Northwest Regional), 2022
- 3rd Prize, 15th China National Undergraduate Computer Design Contest, 07/2022 – 08/2022
- Successful Participant, Mathematical Contest in Modeling (MCM), 2022
- Excellence Award, China AI+ Innovation & Entrepreneurship Competition (Industrial Internet), 12/2021
- 1st Prize, Intelligent Robot Innovation Design, National Robot Championship, 10/2021
