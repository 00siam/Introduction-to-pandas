import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    #      df.drop_duplicate( subset=['column_condition_name'])
    customers.drop_duplicates( subset=['email'] ,keep='first')
    return customers