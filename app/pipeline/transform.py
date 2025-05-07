from typing import List

import pandas as pd


def concat_dataframes(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de dataframes em um único datafram
    """
    return pd.concat(dataframe_list, ignore_index=True)
