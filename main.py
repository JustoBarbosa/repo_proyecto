from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from src.validacion_datos import validacion_datos
from src.procesamiento_datos import filtrar_por_participante
#lo de arriba es para que lo complete quien hizo esa funcion

ruta_datos = "datos/datos_proyecto.csv"

#cargar datos desde el archivo
datos = cargar_datos(ruta_datos)

#filtrar datos validos 

#elegir el participante 
while True: 
    id_buscado = input("ingrese el id del participante: ")
    
    if id_buscado.isdigit(): 
        id_buscado = int(id_buscado)
        break
    else:
        print("error, debe ingresar un ID válido")

participante = filtrar_por_participante (datos, id_buscado)



#calcular resultados 
tiempo_total = calcular_tiempo_total(participante)
promedio = calcular_promedio_uso(participante)
uso_apps = calcular_uso_por_app(participante)

print("tiempo total de uso: ", tiempo_total)
print("promedio de uso: ", promedio)
print("Uso por app: ", uso_apps)

