""" File for homepage """
import sys 
import os 
import dash
from dash import dcc, html


#initialising
dash.register_page(__name__, name='Welcome Page', order=1,path='/')

#Layout 

layout = html.Div(
    [
        html.Br(),
        html.H1('What Is This Web App For?'),
        html.P('Youtube video analyser (YVA) is an app\
            that leverages natural language processing with machine learning techniques,\
                to give you insight about a youtube video without ever watching it.',
                style = {
                    'font-size':'20px',
                }),
        html.Br(),
        html.H2('Currently Supported Features:'),
        html.Li('Main Video Metrics',style={'font-weight': 'bold','font-size':'20px',}),
        html.P('Simple metrics such as likes and views'),
        html.Li('Video Caption',style={'font-weight': 'bold','font-size':'20px',}),
        html.P('If available, will acquire the complete transcript of a video'),
        html.Li('Video Caption Summarisation',style={'font-weight': 'bold','font-size':'20px',}),
        html.P('Summarises the transcript of a video to be as short as possible'),
        html.Li('Named-entity Recognition (NER)',style={'font-weight': 'bold','font-size':'20px',}),
        html.P('Identifies the most mentioned name, organisation and place from a video'),
        html.Li('Sentiment Analysis (SA)',style={'font-weight': 'bold','font-size':'20px',}),
        html.P('Determines the range of emotions evoked by a video'),
    ],
    style = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }
    )


#call backs


