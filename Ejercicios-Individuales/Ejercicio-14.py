"""
14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
"""
def palabrasEmpiezanPor(listaPalabras: list, letra: str) -> list:
    letraLower = letra.lower() 
    listaLower = list(map(lambda a: a.lower() , listaPalabras))
    return list(filter(lambda a: a[:1] == letraLower, listaLower))

liPalabra = ["Sol", "Luna", "Mar", "Montaña", "Río", "Bosque", "Ciudad", "Nube", "Trueno", "Viento", "Tierra", "Estrella", "Cielo", "fuego", "lluvia", "nieve", "arena", "flor", "piedra", "hoja"]
letra = "l"

print(palabrasEmpiezanPor(liPalabra, letra))