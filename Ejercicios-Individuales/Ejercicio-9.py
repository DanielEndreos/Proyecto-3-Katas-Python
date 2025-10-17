"""
9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
"""

def fronteraAnimales(listaAnimal: list, listaExcl: list) -> list:
    return list(filter(lambda a: a not in listaExcl, listaAnimal))

animales = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Elefante", "Jirafa", "León", "Lobo", "Zorro", "Hipopótamo", "Rin"]
animalesExcluidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

listaFinal = fronteraAnimales(animales, animalesExcluidos)
print(listaFinal)