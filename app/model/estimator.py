import joblib
import numpy as np
import os
import pandas as pd

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

def predict_price(data):
    # Expected keys: sqft, floors, surface_type, exterior, coats, paint_quality
    input_df = pd.DataFrame([{
        "sqft": data.get("sqft", 0),
        "floors": data.get("floors", 1),
        "surface_type": data.get("surface_type", "drywall"),
        "exterior": int(data.get("exterior", True)),
        "coats": data.get("coats", 2),
        "paint_quality": data.get("paint_quality", "standard")
    }])

    prediction = model.predict(input_df)
    return round(prediction[0], 2)