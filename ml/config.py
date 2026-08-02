from pathlib import Path

# ----------------------------------------------------
# Project Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

# ----------------------------------------------------
# Data
# ----------------------------------------------------

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "personalized_learning_processed.csv"
)

# ----------------------------------------------------
# Models
# ----------------------------------------------------

MODELS_DIR = (
    BASE_DIR
    / "models"
)

# ----------------------------------------------------
# Model Files
# ----------------------------------------------------

TFIDF_PATH = (
    MODELS_DIR
    / "tfidf_vectorizer.pkl"
)

COSINE_PATH = (
    MODELS_DIR
    / "cosine_similarity.pkl"
)

INDICES_PATH = (
    MODELS_DIR
    / "course_indices.pkl"
)

COURSE_DATA_PATH = (
    MODELS_DIR
    / "course_data.pkl"
)

KNOWLEDGE_GRAPH_PATH = (
    BASE_DIR /
    "knowledge_graph.pkl"
)