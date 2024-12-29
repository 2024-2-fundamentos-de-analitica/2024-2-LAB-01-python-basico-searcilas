"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict

def pregunta_11():
    counter = defaultdict(int)

    with open('./files/input/data.csv', 'r') as file:
        for line in file:
            number = int(line.split('\t')[1])
            for letter in line.split('\t')[3].split(','):
                counter[letter] += number

    return dict(sorted(counter.items()))

