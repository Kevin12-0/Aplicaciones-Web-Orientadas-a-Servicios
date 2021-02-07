import web
import requests
import json

render = web.template.render("pokeapi/")
class Index():
  def GET(self):
    datos=None
    return render.index(datos)

def POST(self):
    form=web.input()
    poke_name=form.poke_name
    resultado = requests.get("https://pokeapi.co/api/v2/pokemon/"+poke_name)
    pokemon = resultado.json()
    type_p = pokemon["types"]
    types = type_p[0]
    type_0=types["type"]
    type_name = type_0["name"]
    ability = pokemon["abilities"]
    abilities = ability[0]
    ability_0 = abilities["ability"]
    ability_name = ability_0 ["name"]
    species = pokemon["species"]
    url = species["url"]
    link ="<a target='blank' href='"+url+"'>"+poke_name+"</a>"
    datos={
      "nombre_pokemon":"Nombre del Pokemon: "+poke_name,
      "tipo_pokempon":"Tipo de Pokemon: "+type_name,
      "abilidad":"abilidad especial: "+ability_name,
      "url":"Link de informacion: "+link
    }
    return render.index(datos)