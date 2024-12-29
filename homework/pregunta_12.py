"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from collections import defaultdict

def pregunta_12():
    diccionario = defaultdict(int)

    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        for fila in lector_csv:
            for valor in fila[4].split(","):
                clave, numero = valor.split(":")
                diccionario[fila[0]] += int(numero)

    return dict(sorted(diccionario.items()))

