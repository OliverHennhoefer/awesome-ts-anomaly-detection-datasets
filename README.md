# Awesome Time-Series Anomaly Detection Datasets

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

The most extensive collection of publicly available **time-series datasets for anomaly detection**
with a focus on real-world data or synthetic data that is representative of real-world data.

# 1 Datasets

## 1.1 Univariate

### [Yahoo! S5](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70) 💻
This is designed to benchmark anomaly detection algorithms using time-series data with tagged anomalies, including outliers and change-points, representing various Yahoo services and synthetic variations.
_This dataset has to explicitly be requested for use._ 

### [AIOps Competition](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master) 💻
The Chinese AIOps Competition series challenges participants to develop innovative algorithms and solutions that can automatically detect and diagnose IT system issues using large-scale datasets.
These competitions often involve tasks like anomaly detection, root cause analysis, and predictive maintenance.

- [AIOps 2018](https://github.com/NetManAIOps/KPI-Anomaly-Detection) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484452272200032281)),
- [AIOps 2019](https://github.com/NetManAIOps/MultiDimension-Localization) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484446614851493956)),
- [AIOps 2020](https://github.com/NetManAIOps/AIOps-Challenge-2020-Data) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484441527290765368))

Official Repository: [NetManAIOps](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master)

## 1.2 Multivariate

### [Tennessee Eastman Process Simulation](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6C3JR1) (TEP) 🏭
The TEP is a benchmark dataset is designed for testing anomaly detection algorithms in industrial process control settings.
It simulates a complex chemical production process with multiple operating conditions and potential faults, providing time-series data that includes normal operations as well as various types of faults or anomalies.
The dataset is widely used to evaluate the performance of anomaly detection methods in identifying and diagnosing these faults in a realistic industrial environment.

_Detailed information available [here](https://keepfloyding.github.io/posts/Ten-East-Proc-Intro/). The Python package [PyTEP](https://github.com/ccreinartz11/pytep) allows for customized
simulation scenarios and setups._

### [Server Machine Dataset](https://github.com/NetManAIOps/OmniAnomaly) (SMD) 💻
The SMD is a benchmark dataset used for evaluating anomaly detection algorithms in the context of server operations.
It consists of several time-series data collected from different server machines, capturing various metrics such as CPU load, memory usage and network traffic.
The dataset includes labeled anomalies, such as spikes or drops in performance.

Introducing Publication: [Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network](https://dl.acm.org/doi/10.1145/3292500.3330672)

### [IoT: Online AD for Drinking Water Quality](https://www.spotseven.de/gecco/gecco-challenge/gecco-challenge-2018/) 🚰
The GECCO 2018 Industrial Challenge invites participants to develop an event detection system for predicting changes in a time series of drinking water composition data, utilizing a real-world dataset provided by Thüringer Fernwasserversorgung.
This year’s challenge emphasizes the practical application of solutions, as the winning submissions may be implemented in real-world scenarios, and for the first time, participants can submit 2-page algorithm descriptions for potential publication in the GECCO Companion.

### [Application Server Dataset](https://github.com/zhhlee/InterFusion/tree/main) (ASD) 💻
The ASD dataset contains data of  12 application servers in a large Internet company.

Corresponding Publication: [Multivariate Time Series Anomaly Detection and Interpretation using Hierarchical Inter-Metric and Temporal Embedding](https://dl.acm.org/doi/10.1145/3447548.3467075)

### [Soil Moisture Active Passive](https://nsidc.org/data/smap/data) (SMAP) 📡 and [Mars Science Laboratory](https://pds-atmospheres.nmsu.edu/data_and_services/atmospheres_data/Mars/Mars.html) (MSL) 📡
SMAP (Soil Moisture Active Passive satellite) and MSL (Mars Science Laboratory rover) are two public datasets from NASA.

Related Repository: [Telemanom](https://github.com/khundman/telemanom) and [OmniAnomaly](https://github.com/NetManAIOps/OmniAnomaly)<br/>
Related Publications: [Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding](https://dl.acm.org/doi/10.1145/3219819.3219845) and [Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network](https://dl.acm.org/doi/10.1145/3292500.3330672)<br/>
Corresponding Download Versions: [OmniAnomaly](https://github.com/NetManAIOps/OmniAnomaly)

### [SUTD & iTrust Dataset Collection](https://itrust.sutd.edu.sg/itrust-labs_datasets/) 💻
This collection of datasets provided by the _Singapur University of Technology and Design_ and the _iTrust Centre for Research in Cyber Security_ contains 5 different datasets suitable for benchmarking anomaly detection algorithms derived from the two available main datasets SWat and WADI (see blow).<br/>
[_All datasets have to explicitly be requested for use._ ](https://docs.google.com/forms/d/e/1FAIpQLSdwOIR-LuFnSu5cIAzun5OQtWXcsOhmC7NtTbb-LBI1MyOcug/viewform)

#### [Secure Water Treatment](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_swat/) (SWaT) 🚰
The Secure Water Treatment (SWaT) dataset is a collection of data from a water treatment testbed, covering 11 days of continuous operation—7 days under normal conditions and 4 days with deliberate attack scenarios.
The dataset includes network traffic and readings from 51 sensors and actuators, with labels indicating normal and abnormal behaviors
During the 4 days of attacks, 41 different attack scenarios were executed based on a cyber-physical system (CPS) attack model developed by the research team.

#### [Water Distriubtion](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_wadi/) (WADI) 🚰
The Water Distribution (WADI) dataset captures data from a water distribution testbed over 16 days of continuous operation—14 days under normal conditions and 2 days featuring deliberate attack scenarios.
The dataset includes readings from 123 sensors and actuators, with the attack scenarios based on a cyber-physical system (CPS) attack model developed by the research team.
During the 2 days of attacks, 15 distinct attack scenarios were executed.

### [Airbus Helicopter Accelerometer](https://www.research-collection.ethz.ch/handle/20.500.11850/415151) 🚁
The Helicopter Vibration Measurement Dataset is provided by Airbus SAS to automate the validation of vibration data and detect abnormal sensor behavior. Vibration measurements are collected from accelerometers placed at various positions on helicopters, measuring in three directions: longitudinal, vertical, and lateral.

### [Pooled Server Metric](https://github.com/eBay/RANSynCoders/tree/main/data) (PSM) 💻
The multivariate PSM dataset comprises 90 key performance indices (KPIs) from eBay, capturing per-minute cart volumes across various subdimensions like user location, device type, and cart types, making it suitable for analyzing temporal and spatial dependencies that reflect business availability and health.

Related Publications: [Practical Approach to Asynchronous Multivariate Time Series Anomaly Detection and Localization](https://dl.acm.org/doi/10.1145/3447548.3467174) and  [Real-Time Synchronization in Neural Networks for Multivariate Time Series Anomaly Detection](https://ieeexplore.ieee.org/document/9413847)

### [3W](https://github.com/petrobras/3W) (Petrobas) 🏭
The3W Dataset consists of instances from three different sources containing undesirable events occurring in oil wells.
Accompanying this dataset is the 3W Toolkit, a software package designed to facilitate experimentation with the dataset for specific problems related to oil well operations.

Related Publications: [A realistic and public dataset with rare undesirable real events in oil wells](https://www.sciencedirect.com/science/article/pii/S0920410519306357?via%3Dihub)

### [(HIL-based Augmented ICS) Security](https://github.com/icsdataset/hai) (HAI) 🏭
The HAI dataset was collected from a realistic industrial control system (ICS) testbed augmented with a Hardware-In-the-Loop (HIL) simulator that emulates steam-turbine power generation and pumped-storage hydropower generation.

### [Industrial Control System Cyber Attack Datasets](https://sites.google.com/a/uah.edu/tommy-morris-uah/ics-data-sets) 🏭
A collection of three datasets regarding power systems, gas pipelines and water storage tanks.

### [Localization Data for Person Activity](https://archive.ics.uci.edu/dataset/196/localization+data+for+person+activity) 🏃
Data contains recordings of five people performing different activities.
Each person wore four sensors (tags) while performing the same scenario five times.

Refactored Version: [Kaggle](https://www.kaggle.com/datasets/jorekai/anomaly-detection-falling-people-events)

# 2 Benchmark Collections

### [Skoltech Anomaly Benchmark](https://github.com/waico/SKAB) (SKAB) 💼
The SKAB is a comprehensive framework designed for evaluating anomaly detection algorithms, focusing on outlier and changepoint detection in multivariate time series data.
SKAB includes datasets, leaderboards, evaluation modules, and Python tools to support algorithm testing. The dataset consists of 35 files of time series data from sensors monitoring a testbed, with each file containing a single experiment and associated anomaly.
SKAB provides both single-point and collective anomaly labels, making it useful for benchmarking various detection algorithms.

### [Numenta Anomaly Benchmark](https://www.numenta.com/resources/htm/numenta-anomoly-benchmark/) (NAB) 💼
The NAB is a comprehensive framework designed to evaluate anomaly detection algorithms specifically for real-time, streaming data applications.
It includes over 50 labeled time-series datasets from both real-world and synthetic sources, along with a novel scoring mechanism tailored for real-time detection scenarios.
NAB provides tools for testing algorithms, a leaderboard for competitive results, and encourages contributions and collaboration from the community.
The benchmark and its associated resources support the development and assessment of algorithms in unsupervised real-time anomaly detection.

Official Repository: [Numenta](https://github.com/numenta/NAB)

### [Controlled Anomalies Time-Series](https://zenodo.org/records/8338435) (CATS) 💼
The CATS dataset is a simulated dataset designed for benchmarking anomaly detection algorithms in multivariate time series.
It includes 17 variables representing sensor readings, control commands, and external stimuli, with 200 precisely injected anomalies across 5 million timestamps.
The dataset offers fine control over ground truth, context for anomalies, and a pure signal without noise, making it ideal for evaluating the performance, robustness, and explainability of anomaly detection methods in a complex dynamical system.


# 3 Honorable Mentions

### [PhysioNet Open Access Databases](https://physionet.org/about/database/) 📍
The repository provides free access to a large collection of medical research data, supporting biomedical research and education through the availability of physiological and clinical data alongside related open-source software.

### [IEEE Dataport](https://ieee-dataport.org/) 📍
Public hub for dataset sharing.


### [NYC Taxi Traffic](https://www.kaggle.com/datasets/julienjta/nyc-taxi-traffic) 📍
Numbers of New Yoek taxi passengers, with five anomalies occurring during the NYC marathon, Thanksgiving, Christmas, New Years day, and a snow storm.
