from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(X, y):
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def save_model(model, path="models/model.pkl"):
    joblib.dump(model, path)

def load_model(path="models/model.pkl"):
    return joblib.load(path)
