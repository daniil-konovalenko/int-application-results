import pandas as pd


def get_subjects(df: pd.DataFrame):
    return [column for column in df.columns if 'id' not in column.lower()]


def get_df(file_storage):
    return pd.read_excel(file_storage.stream)
