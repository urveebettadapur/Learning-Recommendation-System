import pandas as pd
from config import RAW_DATA_PATH


def extract_data():

    df = pd.read_csv(RAW_DATA_PATH)

    print("Data extracted successfully")
    print("Shape:", df.shape)

    return df