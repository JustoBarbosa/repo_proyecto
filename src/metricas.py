def calcular_tiempo_total(datos):
    '''
    Esta funcion va a tomar los datos relacionados al tiempo de uso de cada participante\
    en base a esto va a ser una suma total del tiempo que la usan todos los participantes del archivo enviado.
    
    Parametrs:
        datos: Lista. De esta lista se obtienen los valores asociados a la clave tiempo de uso.
        En base a estos datos se calcula el total.
        
    Return:
        total: int. Se devuelve el tiempo total de uso. 
    '''

    total = 0
    
    for participantes in datos:
        for tiempo in participantes["tiempo_uso"]:
            total = total + tiempo
    
    return total

def calcular_promedio_uso(datos):
    '''
    Esta funcion va a calcular el promedio de la cantidad de uso de cada app.\
    Se va a calcular la cantidad de registros y cuanto tiempo usa cada participante\
    para determinar el promedio.
    
    Parameters:
        datos: lista. Sobre los valores relacionados a la cantidad_uso se va a calcular cantidad total y\
        cantidad de registros asi se obtiene el promedio.
        
    Returns:
        total_uso/total_registros: es el promedio.
    '''
    
    total_uso = 0
    total_registros = 0
    
    for participante in datos:
        for cantidad in participante["cantidad_uso"]:
            total_uso += cantidad
            total_registros += 1
            
    if total_registros == 0:
        return 0.0
    
    return total_uso / total_registros

def calcular_uso_por_app(datos):
    '''
    Esta funcion va a ingresar a la lista para tomar los datos de la app y la cantidad de uso\
    y va a agregar en un diccionarion aparte los datos de las aplicaciones y la cantidad de uso de cada una.
    
    Parameters:
        datos: Lista. En base a estos datos se calcula la cantidad de uso de cada app.
        
    Returns:
        uso_por_app: diccionario. Este diccionario guarda como clave a la aplicacion y como valor la cantidad de uso de la misma.
    '''
    uso_por_app = {}
    
    for participante in datos:
        for i in range(len(participante["app"])):
            app = participante["app"][i]
            tiempo = participante["cantidad_uso"][i]
            if app not in uso_por_app:
                uso_por_app[app] = 0
            uso_por_app[app] += tiempo
    
    return uso_por_app
            