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
        html.P("About", className="about")
    ], className="navHeader"),

    html.Div([
        html.P("Loream Pasum Tores", className="centerHeading"),
        html.Div([

        dcc.Input( id="inputArea", type="text", placeholder="Input Stock Symbol", className="inputArea"),
                         html.Button("Submit", id='submit', className="submitButton"),
        ], className="inputSubmit" )
    ], className="centerContainer")





    ])


if __name__ == '__main__':
    app.run_server(debug=True)