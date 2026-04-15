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
        
        try:
            int(participante)
        except ValueError:
            raise ValueError (f'Error, el ID: {participante}, no es un numero valido')
        
        try: 
            int(cant_uso)
        except ValueError:
            raise ValueError (f'Error, la cantidad de uso {cant_uso}, no es un numero valido')
        
        try: 
            float(tiempo_uso)
        except ValueError:
            raise ValueError (f'Error, el tiempo de uso {tiempo_uso}, no es un numero valido')
            
        if fecha != str: 
                raise ValueError ("La fecha es incorrecta")
                
        if fecha != str: 
            raise ValueError ("La fecha es incorrecta")
                
    
    return registro
        
        
            
            
         
    
        
        
        
        
        
        
    while (registro != int or registro != float) and (registro <0):
        print ("tiene que ser un numero float o int positivo")
        registro= input("Ingrese registro ")
        continue
        return registro
      