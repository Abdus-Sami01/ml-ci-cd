import pandas as pd
import yaml
import mlflow
from sklearn.ensemble import RandomForestRegressor
import joblib

def train():
    params = yaml.safe_load(open("params.yaml"))
    df = pd.read_csv(r"data\raw_preprocessed.csv")

    X = df.drop("condition", axis=1)
    y = df["condition"]

    mlflow.start_run()
    model = RandomForestRegressor(
        n_estimators=params["train"]["n_estimators"]
    )
    model.fit(X, y)

    mlflow.log_params(params["train"])
    mlflow.sklearn.log_model(model, "model")

    joblib.dump(model, "models/model.pkl")
    mlflow.end_run()
