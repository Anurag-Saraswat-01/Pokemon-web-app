import pandas as pd
import plotly.express as px
import plotly.io as plt_io
import re

# df = pd.read_csv("pokedex.csv")
# required = ['name','total_points','hp','attack','defense','sp_attack','sp_defense','speed']
# sdf = df[required]
mons = ['Bulbasaur','Ivysaur','Venusaur','Mega Venusaur',
        'Charmander','Charmeleon','Charizard','Mega Charizard X','Mega Charizard Y',
        'Squirtle','Wartortle','Blastoise','Mega Blastoise',
        'Aegislash Blade Forme','Zacian Hero of Many Battles','Zamazenta Crowned Shield',
        'Alolan Raichu','Galarian Meowth',
        'Zygarde 10% Forme','Darmanitan Standard Mode','Darmanitan Galarian Zen Mode']
# # mons = ['Arceus','Dialga','Palkia','Giratina Altered Forme','Giratina Origin Forme']
# # mons = ['Shuckle','Blissey','Xurkitree','Arceus','Mew']
# # mons = ['Sunkern','Onix','Munchlax','Absol','Infernape','Garchomp','Mega Lucario','Mewtwo','Arceus','Mega Rayquaza']
# # eeveelutions = ['Eeevee','Vaporeon','Jolteon','Flareon','Umbreon','Espeon','Leafeon','Glaceon','Sylveon']
# # mons = eeveelutions
# mons = ['Elekid', 'Magby', 'Mime Jr.', 'Electabuzz', 'Magmar', 'Galarian Mr. Mime', 'Electivire', 'Magmortar', 'Mr. Rime']
# sdf = sdf[sdf['name'].isin(mons)]
# adf = pd.melt(sdf, id_vars='name',value_vars=['speed','sp_defense','sp_attack','defense','attack','hp'],var_name='stat')
# # print(sdf)
# fig = px.bar(
    # adf,
    # y='stat',
    # x='value',
    # color='value',
    # color_continuous_scale=[[0,'red'],[0.35,'yellow'],[0.55,'lime'],[1,'cyan']],
    # range_color=[40,200],
    # facet_col='name',
# )
# for a in fig.layout.annotations:
    # a.text = a.text.split("=")[1]
# fig.update(layout_coloraxis_showscale=False)
# fig.update_xaxes(visible=False)
# fig.update_yaxes(title='')
# fig.show()

# bdf = pd.melt(sdf, id_vars='name',value_vars='total_points',var_name='total_points')
# bfig = px.bar(
    # bdf,
    # y='total_points',
    # x='value',
    # color='value',
    # color_continuous_scale=[[0,'red'],[0.3,'yellow'],[0.7,'lime'],[1,'cyan']],
    # range_color=[300,720],
    # facet_col='name'
# )
# for a in bfig.layout.annotations:
    # a.text = a.text.split("=")[1]
# bfig.update(layout_coloraxis_showscale=False)
# bfig.update_xaxes(visible=False)
# bfig.update_yaxes(title='')
# bfig.show()

for name in mons:
    name = name.lower()
    if name.split()[0] in ['aegislash','zacian','zamazenta','zygarde','wormadam','wishiwashi','lycanroc','morpeko',
                            'gourgeist','pumpkaboo','indeedee','meowstic','toxtricity','urshifu','giratina','deoxys','shaymin',
                            'basculin','castform','darmanitan','eiscue','hoopa','landorus','thundurus','tornadus','meloetta']:
        temp = name.split()
        if '%' in temp[1]:
            temp[1] = temp[1].split('%')[0]
        if len(temp) == 4:
            x = temp[0] + '-' + temp[1] + '-' + temp[2] + '.png'
        else:
            x = temp[0] + '-' + temp[1] + '.png'
    elif name.split('.')[0] in ['jr','mr','galarian mr']:
        if name == 'mime jr.':
            x = 'mime-jr.png'
        elif name == 'mr. mime':
            x = 'mr-mime.png'
        elif name == 'galarian mr. mime':
            x = 'mr-mime-galarian.png'
        else:
            x = 'mr-rime.png'
    elif name.split()[0] in ['mega','galarian','alola','primal','kyurem'] :
        temp = name.split()
        if len(temp) == 3:
            x = temp[1] + '-' + temp[0] + '-' + temp[2] + '.png'
        elif len(temp) == 1:
            x = name + '.png'
        else:
            x = temp[1] + '-' + temp[0] + '.png'
    elif 'calyrex' in name.split():
        if name.split()[0] == 'ice':
            x = 'calyrex-ice-rider.png'
        elif name.split()[0] == 'shadow':
            x = 'calyrex-shadow-rider.png'
        else:
            x = 'calyrex.png'
    else:
        x = name + '.png'
    print(x)