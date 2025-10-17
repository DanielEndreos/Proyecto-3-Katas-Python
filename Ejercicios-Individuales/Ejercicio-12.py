"""
12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
"""
def longEachWord(frase):
    frase = frase.replace(",", "").replace(".", "").replace("!", "").replace("¡","").replace("?","").replace("¿","")  #Eliminamos todos los simbolos no deseados que se me han ocurrido
    palabras = frase.split(" ") #Creamos una lista con todas las palabras
    return list(map(len, palabras))

textFrase = "Pepito de los palotes, comio piedras en un trigal, lloró en las esquinas, y este ejercicio me ha complicado un poco la existencia"

print(longEachWord(textFrase))

