import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


export_simple_system = pd.read_csv(DATA_PATH.joinpath("24toCode_PCDC_Export_Simple_System.csv"))
migration_simple_system = pd.read_csv(DATA_PATH.joinpath("24toCode_PCDC_Migration_HW_Update_Simple_System.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            dcc.Upload(
                                id='upload-data',
                                children=html.Div([
                                    'Drag and Drop or ',
                                    html.A('Select Files')
                                ]),
                                style={
                                    'width': '100%',
                                    'height': '60px',
                                    'lineHeight': '60px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'bordermargin': '0px'
                                },
                                # Allow multiple files to be uploaded
                                multiple=True
                            ),
                            html.Div(id='output-data-upload'),

                            html.Br([]),
                            html.Div(
                                [
                                    html.H5("Compatability Score"),
                                    html.H5("5.1"),

                                    html.Br([]),
                                    html.P(
                                        "\
                                    relevant info here",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Overview 1"], className="subtitle padded"
                                    ),
                                    df=pd.read_csv('data/.csv')
                                    df.head()],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Overview 2",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "1 Year",
                                                        "3 Year",
                                                        "5 Year",
                                                        "10 Year",
                                                        "41 Year",
                                                    ],
                                                    y=[
                                                        "21.67",
                                                        "11.26",
                                                        "15.62",
                                                        "8.37",
                                                        "11.11",
                                                    ],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "1 Year",
                                                        "3 Year",
                                                        "5 Year",
                                                        "10 Year",
                                                        "41 Year",
                                                    ],
                                                    y=[
                                                        "21.83",
                                                        "11.41",
                                                        "15.79",
                                                        "8.50",
                                                    ],
                                                    marker={
                                                        "color": "#dddddd",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Overview 3",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=[
                                                        "2008",
                                                        "2009",
                                                        "2010",
                                                        "2011",
                                                        "2012",
                                                        "2013",
                                                        "2014",
                                                        "2015",
                                                        "2016",
                                                        "2017",
                                                        "2018",
                                                    ],
                                                    y=[
                                                        "10000",
                                                        "7500",
                                                        "9000",
                                                        "10000",
                                                        "10500",
                                                        "11000",
                                                        "14000",
                                                        "18000",
                                                        "19000",
                                                        "20500",
                                                        "24000",
                                                    ],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="",
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0277108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                xaxis={
                                                    "autorange": True,
                                                    "linecolor": "rgb(0, 0, 0)",
                                                    "linewidth": 1,
                                                    "range": [2008, 2018],
                                                    "showgrid": False,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    "range": [0, 30000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 10,
                                                    "ticks": "outside",
                                                    "title": "$",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Overview 4",
                                        className="subtitle padded",
                                    ),
                                    #html.Table(make_dash_table(migration_simple_system)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
