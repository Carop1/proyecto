import os
import registro_prueba as rp
import prueba2 as pb2
import entrenamiento as et
import asignar as asg
import matriculas as mt
import evaluaciones as eva
import riesgo as rg
import reportes as rep
import mostrar_ruta as mr

menu = "1. Registro de estudiantes\n2. Registro de prueba\n3. Creacion de rutas de entrenamiento\n4. Gestor de matriculas\n5. Evaluaciones\n6. Estudiantes en riesgo\n7. Reportes\n:)"
isActive = True
opMenu = 0

while (isActive) :
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
        os.system("pause")
     
    else:
        if (opMenu == 1):
            pb2.registrar_estu()
            print("")
        elif(opMenu==2):
            rp.registrarPrueba()
            print("")
        elif(opMenu==3):
            et.creacion_rutas()
            print("")
        elif(opMenu==4):
            mt.gestorMatri()
            print("")
        elif(opMenu==5):
            eva.evaluacion()
            print("")
        elif(opMenu==6):   
            rg.estudianteRiesgo()
            print("")
        elif(opMenu==7): 
            rep.reportes()
        elif(opMenu==8):
            mr.mostrarRuta()