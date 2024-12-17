# este programa automatiza la llamada aleatoria a participar de los estudiantes y la valoración de su participación
def crear_lista_estudiantes(ubicacion_lista):
    """
    """
    import pandas as pd     
    grupo_df = pd.read_csv(ubicacion_lista) 
    # cuando el .csv file proviene de un .xlsx file, debe utilizarse sep = ';'
    lista_estudiantes = list(grupo_df.nombre.values)
    return lista_estudiantes

#llamar a lista o tomar registro de asistencia a clase
def llamar_estudiantes_a_participar():
    import numpy as np 
    from random import choice
    if len(lista_estudiantes) != 0:
        estudiante = choice(lista_estudiantes)
        lista_estudiantes.remove(estudiante)
        return print(estudiante)
    else:
        print('Todos los estudiantes han participado.\n \
               Muchas gracias y Felicitaciones')
