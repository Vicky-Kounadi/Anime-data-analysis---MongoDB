import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Q_2.1.csv')

df = pd.read_csv(filename, sep = ',', header = None, names = ["id", "Rank", "Name", "Type", "Tags", "Rating", "Release_year", "Content_Warning"], skiprows = 1)

# Scatter Plot
fig = go.Figure(data = go.Scatter(x = df['Release_year'], y = df['Rating'], mode = 'markers'))

fig.update_layout(
    xaxis_title="Release Year",
    yaxis_title="Rating",
)

fig.show()
