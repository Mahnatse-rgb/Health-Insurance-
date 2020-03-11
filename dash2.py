import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import param
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from ipywidgets import widgets

df = pd.read_csv('/home/recruit/Umuzi/visualization/Insurance-Fees/data/insurance.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app  = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children =[
    html.H1(children ='Health Insurance'),

    html.Div(children =[
        html.H4(children = 'dataframe'),
        generate_table(df)
    ]),

    dcc.Graph(
        id = 'sex, charges, smoker',
        figure = px.bar(df, x="sex", y="charges", color='smoker', barmode='group',
             height=400),

    )
])



if __name__ == '__main__':
    app.run_server(debug = True)
