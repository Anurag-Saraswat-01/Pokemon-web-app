from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.io as pio
import pandas as pd

from . import theme
from app import app

pio.templates.default = 'custom'

print('Loading dex')
dex_df = pd.read_csv("pokedex_markdown.csv")

names = []
for name in dex_df['Name']:
    names.append({'label': name, 'value': name})

# eeveelutions = ['Eevee', 'Vaporeon', 'Jolteon', 'Flareon',
#                 'Umbreon', 'Espeon', 'Glaceon', 'Leafeon', 'Sylveon']
eeveelutions = ['Eevee', 'Espeon', 'Umbreon']


# df for stats
stat_df = pd.melt(dex_df, id_vars='Name', value_vars=[
                  'Speed', 'Sp. Defense', 'Sp. Attack', 'Defense', 'Attack', 'HP'], var_name='stat')
# df for Stat Total
bst_df = pd.melt(dex_df, id_vars='Name',
                 value_vars='Stat Total', var_name='Stat Total')
# df for img src
src_df = dex_df[['Name', 'Image', 'Type', 'Ability', 'Hidden Ability']].copy()


def transform(df):
    df = df.set_index('Name')
    df = df[['Image', 'Type', 'Ability', 'Hidden Ability']].transpose()
    # df = df.reset_index()
    return df


# df's for eeveelutions
eevee_stat_df = stat_df[stat_df['Name'].isin(eeveelutions)]
eevee_bst_df = bst_df[bst_df['Name'].isin(eeveelutions)]
eevee_src_df = src_df[src_df['Name'].isin(eeveelutions)]

# eeveelution stat graph
print('Creating eeveelution stat graph')
eevee_stat_fig = px.bar(
    eevee_stat_df,
    x='value',
    y='stat',
    color='value',
    color_continuous_scale=[[0, 'hsla(0, 100, 50, 0.75)'], [0.35, 'hsla(60, 100%, 50%, 0.75)'],
                            [0.55, 'hsla(120, 100%, 50%, 0.75)'], [1, 'hsla(180, 100%, 50%, 0.75)']],
    range_color=[40, 200],
    facet_col='Name',
    text='value',
    title='STAT DISTRIBUTION'
)
for a in eevee_stat_fig.layout.annotations:
    a.text = ''
eevee_stat_fig.update_yaxes(title='')
eevee_stat_fig.update_traces(textfont_color='black', textfont_size=14)

# eeveelution bst graph
print('Creating eeveelution bst graph')
eevee_bst_fig = px.bar(
    eevee_bst_df,
    y='Stat Total',
    x='value',
    color='value',
    color_continuous_scale=[[0, 'hsla(0, 100, 50, 0.75)'], [0.35, 'hsla(60, 100%, 50%, 0.75)'],
                            [0.55, 'hsla(120, 100%, 50%, 0.75)'], [1, 'hsla(180, 100%, 50%, 0.75)']],
    range_color=[300, 720],
    facet_col='Name',
    height=175,
    text='value',
    title='OVERALL'
)
for a in eevee_bst_fig.layout.annotations:
    a.text = ''
eevee_bst_fig.update_layout(margin=dict(l=100))
eevee_bst_fig.update_yaxes(title='')
eevee_bst_fig.update_traces(textfont_color='black', textfont_size=14)

# eeveelution name and src table
print('Creating eeveelution table')
# print(eevee_src_df, '\n')
# print(transform(eevee_src_df))
eevee_data = transform(eevee_src_df).to_dict('records')
eevee_columns = [dict(name=i, id=i, presentation='markdown')
                 for i in transform(eevee_src_df).columns]

layout = html.Div(children=[
    html.Header(children=[
        html.Img(src='/assets/espeon_logo.png', className='esp_logo'),
        html.H1([dcc.Link('COMPAREON', href='/')], className='title'),
        html.Nav([
            dcc.Link('HOME', href='/'),
            dcc.Link('COMPARE', href='/compare', className='current')
        ]),
        html.Img(src='/assets/umbreon_logo.png', className='umbr_logo')
    ]),
    html.Div(className='container', children=[
        html.Div(
            dcc.Dropdown(
                id='dropdown',
                options=names,
                multi=True,
                value=eeveelutions,
                style={'background': '#EDEDED', 'color': 'black'}
            )
        ),
        html.Div(className='content', children=[
            dash_table.DataTable(
                id='table',
                data=eevee_data,
                columns=eevee_columns,
                style_header={'whiteSpace': 'normal', 'height': 'auto', 'padding': '0 5px',
                              'fontFamily': "Georgia, 'Times New Roman', Times, serif"},
                css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                style_cell={'background': '#EDEDED',
                            'border': 'none', 'color': 'black',
                            'whiteSpace': 'normal', 'height': 'auto', 'padding': '0 5px',
                            'fontFamily': "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"},
            ),
            dcc.Graph(id='bar', figure=eevee_stat_fig,
                      config={'displayModeBar': False}),
            dcc.Graph(id='total_bar', figure=eevee_bst_fig,
                      config={'displayModeBar': False})
        ])
    ]),
    html.Footer(className='footer', children='Caffeine 2021')
])

print('Done\n')


@app.callback(Output('bar', 'figure'), Output('total_bar', 'figure'), Output('table', 'data'),
              Output('table', 'columns'), Input('dropdown', 'value'))
def update_graph(dropdown_value):
    dropdown_value = dropdown_value[:10]
    if dropdown_value is None or len(dropdown_value) == 0:
        stat_callback_df = eevee_stat_df
        bst_callback_df = eevee_bst_df
        src_callback_df = eevee_src_df
    else:
        stat_callback_df = stat_df[stat_df['Name'].isin(dropdown_value)]
        # stat_callback_df['Name'] = pd.Categorical(stat_callback_df['Name'], dropdown_value)
        # stat_callback_df.sort_values('Name', inplace=True)

        bst_callback_df = bst_df[bst_df['Name'].isin(dropdown_value)]
        # bst_callback_df['Name'] = pd.Categorical(bst_callback_df['Name'], dropdown_value)
        # bst_callback_df.sort_values('Name', inplace=True)

        src_callback_df = src_df[src_df['Name'].isin(dropdown_value)]
        # src_callback_df['Name'] = pd.Categorical(src_callback_df['Name'], dropdown_value)
        # src_callback_df.sort_values('Name', inplace=True)

    stat_fig = px.bar(
        stat_callback_df,
        y='stat',
        x='value',
        color='value',
        color_continuous_scale=[[0, 'hsla(0, 100, 50, 0.75)'], [0.35, 'hsla(60, 100%, 50%, 0.75)'],
                                [0.55, 'hsla(120, 100%, 50%, 0.75)'], [1, 'hsla(180, 100%, 50%, 0.75)']],
        range_color=[40, 200],
        facet_col='Name',
        text='value',
        title='STAT DISTRIBUTION'
    )
    for a in stat_fig.layout.annotations:
        a.text = ''
    stat_fig.update_yaxes(title='')
    stat_fig.update_traces(textfont_color='black', textfont_size=14)

    bst_fig = px.bar(
        bst_callback_df,
        y='Stat Total',
        x='value',
        color='value',
        color_continuous_scale=[[0, 'hsla(0, 100, 50, 0.75)'], [0.35, 'hsla(60, 100%, 50%, 0.75)'],
                                [0.55, 'hsla(120, 100%, 50%, 0.75)'], [1, 'hsla(180, 100%, 50%, 0.75)']],
        range_color=[300, 720],
        facet_col='Name',
        height=175,
        text='value',
        title='OVERALL'
    )
    for a in bst_fig.layout.annotations:
        a.text = ''
    bst_fig.update_layout(margin=dict(l=100))
    bst_fig.update_yaxes(title='')
    bst_fig.update_traces(textfont_color='black', textfont_size=14)

    data = transform(src_callback_df).to_dict('records')
    columns = [dict(name=i, id=i, presentation='markdown')
               for i in transform(src_callback_df).columns]

    return stat_fig, bst_fig, data, columns
