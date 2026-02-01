Here are details to add to a README file for your Twitter sentiment analysis project:

Twitter Sentiment Analysis with Hadoop Streaming
Project Overview
This project implements a scalable sentiment analysis pipeline for Twitter data, utilizing Hadoop Streaming and a pre-trained machine learning model. It provides functionalities for analyzing text files containing multiple tweets and individual user queries through a Flask-based web interface.

Features

Scalable Sentiment Analysis: Processes large tweet datasets efficiently using Hadoop Streaming for distributed computing.


Machine Learning Integration: Employs a pre-trained Logistic Regression model and TF-IDF vectorizer for accurate positive/negative sentiment classification.


Text Preprocessing: Includes robust cleaning functions to handle URLs, mentions, hashtags, punctuation, and numerical digits in tweets.


Web Interface (Flask): An interactive web application allows users to upload .txt files for batch analysis or input single queries for real-time sentiment prediction.


Sentiment Distribution Visualization: Generates a pie chart (sentiment_pie.png) visualizing the overall sentiment distribution from file analysis.


Top Word Extraction: Identifies and lists the top 10 most frequent positive and negative words from analyzed data.


Modular Design: The pipeline is structured with distinct mapper.py and reducer.py scripts for clarity and Hadoop compatibility.


Technologies Used
Python 3 

Flask 

Hadoop Streaming 

NLTK (for tokenization, stopwords) 

Scikit-learn (Logistic Regression, TF-IDF) 

Joblib (model persistence) 

Matplotlib (for visualizations) 

Project Structure

app.py: Main Flask application handling web routes, file uploads, query analysis, and pipeline execution.

mapper.py: Hadoop mapper; cleans text, predicts sentiment, and emits data for sentiment counts and word counts. Also generates the sentiment distribution pie chart.


reducer.py: Hadoop reducer; aggregates sentiment and word counts, then outputs distribution and top words.


run_sentiment_pipeline.py: Orchestrates the Hadoop Streaming job, managing HDFS interactions.


sentiment_job/: Contains mapper.py, reducer.py, sentiment_model.joblib, vectorizer.joblib, and uploaded tweets.txt.


static/: Stores generated static files, like sentiment_pie.png.


templates/: Contains index.html for the web interface.

Setup and Installation
Prerequisites:

Apache Hadoop installed and configured.

Python 3 and pip.

NLTK data (

punkt, stopwords) (handled by mapper.py on first run).

Steps:

Clone the repository:

Bash

git clone <repository_url>
cd <repository_name>
Install Python dependencies:

Bash

pip install -r requirements.txt
(Create a requirements.txt file with: Flask, scikit-learn, joblib, nltk, matplotlib)

Place pre-trained model/vectorizer: Ensure sentiment_model.joblib and vectorizer.joblib are in the sentiment_job/ directory.

Configure Hadoop paths: Update HADOOP_JAR in run_sentiment_pipeline.py to your hadoop-streaming-x.x.x.jar path. Adjust 

HDFS_INPUT and HDFS_OUTPUT as needed.

Run the Flask application:

Bash

python app.py
Access the web interface: Open your browser to http://localhost:5000.

