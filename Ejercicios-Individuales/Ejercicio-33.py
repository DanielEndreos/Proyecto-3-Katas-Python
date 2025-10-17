"""
33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""

listaA = [3, 8, 15, 22, 5, 11, 19, 27, 34, 40, 2, 9, 17, 23, 31, 38, 45, 49, 52, 60]
listaB = [7, 4, 12, 18, 25, 29, 33, 36, 41, 47, 1, 6, 13, 20, 28, 35, 42, 48, 53, 59]

sumaListas = list(map(lambda a,b: a+b,listaA,listaB))

print(sumaListas)