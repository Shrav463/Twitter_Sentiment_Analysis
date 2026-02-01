from flask import Flask, request, render_template
from flask_cors import CORS
import os
import joblib
from run_sentiment_pipeline import run_sentiment_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'sentiment_job'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
model = joblib.load("sentiment_job/sentiment_model.joblib")
vectorizer = joblib.load("sentiment_job/vectorizer.joblib")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"@\w+|#", '', text)
    text = re.sub(r"[^\w\s]", '', text)
    text = re.sub(r"\d+", '', text)
    return re.sub(r"\s+", ' ', text).strip()

def predict_sentiment(query):
    cleaned = clean_text(query)
    X = vectorizer.transform([cleaned])
    sentiment = "Positive" if model.predict(X)[0] == 1 else "Negative"
    return sentiment

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze_file", methods=["POST"])
def analyze_file():
    file_result = None
    uploaded_file = request.files.get("file")
    if uploaded_file and uploaded_file.filename.endswith(".txt"):
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], "tweets.txt")
        try:
            uploaded_file.save(save_path)
        except Exception as e:
            file_result = f"[ERROR] Failed to save file: {e}"
            return render_template("index.html", file_result=file_result)

        try:
            output = run_sentiment_pipeline()
            file_result = output if "=== Sentiment Analysis Result ===" in output else f"=== Sentiment Analysis Result ===\n{output}"
        except Exception as e:
            file_result = f"[ERROR] Exception occurred: {str(e)}"
        try:
            os.remove(save_path)
        except Exception:
            pass
    else:
        file_result = "[ERROR] Please upload a .txt file."

    return render_template("index.html", file_result=file_result, timestamp=datetime.now().timestamp())

@app.route("/analyze_query", methods=["POST"])
def analyze_query():
    query_result = None
    query = request.form.get("query")
    if query:
        try:
            sentiment = predict_sentiment(query)
            query_result = f"Sentiment for your query: {sentiment}"
        except Exception as e:
            query_result = f"[ERROR] Failed to analyze query: {e}"

    return render_template("index.html", query_result=query_result, timestamp=datetime.now().timestamp())

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)


