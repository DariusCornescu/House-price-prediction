# House Price Prediction

**From raw housing data to a working price-estimation web app.** This project follows one dataset (Ames Housing, about 1,460 homes) through the whole machine-learning workflow: cleaning, feature engineering, clustering, model comparison, and a deployed full-stack app that estimates a house's price from a form.

Built during a machine learning and data science internship.

![The app: a property form on the left, the estimated price and recent predictions on the right](screenshots/full_layout.png)

## The app

Fill in a property's details and get an estimated sale price in USD. The app:

- **Validates input twice**: the React form checks ranges and required fields, and the API checks that the details make sense together (for example, remodel year not before build year, garage area consistent with number of cars, lot larger than living area).
- **Predicts** with a single XGBoost pipeline that handles missing values and categorical encoding, so optional fields can be left blank.
- **Keeps a history** of your last 10 predictions.

| Layer | Technology |
|---|---|
| Backend | FastAPI, Pydantic, uvicorn |
| Frontend | React, Vite, Bootstrap |
| Model | scikit-learn pipeline with XGBoost regressor (500 trees, depth 5), saved with joblib |

Setup and details are in [final_project/README.md](final_project/README.md).

## The data science work

The 14 notebooks in `notebooks/` show how the model was built, in order:

| Stage | What was done |
|---|---|
| **Cleaning** | Missing-value analysis, KNN and simple imputation |
| **Feature engineering and selection** | Derived features such as price per m², zoning score and value indices, then correlation-based selection |
| **Clustering** | K-means with silhouette analysis to find natural groups of homes |
| **Classification** | Price banded into classes. Compared decision tree, random forest and XGBoost with stratified cross-validation and grid search. The best classifier reached **83.3% accuracy** (XGBoost with k-means price bands) |
| **Regression** | Compared linear regression, decision tree, random forest, XGBoost and a stacked ensemble on R², MAE and RMSE, with SHAP and permutation importance for explainability |
| **Production pipeline** | Final XGBoost pipeline tuned with grid search and exported for the app (`final_project/ml_models/`) |

## Run it

```bash
pip install -r requirements.txt

# Backend
cd final_project
uvicorn backend.main:app --reload --port 8000

# Frontend (in a second terminal)
cd final_project/frontend
npm install
npm run dev
```

The app opens at http://localhost:5173. To explore the experiments, run `jupyter notebook notebooks/`.

## Repository layout

```
datasets/        Original and processed datasets
notebooks/       The 14 analysis and modelling notebooks
final_project/   The web app: FastAPI backend, React frontend, trained pipeline
screenshots/     App screenshots
```
