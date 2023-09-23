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
        return dbc.Table.from_dataframe(df)
        
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
        fig = px.line(
            df, x='History',y='Views',
            hover_name=('Title'),markers=True
        )
        return fig
    
    def channel_cl(self) -> object:
        """ Line plot of comments and likes  """
        df = self.channel_line_prep()
        fig = px.line(
            df, x='History',y=['Comments','Likes'],
            hover_name=('Title'),markers=True
        )
        return fig
    
    def channel_engagement(self) ->object:
        """ Line plot of channel engagement metrics"""
        df = self.channel_line_prep()
        fig = px.line(
            df, x='History',y=['LikesPerView','CommentsPerView','LikesPerComment'],
            hover_name=('Title'),markers=True
        )
        return fig
        
        
    
    def caption(self) -> str:
        """ Returns caption to be displayed """
        df = self.get_df('Words_Data')
        summary_entry = list(df['Summarised_Captions'].values)[0]
        summary_res = summary_entry.strip('[{]}:""')[17:]
        return summary_res
    

    def loc(self) ->object:
        """ Gets all ner LOC data from db """
        df = self.get_df('LOC')
        return dbc.Table.from_dataframe(df)
    
    def msc(self) ->object:
        """ Gets all ner MSC data from db """
        df = self.get_df('MSC')
        return dbc.Table.from_dataframe(df)
    
    def org(self) -> object :
        """ Gets all ner ORG data from db """
        df = self.get_df('ORG')
        return dbc.Table.from_dataframe(df)
    
    def per(self) -> object:
        """ Gets all ner PERdata from db """
        df = self.get_df('Per')
        return dbc.Table.from_dataframe(df)
    
    def sa_bar(self) -> object:
        """ Generates barchart figure """
        df = self.get_df('SA_Data').transpose()
        df.reset_index(inplace=True)
        df.columns = ['Emotions','Score']
        df.sort_values(by=['Score'],inplace=True, ascending=False)
        fig = px.bar(df, x='Emotions',y='Score',color='Score')
        return fig 
    



