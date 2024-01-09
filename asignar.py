import json
import random

def asignarRuta():
    arreglo_apro = []
    conca_rutas = []
    union_total = []
    try:
        with open("estudiantes.json",'r') as archivo:
            rutas_datos = json.load(archivo)
    except FileNotFoundError:
        rutas_datos = []
    
    try:
        with open("lista_rutas.json",'r') as archivo2:
            rutas_datos2 = json.load(archivo2)
    except FileNotFoundError:
        rutas_datos2 = []    
            
    for suba in rutas_datos:
        if suba["estado"] == "Aprobado":
            arreglo_apro.append(suba["nombre"])
    #print(arreglo_apro)
    
    for suba2 in rutas_datos2:
        conca_rutas.append(suba2["nombre ruta"])
    
    for i in range(len(rutas_datos)):
        ruta_ran = random.choice(conca_rutas)
        union = [arreglo_apro[i],ruta_ran]
        union_total.append(union)
        print(union)
        