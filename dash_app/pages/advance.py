""" File for Machine Learning Analysis """
import os
import sys 
import dash
from dash import dcc, html, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import time


# registering page
dash.register_page(__name__, order=3, name='Advanced Machine Learning Analysis')


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
        html.H1('Advance Machine Learning Analysis Page'),
        html.Br(),
        #inputs
        html.P('Due to the 6-8 minutes of processing time. Demo values below will display pre-analysed results',style={'color':'red'}),
        html.P('Paste Channel ID',style={'font-weight': 'bold','font-size':'17px',}),
        html.P(['You can search up a channels ID by name via this link ',\
            html.A('Youtube Channel ID Searcher',href='https://commentpicker.com/youtube-channel-id.php',target="_blank")]),
        dbc.Input(id="advance_channel_id",type="text",value='UCVjlpEjEY9GpksqbEesJnNA'),
        html.Br(),
        html.P('Paste Video Name',style={'font-weight': 'bold','font-size':'17px',}),
        dbc.Input(id="advance_video_name",type="text",value='Uncle Roger LOVE The OG Uncle (Martin Yan)'),
        html.Br(),
        #Submit button
        dbc.Button(id='advance_submit_button',n_clicks=0,children='Start Advance Analysis'),
        html.Br(),
        ]),
        
        html.Br(),
        html.Div(
            [
                html.H2("Video Data"),
                html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
                html.Div(id='advance_output')
            ]
        ),
        html.Br(),
        #summarise visualisation
        html.Br(),
        html.Div([
        html.H2("Too Long ; Didn't Watch Summarisation Result"),
        html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
        html.B(id='summarise_output', style={'font-size':'1.428571rem'})
        ]),
        html.Br(),
        html.Br(),
        html.Br(),
        
        #ner visualisation

        html.H2('Named-Entity Recognition Results'),
        html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
        html.B('Table values are ordered from most mentioned to least',style={'font-size':'1rem'}),
        html.Br(),
        dbc.Row(
            [
                #people
                dbc.Col(id='per_output'),
                dbc.Col(id='org_output'),
                dbc.Col(id='loc_output'),
                dbc.Col(id='msc_output'),  
            ]
        ),
        # SA data visualisation
        html.Div(
            [   
                html.H2('Sentiment Analysis Results'),
                html.Hr(style={'borderWidth': "5px", "width": "100%", "color": "#28948c"}),
                dbc.Spinner(
                    dcc.Graph(id='sa_bar_output'),
                    color = 'success',
                    spinner_style={"width": "10rem", "height": "10rem"},
                    fullscreen=True,
                ),
                
            ]
        )
    ],
    style = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        },
    )

@callback(
    [
    Output(component_id='advance_output',component_property='children'),
    Output(component_id='summarise_output',component_property='children'),
    Output(component_id='per_output',component_property='children'),
    Output(component_id='org_output',component_property='children'),
    Output(component_id='loc_output',component_property='children'),
    Output(component_id='msc_output',component_property='children'),
    Output(component_id='sa_bar_output',component_property='figure'),
    ],
    Input('advance_submit_button','n_clicks'),
    [
    State('advance_channel_id','value'),
    State('advance_video_name','value'),
    ],
    prevent_initial_call=True,
)

def create_anlaysis(n_clicks,channel_id,video_name):
    """ Creates analysis object """
    #initialising
    main = MainManager(channel_id,video_name)
    
    # get target video df
    df = main.get_target_data()
    cdf = dbc.Table.from_dataframe(df)
    
    # initialising Visual manager
    vis = Visualise(channel_id)
    
    
    # data for caption vis
    caption = vis.caption()
    
    """ NER vis """
    per = vis.per()
    org = vis.org()
    loc = vis.loc()
    msc = vis.msc()
    
    """ SA vis """
    sa_bar = vis.sa_bar()

    
    
    return cdf,caption,per,org,loc,msc,sa_bar
    
    

