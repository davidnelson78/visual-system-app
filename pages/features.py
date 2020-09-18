import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_equity_char = pd.read_csv(DATA_PATH.joinpath("df_equity_char.csv"))
df_equity_diver = pd.read_csv(DATA_PATH.joinpath("df_equity_diver.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    # Row 1
                    html.Br([]),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Features 1"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(
                                        make_dash_table(df_equity_char),
                                        className="tiny-header",
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Features 2"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(
                                        make_dash_table(df_equity_diver),
                                        className="tiny-header",
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
