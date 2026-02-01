import csv
from datetime import datetime
from joblib import load

# Load model and vectorizer
model = load("sentiment_job/sentiment_model.joblib")
vectorizer = load("sentiment_job/vectorizer.joblib")

def analyze_and_save(texts):
    X = vectorizer.transform(texts)
    predictions = model.predict(X)

    with open("sentiment_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "sentiment", "timestamp"])

        for text, pred in zip(texts, predictions):
            sentiment = "Positive" if pred == 1 else "Negative"
            writer.writerow([text, sentiment, datetime.now()])

    print("✅ sentiment_results.csv created")

if __name__ == "__main__":
    sample_texts = [
        "I love this product",
        "Worst service ever",
        "It was okay, not great",
        "Amazing experience"
    ]
    analyze_and_save(sample_texts)
