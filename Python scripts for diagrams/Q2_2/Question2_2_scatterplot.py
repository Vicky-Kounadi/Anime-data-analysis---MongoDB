import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Q_2.2.csv')

df = pd.read_csv(filename, sep = ',', header = None, names = ["id", "Rank", "Name", "Rating", "tagCount"], skiprows = 1)

# Scatter Plot
fig = go.Figure(data = go.Scatter(x = df['Rating'], y = df['tagCount'], mode = 'markers'))

fig.update_layout(
    xaxis_title="Rating",
    yaxis_title="Tag Count",
)

fig.show()
