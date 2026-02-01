#!/usr/bin/env python
import sys
from collections import defaultdict

sentiment_counts = defaultdict(int)
word_counts = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        key, value = line.split('\t', 1)
    except ValueError:
        continue

    if key == "__SUMMARY__":
        sentiment_counts[value] += 1
    else:
        senti, word = key, value
        word_counts[senti][word] += 1

total = sum(sentiment_counts.values())
if total == 0:
    print("No sentiment data found.")
    sys.exit(0)

print("Sentiment distribution:")
for senti, cnt in sentiment_counts.items():
    pct = cnt / total * 100
    print(f"{senti}: {cnt} ({pct:.2f}%)")

for senti in ["Positive", "Negative"]:
    print(f"\nTop {senti.lower()} words:")
    for w, cnt in sorted(word_counts[senti].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{w}: {cnt}")
