# Deep Learning for Supraspinatus Calcific Tendinopathy Detection

Published research on automated detection of supraspinatus calcific tendinopathy (SSCT) from ultrasound images using convolutional neural networks.

## Publication

**Deep Learning for Detecting Supraspinatus Calcific Tendinopathy on Ultrasound Images**

Pei-Hsin Chiu et al.  
*Journal of Medical Ultrasound*, 30(3), 196–202 (2022).

- [Published Paper (PubMed Central)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9724476/)
- [DOI](https://doi.org/10.4103/jmu.jmu_182_21)

## Research Overview

This study investigated deep learning approaches for identifying calcific tendinopathy in supraspinatus tendon ultrasound images.

Pretrained convolutional neural networks were evaluated using longitudinal and transverse ultrasound views to assess diagnostic performance and model generalization across imaging orientations.

## Methodology

- **Task:** Ultrasound image classification
- **Architecture:** DenseNet-121 with transfer learning
- **Comparison Models:** ResNet50 and VGG19
- **Input:** Longitudinal and transverse supraspinatus tendon ultrasound images
- **Data Augmentation:** Rotation, translation, shear, zoom, channel shift, and horizontal flipping
- **Evaluation:** Accuracy, sensitivity, specificity, and ROC-AUC
- **Interpretability:** Gradient-weighted Class Activation Mapping (Grad-CAM)

## My Contributions

As the first author, I led the technical development and experimental analysis of this research project. My responsibilities included:

- **Data Preprocessing:** Developed preprocessing pipelines to prepare ultrasound images for deep learning experiments.
- **Model Development:** Implemented and trained convolutional neural networks, including DenseNet-121, ResNet50, and VGG19, using transfer learning.
- **Experimental Design:** Designed and conducted experiments to evaluate model performance across longitudinal and transverse ultrasound views.
- **Model Evaluation:** Performed quantitative analysis using accuracy, sensitivity, specificity, and ROC-AUC.
- **Model Interpretability:** Applied Grad-CAM to visualize image regions contributing to model predictions.
- **Results Analysis:** Analyzed and interpreted experimental results, including comparisons across model architectures and imaging orientations.
- **Research Writing:** Prepared the research manuscript and documented the methodology, experiments, and findings.

All model implementation, training, evaluation, and related programming work for this study was performed by me. Clinical image collection and diagnostic labeling were conducted by collaborators.

**Note:** The full original training and model implementation code is not currently included in this repository. The available code consists of selected preprocessing utilities.

## Published Results

The combined longitudinal-transverse DenseNet-121 model achieved:

| Metric | Result |
|---|---|
| Accuracy | 91.32% |
| Sensitivity | 87.89% |
| Specificity | 94.74% |

These results are reported in the published paper.

## Repository Contents

This repository contains selected image preprocessing scripts and research documentation associated with the published study.

- `preprocessing/`: Image preprocessing utilities, including the `rename` and `take` scripts.
- **Master's Thesis (PDF):** Detailed documentation of the research methodology and experimental results.

For the complete methodology, model architectures, experimental setup, and results, please refer to the [published paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9724476/).

## Author

**Pei-Hsin Chiu**

- [GitHub](https://github.com/pei-hsin-chiu)
- [LinkedIn](https://www.linkedin.com/in/pei-hsin-chiu/)
- [Google Scholar](https://scholar.google.com/citations?user=Dj1HDEkAAAAJ)
