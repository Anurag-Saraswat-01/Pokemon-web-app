import dash
from dash.dependencies import Input,Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import plotly.io as plt_io
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__,suppress_callback_exceptions=True,update_title="Updating", title="Compareon")
server = app.server

df = pd.read_csv("pokedex_with_src.csv")
df.rename(columns={'total_points':'BST',
                    'hp':'HP',
                    'attack':'Att',
                    'defense':'Def',
                    'sp_attack':'Sp Att',
                    'sp_defense':'Sp Def',
                    'speed':'Speed'},
           inplace=True)

names = []
for name in df['name']:
    names.append({'label':name, 'value':name})
mons = ['Eevee', 'Vaporeon', 'Jolteon', 'Flareon',
        'Umbreon', 'Espeon', 'Glaceon', 'Leafeon', 'Sylveon']
    
def f(row):
    return "![{0}]({0})".format('/assets/home_images/' + row["src"])
    # return "![{0}]({0})".format('/assets/icons/' + row["src"])

required = ['name','BST','Speed','Sp Def','Sp Att','Def','Att','HP','src']
sdf = df[required]

adf = pd.melt(sdf, id_vars='name',value_vars=['Speed','Sp Def','Sp Att','Def','Att','HP'],var_name='stat')
# for i,row in adf.iterrows():
    # adf.at[i,'stat'] = adf.at[i,'stat'].ljust(10)
bdf = sdf.copy()
bdf = pd.melt(bdf, id_vars='name',value_vars='BST',var_name='BST')
# for i,row in bdf.iterrows():
    # bdf.at[i,'BST'] = bdf.at[i,'BST'].ljust(10)
# print(adf,bdf)

src_df = sdf[['name','src']].copy()
src_df['img'] = src_df.apply(f,axis=1)

def transform(tdf):
    tdf = tdf.set_index('name')
    tdf = tdf[['img']].transpose()
    return tdf

app.layout = html.Div(children=[
    html.Header([
        html.Div(children=[
            html.Img(src='/assets/espeon_logo.png',className='esp_logo'),
            html.P('COMPAREON',className='logo'),
            html.Img(src='/assets/umbreon_logo.png',className='umbr_logo')
        ])
    ]),
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=names,
            multi=True,
            style={'background':'#111111','border':'none'}
        )
    ]),
    html.Div(className='content',children=[
        dash_table.DataTable(
            id='table',
            style_header = {'display':'none'},
            css=[{'selector': 'table', 'rule': 'table-layout: fixed'}],
            style_cell = {'background':'#111111','border':'none'},
        ),
        dcc.Graph(id='bar'),
        dcc.Graph(id='total_bar')
    ]),
    html.Footer('Anurag')
],style={'background':'#cece8a'})

@app.callback(Output('bar','figure'),Output('total_bar','figure'),Output('table','data'),Output('table','columns'),
              Input('dropdown','value'))
def update_graph(dropdown_value):
    if dropdown_value is None or len(dropdown_value)==0:
        axdf = adf[adf['name'].isin(mons)]
        bydf = bdf[bdf['name'].isin(mons)]
        cdf = src_df[src_df['name'].isin(mons)]
    elif type(dropdown_value) is str:
        axdf = adf[adf['name'] == dropdown_value]
        bydf = bdf[bdf['name'] == dropdown_value]
        cdf = src_df[src_df['name'] == dropdown_value]
    else:
        axdf = adf[adf['name'].isin(dropdown_value)]
        bydf = bdf[bdf['name'].isin(dropdown_value)]
        cdf = src_df[src_df['name'].isin(dropdown_value)]

    afig = px.bar(
        axdf,
        y='stat',
        x='value',
        color='value',
        color_continuous_scale=[[0,'red'],[0.35,'yellow'],[0.55,'lime'],[1,'cyan']],
        range_color=[40,200],
        facet_col='name',
        template='plotly_dark',
        text='value'
    )
    for a in afig.layout.annotations:
        a.text = a.text.split("=")[1]
    afig.update(layout_coloraxis_showscale=False,layout_margin=dict(b=0))
    afig.update_xaxes(visible=False)
    afig.update_yaxes(title='')
    afig.update_traces(textfont_color='black')
    
    bfig = px.bar(
        bydf,
        y='BST',
        x='value',
        color='value',
        color_continuous_scale=[[0,'red'],[0.3,'yellow'],[0.7,'lime'],[1,'cyan']],
        range_color=[300,720],
        facet_col='name',
        template='plotly_dark',
        height=70,
        text='value'
    )
    for a in bfig.layout.annotations:
        a.text = ('')
    bfig.update(layout_coloraxis_showscale=False,layout_margin=dict(t=0,b=10))
    bfig.update_xaxes(visible=False)
    bfig.update_yaxes(title='')
    bfig.update_traces(textfont_color='black')
    
    data = transform(cdf).to_dict('records')
    columns = [dict(name=i,id=i,presentation='markdown') for i in transform(cdf).columns]
    
    return afig,bfig,data,columns
    

if __name__ == '__main__':
    app.run_server(debug=True)