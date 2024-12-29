"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv
from collections import defaultdict

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    letras = defaultdict(lambda: [float('-inf'), float('inf')])

    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        
        for fila in lector_csv:
            letra, valor = fila[0], int(fila[1])
            letras[letra][0] = max(letras[letra][0], valor) 
            letras[letra][1] = min(letras[letra][1], valor)  

    return sorted((letra, max_min[0], max_min[1]) for letra, max_min in letras.items())
