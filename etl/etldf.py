""" A file for transforming etl data into dataframe"""
import pandas as pd
import psycopg2 as psy

class EtlDF:
    """ A class to carry convert data into dataframe """
    
    def meta_dataframe(self, metadata: dict[dict[list]]) -> pd.DataFrame:
        """ converts video metadata to dataframe """
        df = pd.DataFrame(metadata)
        
        #convert types 
        df = df.astype({'Title':'str','ID':'str','Duration':'str'})
        df[['Views','Likes','Comments']] = df[['Views','Likes','Comments']].apply(pd.to_numeric)
        #add useful metrics 
        df['LikesPerView'] = df['Likes']/df['Views']
        df['CommentsPerView'] = df['Comments']/df['Views']
        df['LikesPerComment'] = df['Likes']/df['Comments']
        
        return df 
    
    def ner_dataframe(self, ner: dict[dict[list]]) -> list[pd.DataFrame]:
        """ converts  etl ner results to dataframe """
        res = []
        for key,value in ner.items():
            # populate empty data with None 
            if ner[key] == []:
                data = [None]
                df = pd.Series(data,name=key)
            else:
                df = pd.Series(ner[key],name=key,dtype=str)
            res.append(df)
        return res
    
    def sa_dataframe(self, sa: dict[dict[list]]) -> pd.DataFrame:
        """ converts etl sa results to dataframe """
        df = pd.DataFrame(sa, columns=sa.keys(), dtype=float)
        return df 
    
    def sum_dataframe(self, transcript: dict[dict[list]]) -> pd.DataFrame:
        """ converts etl captions results to dataframe """
        df = pd.DataFrame(transcript, columns = transcript.keys(), dtype=str)
        return df 
    
    def captions_dataframe(self, captions: dict[dict[list]]) -> pd.DataFrame:
        df = pd.DataFrame(captions, columns = captions.keys(), dtype=str)
        return df 
    
    def words_dataframe(self, captions: dict[dict[list]], summarised = dict[dict[list]]) -> pd.DataFrame:
        cdf = self.captions_dataframe(captions)
        sdf = self.sum_dataframe(summarised)
        wdf = pd.concat([cdf,sdf], axis = 1)
        return wdf 
        