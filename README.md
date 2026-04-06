# NFL Play Success Predictor

A machine learning project that predicts whether an NFL play will gain positive yards using historical play-by-play data from 2020–2023.

---

## Overview

This project uses the `nfl_data_py` package to pull NFL play-by-play data and trains a **Random Forest Classifier** to predict play success based on down, distance, field position, score differential, and more.

---

## Project Structure

```
MilesStone1Project/
├── data/
│   ├── raw_pbp.csv            # Raw play-by-play data (not tracked by Git)
│   └── processed_pbp.csv      # Cleaned and engineered features
├── notebooks/
│   └── 01_eda.ipynb           # EDA, visualizations, and model training
├── src/
│   ├── load_data.py           # Downloads raw NFL data via nfl_data_py
│   └── preprocess.py          # Cleans data and engineers features
├── models/
│   └── train_model.py         # Trains and evaluates the Random Forest model
├── model/
│   └── nfl_model.pkl          # Saved trained model (not tracked by Git)
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/Zimani-Z/MilesStone1Project.git
cd MilesStone1Project
```

### 2. Create and activate conda environment
```bash
conda create -n myenv python=3.11
conda activate myenv
```

### 3. Install dependencies
```bash
conda install -y -c conda-forge numpy scipy scikit-learn joblib matplotlib seaborn jupyter ipykernel
pip install nfl_data_py
```

### 4. Register Jupyter kernel
```bash
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

---

## How to Run

Run these commands in order from the project root:

```bash
# Step 1 — Download raw NFL play-by-play data (2020–2023)
python src/load_data.py

# Step 2 — Clean and engineer features
python src/preprocess.py

# Step 3 — Train the model and print evaluation metrics
python models/train_model.py

# Step 4 — Launch Jupyter notebook for visualizations
jupyter notebook
```

Then open `notebooks/01_eda.ipynb` and select **Kernel → Python (myenv)**.

---

## Features Used

| Feature | Description |
|---|---|
| `down` | 1st, 2nd, 3rd, or 4th down |
| `ydstogo` | Yards needed for a first down |
| `yardline_100` | Distance from end zone (1–100) |
| `score_differential` | Score difference at time of play |
| `epa` | Expected Points Added |
| `is_pass` | 1 if pass play, 0 if run |
| `red_zone` | 1 if inside opponent's 20-yard line |
| `late_game` | 1 if under 5 minutes remaining |
| `losing_big` | 1 if trailing by more than 7 points |
| `short_yardage` | 1 if 2 or fewer yards to go |

**Target:** `success` — 1 if the play gained positive yards, 0 if not.

---

## Model

- **Algorithm:** Random Forest Classifier (100 trees)
- **Train/Test Split:** 80/20
- **Evaluation:** Accuracy, Precision, Recall, F1, Confusion Matrix

---

## Visualizations (in notebook)

- Play success rate by down
- Success rate by yards to go
- EPA distribution: pass vs run
- Red zone pass vs run comparison
- Confusion matrix heatmap
- Feature importance chart
- Custom play prediction cell

---

## Future Improvements

- Filter and compare specific NFL teams
- Add rolling averages per team
- Hyperparameter tuning with GridSearchCV
- Try Gradient Boosting / XGBoost
- Cross-validation
- Deploy model as a simple API

---

## Data Source

Play-by-play data from [nflverse](https://github.com/nflverse/nflverse-data) via the `nfl_data_py` Python package. Seasons: 2020–2023.

---

## Technologies

Python · Pandas · Scikit-learn · NumPy · Matplotlib · Seaborn · nfl_data_py · Jupyter · conda