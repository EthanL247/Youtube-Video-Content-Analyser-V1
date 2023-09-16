"""
File for ETL of SA data
"""
import json
import ast

class EtlSA:
    """ A class for ETL of raw SA data """
    def load_json(self,path: str) -> json:
        with open(path) as f:
            data = json.load(f)
        return data 
    
    def to_dictionary(self, data: dict[list[str]]) -> dict[list[dict]]:
        """ converts strs in json to their literal data """ 
        res = []
        for s in data['SA']:
            l = ast.literal_eval(s)
            res.append(l)
        
        return res 
    
    def flatten_dictionary(self, data: dict[list[list[dict]]]) -> dict[dict[list]]:
        res = {}
        for l in data:
            results = l[0]
            for entry in results:
                if entry['label'] not in res.keys():
                    res[entry['label']] = []
                    res[entry['label']].append(entry['score'])
                else:
                    res[entry['label']].append(entry['score'])
        
        return res 
    
    def local_etl(self, path: str) -> dict[dict[list]]:
        """ etl local ner json results """
        raw = self.load_json(path)
        data = self.to_dictionary(raw)
        res = self.flatten_dictionary(data)
        return res 
   
    
    def direct_etl(self, data: dict[dict[list[str]]]) -> dict[dict[list]]:
        """ etl of ner results direction from ner function """ 
        raw = self.to_dictionary(data)
        res = self.flatten_dictionary(raw)
        return res 
        
    

                
