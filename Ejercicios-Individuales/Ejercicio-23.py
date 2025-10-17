"""
23. Concatena una lista de palabras. Usa la función reduce().
"""
from functools import reduce

def concatList(inputList:list) -> str:
    return reduce(lambda a, b: a + " " + b, inputList)

palabras = ["Estoy", "muy", "cansado", "del", "lambda", "de", "las", "narices."]


print(concatList(palabras))

