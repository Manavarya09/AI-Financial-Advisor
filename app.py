from data_fetcher import fetch_data
from utils import preprocess_data
from model import train_model, save_model
from predictor import predict_next_day

def main():
    df = fetch_data("AAPL")
    X, y = preprocess_data(df)
    model = train_model(X, y)
    save_model(model)
    prediction = predict_next_day(df)
    print(f"Predicted Next Close Price: ${prediction:.2f}")

if __name__ == "__main__":
    main()
