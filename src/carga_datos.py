def parsear_linea(linea):
    
    linea = linea.strip()
    campos = linea.split(",")
    
    id_participante = int(campos[0])
    fecha = campos[1]
    app = campos[2]
    cantidad_uso = int(campos[3])
    tiempo_uso = float(campos[4])
    
    return [id_participante, fecha, app, cantidad_uso, tiempo_uso]

def cargar_datos(ruta):
    
    participantes = {}
    
    with open(ruta, "r") as archivo:
        primera_linea = True
        for linea in archivo:
            if primera_linea == True:
                primera_linea == False
                continue
            
            campos = parsear_linea(linea)
            
            id_p = campos[0]
            fecha = campos[1]
            app = campos[2]
            cantidad = campos[3]
            tiempo = campos[4]
            
            if id_p not in participantes:
                participantes[id_p] = {
                    "id_participante": id_p,
                    "fecha": fecha,
                    "app": app,
                    "cantidad_uso": cantidad,
                    "tiempo_uso": tiempo
                    }
            participantes[id_p]["fecha"].append(fecha)
            participantes[id_p]["app"].append(app)
            participantes[id_p]["cantidad_uso"].append(cantidad)
            participantes[id_p]["tiempo_uso"].append(tiempo)
            
        return list(participantes.values())