# 🤖 AI Echo - Sentiment Analysis Platform

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

### 📊 EDA Dashboard

* Rating distribution
* Helpful votes analysis
* Verified vs non-verified users
* Review length vs rating

### 📈 Advanced Analytics

* Platform vs rating
* Location-based analysis
* Time trend of ratings
* Version performance
* WordCloud insights

### 📄 Project Explanation

* Step-by-step explanation included in app for easy presentation

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* NLTK
* Streamlit

---

# 🧠 Machine Learning Workflow (Detailed Explanation)

---

## 🔹 1. Problem Statement

The objective is to classify user reviews into:

* Positive
* Negative
* Neutral

👉 This helps in understanding user feedback and improving product quality.

---

## 🔹 2. Data Understanding

The dataset includes:

* Review text
* Rating
* Platform
* Location
* Helpful votes
* Version

👉 Target variable: **Sentiment**

---

## 🔹 3. Exploratory Data Analysis (EDA)

Performed multiple visualizations:

* Rating distribution
* Helpful votes histogram
* Platform vs rating
* Location vs rating
* Time-based trends
* Review length analysis
* WordClouds

👉 **Purpose:**

* Understand patterns and trends
* Detect imbalance
* Identify relationships

---

## 🔹 4. Text Cleaning

Steps performed:

* Convert text to lowercase
* Remove punctuation
* Remove emojis
* Remove extra spaces

👉 **Purpose:**
To remove noise and keep only meaningful information for the model.

---

## 🔹 5. Tokenization

Splits sentences into words.

Example:
`"Good app"` → `["good", "app"]`

👉 **Purpose:**
Machine learning models process words, not full sentences.

---

## 🔹 6. Stopword Removal

Removed common words like:

* is, the, and, etc.

👉 **Purpose:**
These words do not contribute to sentiment and add noise.

---

## 🔹 7. Lemmatization

Converts words into base form.

Example:
`running → run`

👉 **Purpose:**
Reduces redundancy and improves consistency.

---

## 🔹 8. Feature Engineering (TF-IDF)

Text is converted into numerical vectors using TF-IDF.

👉 **Purpose:**

* ML models require numeric input
* Assigns importance to words

---

## 🔹 9. Train-Test Split

Dataset split into:

* Training set (80%)
* Testing set (20%)

👉 **Purpose:**
To evaluate model performance on unseen data.

---

## 🔹 10. Model Training

### ✅ Logistic Regression

* Used as baseline model
* Works well with TF-IDF

👉 **Purpose:**
Simple, fast, and effective for text classification

---

### ✅ Naive Bayes

* Probabilistic classifier
* Assumes word independence

👉 **Purpose:**
Highly efficient for NLP tasks and sparse data

---

## 🔹 11. Model Evaluation

### 📊 Accuracy

Measures overall correctness of predictions

### 📊 Confusion Matrix

Shows correct and incorrect predictions for each class

### 📊 Precision, Recall, F1-score

Evaluates performance for each class

### 📊 ROC-AUC Score

Measures how well the model distinguishes between classes

---

## ⚠️ Note on Accuracy

High accuracy (e.g., 1.0) may indicate:

* Small dataset
* Clean data
* Possible overfitting

---

## 🔹 12. Model Saving

Used `pickle` to save:

* Trained model
* TF-IDF vectorizer

👉 **Purpose:**
To reuse model without retraining

---

## 🔹 13. Deployment (Streamlit)

Built an interactive web app with:

* Real-time prediction
* EDA dashboards
* Advanced analytics

👉 **Purpose:**
Make the model accessible and user-friendly

---

# 📂 Project Structure

```id="r1v82x"
AI_ECHO_PROJECT/
│
├── app.py
├── data.csv
├── model.pkl
├── vectorizer.pkl
├── AI_Echo.ipynb
└── README.md
```

---

## ▶️ How to Run

### Install dependencies

```id="m4v8s9"
pip install streamlit pandas numpy matplotlib seaborn scikit-learn nltk wordcloud
```

### Run app

```id="q9z2p1"
streamlit run app.py
```

---

## 📊 Key Insights

* Most users give mid to high ratings
* Verified users provide more consistent feedback
* Negative reviews highlight bugs and performance issues
* Longer reviews often indicate dissatisfaction

---

## 🎯 Objective

* Analyze customer sentiment
* Build complete ML pipeline
* Deploy interactive dashboard

---

## 🚀 Future Improvements

* Deploy on AWS / Streamlit Cloud
* Add Deep Learning models (BERT, LSTM)
* Improve UI/UX
* Add multilingual support

---

## 🙌 Conclusion

This project demonstrates a complete **Data Science pipeline**:

* Data preprocessing
* Feature engineering
* Model training
* Evaluation
* Deployment

---

## 👩‍💻 Author

Rekha
Aspiring Data Scientist 🚀

    """)
