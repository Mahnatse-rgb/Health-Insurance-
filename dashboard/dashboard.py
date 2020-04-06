import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import os
os.chdir('../data')

df = pd.read_csv('insurance.csv')

app = dash.Dash()

age_options = []
for age in df['age'].unique():
    age_options.append({'label' :str(age), 'value': age})

features = df.columns


app.layout = html.Div([
             html.H1('Health Insursnce Fee Visualization'),

            #First graph : Scatterplot of charges of bmi in a specific region given the age

            dcc.Graph(id ='graph'),
            dcc.Dropdown(id = 'age-picker', options = age_options,
                        value = df['age'].min())

            ,
            html.Hr()
            ,
            #-------- Second plot : Compare any two variables that affect Health Insurance fee

            dcc.Graph(id = 'feature-graph'),

            html.Div([
                dcc.Dropdown(id = 'xaxis',
                             options =[{'label': i, 'value' : i} for i in features],
                             value = 'charges')
            ],style = {'width' : '48%', 'display' : 'inline-block'}),

            html.Div([
                dcc.Dropdown(id = 'yaxis',
                             options =[{'label': i, 'value': i} for i in features],
                             value ='children')
            ],style = {'width' : '48%', 'display' : 'inline-block'})

], style = {'padding':10})

#---------------------------------------------------Callbacks and functions---------------------------------------------------

#function and call back for 2nd plot : feature graph
@app.callback(Output('feature-graph', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])

def update_graph(xaxis_name, yaxis_name):

    return {'data' : [go.Scatter(x = df[xaxis_name],
                                y = df[yaxis_name],
                                text = df.count(),
                                mode = 'markers',
                                marker = {'size': 10})
                                ],
            'layout': go.Layout(title = 'Compare any two variables that affect Health Insurance fee',
                                xaxis = {'title' : xaxis_name},
                                yaxis = {'title': yaxis_name})}




#----------------------------------------function and call back for first graph
@app.callback(Output('graph', 'figure'),
            [Input('age-picker','value')])

def update_figure(selected_age):

    #Display only the data for selected age from dropdown
    filtered_df = df[df['age'] == selected_age]

    trace = []

    for region_name in filtered_df['region'].unique():
        df_by_region = filtered_df[filtered_df['region'] == region_name]
        trace.append(go.Scatter(
            x = df_by_region['bmi'],
            y = df_by_region['charges'],
            mode = 'markers',
            opacity = 0.7,
            marker = {'size' : 7},
            name = region_name
        ))



    return{'data': trace,
           'layout': go.Layout(title = 'Scatterplot of charges of bmi in a specific region given the age',
                               xaxis = {'title' : 'bmi'},
                               yaxis = {'title' : 'charges'})}



if __name__ == '__main__':
    app.run_server(debug = True)
