"""
16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
"""

def filtroXLong(frase: str, numQ: int) -> list:
    palabras = frase.replace(",","").replace(".", " ").split()
    return list(filter(lambda a: len(a)>numQ,palabras))

fraseDestripar = "Cuando un gusano cruzaba la carretera, va y lo atropelló Antonio R."

numFiltro = 6
listaResult = filtroXLong(fraseDestripar, numFiltro)

print(listaResult)