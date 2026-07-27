from extract import extract_data
from transform import transform_data
from load import (
    load_processed_data,
    load_features
)


def run_pipeline():

    # Extract
    df = extract_data()


    # Transform
    transformed_df = transform_data(df)


    # Load
    load_processed_data(transformed_df)
    load_features(transformed_df)


    print("========================")
    print("ETL Pipeline Completed")
    print("========================")



if __name__ == "__main__":
    run_pipeline()