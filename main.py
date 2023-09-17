#libraries 
from youtube_api.ytchannel import Ytchannel
from youtube_api.ytvideo import Ytvideo
from nlp.nlp_ner import NER
from etl.etlner import EtlNER
from youtube_api.transcribe import Transcribe
from nlp.nlp_sa import SA
from etl.etlsa import EtlSA
from etl.etldf import EtlDF
import pandas as pd
from etl.dbmanager import DBmanager
from nlp.nlp_summarisation import Summariser



#initialising
channel_manage = Ytchannel()
video_manage = Ytvideo()
nlp_ner = NER()
nlp_sa = SA()
etlner_manage = EtlNER()
scribe_manage = Transcribe()
etlsa_manage = EtlSA()
etldf = EtlDF()
dbm = DBmanager()
sums = Summariser()

id = 'UCVjlpEjEY9GpksqbEesJnNA'


""" testing 1 video """
# meta
location = channel_manage.get_videos(id)
meta = video_manage.export_info(location)


#transcribe
captions = scribe_manage.get_captions(meta,1)

#summarisation
sum_data = sums.summarise(captions,1)

#sa
# sa_raw = nlp_sa.sa(captions,1)

# #ner
# ner_raw = nlp_ner.ner(captions,1)

