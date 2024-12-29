"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv

def pregunta_10():
    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        return [(fila[0], len(fila[3].split(",")), len(fila[4].split(","))) for fila in lector_csv]

