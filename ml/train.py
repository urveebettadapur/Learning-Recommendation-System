import pandas as pd
import joblib

from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def train():

    # ----------------------------------------------------
    # Project Paths
    # ----------------------------------------------------

    BASE_DIR = Path(__file__).resolve().parent

    DATA_PATH = BASE_DIR / "data" / "processed" / "personalized_learning_processed.csv"

    MODELS_DIR = BASE_DIR / "models"

    MODELS_DIR.mkdir(exist_ok=True)

    # ----------------------------------------------------
    # Load Dataset
    # ----------------------------------------------------

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

    print(f"Dataset Loaded Successfully")
    print(f"Shape : {df.shape}")

    # ----------------------------------------------------
    # Create Combined Features
    # ----------------------------------------------------

    print("Creating combined feature column...")

    df["combined_features"] = (
        df["skills"].fillna("") + " " +
        df["course_description"].fillna("") + " " +
        df["learning_outcomes"].fillna("") + " " +
        df["core_skills"].fillna("") + " " +
        df["goal_role"].fillna("") + " " +
        df["difficulty"].fillna("") + " " +
        df["category"].fillna("")
    )

    # ----------------------------------------------------
    # TF-IDF Vectorization
    # ----------------------------------------------------

    print("Training TF-IDF Vectorizer...")

    tfidf = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = tfidf.fit_transform(
        df["combined_features"]
    )

    print(f"TF-IDF Matrix Shape : {tfidf_matrix.shape}")

    # ----------------------------------------------------
    # Cosine Similarity
    # ----------------------------------------------------

    print("Computing cosine similarity...")

    cosine_sim = cosine_similarity(
        tfidf_matrix
    )

    print(f"Cosine Similarity Shape : {cosine_sim.shape}")

    # ----------------------------------------------------
    # Course Index Mapping
    # ----------------------------------------------------

    print("Creating course index mapping...")

    indices = pd.Series(
        df.index,
        index=df["name"]
    ).drop_duplicates()

    # ----------------------------------------------------
    # Save Trained Objects
    # ----------------------------------------------------

    print("Saving trained models...")

    joblib.dump(
        tfidf,
        MODELS_DIR / "tfidf_vectorizer.pkl"
    )

    joblib.dump(
        cosine_sim,
        MODELS_DIR / "cosine_similarity.pkl"
    )

    joblib.dump(
        indices,
        MODELS_DIR / "course_indices.pkl"
    )

    joblib.dump(
        df,
        MODELS_DIR / "course_data.pkl"
    )

    print("\n==========================================")
    print(" Training Completed Successfully ")
    print("==========================================")

    print(f"Dataset        : {DATA_PATH.name}")
    print(f"Courses        : {len(df)}")
    print(f"Vocabulary     : {tfidf_matrix.shape[1]}")
    print(f"Models Folder  : {MODELS_DIR}")

    print("\nSaved Files")

    print("✓ tfidf_vectorizer.pkl")
    print("✓ cosine_similarity.pkl")
    print("✓ course_indices.pkl")
    print("✓ course_data.pkl")


if __name__ == "__main__":
    train()