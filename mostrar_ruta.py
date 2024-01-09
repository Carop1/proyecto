import json

def mostrarRuta():
    
    try:
        with open("lista_rutas.json", 'r') as ruta:
            rutas = json.load(ruta)
    except FileNotFoundError:
        rutas = []        

    print(rutas['nombre ruta'== 'Java 1'])