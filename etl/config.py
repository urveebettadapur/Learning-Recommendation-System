from pathlib import Path

# Root project directory
ROOT_DIR = Path(__file__).resolve().parent.parent


# Data paths
RAW_DATA_PATH = (
    ROOT_DIR
    / "ml"
    / "data"
    / "raw"
    / "personalized_learning.csv"
)

PROCESSED_DIR = (
    ROOT_DIR
    / "data"
    / "processed"
)

PROCESSED_DATA_PATH = (
    PROCESSED_DIR
    / "personalized_learning_processed.csv"
)

FEATURES_DATA_PATH = (
    PROCESSED_DIR
    / "personalized_learning_features.csv"
)