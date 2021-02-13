import web
import json
import requests
urls = ("/horoscopo/(.*)","Fecha")
app = web.application(urls,globals())
class Fecha:
    def GET(self,dia):
        try: 
            data = {}
            if str(dia) == "marzo-21" or dia == "marzo-22" or dia == "marzo-23" or dia == "marzo-24" or dia == "marzo-25" or dia == "marzo-26" or dia == "marzo-27" or dia == "marzo-28" or dia == "marzo-29" or dia == "marzo-30" or dia == "marzo-31": 
                data["result"]= "Signo: Aries"
                data["color"]="Color: Rojo carmin"
                data["frace"]="Debes mejorar en el amor y el trabajo"
            elif str(dia) == "abril-1" or dia == "abril-2" or dia == "abril-3" or dia == "abril-4" or dia == "abril-5" or dia == "abril-6" or dia == "abril-7" or dia == "abril-8" or dia == "abril-9" or dia == "abril-10" or dia == "abril-11" or dia == "abril-12" or dia == "abril-13" or dia == "abril-14" or dia == "abril-15" or dia == "abril-16" or dia == "abril-17" or dia == "abril-18" or dia == "abril-19":
                data["result"]="Signo: Aries"
                data["color"]="Color: Rojo brillante"
                data["frace"]="Sera un año de prosperidad y de dinero"
            elif str(dia) == "abril-20" or dia == "abril-21" or dia == "abril-22" or dia == "abril-23" or dia == "abril-24" or dia == "abril-25" or dia == "abril-26" or dia == "abril-27" or dia == "abril-28" or dia == "abril-29" or dia == "abril-29" or dia == "abril-30":
                data["result"]="Signo: Tauro"
                data["color"]="Color: Verde"
                data["frace"]="uno de sus negocios brillará con fuerza y recibirá la admiración"
            elif str(dia) == "mayo-1" or dia == "mayo-2" or dia == "mayo-3" or dia == "mayo-4" or dia == "mayo-5" or dia == "mayo-6" or dia == "mayo-6" or dia == "mayo-7" or dia == "mayo-8" or dia == "mayo-9" or dia=="mayo-10" or dia == "mayo-11" or dia == "mayo-13" or dia == "mayo-14" or dia == "mayo-15" or dia == "mayo-16" or dia == "mayo-17" or dia == "mayo-19" or dia == "mayo-20" or dia == "mayo-21" or dia == "mayo-21":
                data["result"]="Signo: Tauro"
                data["color"]="Color: Matiz"
                data["frace"]="con una bella persona surgirán afinidades que facilitarán una cita romántica"
            elif dia == "mayo-22" or dia == "mayo-23" or dia == "mayo-24" or dia == "mayo-25" or dia == "mayo-26" or dia == "mayp-27" or dia == "mayo-28" or dia == "mayo-29" or dia == "mayo-30" or dia == "mayo-30": 
                data["result"]="Signo: Geminis"
                data["color"]="Color: Amarillo "
                data["frace"]="Frace: oportunidad para llegar a más personas o cambiar de empleo"
            elif dia == "junio-1" or dia == "junio-2" or dia == "junio-3" or dia == "junio-4" or dia == "junio-5" or dia == "junio-6" or dia == "junio-7" or dia == "junio-8" or dia == "junio-9" or dia == "junio-10" or dia == "junio-11" or dia == "junio-12" or dia == "junio-13" or dia == "junio-14" or dia == "junio-15" or dia == "junio-16" or dia == "junio-17" or dia == "junio-18" or dia == "junio-19" or dia == "junio-20":  
                data["result"]="Signo: Geminis"
                data["color"]="Color: Dorado"
                data["frace"]="Frace: evite la dispersión y deje hablar a su corazón; se llevará una sorpresa."
            elif dia=="junio-21" or dia == "junio-22" or dia == "junio-23" or dia == "junio-24" or dia == "junio-25" or dia == "junio-26" or dia =="junio-27" or dia == "junio-28" or dia == "junio-29" or dia == "junio-30":
                data["result"]="Signo: Cancer"
                data["color"]="Color: Blanco"
                data["frace"]="Frace: llegará propuesta para cambiar de empleo pero conviene no precipitarse"
            elif dia == "julio-1" or dia=="julio-2" or dia == "julio-3" or dia == "julio-4" or dia == "julo-5" or dia == "julio-6" or dia =="julio-7" or dia == "julio-8" or dia == "julio-9" or dia == "julio-10" or dia=="julio-11" or dia == "julio-12" or dia=="julio-13" or dia == "julio-14" or dia=="julio-15" or dia == "julio-16" or dia=="julio-17" or dia == "julio-18" or dia=="julio-19" or dia == "julio-20" or dia=="julio-21" or dia == "julio-22": 
                data["result"]="Signo: Cancer"
                data["color"]="Color: Plata"
                data["frace"]="Frace: sentirá nostalgia por una relación del pasado"
            elif dia == "julio-22" or dia == "julio-23" or dia =="julio-24" or dia == "julio-25" or dia =="julio-26" or dia =="julio-27" or dia =="julio-28" or dia =="julio-29" or dia =="julio-30" or dia=="julio-31": 
                data["result"]="Signo: Leo"
                data["color"]="Color: Naranja"
                data["frace"]="Frace: le presentan propuestas desmesuradas o fantasiosas"
            elif dia == "agosto-1" or dia == "agosto-2" or dia == "agosto-3" or dia == "agosto-4" or dia == "agosto-5" or dia =="agosto-6" or dia =="agosto-7" or dia =="agosto-8" or dia =="agosto-9" or dia =="agosto-10" or dia =="agosto-11" or dia =="agosto-12" or dia =="agosto-13" or dia =="agosto-14" or dia =="agosto-15" or dia =="agosto-16" or dia == "agosto-17" or dia =="agosto-19" or dia == "agosto-20" or dia =="agosto-21" or dia =="agosto-22":  
                data["result"]="Signo: Leo"
                data["color"]="Color: Dorado"
                data["frace"]="Frace: las nuevas relaciones estarán favorecidas"
            elif dia =="agosto-23" or dia =="agosto-24" or dia =="agosto-25" or dia =="agosto-26" or dia =="agosto-27" or dia =="agosto-28" or dia =="agosto-29" or dia =="agosto-30" or dia =="agosto-31":  
                data["result"]="Signo: Virgo"
                data["color"]="Color: Blanco"
                data["frace"]="Frace: su habilidad facilitará ganancias inesperadas"
            elif dia == "septiembre-1" or dia == "septiembre-2" or dia == "septiembre-3" or dia == "septiembre-4" or dia =="septiembre-5" or dia == "septiembre-6" or dia == "septiembre-7" or dia =="septiembre-8" or dia == "septiembre-9" or dia == "septiembre-10" or dia =="septiembre-11" or dia == "septiembre-12" or dia == "septiembre-13" or dia =="septiembre-14" or dia == "septiembre-15" or dia == "septiembre-16" or dia =="septiembre-17" or dia =="septiembre-18" or dia == "septiembre-19" or dia == "septiembre-20" or dia == "septiembre-21" or dia =="septiembre-22": 
                data["result"]="Signo: Virgo"
                data["color"]="Color: Violeta"
                data["frace"]="Frace: las discusiones provocarán altercados en la pareja"
            elif dia == "septiembre-23" or dia =="septiembre-24" or dia =="septiembre-25" or dia =="septiembre-26" or dia =="septiembre-27" or dia =="septiembre-28" or dia =="septiembre-29" or dia =="septiembre-30":  
                data["result"]="Signo: Libra"
                data["color"]="Color: Rosa"
                data["frace"]="Frace: si invierte más energía en sus futuros planes"
            elif dia=="octubre-1" or dia=="octubre-2" or dia == "octubre-3" or dia == "octubre-4" or dia == "octubre-5" or dia == "octubre-6" or dia == "octubre-7" or dia =="octubre-8" or dia =="octubre-9" or dia == "octubre-10" or dia =="octubre-11" or dia == "octubre-12" or dia == "octubre-13" or dia =="octubre-14" or dia == "octubre-15" or dia == "octubre-16" or dia == "octubre-17" or dia =="octubre-18" or dia== "octubre-19" or dia == "octubre-20" or dia == "octubre-21" or dia == "octubre-22":  
                data["result"]="Signo: Libra"
                data["color"]="Color: Azul"
                data["frace"]="Frace:  querrá enmendar un olvido con una cita a un lugar deslumbrante pero no será fácil"
            elif dia == "octubre-23" or dia == "octubre-24" or dia == "octubre-25" or dia == "octubre-26" or dia=="octubre-27" or dia=="octubre-28" or dia =="octubre-29" or dia =="octubre-30" or dia =="octubre-31": 
                data["result"]="Signo: Escorpio"
                data["color"]="Color: Rojo"
                data["frace"]="Frace: tendrá indecisión frente a varias opciones; cuando elija, acertará"
            elif dia =="noviembre-1" or dia == "noviembre-2" or dia == "noviembre-3" or dia == "noviembre-4" or dia == "noviembre-5" or dia == "noviembre-6" or dia == "noviembre-7" or dia =="noviembre-8" or dia=="noviembre-9" or dia == "noviembre-10" or dia =="noviembre-11" or dia == "noviembre-12" or dia == "noviembre-13" or dia =="noviembre-14" or dia == "noviembre-15" or dia == "noviembre-16" or dia == "noviembre-17" or dia =="noviembre-18" or dia == "noviembre-19" or dia == "noviembre-20" or dia == "noviembre-21": 
                data["result"]="Signo: Escorpio"
                data["color"]="Color: Negro"
                data["frace"]="Frace: si deja hablar a su corazón y acepta sus errores; la armonía volverá y unirá la pareja."
            elif dia=="novimbre-23" or dia=="novimbre-24" or dia =="novimbre-25" or dia =="novimbre-26" or dia =="novimbre-27" or dia =="novimbre-28" or dia =="novimbre-29" or dia =="novimbre-30":  
                data["result"]="Signo: Sagitario"
                data["color"]="Color: Blanco"
                data["frace"]="Frace: con renovado vigor inicia negocio prometedor"
            elif dia == "diciembre-1" or dia == "diciembre-2" or dia == "diciembre-3" or dia == "diciembre-4" or dia == "diciembre-5" or dia == "diciembre-6" or dia == "diciembre-7" or dia =="diciembre-8" or dia =="diciembre-9" or dia == "diciembre-10" or dia == "diciembre-11" or dia == "diciembre-13" or dia == "diciembre-14" or dia == "diciembre-15" or dia == "diciembre-16" or dia == "diciembre-17" or dia == "diciembre-18" or dia == "diciembre-19" or dia == "diciembre-20" or dia =="diciembre-21":  
                data["result"]="Signo: Sagitario"
                data["color"]="Color: Azul"
                data["frace"]="Frace: gran momento, la seducción convertirá la intimidad en un paraíso para la pareja."
            elif dia == "diciembre-22" or dia == "diciembre-23" or dia =="diciembre-24" or dia == "diciembre-25" or dia == "diciembre-26" or dia =="diciembre-27" or dia =="diciembre-28" or dia =="diciembre-29" or dia =="diciembre-30" or dia =="diciembre-31":
                data["result"]="Signo: Capricorno"
                data["color"]="Color: Marron"
                data["frace"]="Frace: el panorama se presenta muy cambiante pero positivo para obtener logros."
            elif dia == "enero-1" or dia == "enero-2" or dia == "enero-3" or dia == "enero-4" or dia =="enero-5" or dia == "enero-6" or dia == "enero-7" or dia =="enero-8" or dia =="enero-9" or dia == "enero-10" or dia =="enero-11" or dia =="enero-12" or dia == "enero-13" or dia =="enero-14" or dia == "enero-15" or dia == "enero-16" or dia == "enero-17" or dia =="enero-18" or dia == "enero-19":  
                data["result"]="Signo: Capricorno"
                data["color"]="Color: Negro"
                data["frace"]="Frace: sentirá atracción por un recién llegado"
            elif dia == "enero-20" or dia == "enero-21" or dia == "enero-22" or dia == "enero-23" or dia == "enero-24" or dia == "enero-25" or dia =="enero-26" or dia =="enero-27" or dia =="enero-28" or dia =="enero-29" or dia =="enero-30" or dia =="enero-31":
                data["result"]="Signo: Acuario"
                data["color"]="Color: Gris"
                data["frace"]="Frace:  una inversión exitosa le permite planificar su futuro con más seguridad"
            elif dia == "febrero-1" or dia == "febrero-2" or dia == "febrero-3" or dia == "febrero-4" or dia == "febrero-5" or dia == "febrero-6" or dia == "febrero-7" or dia =="febrero-8" or dia=="febrero-9" or dia == "febrero-10" or dia =="febrero-11" or dia == "febrero-12" or dia == "febrero-13" or dia =="febrero-14" or dia == "febrero-15" or dia == "febrero-16" or dia == "febrero-17" or dia =="febrero-18": 
                data["result"]="Signo: Acuario"
                data["color"]="Color: Azul"
                data["frace"]="Frace: el entendimiento irá más allá de las palabras"
            elif dia == "febrero-19" or dia =="febrero-20" or dia =="febrero-21" or dia =="febrero-22" or dia =="febrero-23" or dia =="febrero-24" or dia =="febrero-25" or dia =="febrero-26" or dia =="febrero-27" or dia =="febrero-28" or dia =="febrero-29":
                data["result"]="Signo: Pisis"
                data["color"]="Color: Azul"
                data["frace"]="Frace: hallará el camino favorable que despeja todas sus dudas"
            elif dia== "marzo-1" or dia== "marzo-2" or dia== "marzo-3" or dia== "marzo-4" or dia== "marzo-5" or dia=="marzo-6" or dia == "marzo-7" or dia== "marzo-8" or dia== "marzo-9" or dia== "marzo-10" or dia== "marzo-11" or dia == "marzo-12" or dia == "marzo-13" or dia=="marzo-14" or dia == "marzo-15" or dia == "marzo-16" or dia == "marzo-17" or dia == "marzo-18" or dia == "marzo-19" or dia == "marzo-20":  
                data["result"]="Signo: Pisis"
                data["color"]="Color: Morado"
                data["frace"]="Frace: honestos y fieles, y esperan lo mismo de sus parejas"
            result = json.dumps(data)
            return result
        except: 
            data = {}
            data["status"] = 400
            data["error"] = "no es una fecha o no es el formato"
            result = json.dumps(data)
            return result
if __name__ == "__main__":
    app.run()

