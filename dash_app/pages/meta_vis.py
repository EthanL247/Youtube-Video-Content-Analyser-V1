import dash
from dash import dcc, html
from components.sidebar import SideBar

dash.register_page(__name__)

#initialising
side_bar = SideBar()


layout = html.Div(
    [
        html.H1('Page 2'),
    ],
    style = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }
    )