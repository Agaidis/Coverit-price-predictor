import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Mock data
data = pd.DataFrame({
    "sqft": [1000, 1500, 2000, 2500],
    "floors": [1, 2, 2, 3],
    "surface_type": ["drywall", "brick", "stucco", "drywall"],
    "exterior": [1, 1, 1, 0],
    "coats": [2, 2, 3, 1],
    "paint_quality": ["standard", "premium", "premium", "standard"],
    "price": [1800, 2600, 3300, 2000]
})

# Features and target
X = data[["sqft", "floors", "surface_type", "exterior", "coats", "paint_quality"]]
y = data["price"]

# Preprocessing for categorical features
categorical_features = ["surface_type", "paint_quality"]
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'  # Keep numerical features as-is
)

# Build pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Train the model
model.fit(X, y)

# Save it
model_path = os.path.join("app", "model", "model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained and saved with real-world features.")