import dash
from dash import dcc
from dash import html
from dash import Dash, Input, Output, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from flask import Flask


app = Dash(__name__)

app.layout = html.Div([

    html.H1('Hello Dash')
    ])


if __name__ == '__main__':
    app.run_server(debug=True)