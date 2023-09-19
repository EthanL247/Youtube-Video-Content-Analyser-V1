""" A class that calls all other functions """

# adding modules path 
import sys 
import os 
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/etl')
sys.path.insert(1,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/youtube_api')
sys.path.insert(2,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/nlp')

# loading modules
from ytchannel import Ytchannel
from ytvideo import Ytvideo
from etldf import EtlDF
from dbmanager import DBmanager

#initialising 
channel_manage = Ytchannel()
video_manage = Ytvideo()
etldf = EtlDF()
dbm = DBmanager()


class MainManager:
    
    """ A class that calls other functions and operates light high level logic """
    def __init__(self,channel_id: str, video_name: str):
        self.channel_id = channel_id
        self.video_name = video_name 
    
    def get_yt_data(self) -> bool:
        """ Retrieves latest 50 videos data """
        # youtube api 
        channel_data = channel_manage.get_videos(self.channel_id)
        videos_data = video_manage.export_info(channel_data)
        videos_df = etldf.meta_dataframe(videos_data)
        #database management
        db_name = self.channel_id + '.db'
        table_name = self.channel_id + 'Channel_Data'
        if dbm.create_db(db_name):
            dbm.df_to_db(db_name,videos_df,table_name)
        else:
            return False
        
    
    def get_target_video(self) -> None:
        """ Gets the target video data from sqlite video data """




