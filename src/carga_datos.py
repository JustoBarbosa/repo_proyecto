import pandas as pd
import os


def cargar_datos(ruta):
    
    '''
    Esta funcion recibe un archivo, lo va a leer y va a utilizar la funcion parsear_linea para separar\
    los datos en lo que corresponde a cada participante. En base a esta lista va a separar los datos y \
    determinar si ya fueron agregados o no al diccionario de participantes. Si no fueron agregados clasifica\
    cada id, fecha, app, cantidad de uso y tiempo de uso en cada clave, siendo los datos el valor de las mismas. 
    Se devuelve una lista de los valores de ese diccionario. (pre)
    (post): Carga el arciho csv en un DataFrame de pandas. asigna los nombres de columnas correspondientes
    
    Parameters:
        ruta (str): archivo. Se ingresan los datos sobre los cuales se van a calcular las mediciones en posteriores funciones.
        
    Return:
        DataFrame: DataFrame con columnas id_participante, fecha, app, cantidad_uso, tiempo_uso
    Raises:
        Filenotfounderror: Si el archivo no existe en la ruta indicada
    '''
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"no se encotró el archivo en la ruta {ruta}")
    
    df = pd.read_csv(ruta, header = None,
                     names=["id_participante", "fecha", "app", "cantidad_uso", "tiempo_uso"])
    return df