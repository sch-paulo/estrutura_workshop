import glob
import os
from typing import List

import pandas as pd

PATH = 'data/raw'


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de uma pasta 'data/raw' e retornar uma lista de dataframes.

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    dataframe_list = []
    for file in all_files:
        dataframe_list.append(pd.read_excel(file))

    return dataframe_list


if __name__ == '__main__':
    dataframe_list = extract_from_excel(PATH)
    print(dataframe_list)
