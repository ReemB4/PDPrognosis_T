'''
# This app creates a simple sidebar layout using inline style arguments and the
# dbc.Nav component.
# dcc.Location is used to track the current location, and a callback uses the
# current location to render the appropriate page content. The active prop of
# each NavLink is set automatically according to the current pathname. To use
# this feature you must install dash-bootstrap-components >= 0.11.0.
# For more details on building multi-page Dash applications, check out the Dash
# documentation: https://dash.plot.ly/urls
# Source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
# @ Create Time: 2024-03-13 04:49:09.174227
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
'''
import time
import dash
import numpy as np
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(
    title="PDPrognosis",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "21rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

LOGO_STYLE = {
    "width":"10rem",

}

sidebar = html.Div(
    [
        html.Img(src="./img/PDPrognosis.jpeg", style=LOGO_STYLE),
        html.H5("PDPrognosis", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Patients", href="/page-1", active="exact"),
                dbc.NavLink("Profile", href="/page-2", active="exact"),
                dbc.NavLink("Settings", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
    [
        id="page-content",


    ],
    style=CONTENT_STYLE
)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 3!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
