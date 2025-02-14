# 🩺 Cardiolens - Data Description

## 📌 Dataset Overview  
The dataset contains **health-related features** that help predict whether an individual has **cardiovascular disease**. It includes **demographic information, lifestyle habits, and medical measurements**.

## 📊 Feature Description  

| 🏷️ Feature Name    | 📖 Description |
|------------------|-------------|
| 🧑‍ Age          | Age of the individual (in years or days) |
| ⚧️ Gender       | Gender of the individual (e.g., Male/Female/Other) |
| 📏 Height       | Height of the individual (in cm) |
| ⚖️ Weight       | Weight of the individual (in kg) |
| 📉 BMI          | Body Mass Index (derived from height and weight) |
| 💓 Systolic BP  | Systolic blood pressure (higher value) |
| 💗 Diastolic BP | Diastolic blood pressure (lower value) |
| 🩸 Cholesterol  | Cholesterol levels (📌 Normal, 🔺 Above Normal, 🔴 Well Above Normal) |
| 🩺 Glucose      | Blood glucose levels (📌 Normal, 🔺 Above Normal, 🔴 Well Above Normal) |
| 🚬 Smoking      | Whether the individual smokes (✅ Yes / ❌ No) |
| 🍷 Alcohol Intake | Whether the individual consumes alcohol (✅ Yes / ❌ No) |
| 🏃 Physical Activity | Whether the individual engages in physical activity (✅ Yes / ❌ No) |
| ❤️ Cardiovascular Disease | Target variable (❌ No Disease = 0, ✅ Disease Present = 1) |

⚠️ **Note:** Some categorical variables are encoded numerically in the dataset.  

---
💡 **Goal:** Predict whether an individual has **cardiovascular disease** based on health indicators using machine learning models.
