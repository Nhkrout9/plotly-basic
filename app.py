from dash import Dash, html
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World'),
    dcc.Input(
        id='controls-and-radio-item',
        type='number',
        value=5
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(id='my-output'),
])
l=["very worst","worst","Not satisfied","Good","Very Good","Excellent"]
@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def funy(value):
    return l[value]
  


    
if __name__ == '__main__':
    app.run(debug=True)
