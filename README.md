📊 Twitter Sentiment Analysis
📌 Project Overview
This project analyzes Twitter data to understand public sentiment using machine learning–based sentiment classification and presents insights through an interactive Power BI dashboard. The solution is designed to be dataset-agnostic, meaning it works with any compatible sentiment CSV file.

**The project demonstrates an end-to-end analytics workflow, combining ML/NLP concepts, backend processing with Flask, and business intelligence visualization using Power BI.
**
🎯** Project Objectives**
    1.Analyze Twitter sentiment data (Positive, Negative, Neutral, Irrelevant)
    2.Apply machine learning–based sentiment classification results
    3.Visualize sentiment distribution and counts
    4.Enable interactive filtering and drill-down analysis
    5.Build a reusable, portfolio-ready Power BI dashboard

📁 **Project Folder Structure**
Twitter_Sentiment_Analysis/
│
├── app.py
├── export_sentiment.py
├── run_sentiment_pipeline.py
├── mapper.py
├── reducer.py
├── sentiment_job/
│
├── data/
│   └── twitter_training.csv
│
├── sentiment_results.csv
├── sentiment_model.joblib
├── vectorizer.joblib
│
├── Power BI/
│   └── Twitter_Sentiment_Analysis.pbix
│
├── templates/
├── static/
│
├── screenshots/
│   ├── dashboard_overview.png
│   ├── sentiment_distribution.png
│   └── filtered_view.png
│
├── .gitattributes
├── .gitignore

📂 Dataset Description

The dataset used in this project contains the following columns:

  1.Column Name	Description
  2.TweetID	Unique identifier for each tweet
  3.Sentiment	Sentiment label (Positive, Negative, Neutral, Irrelevant)
  4.TweetText	Tweet content
  5.TweetDate	Date column added during preprocessing

✅ The dashboard does not rely on topic-specific columns, making it compatible with a wide range of sentiment datasets.

🧠 Key Features

  1.Machine Learning–Based Sentiment Analysis
  2.Uses ML-generated sentiment labels as input
  3.Interactive Power BI Dashboard
  4.Sentiment distribution (donut chart)
  5.Sentiment counts (bar chart)
  6.KPI cards (Total Tweets, Positive %, Negative & Neutral counts)
  7.Dynamic Filtering
  8.Filter by sentiment and date
  9.Tweet-Level Drill Down
  10.View individual tweet text with sentiment labels
  11.Dataset-Agnostic Design
  12.Works with any CSV containing sentiment and text columns

📊 Power BI Dashboard

An interactive Power BI dashboard was built to visualize insights clearly and intuitively.

🔹 Dashboard Overview
🔹 Sentiment Distribution
🔹 Filtered View

🛠️ Tech Stack
🔹 Machine Learning & NLP
    1.Machine Learning–Based Sentiment Classification
    2.Natural Language Processing (NLP)
    3.Pre-labeled / ML-generated sentiment outputs

🔹 Backend & Application Layer
    1.Python
    2.Flask – backend integration and data flow
    3.Pandas – CSV data processing and manipulation

🔹 Data Visualization & BI
   1.Power BI Desktop
   2.Power Query – data cleaning & schema normalization

DAX – KPI calculations and measures

🔹 Data & Tools

CSV Data Source

1.VS Code
2.Git & GitHub

🔄 End-to-End Workflow

1.Tweet text is analyzed using ML/NLP sentiment classification
2.Data is processed using Python & Pandas
3.Flask manages backend integration
4.Cleaned data is loaded into Power BI
5.Power Query normalizes schema
6.DAX powers interactive KPIs and visuals
7.Dashboard insights are exported as screenshots for GitHub

📈 DAX Measures Used

1.Total Tweets
2.Positive Tweets
3.Positive Percentage
4.Negative Tweets
5.Neutral Tweets

Measures are written to handle filters and missing values gracefully.

🚀 How to Run the Project

1.Clone the repository
2.Open the .pbix file using Power BI Desktop
3.Load the CSV file from the data/ folder (or replace with your own)
4.Ensure required columns exist (Sentiment, TweetText, TweetID)
5.Apply changes — the dashboard updates automatically
6.(Optional) Export as a Power BI Template (.pbit) for reuse.

PowerBI Dashboard:
Distribution of all the sentiments:
<img width="1148" height="637" alt="image" src="https://github.com/user-attachments/assets/92aab078-6321-40a1-8b79-bc5384952005" />

Sentiment: Negative 
<img width="1152" height="637" alt="image" src="https://github.com/user-attachments/assets/2fdd7ab7-ed2a-45fc-b67f-6028a7c52fcd" />

Sentiment: Positive
<img width="1151" height="642" alt="image" src="https://github.com/user-attachments/assets/3c26166d-b9f8-477d-a542-f61e33441e5b" />

Sentiment: Neutral
<img width="1158" height="632" alt="image" src="https://github.com/user-attachments/assets/9d9d5142-5d53-4535-bf7f-1bbd9fe56cc5" />

Sentiment: irrelevant
<img width="1146" height="638" alt="image" src="https://github.com/user-attachments/assets/3ab6cdb5-b683-4c2b-9b19-746bd40d90b3" />


