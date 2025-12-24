from mlflow.tracking import MlflowClient

client = MlflowClient()

# List all registered models
print("Registered models:")
for rm in client.search_registered_models():
    print("-", rm.name)

# List latest versions of a specific model
model_name = "HeartDiseasePrediction"
print(f"\nLatest versions of {model_name}:")
for mv in client.get_latest_versions(model_name):
    print(f"Version: {mv.version}, Stage: {mv.current_stage}, Run ID: {mv.run_id}")

# Promote a specific version
version_to_promote = 1

# Promote to Staging
client.transition_model_version_stage(
    name=model_name,
    version=version_to_promote,
    stage="Staging",
    archive_existing_versions=True
)

# Promote to Production
client.transition_model_version_stage(
    name=model_name,
    version=version_to_promote,
    stage="Production"
)

print(f"\nModel {model_name} version {version_to_promote} is now in Production.")
