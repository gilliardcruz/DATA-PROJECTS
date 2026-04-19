"""
Script de treinamento do modelo de previsão de vendas.
Treina um modelo Random Forest e o salva em disco.
"""

import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from config import DATA_PATH, MODEL_PATH, MODEL_CONFIG, TRAIN_TEST_CONFIG, FEATURE_COLUMNS, TARGET_COLUMN
from preprocess import load_data, preprocess


# Load data
print("Loading data...")
df = load_data(str(DATA_PATH))
print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Preprocess data
print("Preprocessing data...")
df = preprocess(df)
print(f"Data after preprocessing: {df.shape[0]} rows")

# Prepare features and target
X = df[FEATURE_COLUMNS]
y = df[TARGET_COLUMN]

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split data
print("Splitting data into train/test sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, **TRAIN_TEST_CONFIG)

# Train model
print("Training RandomForest model...")
model = RandomForestRegressor(**MODEL_CONFIG)
model.fit(X_train, y_train)

# Evaluate model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Model R² Score - Train: {train_score:.4f}, Test: {test_score:.4f}")

# Save model
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, str(MODEL_PATH))
print(f"Model saved to: {MODEL_PATH}")

