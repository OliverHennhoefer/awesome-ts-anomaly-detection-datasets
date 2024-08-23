# Awesome Time-Series Anomaly Detection Datasets
The most extensive collection of publicly available **time-series datasets for anomaly detection**
with a focus on real-world data or synthetic data that is representative of real-world data.

Most available datasets suffer from an **unrealistically high density of anomalies or unrealistically strong (artificial)
injections of signal**, raising doubts about the practicality for the evaluation of respective algorithms.
This repository aims to provide an exhaustive collection of freely available datasets suitable for developing and evaluating anomaly detection algorithms.

## Admission Criteria

All datasets listed adhere to the following requirements for admission:
- Public availability (attribution might be required)
- Low contamination (preferably <<5%)
- Tabular formatting

## Overview

| Dataset                                        | Subsets | Avg. Length | Features | Contaminated | Missing |   Type    |
|:-----------------------------------------------|:-------:|:-----------:|:--------:|:------------:|:-------:|:---------:|
| [SMD](#server-machine-dataset-smd)             |   28    |   25,300    |    38    |    4.16%     |  0.0%   |   Real    |
| [CATS](#controlled-anomalies-time-series-cats) |    1    |  4,000,000  |    17    |    3.80%     |  0.0%   | Synthetic |
| [AIOps](#aiops-competition)                    |    -    |      -      |    -     |      -%      |   -%    |   Real    |
| [Yahoo! S5](#yahoo!-s5)                        |   367   |    1,561    |    1     |      -%      |   -%    |   Real    |

## Univariate Time-Series

### Yahoo! S5
[**This dataset has to explicitly be requested for use**](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)

| Type           | Datasets | Avg. Length | Contaminated | Missing |
|:---------------|:--------:|:-----------:|:------------:|:-------:|
| Real/Synthetic |   367    |   1,561    |      -%      |   -%    |

### AIOps Competition
Official Repository: [NetManAIOps](https://github.com/NetManAIOps/KPI-Anomaly-Detection/tree/master)<br>
Official Paper: [Constructing Large-Scale Real-World Benchmark Datasets for AIOps](https://arxiv.org/pdf/2208.03938)

#### [AIOps 2018](https://github.com/NetManAIOps/KPI-Anomaly-Detection) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484452272200032281))
#### [AIOps 2019](https://github.com/NetManAIOps/MultiDimension-Localization) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484446614851493956))
#### [AIOps 2020](https://github.com/NetManAIOps/AIOps-Challenge-2020-Data) ([Announcement](https://competition.aiops-challenge.com/home/competition/1484441527290765368))


## Multivariate Time-Series

### [Server Machine Dataset](https://github.com/NetManAIOps/OmniAnomaly) (SMD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

| Type | Datasets | Avg. Length | Features | Contaminated | Missing |
|:-----|---------:|:-----------:|:--------:|:------------:|:-------:|
| Real |       28 |   25,300    |    38    |    4.16%     |  0.0%   |

The Server Machine Dataset (SMD) is a 5-week-long dataset collected from a large Internet company, consisting of data from 28 different machines grouped into three categories.
Each machine's data is divided equally into training and testing sets, with labels provided to identify anomalies and the specific dimensions contributing to them.
The dataset includes four main components: the training data, testing data, anomaly labels for the test set, and interpretation labels indicating which dimensions contribute to each anomaly ([more](https://github.com/NetManAIOps/OmniAnomaly)).

##### Citation
Ya Su, Youjian Zhao, Chenhao Niu, Rong Liu, Wei Sun, and Dan Pei. 2019. Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD '19). Association for Computing Machinery, New York, NY, USA, 2828–2837. https://doi.org/10.1145/3292500.3330672

### [Controlled Anomalies Time-Series](https://zenodo.org/records/8338435) (CATS)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

| Type      | Timestamps | Features | Contaminated | Missing |
|:----------|:----------:|:--------:|:------------:|:-------:|
| Synthetic | 4,000,000  |    17    |     3.8%     |  0.0%   |

CATS includes both nominal and anomalous data segments, allowing for evaluation of semi-supervised and unsupervised detection approaches.
The dataset provides precise control over ground truth and root cause analysis, with no noise or missing data, making it highly customizable for testing algorithm robustness.
Its design balances obvious and challenging anomalies, offering context and flexibility for in-depth analysis ([more](https://www.linkedin.com/posts/solenix_controlled-anomalies-time-series-cats-dataset-activity-7066743805172948994-29dc?utm_source=share&utm_medium=member_desktop)).

##### Citation
Patrick Fleith. (2023). Controlled Anomalies Time Series (CATS) Dataset (Version 2) [Data set]. Solenix Engineering GmbH. https://doi.org/10.5281/zenodo.8338435