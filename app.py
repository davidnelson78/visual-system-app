# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    os_antivirus,
    features,
    firmware,
    modules,
    requirements,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/visual-system-app/os_antivirus":
        return os_antivirus.create_layout(app)
    elif pathname == "/visual-system-app/features":
        return features.create_layout(app)
    elif pathname == "/visual-system-app/firmware":
        return firmware.create_layout(app)
    elif pathname == "/visual-system-app/modules":
        return modules.create_layout(app)
    elif pathname == "/visual-system-app/requirements":
        return requirements.create_layout(app)
    elif pathname == "/visual-system-app/full-view":
        return (
            overview.create_layout(app),
            os_antivirus.create_layout(app),
            features.create_layout(app),
            firmware.create_layout(app),
            modules.create_layout(app),
            requirements.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
