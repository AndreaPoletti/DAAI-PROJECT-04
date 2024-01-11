# Real-Time-Anomaly-Segmentation [[Course Project](https://docs.google.com/document/d/1ElljsAprT2qX8RpePSQ3E00y_3oXrtN_CKYC6wqxyFQ/edit?usp=sharing)]
This repository provides the code for the project 04 - Anomaly segmentation of the DAAI course (Automotive Engineering). It is used to performs anomaly segmentation, producing useful metrics to evaluate anomaly segmentation models performance.

## Packages

* [eval](eval) contains tools for evaluating/visualizing the network's output and performing anomaly segmentation.
* [trained_models](trained_models) Contains the trained models used in our project. 

## Testing datasets:

* **For testing the anomaly segmentation model**: Road Anomaly, Road Obstacle, and Fishyscapes dataset. All testing images are provided here [Link](https://drive.google.com/file/d/1r2eFANvSlcUjxcerjC8l6dRa0slowMpx/view).

## Anomaly Inference:
* The repo provides a pre-trained ERFNet on the cityscapes dataset that can be used to perform anomaly segmentation on test anomaly datasets.

