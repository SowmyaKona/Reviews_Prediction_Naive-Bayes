**📝 Review Sentiment Classification using Naive Bayes**

---------------------------------------------------------------------------------------------------------------------------------------------------

**📌Project Overview**
---------------------------------------------------------------------------------------------------------------------------------------------------
This project implements an end-to-end Text Classification Pipeline using TF-IDF + Bernoulli Naive Bayes to classify customer reviews as:
👍 Liked (1)
👎 Not Liked (0)

---------------------------------------------------------------------------------------------------------------------------------------------------

📂 Project Structure
- Reviews_prediction_Streamlit/
- │
- ├── app.py
- ├── preprocessing.py
- ├── sentiment_pipeline.pkl
- ├── requirements.txt
- ├── output.csv
- └── ML_Task_Naive_Bayes.ipynb

The model is built using Scikit-learn Pipeline and deployed-ready using a saved .pkl file.

---------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Project Workflow

**1️. Data Loading**
- Loaded dataset (output.csv)
- Checked shape, info, missing values
---------------------------------------------------------------------------------------------------------------------------------------------------
**2️.Data Cleaning**
- Removed extra spaces from column names
- Checked null values
- Analyzed review length
---------------------------------------------------------------------------------------------------------------------------------------------------
**3.Text Preprocessing**
- Custom preprocessing function (clean_text) includes:
    - Lowercasing
    - Removing special characters
    - Removing stopwords (NLTK)
    - Lemmatization (WordNetLemmatizer)
Implemented in:
- preprocessing.py

**Why Pipeline?**
-  Keeps preprocessing + model together
-  Prevents data leakage
-  Easy deployment
-  Cleaner code
---------------------------------------------------------------------------------------------------------------------------------------------------
**4.Train-Test Split**
- 80% Training
- 20% Testing

**5.Model Evaluation**
- Metrics Used:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - Confusion Matrix
  - Classification Report
  
---------------------------------------------------------------------------------------------------------------------------------------------------

**🛠️ Tech Stack**
- Python
- Pandas
- Numpy
- Scikit-learn
- NLTK
- Matplotlib / Seaborn
- Streamlit (for deployment)
---------------------------------------------------------------------------------------------------------------------------------------------------

**Streamlit Deployment**
-link: https://reviewspredictionnaive-bayes-nkc8tk9iwlepkp9ypubkw4.streamlit.app/

----------------------------------------------------------------------------------------------------------------------------------------------------

👩‍💻 Author

Sowmya
AI/ML Enthusiast | NLP | Machine Learning | Deployment Ready Projects
