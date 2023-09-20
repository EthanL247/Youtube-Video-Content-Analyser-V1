# importing libraries 
import dash
import dash_bootstrap_components as dbc
from dash import html

# importing custom modules and functions 
from components.sidebar import SideBar


#initialising 
app = dash.Dash(__name__, use_pages=True,external_stylesheets=[dbc.themes.FLATLY])

#components 
sidebar = SideBar()

#layout
app.layout = html.Div([
    sidebar.use(),
    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True)