"""
24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""
from functools import reduce  #Aquí me he orientado de la IA

numLista = [5, 12, 8, 3, 15, 7, 9, 11, 2, 6, 14, 4, 10, 1, 13, 16, 18, 20, 17, 19]

sumNeg = reduce(lambda a, b: a-b, numLista)
sumPos = reduce(lambda a, b: a+b, numLista)

difTotal = sumPos-sumNeg
print(difTotal)