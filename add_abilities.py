from numpy.core.numeric import NaN
import pandas as pd

dex_df = pd.read_csv("pokedex_with_src_icon.csv")


def add_ability(row):
    if row['ability_2'] is NaN:
        row['Ability'] = row['ability_1']
    else:
        row['Ability'] = row['ability_1'] + ' / ' + row['ability_2']
    if row['ability_hidden'] is NaN:
        row['Hidden Ability'] = '-'
    else:
        row['Hidden Ability'] = row['ability_hidden']
    return row


def add_src(row):
    row['Image'] = "![{0}]({0})".format('/assets/home_images/' + row["src"])
    return row


dex_df = dex_df.apply(add_ability, axis=1)
dex_df = dex_df.apply(add_src, axis=1)
# print(dex_df[['name', 'ability_1', 'ability_2', 'ability_hidden', 'Ability', 'Hidden Ability']])
required = ['pokedex_number', 'name', 'generation', 'status', 'species', 'total_points', 'hp', 'attack', 'defense',
            'sp_attack', 'sp_defense', 'speed', 'type_icon', 'Ability', 'Hidden Ability', 'Image']
required_df = dex_df[required].copy()
print(required_df)
required_df.to_csv('pokedex_markdown.csv', index=False)
