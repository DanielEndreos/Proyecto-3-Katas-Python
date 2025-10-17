"""
20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
"""

mixLista = [1, "hola", 3.5, "mundo", 42, "python", 7, "día", 99, "sol", 0, "noche", 23, "GPTín", 5.7, "café", 88, "teclado", 12, "ratón"]

nuevalista = list(filter(lambda a: type(a) != str, mixLista))

print(nuevalista)