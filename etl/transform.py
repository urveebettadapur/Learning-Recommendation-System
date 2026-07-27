import pandas as pd


def clean_data(df):

    # Fill missing values
    df["module_list"] = df["module_list"].fillna("")
    df["prerequisite_level"] = (
        df["prerequisite_level"]
        .fillna("Unknown")
    )

    # Remove duplicates
    df = df.drop_duplicates()

    return df



def create_features(df):

    # Example features
    df["learning_load"] = (
        df["estimated_hours"]
    )


    df["skill_density"] = (
        df["skills"]
        .apply(
            lambda x: len(str(x).split(","))
        )
    )


    return df



def transform_data(df):

    df = clean_data(df)

    df = create_features(df)

    print("Transformation completed")

    return df