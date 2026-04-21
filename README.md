# 🍷 Wine Quality Dataset – Data Cleaning & Visualization

## 📌 Project Overview

This project focuses on **data preprocessing (cleaning)** and **visualization** of the Wine Quality dataset (red and white wine).
The goal is to prepare raw data for analysis and understand patterns using visual techniques.

---

## 📂 Dataset Information

* **File Name:** `wine-quality-white-and-red.csv`
* **Type:** CSV file
* **Description:** Contains physicochemical properties of wines and their quality ratings.

### 🔑 Features Include:

* Fixed acidity
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Free sulfur dioxide
* Total sulfur dioxide
* Density
* pH
* Sulphates
* Alcohol
* Quality
* Type (Red / White wine)

---

## ⚙️ Steps Performed

### 1️⃣ Data Loading

* Imported dataset using **Pandas**
* Displayed initial rows for understanding structure

---

### 2️⃣ Before Cleaning (EDA)

* Checked dataset shape
* Verified data types
* Identified missing values
* Checked duplicate records
* Viewed statistical summary

---

### 3️⃣ Data Cleaning

* Removed duplicate rows
* Handled missing values using mean
* Converted categorical column (`type`) into numeric:

  * White → 0
  * Red → 1
* Reset index after cleaning

---

### 4️⃣ After Cleaning

* Verified dataset shape
* Confirmed no missing values
* Ensured no duplicate records

---

### 5️⃣ Data Visualization

The following plots were generated:

* 📊 **Histogram** → Feature distribution
* 📦 **Boxplot** → Outlier detection
* 📊 **Bar Chart** → Wine quality distribution
* 🔥 **Heatmap** → Correlation between features

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 📈 Key Insights

* Dataset contained duplicate values which were removed
* Most features are numerical
* Some outliers are present in chemical properties
* Alcohol content and quality show noticeable correlation

---

## ▶️ How to Run

1. Open **Jupyter Notebook / Google Colab**
2. Upload the dataset file
3. Run the provided Python code step-by-step

---

## 📌 Conclusion

Data cleaning improves dataset quality and ensures accurate analysis.
Visualization helps in understanding relationships and patterns in wine quality.

---

## 🙌 Author

* Student Name: *(Your Name)*
* Course: Data Science / EDA Lab

---
