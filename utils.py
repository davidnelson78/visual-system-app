import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                    [html.H5("Rockwell Automation Upgrade Compatability Report")],
                    className="twelve columns main-title",
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/visual-system-app/overview",
                className="tab first",
            ),
            dcc.Link(
                "OS / Antivirus",
                href="/visual-system-app/osAntivirus",
                className="tab",
            ),
            dcc.Link(
                "Features",
                href="/visual-system-app/features",
                className="tab",
            ),
            dcc.Link(
                "Firmware",
                href="/visual-system-app/firmware",
                className="tab",
            ),
            dcc.Link(
                "Modules",
                href="/visual-system-app/modules",
                className="tab",
            ),
            dcc.Link(
                "Requirements",
                href="/visual-system-app/requirements",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
