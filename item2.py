import urllib.parse
import json
import requests

print("===================================================")
print("=-------------------------------------------------=")
print("=----------CALCULADOR-DE-RUTAS-MAPQUEST-----------=")
print("=-------------------------------------------------=")
print("===================================================")
print("")

urlbase = "https://www.mapquestapi.com/directions/v2/route?"
api = "5vn0o7Q9aAjdqTDOIYE0wSuAtXjujy6S"

while True:
    print("---- Calcular Ruta ----")
    print("======================================")
    origen = input("Ingrese una Ciudad de Origen (Chilena): ")
    print("======================================")
    destino = input("Ingrese una Ciudad de Destino (Chilena o Latinoamericana): ")

    consulta = urlbase + urllib.parse.urlencode({"key": api, "from": origen, "to": destino})

    print("")
    print("URL =====>  ", consulta)
    print("")

    data = requests.get(consulta).json()
    #print(json.dumps(data, indent=4))

    distancia_km = round(data["route"]["distance"] * 1.60934,1)

    duracion_seg = data["route"]["time"]

    horas = duracion_seg // 3600
    minutos = (duracion_seg % 3600) // 60
    segundos = duracion_seg % 60

    combustible_lts = round(distancia_km / 12,1)

    print("Resultados:")
    print("")
    print("1) La distancia desde", origen, "a", destino, "es:","=====>  ", distancia_km, "kilómetros")
    print("2) El tiempo de demora desde", origen, "a", destino, "es:", "=====>  ", int(horas), "horas,", int(minutos), "minutos y", int(segundos), "segundos")
    print("3) El combustible requerido para el viaje es de:", "=====>  ", combustible_lts, "litros")
    print("4) La narrativa del viaje es: ")
    print("")
    
    for leg in data["route"]["legs"]:
        for step in leg["maneuvers"]:
            print(step["narrative"])
            print("↘")

    otra_ruta_salir = input("¿Desea calcular otra ruta? Enter para continuar o Ingrese 'S' para salir, : ")
    if otra_ruta_salir.upper() == "S":
        print("Saliendo de MapQuest, vuelva pronto....")
        break
