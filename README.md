# Youtube Video Analyser (Version 1.0)
## Use it here: http://ethanl247.pythonanywhere.com/

## Introduction
Youtube Video Analyser (YVA) is web application that leverages natural langauge processing (NLP) via machine learning, to give insight about a Youtube video without ever watching it.

### Current Features:
* **Entity-Named Recognition (NER)** Extracts the most mentioned nouns of people, locations and organisations in a video.
* **Sentiment Analysis** Classifies the most releveant emotions invoked by a video.
* **Common Metric Reports** Plots view, like and comment counts across 50 latest videos.
* **Custom Engagement Metrics** Plots custom metrics such as likes to comment ratio across 50 latest videos

## Technology and Architecture
![alt text]('techmap.png')

### Core technology and frameworks used:
**Testing:**
* Pytest
**Backend:**
* Pandas
* Sqlite
* Transformers library
* Pytorch
* Google-API-Python-Client
**FrontEnd:**
* Dash
* Dash Bootstrap Components
* Dash Core Components
* Flask
* Plotly
**Deployment**
* Python Anywhere


## Setup
1. Install project libraries and dependencies via requirement.txt
2. Enter your own Youtube API Key within youtube_api\ytchannel.py File.
3. Run dash_app\app.py. 

## Limitations and Future
This app is whilst usable is still being worked on and therefore has the following limitations:
1. App can only detect the latest 50 videos uploaded by a channel due to Youtube API free-tier limitations.
2. Pasted channel id and video name must be exact.


## Acknowledgements
NLP pre-trained models credits:
* NER model from https://huggingface.co/dslim/bert-base-NER
* SA model from https://huggingface.co/SamLowe/roberta-base-go_emotions
