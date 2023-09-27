"""
File for ETL of NER results.
"""

import pandas as pd
import psycopg2 as ps
import json
import ast 

class EtlNER:
    """ A class to ETL NER results """ 
    
    def load_json(self,path: str) -> json:
        with open(path) as f:
            data = json.load(f)
        return data 
    
    def to_dictionary(self, data: dict[list[str]]) -> dict[list[dict]]:
        """ converts strs in json to their literal data """ 
        res = []
        for s in data['NER']:
            d = ast.literal_eval(s)
            res.append(d)
        
        return res
    
    def extract_features(self, data: list[dict]) -> dict[dict[list]]:
        """ Extracts I-PER,I-ORG,I-LOC and their scores from results """
        res = {
            'PER':[],
            'ORG':[],
            'LOC':[],
            'MSC':[]
                }
    
        for videos in data:
            for results in videos:
                if results['entity_group'] == 'PER':
                    res['PER'].append(results['word'])
                
                elif results['entity_group'] == 'ORG':
                    res['ORG'].append(results['word'])
                
                elif results['entity_group'] == 'LOC':
                    res['LOC'].append(results['word'])
                
                else:
                    res['MSC'].append(results['word'])
        
        # getting rid of duplciates
        keys = ['PER','ORG','LOC','MSC']
        
        for key in keys:
            if res[key] == []:
                res[key] = None
            else:
                res[key] = list(set(res[key]))
        
        return res
    
    def json_etl(self, path: str) -> dict[dict[list]]:
        """ ETL of NER json files stored locally """
        jdata = self.load_json(path)
        data = self.to_dictionary(jdata)
        res = self.extract_features(data)
        return res 
    
    def direct_etl(self, raw_data: dict) -> dict[dict[list]]:
        """ ETL of raw NER dict output from nlp_ner.py """
        data = self.to_dictionary(raw_data)
        res = self.extract_features(data)
        return res 
