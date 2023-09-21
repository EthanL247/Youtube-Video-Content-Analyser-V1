""" File for visualisation data """
#loading libraries
import plotly
import dash
import os
import sys
import pandas as pd
import sqlite3


#adding module paths
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/main')

#importing custom modules
from main_manager import MainManager


class Visualise:
    """ A class for managing all visulisations via plotly """ 
    def __init__(self, channel_id: str):
        self.db = channel_id + '.db'
    
    def get_df(self,table_name: str) -> pd.DataFrame:
        """ returns data as df from sqlite db """ 
        conn = sqlite3.connect(self.db)
        query = 'SELECT * FROM ' + table_name
        df = pd.read_sql_query(query,conn)
        conn.close()
        return df
    
    def caption_vis(self) -> str:
        """ Returns caption to be displayed """
        df = self.get_df('Words_Data')
        summary_entry = list(df['Summarised_Captions'].values)[0]
        summary_res = summary_entry.strip('[{]}:""')[17:]
        return summary_res
        
    
    

    
    

# id = 'UCVjlpEjEY9GpksqbEesJnNA'
# name = 'Uncle Roger LOVE The OG Uncle (Martin Yan)'
# table_name = 'Words_Data'


# main = MainManager(id,name)
# vis = Visualise(id)
# print(vis.caption_vis())

# df = vis.get_df('Words_Data')
# entry = list(df['Summarised_Captions'].values)[0]
# res = entry.strip('[{]}:""')[17:]
# print(type(res))
