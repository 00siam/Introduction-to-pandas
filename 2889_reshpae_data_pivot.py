import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    #            df.pivot( index = "new_column", columns="condition_column", values="value_column")
    result = weather.pivot(index = "month", columns="city", values="temperature")
    return result