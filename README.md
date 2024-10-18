# Awesome Time-Series Anomaly Detection Datasets [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)


Extensive collection of publicly available **time-series datasets for anomaly detection**
with a focus on real-world data or synthetic data that is representative of real-world data.

**Before using any of the listed datasets for your experiments you may want to read:**
- [Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress](https://arxiv.org/abs/2009.13807)

_(At least skim through the presentation "[Irrational Exuberance: Why we should not believe 95% of Papers on Time-Series Anomaly Detection](https://kdd-milets.github.io/milets2021/slides/Irrational%20Exuberance_Eammon_Keogh.pdf)" for a tl;dr.)_

Many of the popular datasets for benchmarking in anomaly detection suffer from:
- **Triviality**
- **Unrealistic Anomaly Density**
- **Mislabeled Ground Truth**
- (Run-to-Failure Bias)

_Among those are e.g. Yahoo! S5 (ironically listed first here) and the Numenta Benchmark (NAB).
Do not rely [only] on these kinds of datasets for evaluation and experimentation!_

# 1 Datasets

## 1.1 Univariate

### [Yahoo! S5](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)

> This dataset has to be [requested](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70) for access.

S5 is designed to benchmark anomaly detection algorithms using time-series data with tagged anomalies, including outliers and change-points, representing various Yahoo! services and synthetic variations.

### [AIOps Competition](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master)
The Chinese AIOps Competition series challenges participants to develop innovative solutions that can detect and diagnose IT system issues using large-scale datasets.
The competitions involve tasks like anomaly detection, root cause analysis, and predictive maintenance.

- [AIOps 2018](https://github.com/NetManAIOps/KPI-Anomaly-Detection) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484452272200032281)),
- [AIOps 2019](https://github.com/NetManAIOps/MultiDimension-Localization) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484446614851493956)),
- [AIOps 2020](https://github.com/NetManAIOps/AIOps-Challenge-2020-Data) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484441527290765368))

Official Repository: [NetManAIOps](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master)

### [HexagonML Competition](https://compete.hexagon-ml.com/practice/competition/39/#description)
> [Login](https://compete.hexagon-ml.com/profile/login/?next=/practice/competition/39/%23data) is needed for access.
> Data in the linked [repository](https://github.com/intellygenta/KDDCup2021) is publicly available.

Repository: [KDDCup2021](https://github.com/intellygenta/KDDCup2021)

### [The Mackey-Glass Anomaly Benchmark](https://zenodo.org/records/3760086) (MGAB)
Datasets composed of synthetic Mackey-Glass time series with non-trivial anomalies.
In contrast to other synthetic benchmarks, it is very hard for the human eye to distinguish the introduced anomalies from the normal (chaotic) behavior.

Official Repository: [MGAB](https://github.com/MarkusThill/MGAB)
Related Publications: [Time Series Encodings with Temporal Convolutional Networks](https://link.springer.com/chapter/10.1007/978-3-030-63710-1_13)

_The provided code allows for generating an own version of the data with different parameter settings._

## 1.2 Multivariate

### [SMTP](https://odds.cs.stonybrook.edu/smtp-kddcup99-dataset/)
Modified subset of the KDDCUP99 dataset containing 976,157 records with 0.35% of it labeled as attacks.

### [Wind Turbine (SCADA) Repository](https://github.com/sltzgs/Wind_Turbine_SCADA_open_data)
Repository with a total of eight SCADA datasets of various wind farms and additional links to related datasets.

> Some listed sources need either a platform registration or an application.

### [Wind Turbine (SCADA) For Early Fault Detection](https://zenodo.org/records/10958775)
Real-world SCADA data from three wind farms.

Corresponding Publication: [CARE to Compare: A real-world dataset for anomaly detection in wind turbine data](https://arxiv.org/abs/2404.10320)

### [Tennessee Eastman Process Simulation](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6C3JR1) (TEP)
The TEP dataset is designed for anomaly detection in industrial process control settings.
It simulates a complex chemical production process with multiple operating conditions and potential faults, providing time-series data that includes normal operations as well as various types of faults or anomalies.

_Detailed information available [here](https://keepfloyding.github.io/posts/Ten-East-Proc-Intro/). The Python package [PyTEP](https://github.com/ccreinartz11/pytep) allows for customized
simulation scenarios and setups. **The package requires an activated MATLAB/Simulink license.**_ 

### [Server Machine Dataset](https://github.com/NetManAIOps/OmniAnomaly) (SMD)
The SMD is a dataset used for anomaly detection in the context of server operations.
It consists of several time-series collected from different server machines, capturing various metrics such as CPU load, memory usage and network traffic.
The dataset includes labeled anomalies, such as spikes or drops in performance.

Introducing Publication: [Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network](https://dl.acm.org/doi/10.1145/3292500.3330672)

### [IoT: Online AD for Drinking Water Quality](https://www.spotseven.de/gecco/gecco-challenge/gecco-challenge-2018/)
The GECCO 2018 Industrial Challenge invites participants to develop an event detection system for predicting changes in a time series of drinking water composition data, utilizing a real-world dataset provided by _Thüringer Fernwasserversorgung_ (Germany).

### [Application Server Dataset](https://github.com/zhhlee/InterFusion/tree/main) (ASD)
The ASD dataset contains data of  12 application servers in a large Internet company.

Corresponding Publication: [Multivariate Time Series Anomaly Detection and Interpretation using Hierarchical Inter-Metric and Temporal Embedding](https://dl.acm.org/doi/10.1145/3447548.3467075)

### [Soil Moisture Active Passive](https://nsidc.org/data/smap/data) (SMAP) and [Mars Science Laboratory](https://pds-atmospheres.nmsu.edu/data_and_services/atmospheres_data/Mars/Mars.html) (MSL)
SMAP (Soil Moisture Active Passive satellite) and MSL (Mars Science Laboratory rover) are two public datasets from NASA.

Related Repository: [Telemanom](https://github.com/khundman/telemanom) and [OmniAnomaly](https://github.com/NetManAIOps/OmniAnomaly)<br/>
Related Publications: [Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding](https://dl.acm.org/doi/10.1145/3219819.3219845) and [Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network](https://dl.acm.org/doi/10.1145/3292500.3330672)<br/>
Corresponding Download Versions: [OmniAnomaly](https://github.com/NetManAIOps/OmniAnomaly)

### [SUTD & iTrust Dataset Collection](https://itrust.sutd.edu.sg/itrust-labs_datasets/)

> This dataset has to be [requested](https://docs.google.com/forms/d/e/1FAIpQLSdwOIR-LuFnSu5cIAzun5OQtWXcsOhmC7NtTbb-LBI1MyOcug/viewform) for access.

This collection of datasets provided by the _Singapur University of Technology and Design_ and the _iTrust Centre for Research in Cyber Security_ contains 5 different datasets suitable for benchmarking anomaly detection algorithms derived from the two available main datasets SWat and WADI (see blow).<br/>

#### [Secure Water Treatment](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_swat/) (SWaT)
The Secure Water Treatment (SWaT) dataset is a collection of data from a water treatment testbed, covering 11 days of continuous operation—7 days under normal conditions and 4 days with deliberate attack scenarios.
The dataset includes network traffic and readings from 51 sensors and actuators, with labels indicating normal and abnormal behaviors
During the 4 days of attacks, 41 different attack scenarios were executed based on a cyber-physical system (CPS) attack model developed by the research team.

#### [Water Distriubtion](https://itrust.sutd.edu.sg/itrust-labs-home/itrust-labs_wadi/) (WADI)
The Water Distribution (WADI) dataset captures data from a water distribution testbed over 16 days of continuous operation—14 days under normal conditions and 2 days featuring deliberate attack scenarios.
The dataset includes readings from 123 sensors and actuators, with the attack scenarios based on a cyber-physical system (CPS) attack model developed by the research team.
During the 2 days of attacks, 15 distinct attack scenarios were executed.

### [Airbus Helicopter Accelerometer](https://www.research-collection.ethz.ch/handle/20.500.11850/415151)
The Helicopter Vibration Measurement Dataset is provided by Airbus SAS to automate the validation of vibration data and detect abnormal sensor behavior. Vibration measurements are collected from accelerometers placed at various positions on helicopters, measuring in three directions: longitudinal, vertical, and lateral.

### [Pooled Server Metric](https://github.com/eBay/RANSynCoders/tree/main/data) (PSM)
The multivariate PSM dataset comprises 90 key performance indices (KPIs) from eBay, capturing per-minute cart volumes across various sub-dimensions like user location, device type, and cart types, making it suitable for analyzing temporal and spatial dependencies that reflect business availability and health.

Related Publications: [Practical Approach to Asynchronous Multivariate Time Series Anomaly Detection and Localization](https://dl.acm.org/doi/10.1145/3447548.3467174) and  [Real-Time Synchronization in Neural Networks for Multivariate Time Series Anomaly Detection](https://ieeexplore.ieee.org/document/9413847)

### [3W](https://github.com/petrobras/3W) (Petrobas)
The 3W dataset consists of instances from three different sources containing undesirable events occurring in oil wells.
Accompanying this dataset is the 3W Toolkit, a software package designed to facilitate experimentation with the dataset for specific problems related to oil well operations.

Related Publications: [A realistic and public dataset with rare undesirable real events in oil wells](https://www.sciencedirect.com/science/article/pii/S0920410519306357?via%3Dihub)

### [Drive End Bearing Faults](https://engineering.case.edu/bearingdatacenter/download-data-file)
Data was collected for normal bearings, single-point drive end and fan end defects.

### [Gearbox Faults](https://search-data.ubfc.fr/FR-13002091000019-2023-03-06_LASPI-Detection-and-diagnostics-of-gearbox.html) (LAPSI)
Dataset of current, voltage, and vibration measurements of an electromechanical driving system.
The system is a three-phase asynchronous motor that drives a gearbox.

### [Rotor and Stator Faults in Rotating Machines](https://search-data.ubfc.fr/FR-13002091000019-2023-03-06-03_AMPERE-Detection-and-diagnostics-of-rotor-and.html) (AMPERE)
Dataset of speed, current, voltage and vibration measurements of an electromechanical drive system.
The system is a three-phase asynchronous motor.

### [HIL-based Augmented ICS Security](https://github.com/icsdataset/hai) (HAI)
The HAI dataset was collected from a realistic industrial control system (ICS) testbed augmented with a Hardware-In-the-Loop (HIL) simulator that emulates steam-turbine power generation and pumped-storage hydropower generation.

### [Industrial Control System Cyber Attack Datasets](https://sites.google.com/a/uah.edu/tommy-morris-uah/ics-data-sets)
A collection of three datasets regarding power systems, gas pipelines and water storage tanks.

### [Localization Data for Person Activity](https://archive.ics.uci.edu/dataset/196/localization+data+for+person+activity)
Data contains recordings of five people performing different activities.
Each person wore four sensors while performing the same scenario five times.

Refactored Version: [Kaggle](https://www.kaggle.com/datasets/jorekai/anomaly-detection-falling-people-events)

### [EDEN ISS 2020 Telemetry Dataset](https://zenodo.org/records/11485183)
The EDEN ISS 2020 Telemetry Dataset consists of equidistant sensor readings stemming from 97 sensors in the [EDEN ISS](https://eden-iss.net/) research greenhouse.

Related Publications: [Unraveling Anomalies in Time: Unsupervised Discovery and Isolation of Anomalous Behavior in Bio-regenerative Life Support System Telemetry](https://arxiv.org/pdf/2406.09825v1)

# 2 Benchmark Collections

### [UCR Time Series Anomaly Archive (Download Link)](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/UCR_TimeSeriesAnomalyDatasets2021.zip) 💼
Archive of time-series data for anomaly detection that compensate shortcomings of other available datasets for anomaly detection as stated in the corresponding publication(s).

Corresponding Publication: [Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress](https://arxiv.org/abs/2009.13807)

### [Skoltech Anomaly Benchmark](https://github.com/waico/SKAB) (SKAB) 💼
The SKAB is a comprehensive framework designed for evaluating anomaly detection algorithms, focusing on outlier and changepoint detection in multivariate time series data.
SKAB includes datasets, leaderboards, evaluation modules, and Python tools to support algorithm testing. The dataset consists of 35 files of time series data from sensors monitoring a testbed, with each file containing a single experiment and associated anomaly.
SKAB provides both single-point and collective anomaly labels, making it useful for benchmarking various detection algorithms.

### [Numenta Anomaly Benchmark](https://www.numenta.com/resources/htm/numenta-anomoly-benchmark/) (NAB) 💼
The NAB is a comprehensive framework designed to evaluate anomaly detection algorithms specifically for real-time, streaming data applications.
It includes over 50 labeled time-series datasets from both real-world and synthetic sources, along with a novel scoring mechanism tailored for real-time detection scenarios.
NAB provides tools for testing algorithms, a leaderboard for competitive results, and encourages contributions and collaboration from the community.
The benchmark and its associated resources support the development and assessment of algorithms in unsupervised real-time anomaly detection.

### [Controlled Anomalies Time-Series](https://zenodo.org/records/8338435) (CATS) 💼
The CATS dataset is a simulated dataset designed for benchmarking anomaly detection algorithms in multivariate time series.
It includes 17 variables representing sensor readings, control commands, and external stimuli, with 200 precisely injected anomalies across 5 million timestamps.
The dataset offers fine control over ground truth, context for anomalies, and a pure signal without noise, making it ideal for evaluating the performance, robustness, and explainability of anomaly detection methods in a complex dynamical system.

# 3 Related Datasets

### [NYC Taxi Traffic](https://www.kaggle.com/datasets/julienjta/nyc-taxi-traffic) 🖇️
Numbers of New Yoek taxi passengers, with five anomalies occurring during the NYC marathon, Thanksgiving, Christmas, New Years day, and a snow storm.

### [Metro Interstate Traffic Volume](https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume) 🖇️
Hourly Interstate 94 Westbound traffic volume for MN DoT ATR station 301, roughly midway between Minneapolis and St Paul, MN. Hourly weather features and holidays included for impacts on traffic volume.

### [Credit Card Frau Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) 🖇️
Although not particularly a time-series dataset in the classical sense, the dataset shows transactions and their properties in chronological order. 

# 4 Data Hubs

### [EDP Open Data](https://www.edp.com/en/innovation/open-data/data) 🌐
Platform providing open datasets in context of solar photovoltaic, wind and thermal technology.

### [Evaluation Datasets](https://timeeval.github.io/evaluation-paper/notebooks/Datasets.html) 🌐
Lists univariate and multivariate time series anomaly detection datasets used in the experimental evaluation paper.

### [PhysioNet Open Access Databases](https://physionet.org/about/database/) 🌐
The repository provides free access to a large collection of medical research data, supporting biomedical research and education through the availability of physiological and clinical data alongside related open-source software.

### [IEEE Dataport](https://ieee-dataport.org/) 🌐
Public hub for dataset sharing in context of IEEE publications.

### [Zenodo](https://zenodo.org/search?q=anomaly%20detection%20time%20series&f=resource_type%3Adataset&f=access_status%3Aopen&f=file_type%3Acsv&f=file_type%3Atxt&f=file_type%3Azip&f=file_type%3Ahdf5&f=file_type%3Axlsx&l=list&p=1&s=10&sort=bestmatch) 🌐
Open Science platform for dataset sharing and more.

***

# Inspiration 💡

Now, what to do with all these datasets? Here are some **highly competitive** methods (_you probably never heard of_) for inspiration:

##### [Time-Series Discords](https://matrixprofile.org/posts/what-are-time-series-discords/)
Anomaly detection based on _time-series discords_ is a 20-year-old and widely unknown and parameter-light (1) technique, outperforming a wide range of contemporary anomaly detection methods.
The method is able to find the most _subtle_ anomalies in time-series, as this method is said to yield _superhuman_ result.

- [HOT SAX: Finding the Most Unusual Time Series Subsequence: Algorithms and Applications ](https://www.cs.ucr.edu/~eamonn/HOT%20SAX%20%20long-ver.pdf) (2004)
  - Original paper
  - [Disk Aware Discord Discovery: Finding Unusual Time-series in Terabyte-sized Datasets](https://www.cs.ucr.edu/~eamonn/DiskawareDiscords_Journal.pdf) (2008)
  - [Matrix Profile XIII: Time Series Snippets: A New Primitive for Time Series Data Mining](https://ieeexplore.ieee.org/document/8588817) (2018)
  - [Matrix Profile XXIV: Scaling Time Series Anomaly Detection to Trillions of Datapoints and Ultra-fast Arriving Data Streams](https://www.cs.ucr.edu/~eamonn/DAMP_long_version.pdf) (DAMP; 2022)
      - Scalable version able to operate in an _online-manner_.
      - No confusion by _twin freaks_.
      - Handles _concept drift_.
      - (see also the [paper version]((https://link.springer.com/article/10.1007/s10618-022-00911-7)), [online documentation](https://sites.google.com/view/discord-aware-matrix-profile/home), and [presentation](https://drive.google.com/file/d/1FwiLHrgoOUOTHeIXHAFgy2flQ1alRSoN/view))
- [Parameter-Free Discovery of Arbitrary Length Anomalies in Massive Time Series Archives](https://ieeexplore.ieee.org/document/9338376) (2020)
  - [MERLIN++](https://dl.acm.org/doi/10.1007/s10618-022-00876-7) (MERLIN; 2023)