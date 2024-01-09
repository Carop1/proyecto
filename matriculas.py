import json

def gestorMatri():
    rta = "S"
    try:
        with open("estudiantes.json",'r') as archivo:
            rutas_datos = json.load(archivo)
    except FileNotFoundError:
        rutas_datos = []
        
    for suba in rutas_datos:
        while (rta in ["S","s"]):            
            if (suba["estado2"] == "aprobado") and suba["entrenador"] == None:
                suba["entrenador"] = input(f"Ingrese el nombre del entrenador para el estudiante: {suba['nombre']} {suba['apellidos']} ").lower()
                suba["ruta asignada"] = input(f"Ingrese la ruta para el estudiante:  {suba['nombre']} {suba['apellidos']} ").lower()
                suba["fecha inicio"] = input(f"Ingrese fecha de inicio para le estudiante:  {suba['nombre']} {suba['apellidos']} ")
                suba["fecha finalizacion"] = input(f"Ingrese fecha de finalizacion:  {suba['nombre']} {suba['apellidos']} ")
                suba["salon"] = input(f"Ingrese el salon de entrenamiento: {suba['nombre']} {suba['apellidos']} ")
            else:
                pass
            rta = input("Desea registrar otros datos de estudiantes? S(si) N(no u otra letra):  ").upper()
            if rta == "S":
                rta = "S"
            else:
                rta = "N"
            
    with open("estudiantes.json", 'w') as rwf:
        json.dump(rutas_datos, rwf, indent=4)
    #print(rutas_datos)