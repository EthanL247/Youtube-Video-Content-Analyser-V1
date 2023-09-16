""" A file for managing the upload of dataframes into postgres database """

import psycopg2 as psy
from sqlalchemy import create_engine
import pandas as pd 


class DBmanager:
    """ a class for uploading dataframes into postgres """
    
    def __init__(self):
        self.user = 'postgres'
        self.password = 'admin123'
        self.port = '5432'
        self.database = 'main_db'
        self.engine_param = 'postgresql+psycopg2://postgres:admin123@localhost:5432/main_db'
    
    def connection(self) -> object:
        """ checks for connection to postgres database """
        try:
            connection = psy.connect(
                user = self.user,
                password = self.password,
                port = self.port,
                database = self.database
                
            )
            return connection
            print(f"Successful connection to {self.database}")
        except(Exception,psy.Error) as error:
            print(f"Unsuccessful connection to {self.database}")

            
    def upload_df(self,df: pd.DataFrame,name: str) -> None:
        """ uploads dataframe into database """
        con = self.connection()
        engine = create_engine(self.engine_param)
        df.to_sql(name,engine, if_exists='replace',index=False)
        
    
    def upload_nerdf(self, nerdf: pd.DataFrame) -> None:
        """ uploads all of the ner dfs """ 
        for series in nerdf:
            self.upload_df(series,series.name)
            
        

