# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Read Data 
data = pd.read_csv("dataset_collected.csv")
df = pd.DataFrame(data)
df = df[df['Outcome'].str.startswith('True') ]
# create launch outcome

# Silder value and style
marks = {str(payload): {'label': str(payload), 'style': {'transform': 'rotate(00deg)', 'whiteSpace': 'nowrap'}} 
         for payload in range(int(df['PayloadMass'].min()), int(df['PayloadMass'].max())+1, 900)}

app = dash.Dash(__name__)  # Create a dash application
                               
app.layout = html.Div(children=[ 
    html.H1('PayloadMass and LaunchSite scatter plot',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.Div([ dcc.Slider(
        min= df['PayloadMass'].min(),
        max= df['PayloadMass'].max(),
        step=200,
        value=[df['PayloadMass'].min(), df['PayloadMass'].max()],
        marks=marks,
        id='payload_slider')
    ], 
                                style={'font-size': 40}),
    html.Br(),
    html.Div(dcc.Graph(id='line-plot')),
    ])

# add callback decorator
@app.callback( Output(component_id='line-plot', component_property='figure'),
               Input(component_id='payload_slider', component_property='value')
)

# Add computation to callback function and return graph
def get_graph(pay_selected):
    # Select 2019 data

    filtered_df  =  df[df['PayloadMass'] <= pay_selected]
    
    #line_data = df.groupby('PayloadMass')['LaunchSite'].mean().reset_index()
    fig = go.Figure(data=go.Scatter(x=filtered_df['PayloadMass'], y=filtered_df['LaunchSite'], mode='markers', marker=dict(color='green')))
    fig.update_layout(title='', xaxis_title='PayloadMass', yaxis_title='Launch Site')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()