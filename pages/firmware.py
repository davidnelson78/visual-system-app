import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()



def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 4
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Firmware 1"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Strong(),
                                    html.H6(["Firmware 2"],
                                            className="subtitle padded"),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Strong(
                                        "Bar Graph",
                                        style={"color": "#3a3a3a"},
                                    ),
                                    dcc.Graph(
                                        id="graph-6",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[""],
                                                    y=["", ""],
                                                    marker={"color": "#97151c"},
                                                    name="A",
                                                ),
                                                go.Bar(
                                                    x=[""],
                                                    y=[""],
                                                    marker={"color": " #dddddd"},
                                                    name="B",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                annotations=[
                                                    {
                                                        "x": -0.0111111111111,
                                                        "y": 2381.92771084,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995555555556,
                                                        "y": 509.638554217,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995551020408,
                                                        "y": 1730.32432432,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                ],
                                                autosize=False,
                                                height=260,
                                                width=320,
                                                bargap=0.4,
                                                barmode="stack",
                                                hovermode="closest",
                                                margin={
                                                    "r": 40,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 40,
                                                },
                                                showlegend=False,
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 1.5],
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 8,
                                                    },
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "mirror": False,
                                                    "nticks": 3,
                                                    "range": [0, 3000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 10,
                                                    },
                                                    "tickprefix": "$",
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
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Firmware 3"], className="subtitle"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Strong(
                                                                [""],
                                                                style={
                                                                    "color": "#515151"
                                                                },
                                                            )
                                                        ],
                                                        className="three columns right-aligned",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                ["None"],
                                                                style={
                                                                    "color": "#7a7a7a"
                                                                },
                                                            )
                                                        ],
                                                        className="nine columns",
                                                    ),
                                                ],
                                                className="row",
                                                style={
                                                    "background-color": "#f9f9f9",
                                                    "padding-top": "20px",
                                                },
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Strong(
                                                                [""],
                                                                style={
                                                                    "color": "#515151"
                                                                },
                                                            )
                                                        ],
                                                        className="three columns right-aligned",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                ["None"],
                                                                style={
                                                                    "color": "#7a7a7a"
                                                                },
                                                            )
                                                        ],
                                                        className="nine columns",
                                                    ),
                                                ],
                                                className="row",
                                                style={"background-color": "#f9f9f9"},
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Strong(
                                                                [""],
                                                                style={
                                                                    "color": "#515151"
                                                                },
                                                            )
                                                        ],
                                                        className="three columns right-aligned",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                ["None"],
                                                                style={
                                                                    "color": "#7a7a7a"
                                                                },
                                                            )
                                                        ],
                                                        className="nine columns",
                                                    ),
                                                ],
                                                className="row",
                                                style={"background-color": "#f9f9f9"},
                                            ),
                                        ],
                                        className="",
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [""],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        [
                                                            ""
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            ""
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        [""],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            ""
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        [""],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            ""
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        [""],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            ""
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
