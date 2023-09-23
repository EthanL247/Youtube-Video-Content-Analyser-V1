""" A class that calls all other functions and operates high level logic  """

#loading standard libraries 
import sys 
import os 
import pandas as pd 
import sqlite3
import sqlalchemy

# adding modules path 
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/etl')
sys.path.insert(1,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/youtube_api')
sys.path.insert(2,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/nlp')

# loading modules
from ytchannel import Ytchannel
from ytvideo import Ytvideo
from etldf import EtlDF
from dbmanager import DBmanager
from transcribe import Transcribe
from nlp_summarisation import Summariser
from nlp_sa import SA
from nlp_ner import NER
from etldf import EtlDF
from etlner import EtlNER
from etlsa import EtlSA
from dbmanager import DBmanager


#initialising 
channel_manage = Ytchannel()
video_manage = Ytvideo()
etldf = EtlDF()
tm = Transcribe()
sm = Summariser()
sam = SA()
nerm = NER()
etldfm = EtlDF()
etlnerm = EtlNER()
etlsam = EtlSA()
dbm = DBmanager()


class MainManager:
    
    """ A class that calls other functions and operates light high level logic """
    def __init__(self,channel_id: str, video_name: str):
        self.channel_id = channel_id
        self.video_name = video_name
        self.limit = 1
        self.db_name = self.channel_id + '.db'
    
    def get_data(self) -> bool:
        """ Retrieves latest 50 videos data """
        # youtube api 
        channel_data = channel_manage.get_videos(self.channel_id)
        videos_data = video_manage.export_info(channel_data)
        videos_df = etldf.meta_dataframe(videos_data)
        #database management
        table_name = self.channel_id + 'Channel_Data'
        if dbm.create_db(self.db_name):
            dbm.df_to_db(self.db_name,videos_df,table_name)
        else:
            return False
            
    def _df_from_sql(self) -> pd.DataFrame:
        """ returns data as df from sqlite db """ 
        conn = sqlite3.connect(self.db_name)
        table_name = self.channel_id +'Channel_Data'
        query = 'SELECT * FROM ' + table_name
        df = pd.read_sql_query(query,conn)
        conn.close()
        return df 
        
        
    def get_target_data(self) -> pd.Series:
        """ Gets the target video data from sqlite video data """
        df = self._df_from_sql()
        if self.video_name in df['Title'].values:
            target = df.loc[(df['Title'] == self.video_name)].copy(deep=True)
            return target
        else:
            return None
    
    def _get_caption(self) -> None:
        """ gets caption from target video data """
        video_id = self.get_target_data()['ID'].values[0]
        caption = tm.get_captions(video_id,self.limit)
        if caption is None:
            raise ValueError
        else:
            return caption
        
    def _do_nlp(self,caption) -> None:
        """ does nlp from target video caption """
        summarise = sm.summarise(caption,self.limit)
        sa = sam.sa(caption,self.limit)
        ner = nerm.ner(caption,self.limit)
        return (caption,summarise,sa,ner)
    
    def _etl_nlp(self,caption) -> None:
        """ etl target nlp data """
        caption,summarise,sa,ner = self._do_nlp(caption)
        #Transform data 
        sa_data = etlsam.direct_etl(sa)
        ner_data = etlnerm.direct_etl(ner)
        # convert to data frame
        words_df = etldf.words_dataframe(caption,summarise)
        sa_df = etldf.sa_dataframe(sa_data)
        ner_df = etldf.ner_dataframe(ner_data)
        return (words_df,sa_df,ner_df)
    
    def nlp(self) -> None:
        caption = self._get_caption()
        words,sa,ner = self._etl_nlp(caption)
        words_name = 'Words_Data'
        sa_name = 'SA_Data'
        # upload as sqlite db 
        dbm.df_to_db(self.db_name,words,words_name)
        dbm.df_to_db(self.db_name,sa,sa_name)
        dbm.dflist_to_db(self.db_name,ner)
        
# id = 'UCVjlpEjEY9GpksqbEesJnNA'
# video ='Uncle Roger LOVE The OG Uncle (Martin Yan)'
# test = MainManager(id,video)
# v = test.get_target_data()
# print(v)