"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01(input_directory='files/input/tbl0.tsv'):
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    import pandas as pd

    tabla_0 = pd.read_csv(input_directory, sep='\t')
    cantidad = len(tabla_0)
    
    return cantidad