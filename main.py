from youtube_api.ytchannel import Ytchannel
from youtube_api.ytvideo import Ytvideo
from nlp.nlp_ner import NER
from etl.etlner import EtlNER
from youtube_api.transcribe import Transcribe
from nlp.nlp_sa import SA
from etl.etlsa import EtlSA
from etl.database_manager import DataManager as dm
import pandas as pd

#initialising
channel_manage = Ytchannel()
video_manage = Ytvideo()
nlp_ner = NER()
nlp_sa = SA()
etlner_manage = EtlNER()
scribe_manage = Transcribe()
etlsa_mange = EtlSA()
db_manage = dm()
id = 'UCVjlpEjEY9GpksqbEesJnNA'


#testing
df = pd.read_csv('data/uncle_roger_df.csv')
ner = nlp_ner.ner(df,-1,save=True)
