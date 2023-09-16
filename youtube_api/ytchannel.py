""" 
File for retrieving channel data in order to get video data from channel.
"""
from googleapiclient.discovery import build
class Ytchannel:
    """ A class for retrieving raw data from youtube API on channel scale """ 
    def __init__(self):
        self.name = 'youtube'
        self.service = 'v3'
        self.api_key = 'AIzaSyDMg2PyJVlG9sj79VXnlffmlD86wEHzXxI'
    
    def _start(self) -> object:
        """ Returns youtube service object """ 
        return build(self.name,self.service,developerKey=self.api_key)
    
    def channel_info(self,id: str) -> dict:
        """ Retrieves  basic channel statistics """ 
        yt = self._start()
        request = yt.channels().list(
        part='statistics,contentDetails',
        id = id
        )
        return request.execute()
    
    def get_videos(self,channel_name: str) -> list:
        """ Retrieves all video's snippets data  from a channel """ 
        playlist_id = self.channel_info(channel_name)['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        yt = self._start() 
        res = yt.playlistItems().list(
            playlistId = playlist_id,
            part=['snippet'],
            maxResults=50
        )
        videos = []
        next_page_token = None
        while True:
            res = yt.playlistItems().list(
                playlistId=playlist_id,
                part=['snippet'],
                maxResults=50,
                pageToken = next_page_token
            ).execute()
            
            videos += res['items']
            next_page_token = res.get('nextPageToken')
            
            if next_page_token is None:
                break
            
        return videos 
        
