"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from collections import Counter

def pregunta_09():
    counter = Counter()

    with open('./files/input/data.csv', 'r') as file:
        for line in file:
            keys = [pair.split(':')[0] for pair in line.strip().split('\t')[4].split(',')]
            counter.update(keys)  # Actualiza los conteos directamente

    return dict(sorted(counter.items()))  # Ordena el diccionario por clave

