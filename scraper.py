from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import Request, urlopen

# df = pd.read_csv("pokedex.csv")
url = 'https://pokemondb.net/pokedex/all'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
data = soup.find_all('span',class_='img-fixed icon-pkmn')
home_url = 'https://img.pokemondb.net/sprites/home/normal/'

for x in data:
    img_url = x['data-src']
    name = img_url.split('/')[-1]
    img_url_home = home_url+name
    try:
        f = open('home_images/'+name,'wb')
        f.write(requests.get(img_url_home).content)
        f.close()
    except:
        print(f'{name} not downloaded')
print('Download complete')
    