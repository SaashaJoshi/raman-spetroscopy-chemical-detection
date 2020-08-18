# Explosive Detection - Raman Spectrum Recognition 
Uses Deep Convolutional Neural Networks for classification of chemicals present in an explosive from their Raman Spectrum.

## Steps
1. **Data Preprocessing**
	* Smoothening by Savitzky Golay filter
	* Derivatization of spectra
	* Normalization
2. **Principal Component Analysis (PCA)** for dimentionality reduction. (Optional)
3. **Deep Neural Network** (Multi-layer Perceptron architecture) for classification.

## Hardware and Software used

| Hardware | Specs |
| ------ | ------ |
| Processor | Intel i7 |
| RAM | 4 GB |
| HDD | 1 TB |
| GPU | 12GB NVIDIA Tesla K80 GPU |

| Software | Details |
| ------ | ------ |
| Operating System | Linux |
| Development Environment | Google Colab, Jupyter notebook |
| Language and Libraries | Python and libraries (Pandas, Scikit-learn, Matplotlib), Tensorflow, Keras |

## Dataset Used
* Spectra of chemicals including Sulphur, Acetone, Urea, DNT, DMSO, AN, Ethyl aclcohol, Nepthalene, HMX, PNBA etc.
* Data for Open-souce distribution: RRUFF Dataset consisting of 3700 spectrum samples.

## Reference
[Liu J, Osadchy M, Ashton L, Foster M, Solomon CJ, Gibson SJ. Deep convolutional neural networks for Raman spectrum recognition: a unified solution. Analyst. 2017;142(21):4067-74.](https://arxiv.org/pdf/1708.09022.pdf)
