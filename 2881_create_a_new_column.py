import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    # df['New_column_name']
    employees['bonus'] = 2*employees['salary']
    return employees