import sys
import os
import re
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Download required NLTK data (no effect if already downloaded)
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception as e:
    print(f"[ERROR] Failed to download NLTK data: {e}", file=sys.stderr)
    sys.exit(1)

# Script directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model, vectorizer, and stopwords
stop_words = set(stopwords.words('english'))
model_path = os.path.join(THIS_DIR, "sentiment_model.joblib")
vec_path = os.path.join(THIS_DIR, "vectorizer.joblib")

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vec_path)
except FileNotFoundError as e:
    print(f"[ERROR] Model or vectorizer file not found: {e}", file=sys.stderr)
    sys.exit(1)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"@\w+|#", '', text)
    text = re.sub(r"[^\w\s]", '', text)
    text = re.sub(r"\d+", '', text)
    return re.sub(r"\s+", ' ', text).strip()

# Sentiment counts for plotting
sentiment_counts = {"Positive": 0, "Negative": 0}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    cleaned = clean_text(line)
    if not cleaned:
        continue

    tokens = word_tokenize(cleaned)
    words = [w.lower() for w in tokens if w.lower() not in stop_words]

    try:
        X = vectorizer.transform([cleaned])
        sentiment = "Negative" if model.predict(X)[0] == 0 else "Positive"
        sentiment_counts[sentiment] += 1  # Update sentiment count
    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}", file=sys.stderr)
        continue

    print(f"__SUMMARY__\t{sentiment}")
    for w in words:
        print(f"{sentiment}\t{w}")  # Plot Sentiment Distribution

# Plotting the sentiment distribution as a pie chart
labels = list(sentiment_counts.keys())
sizes = list(sentiment_counts.values())
color_map = {
    "Positive": "#ef4444",  # Red for positive sentiment
    "Negative": "#3b82f6"   # Blue for negative sentiment
}

colors = [color_map.get(label, "#9ca3af") for label in labels]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Sentiment Distribution')
plt.axis('equal')

# Save the pie chart as a PNG file
output_dir = 'static'
os.makedirs(output_dir, exist_ok=True)
chart_path = os.path.join(output_dir, 'sentiment_pie.png')
plt.savefig(chart_path)
plt.close()

