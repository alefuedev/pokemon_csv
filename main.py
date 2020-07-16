import requests
import csv


pokemon = requests.get('https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json')

json = pokemon.json()
jsonArray = []

for dic in json:
    jsonArray.append(dic)


with open('pokemon.csv', mode='w') as file:
  writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(['English','Japanese','Chinese','French','Type','Attack'])
  for pokemon in jsonArray:
    kind = pokemon['type']
    kind = ' ,'.join(pokemon['type'])
    writer.writerow([pokemon['name']['english'], pokemon['name']['japanese'], pokemon['name']['chinese'], pokemon['name']['french'],kind,pokemon['base']['Attack']])


