import pandas as pd
import joblib
from sklearn.metrics import r2_score
import mlflow

def evaluate():
    df = pd.read_csv(r"D:/python files/MLops/ml-ci-cd/data/raw.csv")
    model = joblib.load(r"models/model.pkl")

    X = df.drop("condition", axis=1)
    y = df["condition"]

    score = r2_score(y, model.predict(X))
    mlflow.log_metric("r2", score)

    if score < 0.8:
        raise ValueError("Model performance below threshold")
