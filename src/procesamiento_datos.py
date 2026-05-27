def filtrar_por_participante (df, id_participante): 
  
    """
    Recibe un DataFrame y lo filtra para obtener todos los registros de un participante especifico. 
    
    Parametros:
        
        df: DataFrame con los datos de uso. Debe contener la columna id_participante
        id_participante(int): es el numero de identificacion del participante del que se quieren saber los datos
        
    Retorna: 
        
        DataFrame: DataFrame con todas las filas correspondientes al participante indicado.
    
    Raises: 
        ValueError: si el id ingresado no existe en el DataFrame
    """
   
    participante = df[df["id_participante"] == id_participante]
    
    if participante.empty:
        raise ValueError(f"El id ingresado ({id_participante}) no existe")
    return participante         
    

