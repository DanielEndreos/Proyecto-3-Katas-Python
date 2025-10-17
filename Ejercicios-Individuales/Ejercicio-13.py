"""
13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
"""
conjCaracteres = "macarena"

def tupliPower(palabra: str) -> tuple:
    letrasNoRepetidas = sorted(set(palabra))
    return tuple(map(lambda a: (a.lower(), a.upper()) ,letrasNoRepetidas))

prueba = tupliPower(conjCaracteres)
print(prueba)