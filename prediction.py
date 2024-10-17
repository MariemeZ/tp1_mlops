# prediction.py
import joblib
import numpy as np

def load_model():
    model = joblib.load('iris_model.joblib')
    return model

def predict(features):
    model = load_model()
    prediction = model.predict(np.array(features).reshape(1, -1))
    return prediction[0]
