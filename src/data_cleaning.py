import pandas as pd

def check_missing_values(df):
    return df.isnull().sum()

def remove_duplicates(df):
    return df.drop_duplicates()

def dataset_summary(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum()
    }
