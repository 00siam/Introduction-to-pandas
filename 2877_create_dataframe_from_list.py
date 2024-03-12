import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    #                   Data set name, Column name
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
