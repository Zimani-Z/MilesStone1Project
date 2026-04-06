import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os


def train_model():

    print("Loading processed data...")
    df = pd.read_csv("data/processed_pbp.csv")

    
    # Target variable
    
    df["success"] = (df["yards_gained"] > 0).astype(int)

    
    # Features
   
    features = [
        "down",
        "ydstogo",
        "yardline_100",
        "epa",
        "is_pass",
        "red_zone",
        "late_game",
        "losing_big",
        "short_yardage",
    ]

    X = df[features]
    y = df["success"]

   
    # Train/Test split
   
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

   
    # Train model
    
    model = RandomForestClassifier(n_estimators=100)

    print("Training model...")
    model.fit(X_train, y_train)

    
    # Evaluate model
    
    preds = model.predict(X_test)


    accuracy = accuracy_score(y_test, preds)
    print(f"Model Accuracy: {accuracy:.3f}")

    print("\nClassification Report:")
    print(classification_report(y_test, preds, target_names=["No Gain, Gain"]))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, preds,))


    #Feature importance
    importances = pd.Series(model.feature_importances_, index=features)
    print("\nFeature Importances:")
    print(importances.sort_values(ascending=False).to_string())
  
    # Save model
    
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/nfl_model.pkl")
    print("\nModel saved to model/nfl_model.pkl")

    return model, X_test, y_test, preds, importances


if __name__ == "__main__":
    train_model()