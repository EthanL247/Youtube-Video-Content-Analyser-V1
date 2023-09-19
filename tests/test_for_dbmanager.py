""" Test file for dbmanager.py """
import sys
import sqlite3
import os 
import pandas as pd
import pytest 
import pickle

# adding modules path 
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/etl')
sys.path.insert(1,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/youtube_api')
sys.path.insert(2,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/nlp')


# importing modules
from dbmanager import DBmanager


#initialising
dbm = DBmanager()


def test_create_db_db_already_exist():
    """ Tests to see if create_db returns False if db  of insert name already exists """
    db_name = 'test.db'
    #create db
    conn = sqlite3.connect(db_name)
    try:
        assert dbm.create_db(db_name) == False
    finally:
        if conn:
            conn.close()
            os.remove(db_name)
            

def test_create_db_db_is_new():
    """ Tests to see if create_db returns True if db created is new """
    db_name = 'test.db'
    conn = dbm.create_db(db_name) 
    try:
        assert conn == True
    
    finally:
            os.remove(db_name)
            

def test_df_to_db_successful():
    """ Tests to see if dataframe is succesfully loaded into database"""
    csv_filepath = 'D:/python_projects/Youtube-Video-Analyser-GUI-Version/data/uncle_roger_df.csv'
    db_name =  'test.db'
    df_name = 'channel_data'
    
    # create df from local csv
    df = pd.read_csv(csv_filepath)
    # upload df to database
    dbm.df_to_db(db_name,df,df_name)
    
    # query to get table names from db
    conn = sqlite3.connect(db_name)
    query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    print(res[0])
    
    try:
        assert df_name in res[0]
        
    finally:
        conn.close()
        os.remove(db_name)
        
def test_df_to_db_existing_table():
    """ Checks to see if valueError is raised if table already exist in db"""
    csv_filepath = 'D:/python_projects/Youtube-Video-Analyser-GUI-Version/data/uncle_roger_df.csv'
    file_path='D:/python_projects/Youtube-Video-Analyser-GUI-Version/data/'
    db_name =  file_path + 'existing_test.db'
    df_name = 'channel_data'
    
    # create df from local csv
    df = pd.read_csv(csv_filepath)
    
    # upload df to database
    dbm.df_to_db(db_name,df,df_name)
    
    
    # upload again
    with pytest.raises(ValueError):
        dbm.df_to_db(db_name,df,df_name)
        
def test_dflist_to_db_successful():
    """ Checks to see if tables are succesfully uploaded to database """
    db = 'test.db'
    # getting the dataframe 
    file_path='D:/python_projects/Youtube-Video-Analyser-GUI-Version/data/ner_df_list'
    with open(file_path,'rb') as f:
        dflist = pickle.load(f)
    
    # upload to database
    dbm.dflist_to_db(db, dflist)
    
    # query to get table names from db
    conn = sqlite3.connect(db)
    query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cursor = conn.cursor()
    cursor.execute(query)
    tables = cursor.fetchall()
    table_names = ['LOC','PER','ORG','MSC']
    res = [table[0] for table in tables]
    
    
    try:
        assert table_names.sort() == res.sort()
        
    finally:
        conn.close()
        os.remove(db)
    
    