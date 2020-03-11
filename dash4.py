import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from ipywidgets import widgets


app = dash.Dash()

df = pd.read_csv('/home/recruit/Umuzi/visualization/Insurance-Fees/data/insurance.csv')
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


age = widgets.IntSlider(
    value=1.0,
    min=18.0,
    max=64.0,
    step=1.0,
    description='Age:',
    continuous_update=False
)

use_date = widgets.Checkbox(
    description='Age: ',
    value=True,
)

container = widgets.HBox(children=[use_date, age])

origin = widgets.Dropdown(
    description='children:   ',
    #value='DL',
    options=df['children'].unique().tolist()
)

origin = widgets.Dropdown(
    options=list(df['smoker'].unique()),
    #value='LGA',
    description='smoker:',
)

origin = widgets.Dropdown(
    options=list(df['sex'].unique()),
    #value='LGA',
    description='sex:',
)

origin = widgets.Dropdown(
    options=list(df['region'].unique()),
    #value='LGA',
    description='region:',
)


# Assign an empty figure widget with two traces
trace1 = go.Histogram(x=df['age'], opacity=0.75, name='Age')
trace2 = go.Histogram(x=df['bmi'], opacity=0.75, name='bmi')
g = go.FigureWidget(data=[trace1, trace2],
                    layout=go.Layout(
                        title=dict(
                            text='Insurance'
                        ),
                        barmode='overlay'
                    ))
#Let now write a function that will handle the input from the widgets, and alter the state of the graph.

def validate():
    if origin.value in df['origin'].unique() and textbox.value in df['children'].unique():
        return True
    else:
        return False


def response(change):
    if validate():
        if use_date.value:
            filter_list = [i and j and k for i, j, k in
                           zip(df['age'] == age.value, df['salary'] == textbox.value,
                               df['salary'] == salary.value)]
            temp_df = df[filter_list]

        else:
            filter_list = [i and j for i, j in
                           zip(df['salary'], df['age'] == salary.value)]
            temp_df = df[filter_list]
        x1 = temp_df['arr_delay']
        x2 = temp_df['dep_delay']
        with g.batch_update():
            g.data[0].x = x1
            g.data[1].x = x2
            g.layout.barmode = 'overlay'
            g.layout.xaxis.title = 'Delay in Minutes'
            g.layout.yaxis.title = 'Number of Delays'


origin.observe(response, names="value")
#textbox.observe(response, names="value")
age.observe(response, names="value")
use_date.observe(response, names="value")

#Ttrying the app

container2 = widgets.HBox([origin])
widgets.VBox([container,
              container2,
              g])


if __name__ == '__main__':
    app.run_server(debug = True)
