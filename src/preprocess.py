import pandas as pd

input_path=r"D:\python files\MLops\ml-ci-cd\data\raw.csv"
output_path=r"D:\python files\MLops\ml-ci-cd\data\raw_processed.csv"


def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.dropna()
    df=df.drop_duplicates()
    df.to_csv(output_path, index=False)
