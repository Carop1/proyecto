import json
def registrarPrueba():
    try:
        with open("estudiantes.json", 'r') as rwf:
            dato = json.load(rwf)
    except FileNotFoundError:
        print("No hay estudiantes registrados.")
        return

    for estudiante in dato:
        if estudiante["estado"] == "inscrito":
            nota_teo = float(input(f"Ingrese la nota teórica para {estudiante['nombre']} {estudiante['apellidos']}: "))
            nota_prac = float(input(f"Ingrese la nota práctica para {estudiante['nombre']} {estudiante['apellidos']}: "))
            
            estudiante["nota_teo"] = nota_teo
            estudiante["nota_prac"] = nota_prac

            promedio = (nota_teo + nota_prac) / 2
            if promedio >= 60:
                print(f"{estudiante['nombre']} aprobó la prueba.")
                estudiante["estado2"] = "aprobado"
            else:
                print(f"{estudiante['nombre']} {estudiante['apellidos']} no aprobó la prueba.")

    with open("estudiantes.json", 'w') as rwf:
        json.dump(dato, rwf, indent=4)