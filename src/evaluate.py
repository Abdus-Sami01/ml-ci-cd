import pandas as pd
import joblib
from sklearn.metrics import r2_score, mean_squared_error
import yaml

# Load model and data
df = pd.read_csv("data/raw_processed.csv")
model = joblib.load("models/model.pkl")

X = df.drop("condition", axis=1)
y = df["condition"]

# Evaluate
r2 = r2_score(y, model.predict(X))
mse = mean_squared_error(y, model.predict(X))

# Save metrics to metrics.yaml
metrics = {"r2": r2, "mse": mse}
with open("metrics.yaml", "w") as f:
    yaml.dump(metrics, f)

print(f"Metrics saved: {metrics}")
