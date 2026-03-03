NFL Game Outcome Prediction
Overview

This project predicts NFL game outcomes (home team win or loss) using team-level statistics, home-field advantage, and engineered features. The goal is to evaluate how well machine learning models can predict game results using historical data.

Dataset

Data was obtained using the nflverse Python package, which provides comprehensive play-by-play and game-level NFL data.

Seasons used: 2020–2023

Project Structure
nfl-game-prediction/
│
├── data/                # Processed datasets
├── notebooks/           # Exploratory data analysis
├── src/                 # Source code for data processing and modeling
├── models/              # Saved trained models
├── requirements.txt
└── README.md

Features Engineered

Home win (target variable)

Point differential

Additional engineered features to be added:

Turnover differential

Rolling averages

Weather indicators

Modeling Approach

Baseline Model:

Logistic Regression

Future Models:

Random Forest

Gradient Boosting

Evaluation Metrics

Accuracy

Confusion Matrix

Precision / Recall (planned)

Results

Baseline logistic regression achieved approximately XX% accuracy on the test set.

Future Improvements

Add advanced metrics (EPA)

Hyperparameter tuning

Cross-validation

Model comparison

Deploy as API

Technologies Used

Python

Pandas

Scikit-learn

nflverse

Matplotlib / Seaborn