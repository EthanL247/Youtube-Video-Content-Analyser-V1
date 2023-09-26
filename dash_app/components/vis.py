""" File for visualisation data """
#loading libraries
import plotly
import dash
import os
import sys
import pandas as pd
import sqlite3
import dash_bootstrap_components as dbc
import plotly.express as px 
import random
import plotly.graph_objs as go



#adding module paths
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/main')

#importing custom modules
from main_manager import MainManager


class Visualise:
    """ A class for managing all visulisations via plotly """ 
    def __init__(self, channel_id: str):
        self.db = channel_id + '.db'
        self.channel_id = channel_id 
    
    def get_df(self,table_name: str) -> pd.DataFrame:
        """ returns data as df from sqlite db """ 
        conn = sqlite3.connect(self.db)
        query = 'SELECT * FROM ' + table_name
        df = pd.read_sql_query(query,conn)
        conn.close()
        return df
    
    def get_channel_data(self) -> pd.DataFrame:
        """ Returns channel data """
        conn = sqlite3.connect(self.db)
        table_name = self.channel_id +'Channel_Data'
        query = 'SELECT * FROM ' + table_name
        df = pd.read_sql_query(query,conn)
        conn.close()
        return df
    
    def channel_table(self) -> object:
        """ Displays channel data dataframe """
        df = self.get_channel_data()
        return dbc.Table.from_dataframe(
            df,
            striped=True,
            )
        
    def channel_line_prep(self) -> object:
        """ Tweaks channel for line plot """ 
        df = self.get_channel_data()
        # make history row so x axis oldest video first 
        history = [i for i in range(len(df),0,-1)]
        df['History'] = history
        df.sort_values(by=['History'],inplace=True,ascending=True)
        return df
    
    def channel_views(self) -> object:
        """ Line plot of views """
        df = self.channel_line_prep()
        title="Channel Views Across The 50 Last Videos Uploaded"
        fig = px.line(
            df, x='History',y='Views',
            hover_name=('Title'),markers=True,
            color_discrete_sequence=['#FFB7B7'],
            )
        fig.update_layout(
            font={'size':20},
            title={'text':'<b>'+title+'<b>','font':{'size':20}},
            xaxis_title="Last 50 Videos Uploaded Time Line",
            yaxis_title="Views",
        ),
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='black')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='black')
        fig.update_traces(marker=dict(size=12)),
        return fig
    
    def channel_cl(self) -> object:
        """ Line plot of comments and likes  """
        df = self.channel_line_prep()
        title='Comments and Likes Across The Last 50 Videos Uploaded'
        fig = px.line(
            df, x='History',y=['Comments','Likes'],
            hover_name=('Title'),markers=True,
            color_discrete_sequence=['#FFB7B7','#96C291'],
            
        )
        fig.update_layout(
            font={'size':20},
            title={'text':'<b>'+title+'<b>','font':{'size':20}},
            xaxis_title="Last 50 Videos Uploaded Time Line",
            yaxis_title="Count")
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='black')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='black')
        fig.update_traces(marker=dict(size=12))
        
        return fig
    
    def channel_engagement(self) ->object:
        """ Line plot of channel engagement metrics"""
        df = self.channel_line_prep()
        title='Video Engagement Across The Last 50 Videos Uploaded'
        fig = px.line(
            df, x='History',y=['LikesPerView','CommentsPerView','LikesPerComment'],
            hover_name=('Title'),markers=True,
            color_discrete_sequence=['#96C291','#FFDBAA','#FFB7B7',],
        )
        fig.update_layout(
            font={'size':20},
            title={'text':'<b>'+title+'<b>','font':{'size':20}},
            xaxis_title="Last 50 Videos Uploaded Time Line",
            yaxis_title="Count")
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='black')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='black')
        fig.update_traces(marker=dict(size=12))
        return fig
        

    def loc(self) ->object:
        """ Gets all ner LOC data from db """
        df = self.get_df('LOC')
        df.columns=['Most Mentioned Locations']
        return dbc.Table.from_dataframe(df, striped=True)
    
    def msc(self) ->object:
        """ Gets all ner MSC data from db """
        df = self.get_df('MSC')
        df.columns=['Other Most Mentioned Nouns']
        return dbc.Table.from_dataframe(df,striped=True)
    
    def org(self) -> object :
        """ Gets all ner ORG data from db """
        df = self.get_df('ORG')
        df.columns=['Most Mentioned Organisations']
        return dbc.Table.from_dataframe(df,striped=True)
    
    def per(self) -> object:
        """ Gets all ner PERdata from db """
        df = self.get_df('Per')
        df.columns=['Most Mentioned Individuals']
        return dbc.Table.from_dataframe(df,striped=True)
    
    def sa_bar(self) -> object:
        """ Generates barchart figure """
        df = self.get_df('SA_Data').transpose()
        df.reset_index(inplace=True)
        df.columns = ['Emotions','Score']
        df.sort_values(by=['Score'],inplace=True, ascending=True)
        fig = px.bar(df, x='Score',y='Emotions',color='Score',orientation='h')
        title = 'Sentiment Analysis Bar Chart'
        fig.update_layout(
            font={'size':20},
            title={'text':'<b>'+title+'<b>','font':{'size':20}},
            xaxis_title="Score",
            yaxis_title="Emotions",
            width=1500,
            height=800,
        ),
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='black')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='black',tickmode='linear')
        
        return fig 
    




