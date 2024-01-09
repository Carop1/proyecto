import json

def registrar_estu():
    
    estu_id = input("Número de identificación: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    acudiente = input("Acudiente: ")
    celular = input("Teléfono celular: ")
    fijo = input("Teléfono fijo: ")
    estado = input("Inscrito o no inscrito: ")

    estudiante_info = {
        
        "id": estu_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "celular": celular,
        "fijo": fijo,
        "estado": estado,
        "estado2": None,
        "nota_teo": None,
        "nota_prac": None,
        "entrenador": None,
        "ruta asignada": None,
        "fecha inicio": None,
        "fecha finalizacion": None,
        "salon": None,
        "preuba_prac": None,
        "prueba_teo": None,
        "resto trabajos": None,
        "nota modulo":None,
        "aprobar modulo": None
    }

    try:
        with open("estudiantes.json", 'r') as archivo:
            dato = json.load(archivo)
    except FileNotFoundError:
        dato = []

    dato.append(estudiante_info)

    with open("estudiantes.json", 'w') as archivo:
        json.dump(dato, archivo, indent=2)

    print("Estudiante registrado exitosamente.")