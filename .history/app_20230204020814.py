from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1(children='Hello Dash')
    ])


if __name__ == '__main__':
    app.run_server(debug=True)