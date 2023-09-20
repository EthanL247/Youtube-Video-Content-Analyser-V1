import os
import sys 
import dash
from dash import dcc, html, Input, Output, State, callback, dash_table
from components.sidebar import SideBar
import dash_bootstrap_components as dbc
import time

#registering page
dash.register_page(__name__, order=2, name='Start Analysis')


#adding module paths
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/main')

#importing custom modules
from main_manager import MainManager


#layout
layout = html.Div(
    [   
        html.H1('Enter Channel ID and Youtube Video Name'),
        html.Br(),
        html.Br(),
        #inputes
        dcc.Input(id="channel_id",type="text",value='UCVjlpEjEY9GpksqbEesJnNA'),
        dcc.Input(id="video_name",type="text",value='Uncle Roger LOVE The OG Uncle (Martin Yan)'),
        #button
        html.Button(id='submit_button',n_clicks=0,children=' Analyse'),
        
        #spinner
        dbc.Spinner(
            dash_table.DataTable(id='output'),
            color = 'success',
            spinner_style={"width": "5rem", "height": "5rem"},
            fullscreen=True,
            
            
            
        ),
    ],
    style = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }
    )

@callback(
    [
    Output(component_id='output',component_property='data'),
    Output(component_id='output',component_property='columns')
    ],
    Input('submit_button','n_clicks'),
    [State('channel_id','value'),
    State('video_name','value')],
    prevent_initial_call=True,
)

def create_anlaysis(n_clicks,channel_id,video_name):
    """ Creates analysis object """
    #initialising
    main = MainManager(channel_id,video_name)
    #get data
    main.get_data()
    #get target
    df = main.get_target_data()
    #get components to display dataframe
    data = df.to_dict(orient="records")
    columns = [{'name': col, 'id': col} for col in list(df.columns)]
    return data, columns
    
    
    

