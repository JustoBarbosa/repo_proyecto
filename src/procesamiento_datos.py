def filtrar_por_participante (datos, id_participante): 
  
    """
    Recorre una lista con los datos de todos los participantes, donde cada participante es un diccionario. 
    Si el id del participante coincide con el id del parametro de la funcion, agrega a dicho participante a una lista y la devuelve.  
    
    Parametros:
        
        datos(lista): es una lista de diccionarios, donde cada diccionario son los datos de cada participante.
        id_participante(int): es el numero de identificacion del participante del que se quieren saber los datos
        
    Retorna: 
        
        participante(lista): una lista con los datos del participante seleccionado 
    """
   
    participante = []
    for participantes in datos: 
        if participantes["id_participante"] == id_participante: 
            participante.append(participantes)
    
    if len(participante)  == 0: 
         raise ValueError (f"El id ingresado ({id_participante}) no existe")
    else:
         return participante         
    

