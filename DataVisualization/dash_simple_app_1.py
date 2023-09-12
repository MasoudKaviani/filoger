from pathlib import Path
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import os

app = Dash(__name__)

src_file = os.path.join("data", "raw", "EPA_fuel_economy_summary.csv")
df = pd.read_csv(src_file)

fig = px.histogram(
    df,
    x="fuelCost08",
    color="class_summary",
    labels={"fuelCost08": "Annual Fuel Cost"},
    nbins=40,
    title="Fuel Cost Distribution",
)

app.layout = html.Div(children=[
    html.H1("داده‌های مصرف انرژی اتومبیل‌ها"),
    html.Div("سالیانه"),
    dcc.Graph(id="example-histogram", figure=fig),
])

if __name__ == "__main__":
    app.run_server(debug=True)

# Masoud Kaviani