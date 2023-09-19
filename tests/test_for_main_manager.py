""" Test file for main_mananger.py """

# adding modules path 
import sys 
import os 
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/main')

#importing modules
from main_manager import MainManager

#initialising

def test_get_yt_data_positive():
    """ test for data retrieval, and save """
    channel_id = 'UCVjlpEjEY9GpksqbEesJnNA'
    video_name = 'Uncle Roger LOVE The OG Uncle (Martin Yan)'
    db_name = channel_id+'.db'
    main = MainManager(channel_id,video_name)
    main.get_yt_data()
    try:
        assert os.path.isfile(db_name) is True
    finally:
        os.remove(db_name)

def test_get_yt_data_negative():
    """ test for negative when db of same name already exists"""
    channel_id = 'UCVjlpEjEY9GpksqbEesJnNA'
    video_name = 'Uncle Roger LOVE The OG Uncle (Martin Yan)'
    db_name = channel_id+'.db'
    main = MainManager(channel_id,video_name)
    main.get_yt_data()
    try:
        assert main.get_yt_data() is False
    finally:
        os.remove(db_name)


    

    



