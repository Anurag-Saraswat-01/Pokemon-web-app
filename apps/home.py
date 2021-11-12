import dash_core_components as dcc
import dash_html_components as html

layout = html.Div(children=[
    html.Header(children=[
        html.Img(src='/assets/espeon_logo.png', className='esp_logo'),
        html.H1([dcc.Link('COMPAREON', href='/')], className='title'),
        html.Nav([
            dcc.Link('HOME', href='/', className='current'),
            dcc.Link('COMPARE', href='/compare')
        ]),
        html.Img(src='/assets/umbreon_logo.png', className='umbr_logo')
    ]),
    html.Div(className='container', children=[
        html.Div(className='home', children=[
            html.Div([html.Img(src='/assets/Eevee_LG.png')],
                     className='home_img'),
            html.Div(className='home_text', children=[
                html.H2('COMPAREON - Home'),
                html.P(
                    'Compareon is a Web Application built using Python Dash Framework, Plotly and CSS3.'),
                html.P('''
                    The purpose of this application is to allow users to compare the stats viz.
                    Hit Points, Attack, Defense, Special Attack, Special Defense and Speed along with 
                    Types, Abilities and Hidden Abilities of various Pokémon.
                '''),
                html.P('''
                    The Compare Page allows users to compare the different Pokémon. Users can select the 
                    Pokémon they want using the Dropdown menu. As such, there is no limit to the
                    number of Pokémon that can be selected simultaneously, however the results are clipped 
                    to a maximum of 10 Pokémon. 
                '''),
                html.P('''
                    The Pokémon species data is upto date with Generation 8 - 
                    Pokémon Sword and Shield Crown Tundra Expansion Pass.
                '''),
                dcc.Link([html.P('Proceed to Compare')],
                         href='/compare', className='proceed-btn')
            ])
        ])
    ]),
    html.Footer(className='footer', children='Caffeine 2021')
])
