import json

def reportes():
    entrenadores = []
    try:
        with open("estudiantes.json",'r') as archivo:
            rutas_datos = json.load(archivo)
    except FileNotFoundError:
        rutas_datos = []

    print("REPORTES")
    print("A contunuacion aparecera un menu para que pueda escoger el reporte que desee: ")
    print("1. LISTADO CAMPERS EN ESTADO INSCRITO\n2. LISTADO CAMPERS QUE APROBARON EL EXAMEN INICIAL\n3. LISTADO ENTRENADORES QUE SE ENCUENTRAN TRABAJANDO EN CAMPUSLANDS\n4. LISTADO CAMPERS CON BAJO RENDIMIENTO\n5. LISTADO CAMPERS Y ENTRENADOR ASOCIADOS A UNA RUTA DE ENTRENAMIENTO\n6. NUMERO CAMPERS QUE PERDIERON Y APROBARON\n:)")
    print("LISTADO CAMPERS EN ESTADO INSCRITO")
    k =int(input(""))
    if(k == 1):
        for suba in rutas_datos:
            if suba["estado"] == "inscrito":
                print(f"El estudiante: {suba['nombre']} {suba['apellidos']} tiene el estado de inscrito")
    
    if(k == 2):
        print("")
        print("LISTADO CAMPERS QUE APROBARON EL EXAMEN INICIAL")
        for suba in rutas_datos:
            if suba["estado2"] == "aprobado":
                print(f"El estudiante: {suba['nombre']} {suba['apellidos']} desaprobó el examen inicial")
    
    if(k == 3):
        print("")
        print("LISTADO ENTRENADORES QUE SE ENCUENTRAN TRABAJANDO EN CAMPUSLANDS")
        for suba in rutas_datos:
            entrenadores.append(suba["entrenador"])
        print(f"Los entrenadores son: {entrenadores}")
    
    if(k == 4):
        print("")
        print("LISTADO CAMPERS CON BAJO RENDIMIENTO")
        for suba in rutas_datos:
            if suba["aprobar modulo"] == "desaprobado":
                print(f"El estudiante: {suba['nombre']} {suba['apellidos']} tiene bajo rendimiento")
        
    print("")
    print("LISTADO CAMPERS Y ENTRENADOR ASOCIADOS A UNA RUTA DE ENTRENAMIENTO")
    if(k == 5):
        for suba in rutas_datos:
            if suba["ruta asignada"] == "java":
                print(f"El estudiante: {suba['nombre']} {suba['apellidos']} y el entrenador {suba['entrenador']} estan asociados a la ruta de aprendizaje Java")
        
        for suba in rutas_datos:
            if suba["ruta asignada"] == "nodeJS":
                print(f"El estudiante: {suba['nombre']} {suba['apellidos']} y el entrenador {suba['entrenador']} estan asociados a la ruta de aprendizaje NodeJS")
        
        for suba in rutas_datos:
            if suba["ruta asignada"] == "netcore":
                print(f"El estudiante: {suba['nombre']} {suba['apellidos']} y el entrenador {suba['entrenador']} estan asociados a la ruta de aprendizaje NetCore")
        
    print("")
    print("NUMERO CAMPERS QUE PERDIERON Y APROBARON")
    if(k == 6):
        for suba in rutas_datos:
            if suba["ruta asignada"] == "java" and suba["entrenador"] == "miguel":
                if suba["aprobar modulo"] == "aprobado":
                    cont_apro_java= cont_apro_java +1 
                if suba["aprobar modulo"] == "reprobado":
                    cont_repro_java = cont_repro_java +1
                    
            if suba["ruta asignada"] == "java" and suba["entrenador"] == "jose":
                if suba["aprobar modulo"] == "aprobado":
                    cont_apro_java2 = cont_apro_java2 +1 
                if suba["aprobar modulo"] == "reprobado":
                    cont_repro_java2 = cont_repro_java2 +1 
                    
            if suba["ruta asignada"] == "nodejs" and suba["entrenador"] == "miguel":
                    if suba["aprobar modulo"] == "aprobado":
                        cont_apro_nodejs= cont_apro_nodejs +1 
                    if suba["aprobar modulo"] == "reprobado":
                        cont_repro_nodejs = cont_repro_nodejs +1
                        
            if suba["ruta asignada"] == "nodejs" and suba["entrenador"] == "jose":
                if suba["aprobar modulo"] == "aprobado":
                    cont_apro_nodejs2 = cont_apro_nodejs2 +1 
                if suba["aprobar modulo"] == "reprobado":
                    cont_repro_nodejs2 = cont_repro_nodejs2 +1
            
            if suba["ruta asignada"] == "netcore" and suba["entrenador"] == "miguel":
                    if suba["aprobar modulo"] == "aprobado":
                        cont_apro_netcore= cont_apro_netcore +1 
                    if suba["aprobar modulo"] == "reprobado":
                        cont_repro_netcore = cont_repro_netcore +1
                        
            if suba["ruta asignada"] == "netcore" and suba["entrenador"] == "jose":
                if suba["aprobar modulo"] == "aprobado":
                    cont_apro_netcore2 = cont_apro_netcore2 +1 
                if suba["aprobar modulo"] == "reprobado":
                    cont_repro_netcore2 = cont_repro_netcore2 +1            
        
        print(f"El numero de estudiantes que aprobaron el modulo con la ruta de entrenamiento Java y entrenador Miguel son: {cont_apro_java}")
        print(f"El numero de estudiantes que perdieron el modulo con la ruta de entrenamiento Java y entrenador Miguel son: {cont_repro_java}")
        print("")
        print(f"El numero de estudiantes que aprobaron el modulo con la ruta de entrenamiento Java y entrenador Jose son: {cont_apro_java2}")
        print(f"El numero de estudiantes que perdieron el modulo con la ruta de entrenamiento Java y entrenador Jose son: {cont_repro_java2}")
        print("")
        print(f"El numero de estudiantes que aprobaron el modulo con la ruta de entrenamiento Nodejs y entrenador Miguel son: {cont_apro_nodejs}")
        print(f"El numero de estudiantes que perdieron el modulo con la ruta de entrenamiento Nodejs y entrenador Miguel son: {cont_repro_nodejs}")
        print("")
        print(f"El numero de estudiantes que aprobaron el modulo con la ruta de entrenamiento Nodejs y entrenador Jose son: {cont_apro_nodejs2}")
        print(f"El numero de estudiantes que perdieron el modulo con la ruta de entrenamiento Nodejs y entrenador Jose son: {cont_repro_nodejs2}")
        print("")
        print(f"El numero de estudiantes que aprobaron el modulo con la ruta de entrenamiento NetCore y entrenador Miguel son: {cont_apro_netcore}")
        print(f"El numero de estudiantes que perdieron el modulo con la ruta de entrenamiento NetCore y entrenador Miguel son: {cont_repro_netcore}")
        print("")
        print(f"El numero de estudiantes que aprobaron el modulo con la ruta de entrenamiento NetCore y entrenador Jose son: {cont_apro_netcore2}")
        print(f"El numero de estudiantes que perdieron el modulo con la ruta de entrenamiento NetCore y entrenador Jose son: {cont_repro_netcore2}") 