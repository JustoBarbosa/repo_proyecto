def calcular_tiempo_total(datos):
    
    total = 0
    
    for participantes in datos:
        for tiempo in participantes["tiempo_uso"]:
            total = total + tiempo
    
    return total

def calcular_promedio_uso(datos):
    
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
    
    uso_por_app = {}
    
    for participante in datos:
        for i in range(len(participante["app"])):
            app = participante["app"][i]
            tiempo = participante["cantidad_uso"][i]
            if app not in uso_por_app:
                uso_por_app[app] = 0
            uso_por_app[app] += tiempo
    
    return uso_por_app
            