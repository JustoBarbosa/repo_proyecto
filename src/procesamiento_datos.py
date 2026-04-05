def filtrar_por_participante (datos, id_participante): 
   
    participante = []
    for participantes in datos: 
        if participantes["id_participante"] == id_participante: 
            participante.append(participantes)
            
    return participante 

