"""
4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
"""
listaA = [1, 4, 8, 12, 15, 22, 27, 31, 39, 45, 50, 58, 63, 70, 76, 82, 88, 94, 99, 103]
listaB = [10, 45, 123, 8, 99, 150, 3, 67, 21, 55, 32, 78, 91, 11, 175, 4, 500, 1, 63, 23]

def difListas(listaPrimera: list, listaSegunda: list) -> list:
    return list(map(lambda a, b: a - b , listaPrimera, listaSegunda))

diferValue = difListas(listaA, listaB)
print (diferValue)