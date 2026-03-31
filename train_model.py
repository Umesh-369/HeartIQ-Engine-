import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import os

print("--- Heart Disease Prediction ML Training ---")
print("Loading dataset 'Heart_Disease_Prediction.csv'...")

try:
    df = pd.read_csv('Heart_Disease_Prediction.csv')
except FileNotFoundError:
    print("Error: Could not find 'Heart_Disease_Prediction.csv'. Please ensure it's in the same directory.")
    exit(1)

# The dataset target column is 'Heart Disease' with values 'Presence' and 'Absence'
# We map them to 1 (Presence) and 0 (Absence)
df['Heart Disease'] = df['Heart Disease'].map({'Presence': 1, 'Absence': 0})

X = df.drop('Heart Disease', axis=1)
y = df['Heart Disease']

print(f"Dataset loaded. Processing {len(df)} records with {len(X.columns)} features.")

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling - Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Evaluating multiple models to find the best accuracy...")

# Define models and their hyperparameter grids
models_and_params = {
    'Logistic Regression': (
        LogisticRegression(max_iter=1000, random_state=42),
        {'C': [0.1, 1, 10, 100]}
    ),
    'Support Vector Machine': (
        SVC(probability=True, random_state=42),
        {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
    ),
    'Random Forest': (
        RandomForestClassifier(random_state=42),
        {'n_estimators': [50, 100, 200], 'max_depth': [None, 5, 10], 'min_samples_leaf': [1, 2, 4]}
    ),
    'Gradient Boosting': (
        GradientBoostingClassifier(random_state=42),
        {'n_estimators': [50, 100], 'learning_rate': [0.01, 0.1, 0.2], 'max_depth': [3, 4, 5]}
    )
}

best_model = None
best_accuracy = 0
best_model_name = ""

# Grid Search to find the best model
from sklearn.model_selection import GridSearchCV

for name, (model_instance, params) in models_and_params.items():
    print(f"Training {name} with GridSearch...")
    grid = GridSearchCV(model_instance, params, cv=5, n_jobs=-1, scoring='accuracy')
    grid.fit(X_train_scaled, y_train)
    
    # Evaluate
    y_pred = grid.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Validation Accuracy: {grid.best_score_ * 100:.2f}%, Test Accuracy: {acc * 100:.2f}%")
    
    if acc > best_accuracy:
        best_accuracy = acc
        best_model = grid.best_estimator_
        best_model_name = name

print(f"\n[Winner Models Selection] Best Model: {best_model_name} with Accuracy: {best_accuracy * 100:.2f}%")
model = best_model

# Save the trained model and the scaler to disk
print("Saving model to 'heart_disease_model.pkl' and scaling parameters to 'scaler.pkl'...")
joblib.dump(model, 'heart_disease_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Done! You can now start the API server to use this model.")
