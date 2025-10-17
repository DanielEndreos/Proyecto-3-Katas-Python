"""
28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""

elementos = [42, "manzana", 3.14, True, "mesa", 7, "libro", "manzana", 42, "silla"]

vistos = set()
duplicado = None

for revisado in elementos:
    if revisado in vistos:
        duplicado = revisado
        break
    vistos.add(revisado)

print(duplicado)
