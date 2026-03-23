🤖 AI Echo - Sentiment Analysis Platform

---

## 📌 Project Overview

AI Echo is an end-to-end **Sentiment Analysis Web Application** that classifies user reviews into **Positive, Negative, or Neutral** using Natural Language Processing (NLP) and Machine Learning.

The project also includes **Exploratory Data Analysis (EDA)** and an interactive **Streamlit dashboard** for real-time predictions and insights.

---

## 🚀 Features

### 🔍 Real-time Sentiment Prediction

* Input any review text
* Predict sentiment instantly using trained ML model
* Displays output with intuitive UI (😊 😡 😐)

---

### 📊 EDA Dashboard

* Rating distribution
* Helpful votes analysis
* Verified vs non-verified users
* Review length vs rating

---

### 📈 Advanced Analytics

* Platform vs rating
* Location-based analysis
* Time trend of ratings
* Version performance
* WordCloud insights

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* NLTK
* Streamlit

---

# 🧠 Machine Learning Workflow

---

## 🔹 1. Problem Statement

The objective is to classify user reviews into:

* Positive
* Negative
* Neutral

👉 Helps understand user feedback and improve product quality

---

## 🔹 2. Data Understanding

Dataset contains:

* Review text
* Rating
* Platform
* Location
* Helpful votes
* Version

👉 Target variable: **Sentiment**

---

## 🔹 3. Exploratory Data Analysis (EDA)

Performed visualizations:

* Rating distribution
* Helpful votes histogram
* Platform vs rating
* Location vs rating
* Time trends
* Review length analysis
* WordClouds

👉 Purpose:

* Understand patterns
* Identify relationships
* Detect trends

---

## 🔹 4. Text Preprocessing

Steps:

* Lowercase conversion
* Remove punctuation
* Remove emojis
* Remove extra spaces

👉 Removes noise from text

---

## 🔹 5. Tokenization

Splits sentences into words

Example:
"Good app" → ["good", "app"]

---

## 🔹 6. Stopword Removal

Removes common words like:

* is, the, and

👉 Keeps meaningful words only

---

## 🔹 7. Lemmatization

Converts words into base form

Example:
running → run

---

## 🔹 8. Feature Engineering (TF-IDF)

Converts text into numerical vectors

👉 Assigns importance to words
👉 Required for ML models

---

## 🔹 9. Train-Test Split

* Training set: 80%
* Testing set: 20%

👉 Used to evaluate model performance

---

# 🤖 Model Training & Evaluation

---

## 🔹 Models Used

### ✅ Logistic Regression

* Linear model
* Works well with TF-IDF
* Fast and efficient

---

### ✅ Naive Bayes

* Probabilistic model
* Suitable for text data
* Handles word frequency well

---

### ✅ Random Forest

* Ensemble model using multiple trees
* Captures complex patterns
* More computationally heavy

---

## 🔹 Evaluation Metrics

### 📊 Accuracy

Measures overall correctness

### 📊 Confusion Matrix

Shows actual vs predicted values

### 📊 Precision

Correct positive predictions

### 📊 Recall

Correctly identified positives

### 📊 F1-score

Balance of precision and recall

### 📊 ROC-AUC

Model’s ability to distinguish classes

---

## 🔹 Model Performance (Based on Output)

All three models produced **identical results**:

* Accuracy: **1.0**
* Precision: **1.0**
* Recall: **1.0**
* F1-score: **1.0**

Confusion matrix shows values only on the **diagonal**, meaning:

👉 No misclassification
👉 Perfect prediction for all classes

---

## 🔹 Model Comparison

* No performance difference between models
* All models classify sentiment perfectly on this dataset

---

## 🔹 Theoretical Insight

Even though results are identical:

* Logistic Regression → efficient for TF-IDF
* Naive Bayes → best suited for text classification
* Random Forest → works but less efficient for sparse data

👉 Model selection depends on **data type + efficiency**, not just accuracy

---

## ⚠️ Important Observation

Perfect accuracy is likely due to:

* Small dataset
* Clean data
* Low complexity

👉 May lead to **overfitting**

---

## 🔹 Model Saving

Used `pickle` to save:

* Model (`model.pkl`)
* Vectorizer (`vectorizer.pkl`)

---

## 🔹 Deployment (Streamlit)

Features:

* Real-time prediction
* EDA dashboards
* Advanced analytics

---

## 📂 Project Structure

```text
AI_ECHO_PROJECT/
│
├── app.py
├── data.csv
├── model.pkl
├── vectorizer.pkl
├── AI_Echo.ipynb
└── README.md
```


## 📊 Key Insights

* Most users give mid-to-high ratings
* Negative reviews mention bugs and performance issues
* Longer reviews often indicate dissatisfaction

---

## 🎯 Objective

* Perform sentiment analysis
* Build ML pipeline
* Deploy interactive dashboard

---

## 🚀 Future Improvements

* Deploy to cloud
* Add deep learning models
* Improve UI/UX
* Add multilingual support

---

## 🙌 Conclusion

This project demonstrates a complete **end-to-end data science pipeline**:

* Data preprocessing
* Feature engineering
* Model training
* Evaluation
* Deployment

---

## 👩‍💻 Author

Rekha
Aspiring Data Scientist 🚀
 🚀
""")
