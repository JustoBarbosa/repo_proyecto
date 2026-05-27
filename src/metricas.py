def calcular_tiempo_total(df):
    '''
    Esta funcion va a tomar los datos relacionados al tiempo de uso de cada participante\
    en base a esto va a ser una suma total del tiempo que la usan todos los participantes del archivo enviado.
    
    Parametrs:
        df (Dataframe): De este dataframe se obtienen los valores asociados a la clave tiempo de uso.
        En base a estos datos se calcula el total.
        
    Return:
        Float: Suma total de la columna tiempo_uso 
    '''

    if (df["tiempo_uso"] < 0).any():
        raise ValueError("tiempo negativo encontrado")
    
    
    return df["tiempo_uso"].sum()

def calcular_promedio_uso(df):
    '''
    Calcula el promedio de la cantidad de uso de cada app.
    
    Parameters:
        df: Dataframe con los datos de uso. Debe contener la columna cantidad_uso
        
    Returns:
        float: promedio de la columna cantidad_uso
    '''
    
    if (df["cantidad_uso"] < 0).any():
        raise ValueError("cantidad de uso negativa encontrada")
    if df.empty:
        raise ValueError("No se puede calcular promedio: DataFrame vacio")
    
    return df["cantidad_uso"].mean()

def calcular_uso_por_app(df):
    '''
    Calcula la cantidad de uso agrupada por aplicacion.
    
    Parameters:
        df: DataFrame con los datos de uso. Debe contener la columna cantidad_uso y app.
        
    Returns:
        Serie: una serie con el nombre de cada app con la suma total de cantidad_uso de cada una
    '''
    if (df["cantidad_uso"]< 0).any():
        raise ValueError("Cantidad de uso negativa encontrada")
    
    return df.groupby("app")["cantidad_uso"].sum()
            