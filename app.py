import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.P import P
import dash_table
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                update_title="Updating", title="Compareon")
server = app.server

print('Loading dex')
dex_df = pd.read_csv("pokedex_markdown.csv")

names = []
for name in dex_df['Name']:
    names.append({'label': name, 'value': name})

# eeveelutions = ['Eevee', 'Vaporeon', 'Jolteon', 'Flareon',
#                 'Umbreon', 'Espeon', 'Glaceon', 'Leafeon', 'Sylveon']
eeveelutions = ['Eevee', 'Umbreon', 'Espeon']

# df for stats
stat_df = pd.melt(dex_df, id_vars='Name', value_vars=[
                  'Speed', 'Sp. Defense', 'Sp. Attack', 'Defense', 'Attack', 'HP'], var_name='stat')
# df for base stat total
bst_df = pd.melt(dex_df, id_vars='Name',
                 value_vars='Stat. Total', var_name='Stat. Total')
# df for img src
src_df = dex_df[['Name', 'Image', 'Type', 'Ability', 'Hidden Ability']].copy()

# Sp. Defense
# Stat. Total


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
    color_continuous_scale=[[0, 'red'], [
        0.35, 'yellow'], [0.55, 'lime'], [1, 'cyan']],
    range_color=[40, 200],
    facet_col='Name',
    template='plotly_dark',
    text='value'
)
for a in eevee_stat_fig.layout.annotations:
    # a.text = a.text.split("=")[1]
    a.text = ''
eevee_stat_fig.update(layout_coloraxis_showscale=False,
                      layout_margin=dict(b=0), layout_font_family='monospace')
eevee_stat_fig.update_xaxes(visible=False)
eevee_stat_fig.update_yaxes(title='')
eevee_stat_fig.update_traces(textfont_color='black')

# eeveelution bst graph
print('Creating eeveelution bst graph')
eevee_bst_fig = px.bar(
    eevee_bst_df,
    y='Stat. Total',
    x='value',
    color='value',
    color_continuous_scale=[[0, 'red'], [
        0.3, 'yellow'], [0.7, 'lime'], [1, 'cyan']],
    range_color=[300, 720],
    facet_col='Name',
    template='plotly_dark',
    height=70,
    text='value'
)
for a in eevee_bst_fig.layout.annotations:
    a.text = ''
eevee_bst_fig.update(layout_coloraxis_showscale=False,
                     layout_margin=dict(t=0, b=10), layout_font_family='monospace')
eevee_bst_fig.update_xaxes(visible=False)
eevee_bst_fig.update_yaxes(title='')
eevee_bst_fig.update_traces(textfont_color='black')

# eeveelution name and src table
print('Creating eeveelution table')
print(eevee_src_df, '\n')
print(transform(eevee_src_df))
eevee_data = transform(eevee_src_df).to_dict('records')
eevee_columns = [dict(name=i, id=i, presentation='markdown')
                 for i in transform(eevee_src_df).columns]

app.layout = html.Div(children=[
    html.Header(children=[
        html.Img(src='/assets/espeon_logo.png', className='esp_logo'),
        html.P('COMPAREON', className='title'),
        html.Img(src='/assets/umbreon_logo.png', className='umbr_logo')
    ]),
    html.Div(className='container', children=[
        html.Div([
            dcc.Dropdown(
                id='dropdown',
                options=names,
                multi=True,
                style={'background': '#111111',
                       'border': 'none', 'color': 'black'}
            )
        ]),
        html.Div(className='content', children=[
            dash_table.DataTable(
                id='table',
                data=eevee_data,
                columns=eevee_columns,
                # style_header={'display': 'none'},
                css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
                style_cell={'background': '#111111',
                            'border': 'none', 'color': 'white'},
            ),
            dcc.Graph(id='bar', figure=eevee_stat_fig),
            dcc.Graph(id='total_bar', figure=eevee_bst_fig)
        ])
    ]),
    html.Footer(className='footer', children='Anurag')
], style={'background': '#cece8a'})

print('Done\n')


@app.callback(Output('bar', 'figure'), Output('total_bar', 'figure'), Output('table', 'data'),
              Output('table', 'columns'),
              Input('dropdown', 'value'))
def update_graph(dropdown_value):
    if dropdown_value is None or len(dropdown_value) == 0:
        stat_callback_df = eevee_stat_df
        bst_callback_df = eevee_bst_df
        src_callback_df = eevee_src_df
    elif type(dropdown_value) is str:
        stat_callback_df = stat_df[stat_df['Name'] == dropdown_value]
        bst_callback_df = bst_df[bst_df['Name'] == dropdown_value]
        src_callback_df = src_df[src_df['Name'] == dropdown_value]
    else:
        stat_callback_df = stat_df[stat_df['Name'].isin(dropdown_value)]
        bst_callback_df = bst_df[bst_df['Name'].isin(dropdown_value)]
        src_callback_df = src_df[src_df['Name'].isin(dropdown_value)]

    stat_fig = px.bar(
        stat_callback_df,
        y='stat',
        x='value',
        color='value',
        color_continuous_scale=[[0, 'red'], [
            0.35, 'yellow'], [0.55, 'lime'], [1, 'cyan']],
        range_color=[40, 200],
        facet_col='Name',
        template='plotly_dark',
        text='value'
    )
    for a in stat_fig.layout.annotations:
        # a.text = a.text.split("=")[1]
        a.text = ''
    stat_fig.update(layout_coloraxis_showscale=False,
                    layout_margin=dict(b=0), layout_font_family='monospace')
    stat_fig.update_xaxes(visible=False)
    stat_fig.update_yaxes(title='')
    stat_fig.update_traces(textfont_color='black')

    bst_fig = px.bar(
        bst_callback_df,
        y='Stat. Total',
        x='value',
        color='value',
        color_continuous_scale=[[0, 'red'], [
            0.3, 'yellow'], [0.7, 'lime'], [1, 'cyan']],
        range_color=[300, 720],
        facet_col='Name',
        template='plotly_dark',
        height=70,
        text='value'
    )
    for a in bst_fig.layout.annotations:
        a.text = ''
    bst_fig.update(layout_coloraxis_showscale=False,
                   layout_margin=dict(t=0, b=10), layout_font_family='monospace')
    bst_fig.update_xaxes(visible=False)
    bst_fig.update_yaxes(title='')
    bst_fig.update_traces(textfont_color='black')

    data = transform(src_callback_df).to_dict('records')
    columns = [dict(name=i, id=i, presentation='markdown')
               for i in transform(src_callback_df).columns]

    return stat_fig, bst_fig, data, columns


if __name__ == '__main__':
    app.run_server(debug=True)
