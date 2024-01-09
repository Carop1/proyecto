import json

def evaluacion():
    
    try:
        with open("estudiantes.json",'r') as archivo:
            rutas_datos = json.load(archivo)
    except FileNotFoundError:
        rutas_datos = []
        
    for suba in rutas_datos:
        if suba["estado"] == "Aprobado" and suba["prueba_teo"] == None:
            suba["prueba_teo"] = int(input(f"Ingrese la nota de la prueba teorica del estudiante {suba['nombre']} {suba['apellidos']}: "))
            suba["preuba_prac"] = int(input(f"Ingrese la nota de la prueba practica del estudiante {suba['nombre']} {suba['apellidos']}: "))
            suba["resto trabajos"] = int(input(f"Ingrese la nota del los demas trabajos {suba['nombre']} {suba['apellidos']}: "))
            suba["nota modulo"] = (suba["prueba_teo"]*0.3 + suba["resto trabajos"]*0.1 + (suba["preuba_prac"])*0.6)
            if suba["nota modulo"] >= 60:
                suba["aprobar modulo"] = "aprobado"
                
            else:
                suba["aprobar modulo"] = "desaprobado"
      
    with open("estudiantes.json",'w') as archivo2:
            json.dump(rutas_datos, archivo2, indent=2)