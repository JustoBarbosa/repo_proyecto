import pandas as pd
import os


def cargar_datos(ruta):
    
    '''
    Carga un archivo CSV y lo retorna como un DataFrame de pandas
   
    Parameters:
        ruta (str): ruta al archivo CSV con los datos sobre los cuales se van a calcular las mediciones en posteriores funciones.
        
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