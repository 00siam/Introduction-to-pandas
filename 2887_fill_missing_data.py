import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    #                                       df.fillna(value)
    products['quantity'] = products['quantity'].fillna(0)
    return products