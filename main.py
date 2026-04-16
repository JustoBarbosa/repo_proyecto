from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
import sys
#lo de arriba es para que lo complete quien hizo esa funcion

ruta_datos = r"datos/BehaviorTracker_mock_data.csv"
error1 = "datos/BehaviorTracker_mock_dataerror01.csv"
error2= "datos/BehaviorTracker_mock_dataerror02.csv"
error3 = "datos/BehaviorTracker_mock_dataerror03.csv"
error4= "datos/BehaviorTracker_mock_dataerror04.csv"
error6= "datos/BehaviorTracker_mock_dataerror06.csv"
error7= "datos/BehaviorTracker_mock_dataerror07.csv"
error8 = "datos/BehaviorTracker_mock_dataerror08.csv"
error9= "datos/BehaviorTracker_mock_dataerror09.csv"
error10 = "datos/BehaviorTracker_mock_dataerror10.csv"

#cargar datos desde el archivo
try:
    datos = cargar_datos(ruta_datos)
except FileNotFoundError:
    print("Archivo no encontrado, posible ruta incorrecta")
    sys.exit()

#filtrar datos validos 
try: 
    validar = validar_registro(datos)
except ValueError as e:
    print("Hay un error en los tipos de datos del registo", e)
    sys.exit()
else:
    print("Los datos son válidos")

#elegir el participante 
try: 
    id_buscado = int(input("ingrese el id del participante: "))
except ValueError:
        print("Error: debe ingresar un ID válido (un número)")

try: 
    participante = filtrar_por_participante (validar, id_buscado)
except ValueError as e: 
    print (e)
    sys.exit()


#calcular resultados 
try:
    tiempo_total = calcular_tiempo_total(participante)
    promedio = calcular_promedio_uso(participante)
    uso_apps = calcular_uso_por_app(participante)
except ValueError as e:
    print("error al calcular metricas: ", e)
    sys.exit()
else:
    print("tiempo total de uso: ", tiempo_total)
    print("promedio de uso: ", promedio)
    print("Uso por app: ", uso_apps)


