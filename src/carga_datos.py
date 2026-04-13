def parsear_linea(linea):

    '''
    Esta funcion se va a encargar de recibir datos extraidos de un archivo y los va a separar\
    en los datos de cada participante especificando por cada linea un id, una fecha, una app de\
    uso, su cantidad y tiempo.

    Parameters: 
        linea: str. Recibe una linea proveniente de un archivo con datos de los usos de cada usuario
    
    Return:
        id_participante, fecha, app, cantidad_uso, tiempo_uso: lista.
        Es una lista donde se dividieron los datos de cada participante en ese orden puntual para facilitar\
        la posterior medicion de los datos.
    '''    
    linea = linea.strip()
    campos = linea.split(",")
    
    try:
        id_participante = int(campos[0])
        fecha = campos[1]
        app = campos[2]
        cantidad_uso = int(campos[3])
        tiempo_uso = float(campos[4])
    except ValueError:
        raise ValueError("Error en la linea", linea)
        
    
    return [id_participante, fecha, app, cantidad_uso, tiempo_uso]

def cargar_datos(ruta):
    
    '''
    Esta funcion recibe un archivo, lo va a leer y va a utilizar la funcion parsear_linea para separar\
    los datos en lo que corresponde a cada participante. En base a esta lista va a separar los datos y \
    determinar si ya fueron agregados o no al diccionario de participantes. Si no fueron agregados clasifica\
    cada id, fecha, app, cantidad de uso y tiempo de uso en cada clave, siendo los datos el valor de las mismas. 
    Se devuelve una lista de los valores de ese diccionario.
    
    Parameters:
        ruta: archivo. Se ingresan los datos sobre los cuales se van a calcular las mediciones en posteriores funciones.
        
    Return:
        lista. Se devuelven los valores del diccionario creado a partir de la extraccion de datos.
    '''
    participantes = {}
    
    try:
        with open(ruta, "r") as archivo:
            
            for linea in archivo:

                campos = parsear_linea(linea)
            
                id_p = campos[0]
                fecha = campos[1]
                app = campos[2]
                cantidad = campos[3]
                tiempo = campos[4]
                
                if id_p not in participantes:
                    participantes[id_p] = {
                        "id_participante": id_p,
                        "fecha": [],
                        "app": [],
                        "cantidad_uso": [],
                        "tiempo_uso": []
                        }
                participantes[id_p]["fecha"].append(fecha)
                participantes[id_p]["app"].append(app)
                participantes[id_p]["cantidad_uso"].append(cantidad)
                participantes[id_p]["tiempo_uso"].append(tiempo)
    except FileNotFoundError:
        raise FileNotFoundError("No se encontro el archivo", ruta)
    else:
        return list(participantes.values())