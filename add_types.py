import pandas as pd

dex_df = pd.read_csv("pokedex_with_src.csv")

def icon_markdown(type):
    return "![{0}]({0})".format(f'/assets/type_icons/{type}_Type_Icon.svg')

def add_icon(row):
    if row['type_number'] == 1:
        row['type_icon'] = icon_markdown(row['type_1'])
    else:
        row['type_icon'] = icon_markdown(row['type_1']) + ' ' + icon_markdown(row['type_2'])
    return row

dex_df = dex_df.apply(add_icon, axis=1)
dex_df.to_csv("pokedex_with_src_icon.csv")
