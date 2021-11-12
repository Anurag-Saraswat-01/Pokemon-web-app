import os

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                update_title="Loading", title="Compareon")
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

from apps import home, compare

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    elif pathname == '/compare':
        return compare.layout
    else:
        return html.H1('ERROR 404: Page Not Found')

if __name__ == '__main__':
    app.run_server(debug=True)

