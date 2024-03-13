import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    #           iloc[row:column]
    #       employee.iloc[:3]
    return employees.head(3)