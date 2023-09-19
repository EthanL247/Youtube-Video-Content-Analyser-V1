""" 
Transcribing Youtube Videos
Creator: Ethan Liu
"""
from youtube_transcript_api import YouTubeTranscriptApi as ytta
import json
import os



class Transcribe:
    """ A class to acquire captions for videos """
    
    def get_captions(self, video_id ,limit: int)->dict:
        """ Retrieve captions for videos """
        res = {'ID':[],
                    'Captions':[],
                    'WordCount':[]
                    }
        try: 
            transcript = ytta.get_transcript(video_id)
            t_str = ''
            for line in transcript:
                t_str += line['text']+' '
        except:
            t_str = None
        res['ID'].append(video_id)
        res['Captions'].append(t_str)
        if t_str == None:
            res['WordCount'].append(0)
        else:
            res['WordCount'].append(len(t_str))
        return res
    
    def save_captions(self,channel_name: str,limit: int) ->None:
        """ Saves captions as json, returns bool check of file exist """ 
        captions = self.get_captions(channel_name,limit)
        with open('captions.json','w') as outfile:
            json.dump(captions,outfile)
        return print(f"Checking File Existence: {os.path.isfile('captions.json')}")

