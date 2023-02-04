import dash
from dash import dcc
from dash import html
from dash import Dash, Input, Output, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from flask import Flask


server=Flask(__name__)

app = dash.Dash(
    __name__, server=server,
    use_pages=False,
     external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP] 
     )

app.layout = html.Div([

    html.Div([
        html.P("Stockers", className="stockerLogo"),
        
    ])




    ])


if __name__ == '__main__':
    app.run_server(debug=True)