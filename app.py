import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Echo", layout="wide")

# ---------------- SESSION ----------------
if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* AI ECHO Title */
.logo-text {
    color: #facc15;  /* Yellow */
    font-size: 24px;
    font-weight: bold;
}

/* Subtitle */
.subtitle-text {
    color: #facc15;  /* Yellow */
    font-size: 16px;
    margin-bottom: 10px;
}

/* Navigation Title */
.nav-heading {
    color: #38bdf8;  /* Blue */
    font-size: 16px;
    font-weight: bold;
    margin-top: 20px;
}
                    
/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e293b, #0f172a);
}

/* Buttons */
div.stButton > button {
    width: 100%;
    padding: 12px;
    border-radius: 12px;
    background: #ffffff;
    color: black;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Hover */
div.stButton > button:hover {
    background: #6366f1;
    color: white;
}

/* Titles */
h1, h2, h3 {
    color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown('<div class="logo-text">🤖 AI ECHO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Sentiment Analysis Pro</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="nav-heading">📊 Navigation Menu</div>', unsafe_allow_html=True)

    if st.button("🏠 Home"):
        st.session_state.menu = "🏠 Home"
        st.rerun()
    
    if st.button("📄 Project Explanation"):
        st.session_state.menu = "📄 Project Explanation"
        st.rerun()

    if st.button("🔍 Real-time Analysis"):
        st.session_state.menu = "🔍 Real-time Analysis"
        st.rerun()

    if st.button("📊 EDA Dashboard"):
        st.session_state.menu = "📊 EDA Dashboard"
        st.rerun()

    if st.button("📈 Advanced Analytics"):
        st.session_state.menu = "📈 Advanced Analytics"
        st.rerun()

    

# ---------------- MENU ----------------
menu = st.session_state.menu

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data.csv")

if "review_length" not in df.columns:
    df["review_length"] = df["review"].astype(str).apply(len)

df["date"] = pd.to_datetime(df["date"], errors='coerce')

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- HOME ----------------
if menu == "🏠 Home":

    st.title("💬 AI Echo - Smart Sentiment Platform")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews", len(df))
    col2.metric("Locations", df["location"].nunique())
    col3.metric("Platforms", df["platform"].nunique())

# ---------------- PROJECT ----------------
elif menu == "📄 Project Explanation":

    st.title("📄 Project Explanation")

    st.write("""
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


# ---------------- REAL TIME ----------------
elif menu == "🔍 Real-time Analysis":

    st.title("🔍 Sentiment Prediction")

    text = st.text_area("Enter your review:")

    if st.button("Predict Sentiment"):

        if text.strip() != "":
            vec = vectorizer.transform([text])
            pred = model.predict(vec)[0]

            if pred == "Positive":
                st.success(f"😊 {pred}")
            elif pred == "Negative":
                st.error(f"😡 {pred}")
            else:
                st.warning(f"😐 {pred}")
        else:
            st.warning("Please enter text")

# ---------------- EDA DASHBOARD ----------------
elif menu == "📊 EDA Dashboard":

    st.title("📊 Exploratory Data Analysis")

    # Rating Distribution
    st.subheader("⭐ Rating Distribution")
    fig, ax = plt.subplots(figsize=(10,3))
    sns.countplot(x='rating', data=df, color='purple', ax=ax)
    st.pyplot(fig)

    # Helpful Votes
    st.subheader("👍 Helpful Votes")
    fig, ax = plt.subplots(figsize=(10,3))
    sns.histplot(df['helpful_votes'], bins=20, color='green', ax=ax)
    st.pyplot(fig)

    col3, col4 = st.columns(2)

    # Verified vs Rating
    st.subheader("✅ Verified vs Rating")
    fig, ax = plt.subplots(figsize=(10,3))
    sns.countplot(x='verified_purchase', hue='rating', data=df, ax=ax)
    st.pyplot(fig)

    # Review Length
    st.subheader("📝 Review Length Analysis")
    fig, ax = plt.subplots(figsize=(10,3))
    sns.boxplot(x='rating', y='review_length', data=df, color='red', ax=ax)
    st.pyplot(fig)

# ---------------- ADVANCED ----------------
elif menu == "📈 Advanced Analytics":

    st.title("📈 Advanced Analytics")

    # Platform
    st.subheader("📱 Platform wise Rating Analysis")
    fig, ax = plt.subplots(figsize=(10,3))
    sns.barplot(x='platform', y='rating', data=df, color='red', ax=ax)
    plt.xticks(rotation=30)
    st.pyplot(fig)

    # Location
    st.subheader("🌍 Location wise Insights")
    loc = df.groupby("location")["rating"].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10,3))
    loc.plot(kind='bar', color='green', ax=ax)
    st.pyplot(fig)

    col3, col4 = st.columns(2)

    # Time Trend
    st.subheader("📅Time Based Rating Trend")
    trend = df.groupby(df["date"].dt.to_period("M"))["rating"].mean()
    fig, ax = plt.subplots(figsize=(10,3))
    trend.plot(kind='line', marker='o', color='red', ax=ax)
    st.pyplot(fig)

    # Version
    st.subheader("⚙️ Version wise Performance")
    ver = df.groupby("version")["rating"].mean()
    fig, ax = plt.subplots(figsize=(10,3))
    ver.plot(kind='bar', color='purple', ax=ax)
    st.pyplot(fig)

    # WordClouds
    st.subheader("🧠 NLP Insights")

    col5, col6 = st.columns(2)

    with col5:
        st.write("😊 Positive Words")
        pos = " ".join(df[df["rating"] >= 4]["review"].astype(str))
        wc = WordCloud(background_color="white").generate(pos)
        fig, ax = plt.subplots(figsize=(5,3))
        ax.imshow(wc)
        ax.axis("off")
        st.pyplot(fig)

    with col6:
        st.write("😡 Negative Words")
        neg = " ".join(df[df["rating"] <= 2]["review"].astype(str))
        wc2 = WordCloud(background_color="white").generate(neg)
        fig, ax = plt.subplots(figsize=(5,3))
        ax.imshow(wc2)
        ax.axis("off")
        st.pyplot(fig)

