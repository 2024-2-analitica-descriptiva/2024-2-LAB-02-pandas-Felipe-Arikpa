"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_02(input_directory='files/input/tbl0.tsv'):
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    import pandas as pd

    tabla_0 = pd.read_csv(input_directory, sep='\t')

    cantidad_columnas = len(tabla_0.columns)
    
    return cantidad_columnas