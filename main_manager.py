""" A class that calls all other functions """

#loading libraries
from youtube_api import*
from nlp import*
from etl import*


class MainManager:
    
    """ A class that calls other functions and operates light high level logic """
    def __init__(self,channel_id: str):
        self.channel_id = channel_id
        
     