import pandas as pd
from config import DATA_PATH


df = pd.read_csv(DATA_PATH)


columns = [
    "prerequisites",
    "recommended_background",
    "core_skills",
    "skills",
    "next_courses"
]


for col in columns:

    print("\n====================")
    print(col)

    print(
        df[col].head(10).to_string()
    )