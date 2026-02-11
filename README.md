# House Price Prediction — Internship Project

**Author:** Cornescu Darius  
**Project:** Machine Learning & Data Science Internship

---

## Overview

This repository documents the complete work performed during an internship focused on **house price prediction** using machine learning. The project spans data cleaning, exploratory analysis, feature engineering, model selection, and deployment of a full-stack web application.

---

## Project Structure

```
House-price-prediction/
├── datasets/              # Processed datasets
├── notebooks/             # Jupyter notebooks (analysis & experimentation)
├── final_project/         # Production app (backend + frontend + ML model)
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Datasets

| File | Description |
|------|-------------|
| `house_prices.csv` | Original Ames Housing dataset (1,460+ records) |
| `house_prices_selection.csv` | Subset with selected features for analysis |
| `Cornescu_Darius_encoded.csv` | Encoded dataset after preprocessing |
| `Cornescu_Darius_features_encoded.csv` | Features with one-hot encoding |
| `Cornescu_Darius_new_features.csv` | Feature-engineered dataset |
| `Cornescu_Darius_selected_features.csv` | Final selected features for modeling |
| `subset_classification_Cornescu_Darius.csv` | Subset used for classification tasks |

---

## Internship Work — Notebooks

### 1. Data Cleaning (`1_data_cleaning_Cornescu_Darius.ipynb`)
- Missing value analysis and handling
- Dropping high-missing columns (e.g., Cabin, Age)
- Imputation strategies (KNN, SimpleImputer)
- Basic EDA and survival analysis (Titanic dataset)

### 2. Subdataset Analysis (`2_subdataset_analysis_Cornescu_Darius.ipynb`)
- Working with house price subsets
- Exploratory analysis on lot, zoning, condition, neighborhood
- Sale price distribution and relationships

### 3. Feature Engineering (`3_feature_engineering_Cornescu_Darius.ipynb`)
- Creating derived features:
  - `LotArea_m²` (lot area in square meters)
  - `Price_per_m²` (price per square meter)
  - `ZoningScore`, `SubClassScore`, `LotAreaNorm`
  - `PDI` (Price Density Index)
  - `EVI` (derived value index)
- Normalization and scaling

### 4. Feature Selection (`4_FeatureSelection_CorenscuDarius.ipynb`)
- Correlation analysis with SalePrice
- Identifying top predictive features (LotFrontage, ZoningScore, EVI, etc.)
- Selection of numerical and categorical features for modeling

### 5. Clustering (`5_Cornescu_Darius_Clustering.ipynb`)
- K-means clustering on house price data
- Feature selection for clustering (LotFrontage, ZoningScore, EVI, LotArea, etc.)
- Visualizing clusters with Plotly

### 6. Clustering — Silhouette Analysis (`6_Cornescu_Darius_Clustering_Silhouette.ipynb`)
- Evaluating optimal number of clusters using silhouette score
- Comparing clustering quality across different k values

### 7. Pipeline (`7_Cornescu_Darius_pipeline.ipynb`)
- Building sklearn pipelines with preprocessing
- ColumnTransformer (numerical + categorical)
- DecisionTreeRegressor for regression
- SHAP for model interpretability

### 8. Split Comparison (`8_Cornescu_Darius_split_comparison.ipynb`)
- **Manual determination of optimal intervals** for clusters (binning) based on price distribution analysis
- Distribution analysis with different bin widths (100k, 50k, 20k, 10k, 5k)
- `create_smart_bins` — custom intervals for classification (very_cheap, affordable, medium_low, etc.)
- Iterative adjustment of boundaries to **maximize metrics** (e.g., very_cheap 80k→90k → improvement from 0.64 to 0.688)
- Decision Tree vs Random Forest; Stratified K-Fold; GridSearchCV

### 9. Random Forest (`9_Cornescu_Darius_RandomForest.ipynb`)
- Random Forest vs Decision Tree classification
- Confusion matrices, precision, recall, F1-score
- Model comparison

### 10. Split Random Forest (`10_Cornescu_Darius_split_RandomForest.ipynb`)
- XGBoost vs Random Forest vs Decision Tree
- Price binning methods: qcut, kmeans, custom
- Best accuracy: **83.33%** (XGBoost + KMEANS binning)

### 11. Linear Regression — Full Dataset (`11_Cornescu_Darius_LinearRegression_Full_dataset.ipynb`)
- Linear Regression, Decision Tree, Random Forest, XGBoost on full house price dataset
- R², MAE, RMSE comparison
- Model stacking (StackingRegressor)
- SHAP and Permutation Importance for feature importance

### 12. User Experience Features (`12_User_experince_features_Cornescu_Darius.ipynb`)
- **Final production pipeline** — `complete_pipeline.joblib`
- XGBRegressor (n_estimators=500, max_depth=5)
- GridSearchCV for hyperparameter tuning
- Features: OverallQual, GrLivArea, GarageCars, etc.
- Export for deployment

### 13. Clustering — Full Dataset (`Cornescu_Darius_Clustering_Full_dataset.ipynb`)
- K-means on full dataset with engineered features
- Classification: XGBoost, Logistic Regression, SVM
- Ensemble: Voting, Stacking, Bagging
- SHAP feature importance comparison

### 14. Entire Selected Features (`entire_selected_features_Cornescu_Darius.ipynb`)
- Modeling with full selected feature set
- Cross-validation and model evaluation

---

## Technologies Used

- **Python:** pandas, numpy, matplotlib, seaborn, scikit-learn
- **ML:** XGBoost, Random Forest, Decision Tree, Linear Regression, K-means
- **Visualization:** Plotly, SHAP
- **Tools:** Jupyter, sklearn Pipelines, ColumnTransformer

---

## Final Project

The production application is in `final_project/` — a full-stack House Price Prediction web app:
- **Backend:** FastAPI (Python)
- **Frontend:** React + Vite + Bootstrap
- **Model:** XGBoost regressor (serialized via joblib)

For detailed documentation of the final app, see [README in final_project](final_project/README.md).

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run notebooks (from project root)
jupyter notebook notebooks/
```

---

## Summary

| Phase | Deliverables |
|-------|--------------|
| 1. Data | Cleaning, subset analysis, encoding |
| 2. Features | Engineering (PDI, EVI, ZoningScore), selection |
| 3. Unsupervised | K-means clustering, silhouette analysis |
| 4. Supervised | Classification (RF, DT, XGBoost), Regression (LR, RF, XGBoost) |
| 5. Deployment | FastAPI backend + React frontend + XGBoost model |

---

*Internship project by Cornescu Darius — House Price Prediction.*
