import json

def estudianteRiesgo():
    
    try:
        with open("estudiantes.json",'r') as archivo:
            rutas_datos = json.load(archivo)
    except FileNotFoundError:
        rutas_datos = []
        
    for suba in rutas_datos:
        if suba["aprobar modulo"] == "desaprobado":
            print(f"El estudiante: {suba['nombre']} {suba['apellidos']} desaprobó el modulo")
            