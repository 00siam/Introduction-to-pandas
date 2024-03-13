import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    
    #            df[condition][[column name]]
    return students[students.student_id==101][['name', 'age']]