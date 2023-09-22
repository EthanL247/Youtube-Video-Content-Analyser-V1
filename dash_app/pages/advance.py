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
        html.H1('Enter Channel ID and Youtube Video Name'),
        html.Br(),
        html.Br(),
        #inputs
        dbc.Input(id="advance_channel_id",type="text",value='UCVjlpEjEY9GpksqbEesJnNA'),
        dbc.Input(id="advance_video_name",type="text",value='Uncle Roger LOVE The OG Uncle (Martin Yan)'),
        #Submit button
        dbc.Button(id='advance_submit_button',n_clicks=0,children='Start Advance Analysis'),
        html.Br(),
        ]),
        
        #caption visualisation
        html.Br(),
        html.Div([
        html.H2("Too long ; didn't watch summarisation result: "),
        html.Div(id='summarise_output', className="lead"),
        html.Br(),
        ]),
        
        #ner visualisation
        html.Br(),
        dbc.Row(
            [
                #people
                dbc.Row(html.P(id='per_output')),
                dbc.Row(html.P(id='org_output')),
                dbc.Row(html.P(id='loc_output')),
                dbc.Row(html.P(id='msc_output')),  
            ]
        ),
 
        # video data visualisation
        html.Div([
        dbc.Spinner(
            dash_table.DataTable(id='advance_output'),
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
    Output(component_id='advance_output',component_property='data'),
    Output(component_id='advance_output',component_property='columns'),
    Output(component_id='summarise_output',component_property='children'),
    Output(component_id='per_output',component_property='children'),
    Output(component_id='org_output',component_property='children'),
    Output(component_id='loc_output',component_property='children'),
    Output(component_id='msc_output',component_property='children'),
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
    
    # get target vide df
    df = main.get_target_data()
    
    # initialising Visual manager
    vis = Visualise(channel_id)
    
    
    # data for caption vis
    caption = vis.caption_vis()
    
    #data video data vis 
    data = df.to_dict(orient="records")
    columns = [{'name': col, 'id': col} for col in list(df.columns)]
    
    """ NER Data Get """
    # People
    per = vis.get_per()
    org = vis.get_org()
    loc = vis.get_loc()
    msc = vis.get_msc()

    
    
    return data,columns,caption,per,org,loc,msc
    
    

