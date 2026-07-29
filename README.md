# 🎓 Learning Recommendation System

An AI-powered Learning Recommendation System that recommends similar courses using **TF-IDF Vectorization** and **Cosine Similarity**. The project follows a modular machine learning workflow with ETL, model training, and prediction components.

---

## Features

- ETL Pipeline (Extract, Transform, Load)
- Data Preprocessing
- Feature Engineering
- TF-IDF Recommendation Engine
- Cosine Similarity based Recommendations
- Model Training Pipeline
- Prediction Pipeline
- Intelligent Course Search
  - Exact Match
  - Case-Insensitive Match
  - Partial Match
  - Close Match Suggestions

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI

---

## Project Structure

Learning-Recommendation-System/

├── backend/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── .env
│   └── main.py
│
├── data/
│   └── processed/
│       ├── personalized_learning_processed.csv
│       └── personalized_learning_features.csv
│
├── docs/
│   ├── api_documentation.md
│   ├── architecture.md
│   └── database_schema.md
│
├── etl/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── ml/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── models/
│   │   ├── tfidf_vectorizer.pkl
│   │   ├── cosine_similarity.pkl
│   │   ├── course_indices.pkl
│   │   └── course_data.pkl
│   ├── notebooks/
│   │   ├── eda.ipynb
│   │   ├── feature_engineering.ipynb
│   │   └── model_training.ipynb
│   ├── config.py
│   ├── train.py
│   └── predict.py
│
├── postman/
│   └── learning_recommendation_api.json
│
├── requirements.txt
├── README.md
└── .gitignore

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the ETL Pipeline

```bash
python etl/pipeline.py
```

### 3. Train the Recommendation Model

```bash
python ml/train.py
```

### 4. Run the Prediction Module

```bash
python ml/predict.py
```

---

## Current Status

✅ ETL Pipeline

✅ Data Preprocessing

✅ Feature Engineering

✅ Recommendation Engine

✅ Model Training

✅ Prediction Module

🚧 FastAPI Integration

---

## Future Improvements

- FastAPI API Endpoints
- Frontend User Interface
- User Authentication
- Hybrid Recommendation System
- Docker Deployment
- Cloud Deployment

---

## Author

Developed as part of an AI/ML learning project focused on building an end-to-end Learning Recommendation System.
