import pandas as pd
from pandas import DataFrame
import csv

class DataLoader:

    def open_dict_csv(path) -> dict:
        with open('dict.csv') as csv_file:
            reader = csv.reader(csv_file)
            mydict = dict(reader)
        return mydict

    def load_file_excel(path) -> DataFrame:
        file_errors_location = path
        df = pd.read_excel(file_errors_location)
        return df

    def load_file_csv(path) -> DataFrame:
        file_errors_location = path
        df = pd.read_csv(file_errors_location, encoding='utf8')
        return df

    @staticmethod
    def save_df_to_csv(df, name:str):
        df.to_csv(name, sep=',', encoding='utf-8')