"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_06():
    resultado = {}

    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")

        for linea in lector:
            valores = linea[4].split(",")
            for elemento in valores:
                clave, valor = elemento.split(":")
                valor = int(valor)

                if clave not in resultado:
                    resultado[clave] = [valor, valor]
                else:
                    resultado[clave][0] = min(resultado[clave][0], valor)
                    resultado[clave][1] = max(resultado[clave][1], valor)

    return sorted([(clave, limites[0], limites[1]) for clave, limites in resultado.items()])

print(pregunta_06())
