import json

def creacion_rutas():
    rta = "S"
    while (rta in ["S","s"]):
        nombre_ruta = input("Escriba el nombre de la nueva ruta: ")
        funda_pro = input("Escoja alguna de la siguientes opciones: Introducción a la algoritmia, PSeInt y Python: ")
        pro_web = input("Escoja alguna de la siguientes opciones: HTML, CSS y Bootstrap: )")
        pro_formal = input("Escoja alguna de la siguientes opciones: Java, JavaScript, C#: ")
        bases_datos_prin = input("Escoja alguna de la siguientes opciones(SGDB principal): Mysql, MongoDb y Postgresql: ") 
        bases_datos_sec = input("Escoja alguna de la siguientes opciones(SGDB secundaria): Mysql, MongoDb y Postgresql: ") 
        backend = input("Escoja alguna de la siguientes opciones: NetCore, Spring Boot, NodeJS y Express")
        
        ruta_nueva = {
            "nombre ruta": nombre_ruta,
            "fundamentos": funda_pro,
            "web": pro_web,
            "formal": pro_formal,
            "db principal": bases_datos_prin,
            "db secundaria": bases_datos_sec,
            "backend": backend
        }
    
        try:
            with open("lista_rutas.json",'r') as archivo:
                rutas_datos = json.load(archivo)
        except FileNotFoundError:
            rutas_datos = []

        rutas_datos.append(ruta_nueva)

        with open("lista_rutas.json",'w') as archivo:
            json.dump(rutas_datos, archivo, indent=4)

        print(f"La nueva ruta: '{nombre_ruta}' se creo exitosamente.")

        rta = input("Desea registrar otra ruta de entrenamiento? S(si) o N(no u otra letra):  ").upper()
        if (rta in ["S","s"]):
            rta = "S"
        else:
            rta = "N"
            