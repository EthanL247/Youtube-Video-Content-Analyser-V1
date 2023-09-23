""" File for homepage """
import sys 
import os 
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


#initialising
dash.register_page(__name__, name='Welcome Page', order=1,path='/')


#get pictures 
image1 = 'assets/basic_demo.png'
image2 = 'assets/sa_demo.png'

#Layout 

layout = html.Div(
    [   
        #welcome content
        html.Div(children=[
        html.H1('What Is This Web App For?'),
        html.P('Youtube video analyser (YVA) is an app\
            that leverages natural language processing with machine learning techniques,\
                to give you insight about a youtube video without ever watching it.',
                style = {
                    'font-size':'20px',
                })]),
        html.Br(),
        
        #advance content
        html.Div(
            [
                html.H2('Advance Machine Learning Analysis Features'),
                html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Li('Summarisation',style={'font-weight': 'bold','font-size':'20px',}),
                                html.P('Summarise an entire videos caption to just a few sentences.',style={'font-size':'17px'}), 
                            ]
                        ),
                        dbc.Col(
                            [
                                html.Li('Named-Entity Recognition (NER)',style={'font-weight': 'bold','font-size':'20px',}),
                                html.P('Extracts most mentioned individuals name, organisation and location from a video.',style={'font-size':'17px'}), 
                            ]
                        ),
                        dbc.Col(
                            [
                                html.Li('Sentiment Analysis (SA)',style={'font-weight': 'bold','font-size':'20px',}),
                                html.P('Extracts the most releveant emotions invoked by a video.',style={'font-size':'17px'}), 
                            ]
                        ),
                        
                    ]
                )
                
                   
            ]
        ),
        html.Img(src=image2),
        
        #basic content
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2('Basic Analysis Features'),
        html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Li('Simple Metrics',style={'font-weight': 'bold','font-size':'20px',}),
                        html.P('Plots view, like and comment counts across 50 latest videos.',style={'font-size':'17px'}),
                    ], width=4
                ),
                
                dbc.Col(
                    [
                        html.Li('Custom Engagement Metrics',style={'font-weight': 'bold','font-size':'20px',}),
                        html.P('Plots metrics such as likes to comment ratio across 50 latest videos.',style={'font-size':'17px'})
                        
                    ]
                    
                    
                    ),
                dbc.Col(
                            [
                                html.Li('Other Video Data Acess',style={'font-weight': 'bold','font-size':'20px',}),
                                html.P('Extracts data from other videos uploaded within a 50 videos upload window.',style={'font-size':'17px'}), 
                            ]
                        ),
                    ]
                ),
        html.Img(src=image1),
        #Limitations
        html.Div(
            [
                html.H4('Limitations',style={'color':'red'}),
                html.P('Current state of the web app is considered a vertical slice and  development is on going.\
                    Therefore the following limitations exists:'),
                html.Li('Advance machine learning analysis takes approximated 6-8 minutes to process per video due to the libraries used.'),
                html.Li('Only the latest 50 videos of any channel can be used on this web app due to Youtube API limitations.')
            ]
        ),
    ],
    style = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
            'text-align': 'justify',
            'text-justify': 'inter-word',
        }
    )


