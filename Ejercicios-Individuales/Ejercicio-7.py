"""
7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""

def tuplaToList(listTupla: tuple) -> list:
    return list(map(lambda a:a, listTupla))

userPrometeo = ("Dani", 8.5, "Aprobado")

print(tuplaToList(userPrometeo))