import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    #       Row             ,   COLUMN
    return [players.shape[0], players.shape[1]]