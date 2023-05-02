
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# NASA Exoplanet URL
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

new_stars_data = []

page = requests.get(url)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')      

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    new_stars_data.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(new_stars_data)):
    Star_names.append(new_stars_data[i][0])
    Distance.append(new_stars_data[i][5])
    Mass.append(new_stars_data[i][7])
    Radius.append(new_stars_data[i][8])

df2 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius)),columns = ['star_name','distance','mass','radius'])
print(df2)
df2.to_csv('dwarf_stars.csv')