import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                update_title="Updating", title="Compareon")
server = app.server

app.layout = html.Div(children=[
    html.H1('ABOUT'),
    html.P('Compareon is a Web Application built using Python Dash Framework and CSS3.'),
    html.P('''
        The purpose of this application is to allow users to compare the stats viz.
        Hit Points, Attack, Defense, Special Attack, Special Defense and Speed along with 
        Types, Abilities and Hidden Abilities of various Pokémon.
    '''),
    html.P('''
        The Home Page allows users to compare the different Pokémon. Users can select the 
        Pokémon they want using the Dropdown menu. As such, there is no limit to the
        number of Pokémon that can be selected simultaneously, however it is recommended that 
        you select maximum of 10 Pokémon. The Pokémon species data is upto date with Generation 8 - 
        Pokémon Sword and Shield Crown Tundra Expansion Pass.
    '''),
    html.H3('Enjoy and Have Fun!!!')
])

if __name__ == '__main__':
    app.run_server(debug=True)
