import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    #       df[condition].sort_values(['column_name'], ascending= False)[['which column i want to show']]
    return animals[animals['weight']>100 ].sort_values(['weight'], ascending= False)[['name']]