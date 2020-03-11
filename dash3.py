import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/home/recruit/Umuzi/visualization/Insurance-Fees/data/insurance.csv')


app.layout = html.Div([
    html.H1('The Scatter plot of charges vs bmi as per region'),
    dcc.Graph(
        id='charges-vs-bmi',
        figure={
            'data': [
                dict(
                    x=df[df['region'] == i]['bmi'],
                    y=df[df['region'] == i]['charges'],
                    text=df[df['region'] == i]['region'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.region.unique()
            ],
            'layout': dict(
                xaxis={ 'title': 'bmi'},
                yaxis={'title': 'charges'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='cloBsest'
            )

        }
    )
])

if __name__ == '__main__':
    app.run_server(debug = True)
