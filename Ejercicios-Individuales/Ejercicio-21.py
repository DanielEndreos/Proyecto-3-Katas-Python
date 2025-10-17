"""
21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
"""
def calcCube(numDado: int) -> int:
    return (lambda a: a**3)(numDado)

dado = 3
resultado = calcCube(dado)

print(resultado)