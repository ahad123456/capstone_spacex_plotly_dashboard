from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def all_success_pichart(data):
   # For pir chart 
    filter_data = data[data['Outcome'].isin(['True ASDS','True Ocean'])]
    filter_data = filter_data[['LaunchSite','Outcome']]
    
    #group_data = filter_data.groupby(['LaunchSite','Outcome']).size().reset_index(name='count')
    filter_data = filter_data['LaunchSite'].value_counts().reset_index()
    filter_data.columns = ['LaunchSite','count']
    fig = go.Figure(
    data=[go.Pie(
        labels=filter_data['LaunchSite'],
        values=filter_data['count'],
        marker=dict(colors=['Gold', 'MediumTurquoise', 'LightGreen']),
        textinfo='label+value'
        )]
    )
    fig.show()


def main():
    # Read Data 
    data = pd.read_csv("dataset_collected.csv")
    df = pd.DataFrame(data)

    # All success in PiChart
    all_success_pichart(data)

if __name__ == '__main__':
  main()
