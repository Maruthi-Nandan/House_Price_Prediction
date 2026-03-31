# 🏠 House Price Prediction — End-to-End MLOps Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![ZenML](https://img.shields.io/badge/ZenML-Pipeline-blueviolet?logo=zenml)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange?logo=mlflow)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

An end-to-end Machine Learning pipeline for predicting house prices, built with **ZenML** for pipeline orchestration and **MLflow** for experiment tracking and model management.

---

## 📌 Problem Statement

Predicting house prices accurately is a critical challenge in the real estate industry. Manual estimation is time-consuming and inconsistent. This project builds a **production-ready ML pipeline** that automates the entire workflow — from raw data ingestion to model deployment — enabling fast, reliable, and reproducible price predictions.

---

## 🏗️ Pipeline Architecture

```
Raw Data
   │
   ▼
📥 Data Ingestion
   │   └── Load dataset, validate schema
   │
   ▼
🔧 Data Preprocessing
   │   └── Handle missing values, feature engineering, encoding, scaling
   │
   ▼
🤖 Model Training
   │   └── Train Regression model, log parameters with MLflow
   │
   ▼
📊 Model Evaluation
   │   └── Evaluate metrics, log results to MLflow tracking server
   │
   ▼
🚀 Model Deployment
       └── Register best model, serve predictions
```

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Pipeline Orchestration** | ZenML |
| **Experiment Tracking** | MLflow |
| **ML / Modeling** | Scikit-learn (Regression) |
| **Data Processing** | Pandas |
| **Visualization** | Matplotlib, Seaborn |
| **Language** | Python 3.8+ |

---

## 📂 Project Structure

```
house-price-prediction/
│
├── analysis/
│   ├── analyze_src/   
│       ├── basic_data_inspection.py
│       ├── bivariate_analysis.py
│       ├── missing_values_analysis.py
│       ├── multivariate_analysis.py
│       └── univariate_analysis.py
│
│   └── EDA.ipynb                  # Exploratory Data Analysis
│
├── pipelines/
│   ├── deployment_pipeline.py          # deployment pipeline
│   └── training_pipeline.py       # ZenML pipeline definition
│
├── steps/
│   ├── data_ingestion_step.py             # Data ingestion step
│   ├── data_splitter_step.py              # Preprocessing step
│   ├── dynamic_importer.py             # Importer step
│   ├── feature_engineering_step.py          # Feature engineering step
│   ├── handle_missing_values.py          # Missing values evaluation step
│   ├── model_building_step.py          # Model builder step
│   ├── model_evaluator_step.py          # Model evaluation step
│   ├── outlier_detection_step.py          # Outlier detection step
│   ├── prediction_service_loader.py          # Prediction service step
│   └── predictor.py      # Deployment step
│   
├── src/
│   ├── data_splitter.py           
│   ├── feature_engineering.py
│   ├── handle_missing_values.py           
│   ├── ingest_data.py           
│   ├── model_building.py           
│   ├── model_evaluator.py           
│   └── outlier_detection.py                   
│
├── config.yaml
├── requirements.txt
├── run_deployment.py
├── run_pipeliene.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize ZenML
```bash
zenml init
zenml integration install mlflow -y
```

### 4. Set Up MLflow Stack
```bash
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow_deployer --flavor=mlflow
zenml stack register mlflow_stack \
    -a default \
    -o default \
    -d mlflow_deployer \
    -e mlflow_tracker \
    --set
```

### 5. Run the Pipeline
```bash
python run_pipeline.py
```

### 6. View Experiments in MLflow UI
```bash
mlflow ui
```
Open your browser at `http://localhost:5000` to view tracked experiments, metrics, and registered models.

---

## 📊 Key Features

- ✅ **Reproducible pipelines** — Every run is tracked and versioned with ZenML
- ✅ **Experiment tracking** — All model parameters and metrics logged automatically via MLflow
- ✅ **Model registry** — Best performing model registered and versioned in MLflow Model Registry
- ✅ **Automated deployment** — Model deployment triggered automatically when evaluation criteria are met
- ✅ **Modular steps** — Each pipeline step is independently testable and reusable

---

## 🔍 Exploratory Data Analysis

Key insights from EDA:

- Analyzed feature correlations using heatmaps (Seaborn)
- Identified and handled outliers in price distribution
- Visualized relationships between key features (area, location, rooms) and target price using Matplotlib

---

## 🧠 Model Details

| Parameter | Detail |
|---|---|
| **Algorithm** | Regression (Scikit-learn) |
| **Target Variable** | House Price |
| **Tracking** | MLflow (parameters, metrics, artifacts) |
| **Versioning** | MLflow Model Registry |

---

## 📈 MLflow Tracking

All experiments are tracked including:
- Model hyperparameters
- Evaluation metrics (RMSE, MAE, R² Score)
- Model artifacts and versions
- Pipeline run history

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Maruthi Nandan**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/maruthi10/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/Maruthi-Nandan)
