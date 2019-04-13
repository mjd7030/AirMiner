# -*- coding: utf-8 -*-
import dash
import dash_table
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as ply
#import plotly.plotly as py
import plotly.figure_factory as ff

df = pd.read_csv('ENTER YOUR GOOGLE SHEET URL FROM FILE -> PUBLISH -> LINK AS CSV')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF' 
}

params = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','nextday']
df_hour_list = df['hour'].to_list()
df_nextday_list = df['nextday'].to_list()


def generate_table(dataframe, max_rows=25):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

#da = [ go.Scatter(x=df['hour'], # assign x as the dataframe column 'x'
 #               y=df['nextday'])
                    #{'x': df[df[columns='hour']].to_numpy(), 'y':df[df(columns='nextday')].to_numpy(), 'type': 'line'}
#],

app.layout = html.Div(
    children=[
    
    html.H4(children='AIR MINER DATA (WEEKLY) - MAULIK\'S HOME'),
   
    #generate_table(df),

    dash_table.DataTable(
            id='table-editing-simple',
            columns=(
             #   [{'id': 'hour', 'name': 'hour'}] #+
                 [{'id': p, 'name': p} for p in df.columns]
            ),  
            data=df.to_dict('rows'),
            #dict(hour=i,i for i in hourlist)],         
            editable=True
        ),
        
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x':df_hour_list,'y':df_nextday_list}
                #{'x': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],'y': [10,8,5,3,4,5,9,10,12,15,15,15,11,12,12,11,11,11,13,14,15,15,14,12],'type': 'line', 'name': 'SF'}#,
                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                    }
            }
        }
    )

])
    #x=df['hour'].to_values()
    #y=df[8]



if __name__ == '__main__':
    app.run_server(debug=True)
