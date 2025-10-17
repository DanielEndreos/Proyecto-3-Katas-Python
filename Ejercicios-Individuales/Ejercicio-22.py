"""
22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
"""
from functools import reduce

nums = [4, 7, 2, 9, 5]

prodTotal = reduce(lambda a, b: a*b, nums)
print(prodTotal)