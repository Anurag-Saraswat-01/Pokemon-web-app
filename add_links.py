import pandas as pd


def get_png(mons):
    sources = []
    for name in mons:
        name = name.lower()
        if name.split()[0] in ['aegislash', 'zacian', 'zamazenta', 'zygarde', 'wormadam', 'wishiwashi', 'lycanroc', 'morpeko', 'eternatus',
                               'gourgeist', 'pumpkaboo', 'indeedee', 'meowstic', 'toxtricity', 'urshifu', 'giratina', 'deoxys', 'shaymin',
                               'basculin', 'castform', 'darmanitan', 'eiscue', 'hoopa', 'landorus', 'thundurus', 'tornadus', 'meloetta']:
            temp = name.split()
            if name.split()[0] == 'zygarde' and '%' in temp[1]:
                temp[1] = temp[1].split('%')[0]
            if len(temp) == 4:
                x = temp[0] + '-' + temp[1] + '-' + temp[2] + '.png'
            elif name == 'castform' or name == 'eternatus':
                x = name + '.png'
            else:
                x = temp[0] + '-' + temp[1] + '.png'
        elif name.split('.')[0] in ['jr', 'mr', 'galarian mr']:
            if name == 'mime jr.':
                x = 'mime-jr.png'
            elif name == 'mr. mime':
                x = 'mr-mime.png'
            elif name == 'galarian mr. mime':
                x = 'mr-mime-galarian.png'
            else:
                x = 'mr-rime.png'
        elif name.split()[0] in ['mega', 'galarian', 'alolan', 'primal', 'black', 'white', 'ultra'] or name.split('-')[0] == 'ash':
            if name.split('-')[0] == 'ash':
                temp = name.split('-')
            else:
                temp = name.split()
            if len(temp) == 3:
                x = temp[1] + '-' + temp[0] + '-' + temp[2] + '.png'
            elif len(temp) == 1:
                x = name + '.png'
            else:
                x = temp[1] + '-' + temp[0] + '.png'
        elif 'necrozma' in name.split():
            if name.split()[0] == 'dusk':
                x = 'necrozma-dusk-mane.png'
            elif name.split()[0] == 'dawn':
                x = 'necrozma-dawn-wings.png'
            else:
                x = 'necrozma.png'
        elif 'calyrex' in name.split():
            if name.split()[0] == 'ice':
                x = 'calyrex-ice-rider.png'
            elif name.split()[0] == 'shadow':
                x = 'calyrex-shadow-rider.png'
            else:
                x = 'calyrex.png'
        elif name.split()[0] == 'partner':
            temp = name.split()
            x = temp[1] + '-lets-go.png'
        elif name == 'nidoran♀':
            x = 'nidoran-f.png'
        elif name == 'nidoran♂':
            x = 'nidoran-m.png'
        elif name == 'flabébé':
            x = 'flabebe.png'
        else:
            x = name + '.png'
        sources.append(x)
    return sources


if __name__ == '__main__':
    df = pd.read_csv("pokedex.csv")
    df['src'] = get_png(df['name'])
    # print(df[df['name'] == 'Ultra Necrozma'])
    df.to_csv("pokedex_with_src.csv")
