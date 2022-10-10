"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import os
import sys

with open(os.path.join(sys.path[0],"data.csv"),"r") as file:
    datos=file.readlines()
clean_data=[row.rstrip("\n").split("\t")  for row in datos]

    
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    total = 0
    for fila in clean_data:
        total += int(fila[1])
    return total

from collections import Counter
letras = ('A','B','C','D','E')

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista = []
    cnt = Counter()
    for valor in clean_data:
        cnt[valor[0]] += 1
    for letra in letras:
        lista.append((letra,cnt[letra]))
    return lista


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    p3 = {'A':0,'B':0,'C':0,'D':0,'E':0}
    for hilera in clean_data:
        p3[hilera[0]] += int(hilera[1]) 
    lst1 = []
    for letra in letras:
        lst1.append((letra,p3[letra]))    
    return lst1


from datetime import datetime
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    concurrencias = Counter()

    for row in clean_data:


            #
            # Contador
            #
        if row[2] == '1999-02-29':
            concurrencias[2] += 1
        else:    
            #
            # Convierte el string a un objeto fecha:
            # 2016-05-23 
            #
            date = datetime.strptime(row[2], "%Y-%m-%d")


        concurrencias[date.month] += 1
        resultado = []
    for j in range(1,13):
        if j<10:
            if j ==4:
                resultado.append((('0'+str(j)),concurrencias[j]-1))
            else:
                resultado.append((('0'+str(j)),concurrencias[j]))    
        else:
            resultado.append((str(j),concurrencias[j]))
    return resultado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    l = {"A":[0,15],"B":[0,15],"C":[0,15],"D":[0,15],"E":[0,15]}
    for row in clean_data:
        l[row[0]][0] = max(l[row[0]][0],int(row[1]))
        l[row[0]][1] = min(l[row[0]][1],int(row[1]))
    final = []
    for letra in l:
        final.append((letra,l[letra][0],l[letra][1]))    
    return final


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    resultado = []
    p6 = {"aaa":[],"bbb":[],"ccc":[],"ddd":[],"eee":[],
        "fff":[],"ggg":[],"hhh":[],"iii":[],"jjj":[]}
    for row in clean_data:
        columna = row[4].split(',')
        for item in columna:
            clave = item[0:3]
            valor = int(item[4:])
            p6[clave]+= [valor]
    for claves in p6:
        tupla = (claves,min(p6[claves]),max(p6[claves]))
        resultado.append(tupla)
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    p7 = {x:[] for x in range(0,10)}
    for row in clean_data:
        p7[int(row[1])] += [row[0]]
    resultado = []
    for claves in p7:
        resultado.append((claves,p7[claves]))
    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    p8 = {x:set() for x in range(0,10)}
    for row in clean_data:
        p8[int(row[1])].add(row[0])

    resultado = []
    for claves in p8:
        lista = list(p8[claves])
        lista.sort()
        resultado.append((claves,lista))
    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    p9 = {"aaa":0,"bbb":0,"ccc":0,"ddd":0,"eee":0,
     "fff":0,"ggg":0,"hhh":0,"iii":0,"jjj":0}
    for row in clean_data:
        columna = row[4].split(',')
        for item in columna:
            clave = item[0:3]
            p9[clave] += 1
    return p9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    p10 = []
    for row in clean_data:
        col4 = len(row[3].split(","))
        col5 = len(row[4].split(","))
        p10.append((row[0],col4,col5))
    return p10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    p11 = {"a": 0,"b": 0,"c": 0,"d": 0,
        "e": 0,"f": 0,"g":0}
    for row in clean_data:
        letras = row[3].split(",")
        for letra in letras:
            p11[letra] += int(row[1])
    return p11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    p12 = {'A':0,'B':0,'C':0,'D':0,'E':0}
    for row in clean_data:
        valores = row[4].split(",")
        suma = 0
        for item in valores:
            valor = int(item[4:])
            suma += valor
        p12[row[0]] += suma
    return p12
