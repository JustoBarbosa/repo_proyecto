def validar_registro(registro):
    '''
    la funcion valida que los datos ingresados sean correctos 
    Parameters
    ----------
    registro : diccionario
        es un diccionario que contiene los datos de las personas

    Returns
    -------
    registro : diccionario 
        devuelve un diccionario con los datos ya validados.

    '''
    while (registro != int or registro != float) and (registro <0):
        print ("tiene que ser un numero float o int positivo")
        registro= input("Ingrese registro ")
        continue
        return registro
      