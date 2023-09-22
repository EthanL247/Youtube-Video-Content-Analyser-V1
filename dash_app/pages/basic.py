""" File for Machine Learning Analysis """
import os
import sys 
import dash
from dash import dcc, html, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import time


# registering page
dash.register_page(__name__, order=2, name='Basic Analysis')


#adding module paths
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/main')
sys.path.insert(0, 'D:/python_projects/Youtube-Video-Analyser-GUI-Version/dash_app/components')

#importing custom modules
from main_manager import MainManager
from vis import Visualise

#layout
layout = html.Div(
    children=[   
        #input section 
        html.Div([
        html.H1('Enter Channel ID and Youtube Video Name'),
        html.Br(),
        html.Br(),
        #inputs
        dbc.Input(id="basic_channel_id",type="text",value='UCVjlpEjEY9GpksqbEesJnNA'),
        dbc.Input(id="basic_video_name",type="text",value='Uncle Roger LOVE The OG Uncle (Martin Yan)'),
        #Submit button
        dbc.Button(id='basic_submit_button',n_clicks=0,children='Start Basic Analysis'),
        html.Br(),
        ]),
    
        #video data 
        html.Br(),
        html.H2('Channel Latest Video Analysis'),
        html.Br(),
        dbc.Row(
            [
                #people
                dbc.Col(id='video_output'),
            ]
        ),
 
        # channel data visualisation
        html.Div([
            

            
            # Views time series 
            dcc.Graph(id='views_line_output'),
            dcc.Graph(id='commentlikes_line_output'),
            dcc.Graph(id='engagement_line_output'),
            
            #basic metric line plot
        dbc.Spinner(
            html.Div(id='channel_output'),
            color = 'success',
            spinner_style={"width": "10rem", "height": "10rem"},
            fullscreen=True,
        ),
        ]),
    ],
    style = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        },
    )

@callback(
    [
    Output(component_id='video_output',component_property='children'),
    Output(component_id='channel_output',component_property='children'),
    Output(component_id='views_line_output',component_property='figure'),
    Output(component_id='commentlikes_line_output', component_property='figure'),
    Output(component_id='engagement_line_output',component_property='figure'),
    ],
    Input('basic_submit_button','n_clicks'),
    [
    State('basic_channel_id','value'),
    State('basic_video_name','value'),
    ],
    prevent_initial_call=True,
)

def create_anlaysis(n_clicks,channel_id,video_name):
    """ Creates analysis object """
    #initialising
    main = MainManager(channel_id,video_name)
    
    # get target video df
    df = main.get_target_data()
    vdf = dbc.Table.from_dataframe(df)
    
    # initialising Visual manager
    vis = Visualise(channel_id)
    
    """ NER vis """

    cdf = vis.channel_table()
    
    #basic metric line plot 
    views = vis.channel_views()
    comment_likes = vis.channel_cl()
    engagement = vis.channel_engagement()
    
    
    
    return vdf,cdf,views,comment_likes,engagement
    
    

