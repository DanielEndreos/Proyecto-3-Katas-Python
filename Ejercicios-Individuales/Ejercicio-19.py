"""
19. Crea una función lambda que filtre los números impares de una lista dada.
"""

lista = [0,1,2,3,4,5,6,7,8,9,10,11]
newLista = list(filter(lambda numero: numero%2 != 0, lista))

print(lista)
print(newLista)