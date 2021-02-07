import web
import requests
import json
resultado = requests.get("https://pokeapi.co/api/v2/pokemon/geodude")
print(resultado.status_code)
print(resultado.headers["Content-Type"])
pokemon = resultado.json()
#nombre
name = pokemon["name"]
print(name)
#especie
type = pokemon["types"]
types = type[0]
type_0=types["type"]
type_name = type_0["name"]
print(type_name)
#abilidad
ability = pokemon["abilities"]
abilities = ability[0]
ability_0 = abilities["ability"]
ability_name = ability_0 ["name"]
print(ability_name)
#url
species = pokemon["species"]
url = species["url"]
print(url)