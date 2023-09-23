import dash
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

""" File for customing and creating a side bar for navigation """



class SideBar:
    """ class for sidebar """ 
    def __init__(self):
        self.SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        'border':'5px grey solid',
        'border-radius': '10px',
            }
        
        self.CONTENT_STYLE = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }
    
    def darkmode(self):
        """ addition of darkmode toggler """ 
        return ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.FLATLY, dbc.themes.DARKLY])



    def use(self):
        return html.Div(
            [
                html.H2("Youtube Video Analyser", className="display-4"),
                self.darkmode(),
                html.Hr(),
                html.P(
                    " Use the pages below in order to start your analysis", className="lead"
                ),
                dbc.Nav(
                    [
                        dbc.NavLink(
                            html.Div(page['name']),
                            href = page['path'],
                            active = 'exact',
                        )
                        for page in dash.page_registry.values()
                    ],
                    vertical = True,
                    pills = True,
                )
            ],
            style = self.SIDEBAR_STYLE,
    
        )