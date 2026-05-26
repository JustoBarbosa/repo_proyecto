import pandas as pd

def validar_registro(df):
    '''
    la funcion valida que los datos ingresados sean correctos 
    Parameters
    ----------
    registro : df
        es un dataframe que contiene los datos de las personas

    Returns
    -------
    registro : dataframe
        devuelve un lista con los datos ya validados.
    raises:
        ValueError: Si se detecta algun dato invalido

    '''
    if df.empty:
        raise ValueError("el DataFrame esta vacio")
        
    if df.isna().any().any():
        raise ValueError("Error: el archivo contiene campos vacios o valores nulos")
        
    if (df["id_participante"] <= 0).any():
        raise ValueError("Error: se encontraron IDs menores o iguales a 0.")
    
    if (df["cantidad_uso"] < 0).any():
        raise ValueError("Error: se encontraron valores negativos en cantidad_uso")
    
    if (df["tiempo_uso"] < 0).any():
        raise ValueError("Error: se encontraron valores negativos en tiempo_uso")
         
    
    
    return df
        
        
            
            
         
    
        
        
        
        
        
        
   
      