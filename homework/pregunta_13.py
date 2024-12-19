"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13(input_directory_1 = 'files/input/tbl0.tsv',
                input_directory_2 = 'files/input/tbl2.tsv'):
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    import pandas as pd

    tbl_0 = pd.read_csv(input_directory_1, sep='\t')
    tbl_2 = pd.read_csv(input_directory_2, sep='\t')

    tbl_merged = pd.merge(tbl_0, tbl_2, left_on='c0', right_on='c0')
    tbl_merged = tbl_merged.groupby('c1')['c5b'].sum()
    
    return tbl_merged


