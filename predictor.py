import pandas as pd
from model import load_model

def predict_next_day(df, model_path="models/model.pkl"):
    model = load_model(model_path)
    features = df[["Open", "High", "Low", "Volume"]].iloc[-1].values.reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]
