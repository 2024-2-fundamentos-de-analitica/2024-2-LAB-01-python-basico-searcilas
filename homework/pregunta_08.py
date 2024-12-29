"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    agrupados = {}

    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            letra, numero, *_ = linea.strip().split('\t')
            numero = int(numero)

            if numero not in agrupados:
                agrupados[numero] = []

            if letra not in agrupados[numero]:
                agrupados[numero].append(letra)
                agrupados[numero].sort()

    resultado = sorted(agrupados.items())
    return resultado

