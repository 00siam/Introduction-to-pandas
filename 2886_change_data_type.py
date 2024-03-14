import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    #                                  df.astype('DataType')
    students['grade'] = students['grade'].astype('int')
    return students