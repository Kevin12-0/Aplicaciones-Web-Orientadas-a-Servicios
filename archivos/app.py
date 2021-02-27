import json
import web
urls = ('/action?', 'Action')
app = web.application(urls, globals())
ruta = "/home/runner/Aplicaciones-Web-Orientadas-a-Servicios/archivos/static/datos.json"
data_file={}
class Action:
    def GET(self):
            try:#
                parameters = web.input()
                action = parameters["action"]
                if action == "get": # 
                    with open(ruta) as contenido:
                        data_file = json.load(contenido)
                    return data_file
                if action == "agregar":
                    name = parameters.name
                    date = parameters.date
                    year = int(parameters.year)
                    cal = 2021 - year
                    edad = {
                        "nombre": name,
                        "fecha_nacimiento": date,
                        "edad": cal
                    }
                    with open(ruta) as contenido:#######
                        data_file = json.load(contenido)
                        data_file["edades"].append(edad)
                        with open(ruta, "w") as contenido:
                            json.dump(data_file,contenido)
                            return "Resgistro Correcto"
            except:
                return "Error"
if __name__=='__main__':
    app.run()