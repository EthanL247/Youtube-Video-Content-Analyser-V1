""" Test file for main_mananger.py """

# adding modules path 
import sys 
import os 
import sqlite3
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
    main.get_data()
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
    main.get_data()
    try:
        assert main.get_data() is False
    finally:
        os.remove(db_name)
        
        
def test_get_target_video():
    """ Test to see target video data acquired from db """ 
    channel_id = 'UCVjlpEjEY9GpksqbEesJnNA'
    db = channel_id+'.db'
    video_name = 'Uncle Roger LOVE The OG Uncle (Martin Yan)'
    main = MainManager(channel_id, video_name)
    main.get_data()
    df = main.get_target_data()
    try:
        assert video_name == df['Title'].values
    finally:
        os.remove(db)
        
def test_nlp():
    """ After running test_NLP in main the db is quered ensure tables appear"""
    conn = sqlite3.connect('D:/python_projects/Youtube-Video-Analyser-GUI-Version/data/test.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    raw_res = cur.fetchall()
    res =[i[0] for i in raw_res]
    expected = ['UCVjlpEjEY9GpksqbEesJnNAChannel_Data', 'Words_Data', 'SA_Data', 'PER', 'ORG', 'LOC', 'MSC']
    assert sorted(expected) == sorted(res)

