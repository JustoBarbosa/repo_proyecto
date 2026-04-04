from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
# from src.validacion_datos import....
#from src.procesamiento_datos import....
#lo de arriba es para que lo complete quien hizo esa funcion

ruta_datos = "datos/datos_proyecto.csv"

datos = cargar_datos(ruta_datos)

tiempo_total = calcular_tiempo_total(datos)
promedio = calcular_promedio_uso(datos)
uso_apps = calcular_uso_por_app(datos)

print("tiempo total de uso: ", tiempo_total)
print("promedio de uso: ", promedio)
print("Uso por app: ", uso_apps)

