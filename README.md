# Bank Product Usage Prediction using Random Forest

This project demonstrates a basic use case of the Random Forest classification algorithm to predict whether a customer will opt for a specific bank product based on demographic and financial information.

## Project Overview

The model predicts the likelihood of a customer using a bank product based on the following features:
- **Age**
- **Income**
- **Credit Score**
- **Marital Status**
- **Owns House**
- **Job Type**

The dataset is synthetically generated in Python and consists of 1,000 samples.

## Code Details

The code in this project includes the following components:

1. **Data Generation**: Creates a synthetic dataset with relevant customer information.
2. **Data Preprocessing**: Encodes non-numeric categorical features (such as marital status, home ownership, and job type) into numeric values for compatibility with the model.
3. **Model Training**: Splits the dataset into training and testing sets, and trains a Random Forest classifier on the training data.
4. **Model Evaluation**: Evaluates the model by printing its accuracy and a classification report that details performance metrics like precision, recall, and F1-score.

## Requirements

To run the code, you need the following Python libraries:
- `pandas`
- `numpy`
- `scikit-learn`
- `pyautogui` (optional, for automated typing demonstration)

Install them with:
```bash
pip install pandas numpy scikit-learn
