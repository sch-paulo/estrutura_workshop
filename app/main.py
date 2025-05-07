from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframes

if __name__ == '__main__':
    dataframe_list = extract_from_excel('data/raw')
    print(type(dataframe_list))
    df_concat = concat_dataframes(dataframe_list)
    print(type(df_concat))
    load_excel(df_concat, 'data/processed', 'output')
