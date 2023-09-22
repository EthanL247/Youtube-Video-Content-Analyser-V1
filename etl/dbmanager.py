""" A file for managing the upload of dataframes into sqlite3 database """
import sqlite3
import pandas as pd
import os
from sqlite3 import Error


class DBmanager:
    """ a class for uploading dataframes into sqlite3 database """
    def create_db(self, db_name: str) -> bool:
        """ creates a sqlite3 database """
        #checks if db already exists 
        if  os.path.isfile(db_name) is False:
            try:
                conn = sqlite3.connect(db_name)
                return True
            
            except Error as e:
                return e 
                
            finally:
                if conn:
                    conn.close()
               
        #returns False if db exists 
        else:
            return False 
        
    def connect(self, db_name: str) -> object:
        """ Connects to a sqlite3 database """
        try:
            conn = sqlite3.connect(db_name)
            return conn
        
        except Error as e:
            return e
        
    def df_to_db(self,db: str, df: pd.DataFrame,df_name: str) -> None:
        conn = self.connect(db)
        df.to_sql(df_name,conn,index=False,if_exists='fail')
        conn.close()
        
    def dflist_to_db(self,db:str ,dflist: list[pd.DataFrame]) -> None:
        table_names = []
        for df in dflist:
            table_names.append(df.name)
        
        for name,df in zip(table_names,dflist):
            self.df_to_db(db,df,name)
        
        
            
        
        