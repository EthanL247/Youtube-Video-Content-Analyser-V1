""" 
For retrieving video data
Creator: Ethan Liu
"""
from googleapiclient.discovery import build

class Ytvideo:
    """ Class for retrieving full video data """
    def __init__(self):
        """ Parameters to get youtube discovery object """
        self.name = 'youtube'
        self.service = 'v3'
        self.api_key = 'AIzaSyDMg2PyJVlG9sj79VXnlffmlD86wEHzXxI'
        
    def _start(self) -> object:       
        """ Returns youtube service object """ 
        return build(self.name,self.service,developerKey=self.api_key)
            
    
    def get_ids(self,video_data: str) -> list[str]:
        """ gets all video ids """ 
        vid = [i['snippet']['resourceId']['videoId'] for i in video_data[:50]] #YoutubeAPILimit of 50 items
        return vid

    def get_info(self,video_data: str) -> list:
        """ gets full video details from youtube""" 
        ids = self.get_ids(video_data)
        yt = self._start()
        request = yt.videos().list(
                part="contentDetails,statistics,snippet,status",
                id =ids )
        
        return request.execute()
    
    def export_info(self,video_data: str) -> dict:
        """ retrieves and formats relevant video info then exports as dic"""
        data = self.get_info(video_data)['items']
        d = {
            'ID':[],
            'Title':[],
            'Duration':[],
            'Views':[],
            'Likes':[],
            'Comments':[]
        }
    
        for i in data:
            d['ID'].append(i['id']),
            d['Title'].append((i['snippet']['title'])),
            d['Duration'].append(i['contentDetails']['duration']),
            d['Views'].append(i['statistics']['viewCount']),
            d['Likes'].append(i['statistics']['likeCount']),
            d['Comments'].append(i['statistics']['commentCount']),

        return d


