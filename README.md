# Awesome Time-Series Anomaly Detection Datasets
The most extensive collection of publicly available **time-series datasets for anomaly detection**
with a focus on real-world data or synthetic data that is representative of real-world data.

Most available datasets suffer from an **unrealistically high density of anomalies or unrealistically strong (artificial)
injections of signal**, raising doubts about the practicality for the evaluation of respective algorithms.
This repository aims to provide an exhaustive collection of publicly available datasets suitable for developing and evaluating anomaly detection algorithms.


# 1 Datasets

## 1.1 Univariate

### [Yahoo! S5](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)
This is designed to benchmark anomaly detection algorithms using time-series data with tagged anomalies, including outliers and change-points, representing various Yahoo services and synthetic variations.
_This dataset has to explicitly be requested for use._ 

### [AIOps Competition](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master)
The Chinese AIOps Competition series challenges participants to develop innovative algorithms and solutions that can automatically detect and diagnose IT system issues using large-scale datasets.
These competitions often involve tasks like anomaly detection, root cause analysis, and predictive maintenance.

- [AIOps 2018](https://github.com/NetManAIOps/KPI-Anomaly-Detection) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484452272200032281)),
- [AIOps 2019](https://github.com/NetManAIOps/MultiDimension-Localization) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484446614851493956)),
- [AIOps 2020](https://github.com/NetManAIOps/AIOps-Challenge-2020-Data) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484441527290765368))

Official Repository: [NetManAIOps](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master)

### [Numenta Anomaly Benchmark](https://github.com/numenta/NAB) (NAB)
The NAB is a comprehensive framework designed to evaluate anomaly detection algorithms specifically for real-time, streaming data applications.
It includes over 50 labeled time-series datasets from both real-world and synthetic sources, along with a novel scoring mechanism tailored for real-time detection scenarios.
NAB provides tools for testing algorithms, a leaderboard for competitive results, and encourages contributions and collaboration from the community.
The benchmark and its associated resources support the development and assessment of algorithms in unsupervised real-time anomaly detection.

## 1.2 Multivariate

### [Tennessee Eastman Process Simulation](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6C3JR1) (TEP)
The TEP is a benchmark dataset is designed for testing anomaly detection algorithms in industrial process control settings.
It simulates a complex chemical production process with multiple operating conditions and potential faults, providing time-series data that includes normal operations as well as various types of faults or anomalies.
The dataset is widely used to evaluate the performance of anomaly detection methods in identifying and diagnosing these faults in a realistic industrial environment.

_Detailed information available [here](https://keepfloyding.github.io/posts/Ten-East-Proc-Intro/). The Python package [PyTEP](https://github.com/ccreinartz11/pytep) with customized
simulation scenarios and setups._

### [Server Machine Dataset](https://github.com/NetManAIOps/OmniAnomaly) (SMD)
The SMD is a benchmark dataset used for evaluating anomaly detection algorithms in the context of server operations.
It consists of several time-series data collected from different server machines, capturing various metrics such as CPU load, memory usage and network traffic.
The dataset includes labeled anomalies, such as spikes or drops in performance.

Introducing Publication: [Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network](https://dl.acm.org/doi/10.1145/3292500.3330672)

### [Controlled Anomalies Time-Series](https://zenodo.org/records/8338435) (CATS)
The CATS dataset is a simulated dataset designed for benchmarking anomaly detection algorithms in multivariate time series.
It includes 17 variables representing sensor readings, control commands, and external stimuli, with 200 precisely injected anomalies across 5 million timestamps.
The dataset offers fine control over ground truth, context for anomalies, and a pure signal without noise, making it ideal for evaluating the performance, robustness, and explainability of anomaly detection methods in a complex dynamical system.

### [Skoltech Anomaly Benchmark](https://github.com/waico/SKAB) (SKAB)
The SKAB is a comprehensive framework designed for evaluating anomaly detection algorithms, focusing on outlier and changepoint detection in multivariate time series data.
SKAB includes datasets, leaderboards, evaluation modules, and Python tools to support algorithm testing. The dataset consists of 35 files of time series data from sensors monitoring a testbed, with each file containing a single experiment and associated anomaly.
SKAB provides both single-point and collective anomaly labels, making it useful for benchmarking various detection algorithms.