"""
27. Crea una función que calcule el promedio de una lista de números.
"""

lista = [0,1,2,3,4,5,6,7,8,9,10]

def promedioNumeros(listaArray):
    return sum(listaArray)/len(listaArray)

promedioNumeros(lista)