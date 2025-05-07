import os

import pandas as pd


def load_excel(
    dataframe: pd.DataFrame, output_path: str, filename: str
) -> str:
    """
    Receber um dataframe e salvar como excel

    args:
    dataframe (pd.DataFrame): DataFrame a ser salvo como Excel
    output_path (str): caminho onde o arquivo será salvo
    filename (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    dataframe.to_excel(f'{output_path}/{filename}.xlsx', index=False)
    return 'Arquivo salvo com sucesso'
