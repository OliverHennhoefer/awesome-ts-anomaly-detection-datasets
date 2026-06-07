# Awesome Time-Series Anomaly Detection Datasets [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A curated list of public and research-accessible datasets for time-series anomaly detection, event detection, fault detection, and closely related benchmarking tasks.

The focus is on datasets with temporal structure and a plausible anomaly-detection use case. Some datasets are directly labeled for anomalies, while others are commonly used through benchmark preprocessing, rare-event labels, domain events, or fault classes.

## Contents

- [Selection Notes](#selection-notes)
- [Univariate Datasets](#univariate-datasets)
- [Multivariate Datasets](#multivariate-datasets)
- [Benchmark Collections](#benchmark-collections)
- [Related Datasets](#related-datasets)
- [Data Hubs and Catalogs](#data-hubs-and-catalogs)
- [Contributing](#contributing)

## Selection Notes

- Prefer official dataset pages, archival records, or maintained repositories over reuploads.
- Keep access requirements visible: open download, request form, login, or license restrictions.
- Include datasets that are useful for benchmarking, even if the original task is fault detection, event detection, operations monitoring, or rare-event classification.
- Avoid treating benchmark scores as directly comparable unless preprocessing, label policy, point adjustment, and metrics are aligned.

## Univariate Datasets

### [Yahoo! S5](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)

Synthetic and real Yahoo service time series released through Yahoo Webscope for anomaly-detection research.

- Access: request required through Yahoo Webscope.
- Notes: often used as a classic univariate anomaly-detection benchmark; check the Webscope terms before redistribution.

### [AIOps KPI Anomaly Detection](https://github.com/NetManAIOps/KPI-Anomaly-Detection)

KPI time series from the AIOps Challenge series for detecting anomalies in large-scale IT operations metrics.

- Access: public GitHub repositories.
- Included editions: [AIOps 2018](https://github.com/NetManAIOps/KPI-Anomaly-Detection), [AIOps 2019](https://github.com/NetManAIOps/MultiDimension-Localization), [AIOps 2020](https://github.com/NetManAIOps/AIOps-Challenge-2020-Data).
- Related pages: [2018 announcement](https://competition.aiops-challenge.com/home/competition/1484452272200032281), [2019 announcement](https://competition.aiops-challenge.com/home/competition/1484446614851493956), [2020 announcement](https://competition.aiops-challenge.com/home/competition/1484441527290765368).

### [HexagonML / KDDCup2021 Practice Dataset](https://compete.hexagon-ml.com/practice/competition/39/#description)

Competition-style time-series anomaly-detection data associated with the KDDCup2021 practice material.

- Access: HexagonML login required for the competition page.
- Public mirror: [intellygenta/KDDCup2021](https://github.com/intellygenta/KDDCup2021).

### [Mackey-Glass Anomaly Benchmark](https://zenodo.org/records/3760086) (MGAB)

Synthetic Mackey-Glass time series with deliberately injected, non-trivial anomalies.

- Access: open Zenodo record.
- Repository: [MarkusThill/MGAB](https://github.com/MarkusThill/MGAB).
- Publication: [Time Series Encodings with Temporal Convolutional Networks](https://link.springer.com/chapter/10.1007/978-3-030-63710-1_13).

### [Microsoft Cloud Monitoring Dataset](https://github.com/microsoft/cloud-monitoring-dataset)

Real service and client telemetry time series from Microsoft cloud monitoring scenarios, with expert-labeled anomaly points.

- Access: public GitHub repository.
- Domain: production cloud telemetry, service rates, latencies, crash rates, and related operational metrics.

## Multivariate Datasets

### [SMTP](https://odds.cs.stonybrook.edu/smtp-kddcup99-dataset/)

A modified subset of KDD Cup 1999 network traffic records used for outlier and attack detection.

- Access: open ODDS download page.
- Notes: tabular/network dataset with temporal-adjacent usage in anomaly-detection benchmarks; validate suitability for sequence models before use.

### [Kitsune Network Attack](https://archive.ics.uci.edu/dataset/516/kitsune+network+attack)

Chronologically ordered network-packet feature streams from IoT and surveillance-system attacks, with benign/malicious labels.

- Access: public UCI Machine Learning Repository dataset.
- Domain: online intrusion detection, IoT network monitoring, and sequential attack detection.
- Publication: [Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection](https://arxiv.org/abs/1802.09089).

### [N-BaIoT](https://archive.ics.uci.edu/dataset/442/detection+of+iot+botnet+attacks+n+baiot)

Sequential network-traffic feature data from nine commercial IoT devices infected by Mirai and BASHLITE botnets.

- Access: public UCI Machine Learning Repository dataset.
- Domain: IoT intrusion detection and anomaly-based botnet detection.
- Publication: [N-BaIoT: Network-Based Detection of IoT Botnet Attacks Using Deep Autoencoders](https://ieeexplore.ieee.org/document/8399342).

### [CESNET-TimeSeries24](https://zenodo.org/records/13382427)

Large-scale ISP traffic time series derived from the CESNET3 network for network-traffic forecasting and anomaly detection.

- Access: open Zenodo record; helper tooling is available through [CESNET/cesnet-tszoo](https://github.com/CESNET/cesnet-tszoo).
- Scope: 40 weeks of traffic aggregates over IP, institutional, and subnet levels.
- Publication: [CESNET-TimeSeries24: Time Series Dataset for Network Traffic Anomaly Detection and Forecasting](https://www.nature.com/articles/s41597-025-04603-x).

### [Wind Turbine SCADA Open Data](https://github.com/sltzgs/Wind_Turbine_SCADA_open_data)

Curated repository linking multiple open wind-turbine SCADA datasets from different wind farms.

- Access: mixed; some sources require platform registration or an application.
- Domain: renewable-energy operations, turbine telemetry, condition monitoring, and fault detection.

### [Wind Turbine SCADA for Early Fault Detection](https://zenodo.org/records/10958775)

Real-world SCADA data from three wind farms, released for wind-turbine anomaly and early-fault detection.

- Access: open Zenodo record.
- Publication: [CARE to Compare: A real-world dataset for anomaly detection in wind turbine data](https://arxiv.org/abs/2404.10320).

### [Tennessee Eastman Process Simulation](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6C3JR1) (TEP)

A standard industrial process-control benchmark built around simulated plant operations and process faults.

- Access: open Harvard Dataverse record.
- Helpful resources: [TEP introduction](https://keepfloyding.github.io/posts/Ten-East-Proc-Intro/) and [PyTEP](https://github.com/ccreinartz11/pytep).
- Notes: PyTEP requires an activated MATLAB/Simulink license for customized simulations.

### [Server Machine Dataset](https://github.com/NetManAIOps/OmniAnomaly) (SMD)

Server-machine telemetry used for multivariate anomaly detection in operations monitoring.

- Access: public through the OmniAnomaly repository.
- Publication: [Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network](https://dl.acm.org/doi/10.1145/3292500.3330672).

### [GECCO Drinking Water Quality Challenges](https://zenodo.org/records/3884398)

Water-quality sensor data from the GECCO Industrial Challenges on online anomaly and event detection for drinking-water monitoring.

- Access: open Zenodo records for [GECCO 2018](https://zenodo.org/records/3884398) and [GECCO 2019](https://zenodo.org/records/4304080); original challenge page: [GECCO 2018](https://www.spotseven.de/gecco/gecco-challenge/gecco-challenge-2018/).
- Domain: environmental IoT and water-quality event detection.

### [Application Server Dataset](https://github.com/zhhlee/InterFusion/tree/main) (ASD)

Application-server metrics from a large Internet company, released with the InterFusion benchmark material.

- Access: public GitHub repository.
- Publication: [Multivariate Time Series Anomaly Detection and Interpretation using Hierarchical Inter-Metric and Temporal Embedding](https://dl.acm.org/doi/10.1145/3447548.3467075).

### [NASA SMAP and MSL](https://github.com/khundman/telemanom)

Spacecraft telemetry from NASA's Soil Moisture Active Passive satellite and Mars Science Laboratory rover.

- Access: processed benchmark data in [Telemanom](https://github.com/khundman/telemanom) and [OmniAnomaly](https://github.com/NetManAIOps/OmniAnomaly); source programs: [SMAP](https://nsidc.org/data/smap/data) and [MSL](https://pds-atmospheres.nmsu.edu/data_and_services/atmospheres_data/Mars/Mars.html).
- Publications: [Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding](https://dl.acm.org/doi/10.1145/3219819.3219845) and [OmniAnomaly](https://dl.acm.org/doi/10.1145/3292500.3330672).

### [SUTD iTrust Dataset Collection](https://itrust.sutd.edu.sg/itrust-labs_datasets/)

Cyber-physical security datasets from Singapore University of Technology and Design and the iTrust Centre for Research in Cyber Security.

- Access: request required through the iTrust form.
- Main datasets: [SWaT](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_swat/) and [WADI](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_wadi/).

#### [Secure Water Treatment](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_swat/) (SWaT)

Water-treatment testbed data with normal operation and deliberate cyber-physical attack scenarios.

- Scope: 11 days of operation, including 7 days normal and 4 days under attack.
- Signals: 51 sensors and actuators with normal/abnormal labels.

#### [Water Distribution](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_wadi/) (WADI)

Water-distribution testbed data with normal operation and deliberate attack scenarios.

- Scope: 16 days of operation, including 14 days normal and 2 days under attack.
- Signals: 123 sensors and actuators with attack periods.

### [Industrial Control System Cyber Attack Datasets](https://sites.google.com/a/uah.edu/tommy-morris-uah/ics-data-sets)

A University of Alabama in Huntsville collection covering cyber attacks and faults in industrial-control settings.

- Access: public dataset page.
- Domains: power systems, gas pipelines, water storage tanks, and energy-management systems.

### [BATADAL](https://www.batadal.net/index.html)

Challenge datasets with SCADA measurements from the C-Town water distribution network under normal operation and cyber-attack scenarios.

- Access: public challenge website.
- Domain: water-distribution cyber-physical attack detection.
- Publication: [Battle of the Attack Detection Algorithms: Disclosing Cyber Attacks on Water Distribution Networks](https://riunet.upv.es/handle/10251/144105).

### [WDSEventDB](https://zenodo.org/records/17547955)

Real-time water-distribution testbed data with cyberattack, leakage, and sensor-failure events for event diagnosis and anomaly detection.

- Access: open Zenodo record.
- Domain: smart water systems, operational failures, and cyber-physical event diagnosis.
- Related work: Hardware-in-the-loop investigations of multimodal cybersecurity and operational failure detection in smart water systems.

### [Hourly Anomaly Scores and Leak Labels for Urban Water Distribution](https://zenodo.org/records/15096167)

Hourly multi-source water-distribution data from a Slovak utility, with SCADA, energy, and environmental anomaly scores mapped to confirmed leak labels.

- Access: open Zenodo record.
- Domain: urban water-network leak detection, fault prediction, and early-warning systems.
- Publication: [A multisource dataset for anomaly detection and fault prediction in urban water distribution networks](https://www.nature.com/articles/s41597-026-07203-5).

### [Leak Simulations in Experimental Water Distribution Systems](https://data.mendeley.com/datasets/tbrnp6vrnj/1)

Labeled leak and no-leak sensor signals from a laboratory-scale water distribution testbed.

- Access: open Mendeley Data record.
- Signals: accelerometer, hydrophone, and dynamic-pressure measurements under multiple leak types, network topologies, and background conditions.
- Publication: [Benchmarking dataset for leak detection and localization in water distribution systems](https://www.sciencedirect.com/science/article/pii/S2352340923002676).

### [Rate Anomalies](https://www.kaggle.com/datasets/drscarlat/time-series)

Kaggle dataset with roughly 509k rows, 11 features, and a very low anomaly density.

- Access: Kaggle account may be required.
- Notes: useful as a realistic imbalance case; provenance is less clear than archival or paper-backed datasets.

### [Airbus Helicopter Accelerometer](https://www.research-collection.ethz.ch/handle/20.500.11850/415151)

Helicopter vibration measurements from accelerometers placed at multiple positions and directions.

- Access: ETH Research Collection record.
- Domain: aerospace vibration validation and abnormal sensor behavior detection.

### [Real Electronic Signal Data from Particle Accelerator Power Systems](https://data.mendeley.com/datasets/kbbrw99vh8/5)

Waveform time series from High Voltage Converter Modulators at the Spallation Neutron Source, labeled as normal or faulty.

- Access: open Mendeley Data record.
- Domain: particle accelerator power electronics, early fault detection, and signal-based anomaly detection.
- Publication: [Real electronic signal data from particle accelerator power systems for machine learning anomaly detection](https://pmc.ncbi.nlm.nih.gov/articles/PMC9309398/).

### [Pooled Server Metrics](https://github.com/eBay/RANSynCoders/tree/main/data) (PSM)

Multivariate eBay KPI data with per-minute cart-volume metrics across business and user subdimensions.

- Access: public GitHub repository.
- Publications: [Practical Approach to Asynchronous Multivariate Time Series Anomaly Detection and Localization](https://dl.acm.org/doi/10.1145/3447548.3467174) and [Real-Time Synchronization in Neural Networks for Multivariate Time Series Anomaly Detection](https://ieeexplore.ieee.org/document/9413847).

### [3W](https://github.com/petrobras/3W)

Oil-well time-series instances containing rare undesirable events, released with tooling for dataset exploration and experimentation.

- Access: public GitHub repository.
- Publication: [A realistic and public dataset with rare undesirable real events in oil wells](https://www.sciencedirect.com/science/article/pii/S0920410519306357).

### [NoBOOM](https://www.kaggle.com/datasets/faebs94/noboom-anomaly-detection-in-chemical-processes)

Chemical-process time-series anomaly-detection collection with industrial, pilot-scale, and laboratory-scale process data.

- Access: public Kaggle dataset; code repository: [wagner-d/noboom](https://github.com/wagner-d/noboom).
- Domain: chemical process monitoring and industrial fault detection.
- Publication: [NoBOOM: Chemical Process Datasets for Industrial Anomaly Detection](https://openreview.net/forum?id=qiLboR0ocm).

### [Packaging Industry Anomaly Detection](https://zenodo.org/records/7071747) (PIADE)

Industrial packaging-machine production intervals, machine states, alarms, throughput, and one-hour aggregate sequences.

- Access: open Zenodo record.
- Domain: packaging machinery, alarm forecasting, throughput monitoring, and industrial anomaly detection.

### [MetroPT-3](https://archive.ics.uci.edu/dataset/791/metropt+3+dataset)

Air-compressor sensor data from the Porto metro system for online anomaly detection and failure prediction in railway maintenance.

- Access: public UCI Machine Learning Repository dataset; archival record: [Zenodo](https://zenodo.org/records/6854240).
- Domain: predictive maintenance, air-production units, and metro operations.
- Publication: [The MetroPT dataset for predictive maintenance](https://www.nature.com/articles/s41597-022-01877-3).

### [Case Western Reserve University Bearing Data](https://engineering.case.edu/bearingdatacenter/download-data-file) (CWRU)

Bearing vibration data for normal bearings and single-point drive-end and fan-end defects.

- Access: public download page.
- Domain: rotating machinery and fault diagnosis.

### [Gearbox Faults](https://search-data.ubfc.fr/FR-13002091000019-2023-03-06_LASPI-Detection-and-diagnostics-of-gearbox.html) (LASPI)

Current, voltage, and vibration measurements from an electromechanical drive system with gearbox faults.

- Access: UBFC data record.
- Domain: gearbox fault detection and diagnosis.

### [Rotor and Stator Faults in Rotating Machines](https://search-data.ubfc.fr/FR-13002091000019-2023-03-06-03_AMPERE-Detection-and-diagnostics-of-rotor-and.html) (AMPERE)

Speed, current, voltage, and vibration measurements from a three-phase asynchronous motor system.

- Access: UBFC data record.
- Domain: rotating-machine fault detection and diagnosis.

### [HIL-based Augmented ICS Security](https://github.com/icsdataset/hai) (HAI)

Industrial-control testbed data augmented with Hardware-in-the-Loop simulation for power generation and pumped-storage hydropower scenarios.

- Access: public GitHub repository.
- Domain: ICS anomaly detection and cyber-physical security.

### [Localization Data for Person Activity](https://archive.ics.uci.edu/dataset/196/localization+data+for+person+activity)

Sensor recordings from five people performing activity scenarios, commonly adapted for fall or rare-event detection.

- Access: public UCI dataset page.
- Refactored version: [Kaggle anomaly-detection falling events](https://www.kaggle.com/datasets/jorekai/anomaly-detection-falling-people-events).

### [EDEN ISS 2020 Telemetry](https://zenodo.org/records/11485183)

Equidistant telemetry from 97 sensors in the EDEN ISS research greenhouse.

- Access: open Zenodo record.
- Publication: [Unraveling Anomalies in Time](https://arxiv.org/pdf/2406.09825v1).

### [Exathlon](https://github.com/exathlonbenchmark/exathlon)

Benchmark for explainable anomaly detection over high-dimensional time series from repeated Apache Spark executions.

- Access: public GitHub repository; dataset files are included under the repository data path.
- Publication: [Exathlon: A Benchmark for Explainable Anomaly Detection over Time Series](https://arxiv.org/abs/2010.05073).

### [Multi-Source Distributed System Data](https://zenodo.org/records/3549604) (MSDS)

Multi-source observability data from an OpenStack system, including metrics, logs, traces, workloads, and injected faults.

- Access: open Zenodo record.
- Repository: [SashoNedelkoski/multi-source-observability-dataset](https://github.com/SashoNedelkoski/multi-source-observability-dataset/).
- Domain: AIOps anomaly detection, root-cause analysis, and multimodal operations analytics.

## Benchmark Collections

### [UCR Time Series Anomaly Archive](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/UCR_TimeSeriesAnomalyDatasets2021.zip)

A large archive of univariate time-series anomaly-detection datasets designed to address common benchmark flaws.

- Access: direct ZIP download; alternative record: [Figshare](https://figshare.com/articles/dataset/UCR_Time_Series_Anomaly_Detection_datasets_2021_/26410744).
- Publication: [Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress](https://arxiv.org/abs/2009.13807).

### [Time-Series Benchmarking Suite for Univariate Anomaly Detection](https://github.com/TheDatumOrg/TSB-UAD) (TSB-UAD)

Open benchmark suite for evaluating univariate time-series anomaly-detection methods across many labeled series and domains.

- Access: public GitHub repository.
- Related repository: [TheDatumOrg/TSB-AD](https://github.com/TheDatumOrg/TSB-AD).

### [Skoltech Anomaly Benchmark](https://github.com/waico/SKAB) (SKAB)

Multivariate benchmark built from sensor readings of a testbed under different anomaly and changepoint scenarios.

- Access: public GitHub repository.
- Includes: datasets, evaluation utilities, examples, and benchmark tooling.

### [Numenta Anomaly Benchmark](https://github.com/numenta/NAB) (NAB)

Streaming anomaly-detection benchmark with labeled real and synthetic time series plus a scoring system for real-time detection.

- Access: public GitHub repository; overview page: [Numenta NAB resource](https://www.numenta.com/resources/htm/numenta-anomoly-benchmark/).
- Notes: useful for online detection experiments; scoring assumptions differ from pointwise offline benchmarks.

### [Controlled Anomalies Time-Series](https://zenodo.org/records/8338435) (CATS)

Simulated multivariate benchmark with controlled anomaly injection and detailed ground truth.

- Access: open Zenodo record.
- Scope: 17 variables, 5 million timestamps, and 200 injected anomalies.

### [GutenTAG](https://github.com/TimeEval/GutenTAG)

Synthetic time-series anomaly generator and dataset collection integrated with TimeEval.

- Access: public GitHub repository and Python package.
- Scope: configurable univariate and multivariate time series with multiple anomaly kinds.
- Publication: [TimeEval: A Benchmarking Toolkit for Time Series Anomaly Detection Algorithms](https://vldb.org/pvldb/vol15/p3678-schmidl.pdf).

### [TimeEval Dataset Collection](https://timeeval.github.io/evaluation-paper/notebooks/Datasets.html)

Dataset overview behind the TimeEval evaluation work, covering many univariate and multivariate anomaly-detection datasets.

- Access: public overview and linked downloads.
- Tooling: [TimeEval](https://github.com/TimeEval/TimeEval).
- Notes: a useful cross-check for dataset provenance, dimensions, labels, and benchmark metadata.

### [mTSBench](https://github.com/PLAN-Lab/mTSBench)

Large-scale benchmark for multivariate time-series anomaly detection and model selection.

- Access: public GitHub repository with dataset-loading guidance.
- Publication: [mTSBench: Benchmarking Multivariate Time Series Anomaly Detection and Model Selection at Scale](https://arxiv.org/abs/2506.21550).

## Related Datasets

These datasets are not always direct anomaly-detection benchmarks, but they are useful for rare-event detection, temporal outlier detection, event detection, or realistic preprocessing examples.

### [NYC Taxi Traffic](https://www.kaggle.com/datasets/julienjta/nyc-taxi-traffic)

Passenger-count time series with known unusual events such as holidays, the NYC marathon, and a snow storm.

### [Metro Interstate Traffic Volume](https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume)

Hourly traffic volume on Interstate 94 with weather and holiday covariates.

### [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

Chronologically ordered credit-card transactions with highly imbalanced fraud labels.

- Notes: not a classical time-series dataset, but useful for temporal fraud-detection baselines.

### [PaySim](https://github.com/BBQtime/Synthetic-Financial-Datasets-For-Fraud-Detection)

Synthetic mobile-money transaction data for fraud-detection experiments.

- Related Kaggle dataset: [PaySim 1.0](https://www.kaggle.com/datasets/ealaxi/paysim1).

### [Daphnet Freezing of Gait](https://archive.ics.uci.edu/dataset/245/daphnet+freezing+of+gait)

Wearable accelerometer recordings from Parkinson's disease patients with annotated freezing-of-gait episodes.

- Access: public UCI dataset page.
- Domain: wearable health monitoring and rare-event detection in multivariate sensor streams.

### [CalIt2 Building People Counts](https://archive.ics.uci.edu/dataset/156/calit2+building+people+counts)

Two-stream people-count data from the UCI CalIt2 building, used for detecting unusual building events.

- Access: public UCI dataset page.
- Domain: urban/building event detection.

## Data Hubs and Catalogs

### [EDP Open Data](https://www.edp.com/en/innovation/open-data/data)

Open datasets for solar photovoltaic, wind, and thermal-energy technology.

### [Open Time Series](https://opentimeseries.com/datasets/public_datasets/)

Catalog of public time-series dataset portals, benchmark collections, and domain-specific sources.

### [PhysioNet Open Access Databases](https://physionet.org/about/database/)

Large collection of physiological and clinical research data with software and documentation.

### [IEEE DataPort](https://ieee-dataport.org/)

Dataset sharing platform connected to IEEE research publications.

### [Zenodo Time-Series Anomaly Search](https://zenodo.org/search?q=anomaly%20detection%20time%20series&f=resource_type%3Adataset&f=access_status%3Aopen&f=file_type%3Acsv&f=file_type%3Atxt&f=file_type%3Azip&f=file_type%3Ahdf5&f=file_type%3Axlsx&l=list&p=1&s=10&sort=bestmatch)

Open-science search for time-series anomaly-detection datasets across CSV, TXT, ZIP, HDF5, and XLSX records.

### [Hugging Face Datasets](https://huggingface.co/datasets?sort=trending&search=time+series+anomaly)

Community dataset hub with an increasing number of time-series and anomaly-detection dataset mirrors.

### [NASA Prognostics Center of Excellence Data Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

NASA repository for prognostics and systems-health datasets, including battery, bearing, milling, and C-MAPSS turbofan degradation time series.

### [PHM Society Data Repository](https://data.phmsociety.org/)

Prognostics and Health Management Society repository for data challenges and condition-monitoring datasets.

### [ADRepository](https://github.com/mala-lab/ADBenchmarks-anomaly-detection-datasets)

Research dataset repository for anomaly detection across modalities, including a dedicated time-series section.

## Contributing

Contributions are welcome. Please prefer official sources and include enough context for readers to decide whether a dataset fits their benchmark.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the recommended entry format and review checklist.
