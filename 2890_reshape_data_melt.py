import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # pd.melt(dataset, id_vars=['Output_column'], var_name = 'output_col', value_name = 'output_column')
    return pd.melt(report, id_vars=['product'], var_name='quarter',value_name='sales')