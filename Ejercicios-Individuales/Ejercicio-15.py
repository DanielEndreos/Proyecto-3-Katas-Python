"""
15. Crea una función lambda que sume 3 a cada número de una lista dada.
"""

lista = [0,12,23,213,2442,23,2,23,13]
newLista = list(map(lambda numeros:numeros + 3,lista))

print(lista)
print(newLista)