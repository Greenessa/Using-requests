import requests
url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
#print(resp.status_code)
super_heroes = resp.json()
dict_final = {}
# print(super_heroes)
for hero in super_heroes:
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        str = hero['name']
        #print(str)
        dict_final[str] = hero['powerstats']['intelligence']
        #print(dict_final)
result = sorted(dict_final.values(), reverse = True)
#print(result)
clever = result[0]
#print(clever)
for hero, int in dict_final.items():
    if int == clever:
        print(f'Самый умный из трех супергероев- Hulk, Captain America, Thanos: {hero}')