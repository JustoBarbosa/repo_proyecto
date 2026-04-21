def validar_registro(registro):
    '''
    la funcion valida que los datos ingresados sean correctos 
    Parameters
    ----------
    registro : lista
        es un lista que contiene los datos de las personas

    Returns
    -------
    registro : lista
        devuelve un lista con los datos ya validados.

    '''
    
     
    if len(registro) == 0 :
        raise ValueError("La lista de registros esta vacia")
    
    for i in registro: 
        participante = i["id_participante"] 
        fecha =i["fecha"]
        aplicacion = i ["app"]
        cant_uso = i ["cantidad_uso"]
        tiempo_uso = i ["tiempo_uso"]
        
        if participante <= 0:
            raise ValueError (f'Error, el ID: {participante}, no es un numero valido')
        
        for cantidad in cant_uso:
            try: 
                int(cantidad)
            except (ValueError, TypeError):
                raise ValueError (f'Error, la cantidad de uso {cant_uso}, no es un numero valido')
            if cantidad < 0:
                raise ValueError(f"cantidad de uso negativa {cantidad}")
            
            for tiempo in tiempo_uso:
                try: 
                    float(tiempo)
                except (ValueError, TypeError):
                    raise ValueError (f'Error, el tiempo de uso {tiempo_uso}, no es un numero valido')
                if tiempo < 0:
                    raise ValueError(f"Error tiempo de uso negativo {tiempo}")
        
        if not fecha:
            raise ValueError(f"Fecha vacia para participante {participante}")
                
    
    return registro
        
        
            
            
         
    
        
        
        
        
        
        
   
      