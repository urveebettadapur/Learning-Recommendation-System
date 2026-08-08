# 🎓 Adaptive AI Learning Recommendation System

An AI-powered personalized learning platform that analyzes learner skills, identifies knowledge gaps, and generates optimized learning roadmaps using **Knowledge Graphs, Machine Learning, and Recommendation Algorithms**.

The system combines:

- Course recommendation using **TF-IDF Vectorization + Cosine Similarity**
- Knowledge graph based prerequisite analysis
- Skill gap detection
- Personalized learning path optimization
- Learning duration estimation
- Difficulty progression planning
- REST API integration using FastAPI
- React-based frontend interface


---

# 🚀 Features

## 1. Intelligent Course Recommendation System

- TF-IDF based feature extraction
- Cosine similarity recommendation engine
- Course ranking based on learner requirements
- Exact, partial, and fuzzy course matching


## 2. Knowledge Graph Learning Engine

- Builds relationships between:
    - Courses
    - Skills
    - Prerequisites

Supports:

- Skill dependency discovery
- Prerequisite traversal
- Graph-based learning recommendations


## 3. Skill Gap Detection

Given:

- Learner's current skills
- Target skill / career goal


The system identifies:

- Missing skills
- Required prerequisites
- Knowledge gaps


Example:

```
Current Skills:
Python Programming

Target:
Deep Learning


Missing:
- Machine Learning
- Artificial Intelligence
- PyTorch
- Neural Networks
```

---

## 4. Personalized Learning Path Optimization

Generates:

- Recommended learning sequence
- Dependency-aware roadmap
- Difficulty progression
- Estimated completion duration


Example:

```
Python
   ↓
Machine Learning
   ↓
Artificial Neural Networks
   ↓
Deep Learning
```


---

## 5. Full Stack AI Application

Frontend:

- React + Vite
- Axios API integration


Backend:

- FastAPI
- REST endpoints
- Service based architecture


Machine Learning:

- Scikit-learn
- NetworkX
- Knowledge Graph Engine


---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn


## Machine Learning

- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity
- NetworkX


## Frontend

- React
- Vite
- JavaScript
- Axios


## Development Tools

- Git
- GitHub
- VS Code


---

# 📂 Project Structure


```text
Learning-Recommendation-System/
│
├── .venv/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── .env
│   │
│   ├── database/
│   │
│   ├── models/
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── recommendation.py
│   │   └── learning_path.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── recommendation.py
│   │   └── learning_path.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── recommendation_service.py
│       └── learning_path_service.py
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
│   │
│   ├── node_modules/
│   │
│   ├── public/
│   │   ├── favicon.svg
│   │   └── icons.svg
│   │
│   ├── src/
│   │   │
│   │   ├── api/
│   │   │   └── api.js
│   │   │
│   │   ├── assets/
│   │   │   ├── hero.png
│   │   │   ├── react.svg
│   │   │   └── vite.svg
│   │   │
│   │   ├── components/
│   │   │   │
│   │   │   ├── animations/
│   │   │   │   ├── BackgroundCanvas.jsx
│   │   │   │   ├── CursorGlow.jsx
│   │   │   │   └── FloatingNodes.jsx
│   │   │   │
│   │   │   ├── common/
│   │   │   │   ├── Button.jsx
│   │   │   │   ├── Input.jsx
│   │   │   │   ├── Loading.jsx
│   │   │   │   └── Modal.jsx
│   │   │   │
│   │   │   ├── dashboard/
│   │   │   │   └── DashboardOverview.jsx
│   │   │   │
│   │   │   ├── layout/
│   │   │   │   ├── Footer.jsx
│   │   │   │   └── Navbar.jsx
│   │   │   │
│   │   │   ├── learning/
│   │   │   │   └── LearningPath.jsx
│   │   │   │
│   │   │   ├── onboarding/
│   │   │   │   ├── OnboardingProgress.jsx
│   │   │   │   ├── RoleSelector.jsx
│   │   │   │   └── SkillSelector.jsx
│   │   │   │
│   │   │   └── roadmap/
│   │   │       ├── LearningPath.jsx
│   │   │       ├── ProgressOverview.jsx
│   │   │       ├── RecommendationCard.jsx
│   │   │       ├── SkillGraph.jsx
│   │   │       ├── StrengthsSection.jsx
│   │   │       └── WeaknessSection.jsx
│   │   │
│   │   ├── hooks/
│   │   │   └── useLearningPath.js
│   │   │
│   │   ├── pages/
│   │   │   ├── Roadmap.jsx
│   │   │   ├── RoleSelection.jsx
│   │   │   ├── SignIn.jsx
│   │   │   ├── SignUp.jsx
│   │   │   ├── Skills.jsx
│   │   │   ├── Splash.jsx
│   │   │   └── Welcome.jsx
│   │   │
│   │   ├── services/
│   │   │   ├── authService.js
│   │   │   └── recommendationService.js
│   │   │
│   │   ├── styles/
│   │   │   ├── animations.css
│   │   │   └── globals.css
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── utils/
│   │
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   └── vite.config.js
│
├── ml/
│   │
│   ├── data/
│   │   ├── raw/
│   │   │   └── personalized_learning.csv
│   │   │
│   │   └── processed/
│   │       ├── personalized_learning_processed.csv
│   │       └── personalized_learning_features.csv
│   │
│   ├── models/
│   │   ├── tfidf_vectorizer.pkl
│   │   ├── cosine_similarity.pkl
│   │   ├── course_indices.pkl
│   │   └── course_data.pkl
│   │
│   ├── notebooks/
│   │   ├── eda.ipynb
│   │   ├── feature_engineering.ipynb
│   │   └── model_training.ipynb
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── train.py
│   ├── predict.py
│   ├── recommendation_engine.py
│   ├── course_ranking_engine.py
│   ├── skill_gap_detector.py
│   ├── graph_builder.py
│   ├── graph_engine.py
│   ├── skill_dependency_builder.py
│   ├── learning_path_optimizer.py
│   ├── roadmap_enhancer.py
│   ├── check_columns.py
│   ├── debug_graph.py
│   └── knowledge_graph.pkl
│
├── postman/
│   └── learning_recommendation_api.json
│
├── .gitignore
├── README.md
└── requirements.txt

```

---

# ▶️ Running the Project

## Backend Setup

Create environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```


Run FastAPI:

```bash
uvicorn backend.main:app --reload
```


API Documentation:

```
http://127.0.0.1:8000/docs
```


---

## Frontend Setup


Navigate:

```bash
cd frontend
```


Install dependencies:

```bash
npm install
```


Run:

```bash
npm run dev
```


Frontend:

```
http://localhost:5173
```


---

# 🔌 API Endpoints


## Health Check

```
GET /health
```


## Course Recommendation

```
POST /recommend
```


## Adaptive Learning Path

```
POST /recommend-learning-path
```


Example Request:

```json
{
  "goal_role":"ML Engineer",
  "known_skills":[
      "Python Programming",
      "Machine Learning"
  ],
  "experience":"Intermediate"
}
```


Example Response:

```json
{
 "missing_skills":[
    "Deep Learning",
    "Artificial Intelligence"
 ],
 "estimated_duration":{
    "total_hours":40,
    "estimated_weeks":8
 },
 "learning_path":[
    "Machine Learning",
    "Deep Learning"
 ]
}
```


---

# ✅ Current Status

✔ Data Processing Pipeline

✔ Feature Engineering

✔ ML Recommendation Engine

✔ Knowledge Graph Construction

✔ Skill Gap Detection

✔ Learning Path Optimization

✔ Duration Estimation

✔ Difficulty Progression

✔ FastAPI Backend

✔ React Frontend Integration


---

# 🔮 Future Improvements

- User authentication
- Learner progress tracking
- Database integration
- Hybrid recommendation models
- Reinforcement learning based path optimization
- Docker deployment
- Cloud deployment


---

# 👩‍💻 Author

Developed as an AI/ML project focused on building an end-to-end adaptive personalized learning platform.
