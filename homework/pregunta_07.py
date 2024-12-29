"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv
from collections import defaultdict

def pregunta_07():

    diccionario = defaultdict(list)

    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        
        for fila in lector_csv:
            valor, letra = int(fila[1]), fila[0]
            diccionario[valor].append(letra)  # Añadir letra al valor correspondiente

    return sorted(diccionario.items())  # Ordenar por clave (valores numéricos)

print(pregunta_07())