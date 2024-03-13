import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # df.dropna(subset = ['Column_name'])
    return students.dropna(subset = ['name'])