from dash import Dash, dcc, html, Input, Output, callback
import sys 

# adding modules path 
sys.path.insert(0,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/etl')
sys.path.insert(1,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/youtube_api')
sys.path.insert(2,'D:/python_projects/Youtube-Video-Analyser-GUI-Version/nlp')

# import custom modules
from ytchannel import Ytchannel 
from ytvideo import Ytvideo 
from transcribe import Transcribe 
from nlp_ner import NER
from nlp_sa import SA 
from nlp_summarisation import Summariser 
from etlner import EtlNER 
from etlsa import EtlSA 
from etldf import EtlDF 

#initiasing 
channel_helper = Ytchannel()
video_helper = Ytvideo()
transcribe_helper = Transcribe()
ner_helper = NER()
sa_helper = SA()
sum_helper = Summariser()
etlner_helper = EtlNER()
etlsa_helper = EtlSA()
etldf_helper = EtlDF()



app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='UCVjlpEjEY9GpksqbEesJnNA', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def res(input_value):
    location = channel_helper.get_videos(input_value)
    meta = video_helper.export_info(location)
    captions = transcribe_helper.get_captions(meta,1)

    return f'Output: {str(captions)}'


if __name__ == '__main__':
    app.run(debug=True)
