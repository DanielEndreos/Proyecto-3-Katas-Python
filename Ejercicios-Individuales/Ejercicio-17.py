"""
17. Crea una función que tome una lista de dígitos y devuelva el número . Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
"""
from functools import reduce

def listToNum(inputList:list) -> int:
    return reduce(lambda a, b: a*10 + b, inputList)

itemsList = [5,7,2,2,1,3]

print(listToNum(itemsList))