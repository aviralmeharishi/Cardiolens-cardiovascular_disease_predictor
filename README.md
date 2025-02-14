# 🚑 Cardiolens: Health Predictor

## 📌 Overview
Cardiolens is a machine learning-based web application that predicts the probability of cardiovascular disease in individuals based on various health parameters. The project involves data preprocessing, exploratory data analysis (EDA), feature engineering, and model training to achieve high prediction accuracy. The final model used is **LGBMClassifier**, achieving an **F1 score of 0.49** and **accuracy of 0.87**.

🚀 **Live Demo:** [Cardiolens: Health Predictor](https://cardiolens-health-predictor.streamlit.app/)

---

## 📖 Table of Contents
- [📊 Dataset](#-dataset)
- [🛠️ Data Preprocessing](#-data-preprocessing)
- [📈 Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
- [🎯 Feature Engineering](#-feature-engineering)
- [🧠 Model Selection](#-model-selection)
- [📏 Model Evaluation](#-model-evaluation)
- [🌐 Application Deployment](#-application-deployment)
- [✅ Conclusion](#-conclusion)
- [⚙️ Installation and Usage](#-installation-and-usage)
- [📊 Results](#-results)
- [🚀 Future Improvements](#-future-improvements)
- [📩 Contact](#-contact)

---

## 📊 Dataset
The dataset contains various demographic, lifestyle, and medical factors contributing to cardiovascular disease. Key features include:

- 🏥 **General_F** (General health condition)
- 🩺 **Checkup** (Frequency of health checkups)
- 🏃 **Exercise** (Physical activity status)
- ❤️ **Heart_Dis** (Presence of heart disease)
- 🍽️ **Diet_Pref** (Dietary preference - Veg/Non-Veg)
- 🚬 **Smoking_I** (Smoking habit)
- 🍷 **Alcohol_C** (Alcohol consumption level)
- ⚖️ **BMI** (Body Mass Index)
- 💉 **Diabetes** (Diabetes status)
- 🔢 **BP** (Blood Pressure level)
- 🔬 **Blood_gp** (Blood group)
- 🍏 **Fruit_Cons** (Fruit consumption)
- 🥗 **Green_Ve** (Green vegetable consumption)
- 🍟 **Friedfood_consumption** (Fried food intake)

---

## 🛠️ Data Preprocessing
To ensure high-quality data, the following steps were performed:

- 🔍 **Handling Missing Values**: Imputed missing values using statistical techniques.
- 🔢 **Data Type Correction**: Converted categorical and numerical data appropriately.
- 📏 **Feature Scaling**: Used MinMaxScaler for numerical features.
- ⚖️ **Class Balancing**: Applied **SMOTE** for class imbalance correction.

---

## 📈 Exploratory Data Analysis (EDA)
EDA was performed to gain insights into the dataset:

- 📊 **Univariate Analysis**: Histograms, bar charts, and box plots.
- 🔗 **Bivariate Analysis**: Correlation heatmaps and scatter plots.
- ⚠️ **Outlier Detection**: Identified and treated outliers using **IQR method**.
- 📉 **Feature Importance**: Evaluated using correlation and **mutual information scores**.

---

## 🎯 Feature Engineering
Feature engineering techniques applied:

- 🔤 **Encoding Categorical Features**: Used one-hot and label encoding.
- 🔄 **Feature Transformation**: Applied log transformation for better distribution.
- 📉 **Dimensionality Reduction**: **PCA** used to remove redundant features.

---

## 🧠 Model Selection
Various machine learning models were applied:

1. 🤖 **Logistic Regression**
2. 🌳 **Decision Tree Classifier**
3. 🌲 **Random Forest Classifier**
4. 🚀 **XGBoost Classifier**
5. ⚡ **LGBMClassifier** (Final Model)

✅ **Final Model:** **LGBMClassifier** was selected based on superior performance.

---

## 📏 Model Evaluation
The final model, **LGBMClassifier**, was evaluated using:

- 🎯 **Accuracy**: **0.87**
- 📊 **F1 Score**: **0.49**
- 🏆 **ROC-AUC Score**: Measured classification ability.
- 📉 **Confusion Matrix**: Analyzed false positives & negatives.

---

## 🌐 Application Deployment
The model was deployed as a **Streamlit** web application:

🌍 **Live App**: [Cardiolens: Health Predictor](https://cardiolens-health-predictor.streamlit.app/)

---

## ✅ Conclusion
Cardiolens provides an efficient way to assess cardiovascular disease risk using **machine learning techniques**. The model demonstrates **high predictive capability** and serves as a valuable health assessment tool.

---

## ⚙️ Installation and Usage
To run the project locally:

### Prerequisites
- 🐍 **Python 3.8+**
- 📦 Required Libraries: `pandas`, `numpy`, `scikit-learn`, `lightgbm`, `streamlit`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/aviralmeharishi/cardiolens.git
