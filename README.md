

# EcoToxicityMachineLearning

![Project Logo](path/to/logo.png) *// If you have a project logo, place it here.*

## Table of Contents
- [EcoToxicityMachineLearning](#ecotoxicitymachinelearning)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [How to run?](#how-to-run)
  - [Usage](#usage)
  - [Dataset IR - specta](#dataset-ir---specta)
  - [EcoTOX](#ecotox)
    - [Example Results](#example-results)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Project Overview

This project focuses on predicting the toxicity of chemical compounds based on their infrared (IR) spectra. We utilize machine learning techniques to develop models that can accurately classify and predict the toxicity levels of various substances.

## How to run? 

To run this project, you need to have Python installed on your system. Follow the steps below to set up your environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/IR-Spectra-Toxicity-Prediction.git
    cd IR-Spectra-Toxicity-Prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run Jupyter notebook:
    ```bash
    jupyter-notebook
    ```

## Usage

After setting up your environment, you can use the following commands to preprocess the data, train the model, and make predictions.

* Preprocessing Data - '*ipynb'

* Training the Model, SHAP and plotting - '*ipynb'

## Dataset IR - specta

The dataset used in this project includes IR spectra of various chemical compounds along with their corresponding toxicity levels. The data is preprocessed to ensure it is suitable for training machine learning models. You can find the dataset [here](link-to-dataset).

## EcoTOX

The model training process involves several steps, including data preprocessing, feature extraction, and model selection. We have included scripts for each of these steps to make the process reproducible.

### Example Results
```plaintext
XGB Recall: 0.91
XGB F1-Score: 0.90
```

## Contributing

We welcome contributions to this project. If you have any ideas, bug reports, or pull requests, please feel free to submit them.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

We would like to thank the following resources and contributors:

- [EcoTOX](link-to-data-source)
- [Author of IR-dataset](https://scikit-learn.org/)