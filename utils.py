import pandas as pd

def preprocess_data(df):
    df = df.dropna()
    df["Target"] = df["Close"].shift(-1)
    df = df.dropna()
    X = df[["Open", "High", "Low", "Volume"]]
    y = df["Target"]
    return X, y
