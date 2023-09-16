""" 
File for performing sentiment analysis 
"""
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
import json
import os 

class SA:
    """ a class for performing SamLowe/roberta-base-go_emotions sentiment analysis """
    

    def prepdata(self,data: dict[dict[list]]) -> list[str]:
        """ Prepares data to be summarised"""
        res = data['Captions']
        return res 
            
    
    def prepmodel(self) -> object:
        """ creates model object """ 
        tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
        model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
        sa = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions",truncation=True,return_all_scores=True)
        return sa
    
    def savej(self,data: any) -> None:
        """ saves sa output as json """
        with open('sa_results.json','w') as f:
            json.dump(data,f)
        return os.path.isfile('sa_results.json')
    
    
    def sa(self,source: dict, limit: int, save=False)-> dict:
        """ performs sentiment analysis """
        data = self.prepdata(source) 
        model = self.prepmodel()
        res = {'SA':[]}
        if limit == -1:
            n = len(data)
        else:
            n = limit
        
        for i in range(n):
            sares = model(data[i])
            res['SA'].append(str(sares))
            print(f"job: {i+1} /{n} done.")
        
        if save == True:
            self.savej(res)
            
        return res 
        
        
    
        
    