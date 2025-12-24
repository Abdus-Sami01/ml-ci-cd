# ML CI/CD Project

This repository demonstrates a **fully reproducible ML CI/CD pipeline** using:

- **Git** → version control  
- **DVC** → data and pipeline management  
- **MLflow** → experiment tracking and model registry  
- **DagsHub** → remote repository + experiment tracking UI  

The pipeline includes **data preprocessing, model training, evaluation, and automatic promotion** to Production if metrics meet thresholds.

---

## 📂 Project Structure

ml-ci-cd/
├── data/
│ └── raw.csv # Raw dataset
├── src/
│ ├── preprocess.py # Data preprocessing
│ ├── train.py # Model training
│ └── evaluate.py # Evaluation & metric checks
├── models/ # Trained model artifacts
├── params.yaml # Hyperparameters & thresholds
├── dvc.yaml # DVC pipeline stages
├── requirements.txt # Python dependencies
├── ci_cd_pipeline.py # Full CI/CD automation script
└── README.md



## ⚡ Features

- **Reproducible pipeline** with DVC (`dvc exp run`)  
- **Experiment tracking** with MLflow  
- **Model registry** with versioning and auto-promotion  
- **Automatic CI/CD**:
  - Runs pipeline
  - Trains model
  - Logs metrics to MLflow
  - Registers model
  - Promotes to Production if metric thresholds are met  
- **Git + DagsHub integration** for version control and artifact storage
- 
---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Abdus-Sami01/ml-ci-cd.git
cd ml-ci-cd
```


Install dependencies:

```bash
pip install -r requirements.txt
pip install dvc[all] mlflow scikit-learn pandas joblib
```

Initialize DVC and connect remote (if not done already):

```bash
dvc init
dvc remote add -d storage <DagsHub_DVC_remote_URL>
git add .dvc/config
git commit -m "Configured DVC remote"
```

📊 Usage
1️⃣ Run DVC pipeline manually
```bash
dvc exp run
```

2️⃣ Run the automated CI/CD pipeline
```bash
python ci_cd_pipeline.py
```

This will:

Run the DVC pipeline

Train the model using parameters from params.yaml

Log metrics and artifacts to MLflow

Register the model in MLflow Model Registry

Promote the model to Production if metrics meet thresholds

3️⃣ MLflow UI (Local)
```bash
mlflow ui
```
Open http://127.0.0.1:5000 to track experiments, metrics, and models.

📝 Configuration
```yaml
train:
  model_type: random_forest
  n_estimators: 200
  r2_threshold: 0.8
model_type → "random_forest" or "linear_regression"

n_estimators → only for random forest

r2_threshold → minimum R2 score for auto-promotion
```

🔄 CI/CD Workflow
Modify code or parameters

Run ci_cd_pipeline.py

Automatically runs DVC pipeline

Logs metrics & model to MLflow

Registers model

Promotes to Production if thresholds pass

Push to Git/DagsHub for versioning and artifact storage

📦 Model Registry
Registered models can be viewed on MLflow UI or DagsHub experiments tab

Each run is fully reproducible with DVC + MLflow

Staging/Production stages are handled automatically by the CI/CD script

🧰 Requirements
Python ≥ 3.9
DVC
MLflow ≥ 1.30
scikit-learn
pandas
joblib

Create a new feature branch

Make changes, run DVC pipeline locally

Push branch and create a pull request

CI/CD pipeline ensures reproducibility and registers the model

📖 References
DVC Documentation
MLflow Documentation
DagsHub

Author: Abdus Sami
Date: 2025-12-24
