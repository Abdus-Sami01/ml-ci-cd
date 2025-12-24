import pandas as pd
import yaml
import mlflow
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load parameters
params = yaml.safe_load(open("params.yaml"))

# Load processed data
df = pd.read_csv("data/raw_processed.csv")

X = df.drop("condition", axis=1)  # replace 'price' with your target column
y = df["condition"]

mlflow.start_run()

# Train model
model = RandomForestRegressor(n_estimators=params["train"]["n_estimators"])
model.fit(X, y)

# Log params and model
mlflow.log_params(params["train"])
mlflow.sklearn.log_model(model, "model")

# Save model locally to match DVC output
joblib.dump(model, "models/model.pkl")

mlflow.end_run()

print("Model saved to models/model.pkl")
