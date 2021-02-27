import json
class Datos():

    json_file = {}

    def read(self):
        try:
            with open("datos.json") as file:
                self.json_file = json.load(file)
            print(self.json_file)

        except Exception as error:
            print("Error {}".format(error.args[0]))

    def writePersonas(self, nombre, email):
        try:
            persona = {
                "nombre": nombre,
                "email": email
            }
            self.json_file["personas"].append(persona)
            with open("datos.json","w") as file:
                json.dump(self.json_file, file)
        except Exception as error:
            print("Error {}".format(error.args[0]))

    def writeDirecciones(self, direccion):
        try:
            direccion = {
                "direccion": direccion
            }
            self.json_file["direcciones"].append(direccion)
            with open("datos.json","w") as file:
                json.dump(self.json_file, file)
        except Exception as error:
            print("Error {}".format(error.args[0]))

objeto = Datos()
objeto.read()
objeto.writePersonas("ccc", "ccc@email")
objeto.writeDirecciones("colonia sur")