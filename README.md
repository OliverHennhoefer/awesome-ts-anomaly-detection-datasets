# Awesome Time-Series Anomaly Detection Datasets
The most extensive collection of publicly available **time-series datasets for anomaly detection**
with a focus on real-world data or synthetic data that is representative of real-world data.

Most available datasets suffer from an **unrealistically high density of anomalies or unrealistically high (artificial)
anomaly signal injections**, raising doubts about the practicality for the evaluation of respective algorithms.
This repository aims to provide an exhaustive collection of freely available datasets suitable for developing and evaluating anomaly detection algorithms.

## Admission Criteria

All datasets listed adhere to the following requirements for admission:
- Public availability (attribution might be required)
- Low contamination (preferably <<5%)
- Tabular formatting

## Univariate Time-Series

### AIOps Competition
Official Repository: [NetManAIOps](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master)<br>
Official Paper: [Constructing Large-Scale Real-World Benchmark Datasets for AIOps](https://arxiv.org/pdf/2208.03938)

#### [AIOps 2018](https://github.com/NetManAIOps/KPI-Anomaly-Detection) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484452272200032281))
#### [AIOps 2019](https://github.com/NetManAIOps/MultiDimension-Localization) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484446614851493956))
#### [AIOps 2020](https://github.com/NetManAIOps/AIOps-Challenge-2020-Data) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484441527290765368))


## Multivariate Time-Series

### [Controlled Anomalies Time-Series (CATS)](https://zenodo.org/records/8338435)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8338435.svg)](https://doi.org/10.5281/zenodo.8338435)

| Type      | Observations | Features | Contaminated | Missing |
|:----------|:------------:|:--------:|:------------:|:-------:|
| Synthetic |  4,000,000   |    17    |     3.8%     |  0.0%   |

CATS includes both nominal and anomalous data segments, allowing for evaluation of semi-supervised and unsupervised detection approaches.
The dataset provides precise control over ground truth and root cause analysis, with no noise or missing data, making it highly customizable for testing algorithm robustness.
Its design balances obvious and challenging anomalies, offering context and flexibility for in-depth analysis ([more](https://www.linkedin.com/posts/solenix_controlled-anomalies-time-series-cats-dataset-activity-7066743805172948994-29dc?utm_source=share&utm_medium=member_desktop)).

##### Citation
Patrick Fleith. (2023). Controlled Anomalies Time Series (CATS) Dataset (Version 2) [Data set]. Solenix Engineering GmbH. https://doi.org/10.5281/zenodo.8338435