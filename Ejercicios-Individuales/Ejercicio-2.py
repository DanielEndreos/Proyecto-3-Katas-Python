"""
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
"""
lista = [0,2,2,32,32,2,1,1]
newLista = list(map(lambda numero: numero * 2, lista))

print(lista)
print(newLista)