"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    lista = []
    dic = {}

    with open("files/input/data.csv", 'r') as file:
        for line in file:
            columnas = line.strip().split(',')
            numero = columnas[0].split()
            lista.append(numero[0])
        for line in lista:
            print(line[0])
            letra = line[0]
            if letra in dic:
                dic[letra] += 1
            else:
                dic[letra] = 1

        result = sorted(dic.items())
    return result
