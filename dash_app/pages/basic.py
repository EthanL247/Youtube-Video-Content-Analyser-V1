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
        html.H1('Basic Analysis Page'),
        html.Br(style={"line-height": "5px"}),
        #inputs
        html.H4('Usage Guidelines: '),
        html.Li('Basic analysis takes 1-2 minutes. Demo values below will display pre-analysed results.',style={'color':'red'}),
        html.Li('Video name must be exactly the same as the title on the video page.',style={'color':'red'}),
        html.Li('If input is correct, loading screen and results will appear, if not then input is incorrect.',style={'color':'red'}),
        html.Br(),
        html.P('Paste Channel ID',style={'font-weight': 'bold','font-size':'17px',}),
        html.P(['You can search up a channels ID by name via this link ',\
        html.A('Youtube Channel ID Searcher',href='https://commentpicker.com/youtube-channel-id.php',target="_blank")]),
        dbc.Input(id="basic_channel_id",type="text",value='UCVjlpEjEY9GpksqbEesJnNA'),
        html.Br(style={"line-height": "5"}),
        html.P('Paste Video Name',style={'font-weight': 'bold','font-size':'17px',}),
        dbc.Input(id="basic_video_name",type="text",value='Uncle Roger Review OG UNCLE Mongolian Beef (Martin Yan)'),
        #Submit button
        html.Br(style={"line-height": "5px"}),
        dbc.Button(id='basic_submit_button',n_clicks=0,children='Start Basic Analysis'),
        ]),
    
        #video data 
        html.Br(style={"line-height": "5px"}),
        html.H2('Video Data'),
        html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
        dbc.Row(
            [
                #people
                dbc.Col(id='video_output'),
            ]
        ),
        html.Br(style={"line-height": "20px"}),
 
        # channel data visualisation
        html.Div([
            

            
            # Views time series 
            html.H2('Simple Trends'),
            html.H4('Hover over data points in any graphto see the data values of a video.',style={'color':'red'}),
            html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
            dcc.Graph(id='views_line_output'),
            dcc.Graph(id='commentlikes_line_output'),
            html.Br(style={"line-height": "20"}),
            
            html.H2('Engagement Trends'),
            html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
            dcc.Graph(id='engagement_line_output'),
            html.Br(style={"line-height": "20"}),
            
        #other videos 
        html.H2('Same Upload Window Related Videos'),
        html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
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
    # initialising Visual manager
    vis = Visualise(channel_id)
    
    #getting channel data 
    main.get_data()
    
    # get target video df
    df = main.get_target_data()
    
    """ Visualisations """
    vdf = dbc.Table.from_dataframe(df, striped=True)
    
    cdf = vis.channel_table()
    
    #basic metric line plot 
    views = vis.channel_views()
    comment_likes = vis.channel_cl()
    engagement = vis.channel_engagement()

    
    return vdf,cdf,views,comment_likes,engagement
    
    

