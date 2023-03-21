from dash import html, dcc
import plotly.graph_objs as go
from navbar import create_navbar
import pandas as pd

# Criar um DataFrame de exemplo
df = pd.read_excel('BOPIS_20-03-2023.xlsx')

# Criar um gráfico de linhas com Plotly
trace = go.Line(x=df['LOJA'], y=df['LEAD TIME'], text=df['LEAD TIME'], textposition='top center')
fig = go.Figure(data=[trace], layout={'title': 'Example Graph'})

# Criar o layout da página
nav = create_navbar()
header = html.H3('LEAD TIME')
graph = dcc.Graph(id='example-graph', figure={'data': [trace], 'layout': {'title': 'BOPIS: LEAD TIME DE FATURAMENTO' }})

def create_page_2():
    layout = html.Div([
        nav,
        header,
        graph
    ])
    return layout

