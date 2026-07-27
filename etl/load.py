from config import (
    PROCESSED_DATA_PATH,
    FEATURES_DATA_PATH,
    PROCESSED_DIR
)


def load_processed_data(df):
    """
    Saves cleaned processed dataset
    """

    # Create processed folder if it doesn't exist
    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print("Processed data saved:")
    print(PROCESSED_DATA_PATH)



def load_features(df):
    """
    Saves feature-engineered dataset
    """

    # Create processed folder if it doesn't exist
    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        FEATURES_DATA_PATH,
        index=False
    )

    print("Feature data saved:")
    print(FEATURES_DATA_PATH)