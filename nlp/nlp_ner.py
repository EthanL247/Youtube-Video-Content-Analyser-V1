"""
File for NER functionality 

"""
from transformers import pipeline
import pandas as pd
import torch
import json
import os
from transformers import AutoTokenizer, AutoModelForTokenClassification
import ast

class NER:
    """ A class for performing Bert-Base Named Entity Recognition """
    def prepdata(self,data: dict[dict[list]]) -> list[str]:
        """ Prepares data to be summarised"""
        res = data['Captions']
        return res 
        
    
    def prepmodel(self) -> object:
        """ creates model object """ 
        tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
        nlp = pipeline('ner',model=model, tokenizer=tokenizer, aggregation_strategy="simple")
        return nlp
    
    def savej(self,data: any) -> None:
        """ saves NER output as json """
        with open('ner_results.json','w') as f:
            json.dump(data,f)
        return os.path.isfile('ner_results.json')
    
    def ner(self,source: any, limit: int, save=False) -> dict[str:list]:
        """ performs NER """
        data = self.prepdata(source)
        model = self.prepmodel()
        res = {'NER':[]}
        if limit == -1:
            n = len(data)
        else:
            n = limit
        
        for i in range(n):
            nres = model(data[i])
            res['NER'].append(str(nres))
            print(f"job: {i+1} /{n} done.")
            
        if save == True:  
            self.savej(res)
        return res
    

