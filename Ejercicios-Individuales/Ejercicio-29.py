"""
29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
"""

#Hasta sacar los 4 últimos digitos he podido, pero queria probar con replace y al final he tirado de GPT para hacer esto ( "#"*(len(a)-4) + )

#Se podría decir que aquí he hecho yo el 80% y la IA el otro 20% por el comentario de arriba
#Aunque la solución aportada por GPT la había barajado previamente, intentaba no crear yo los # y quería sustituirlos.
def enmascareison(variableTo: any) -> str:
    textInput = str(variableTo)
    return (lambda a: "#"*(len(a)-4) + a[len(a)-4:]  )(textInput)

#Este método lo he realizado yo, ya que no se pide lambda en el ejercicio y la funcionalidad es la misma
#¿Que hago? Es sencillo, divido la frase por la parte que necesito y creo dos partes.
#La primera parte hago replace del valor de i, habiendo sacado la longitud previamente y restandole las posiciones
#que no quiero reemplazar, luego uno la frase nuevamente y resuelto. 
def funcionenmascara(variableTo: any) -> str:
    textInput =str(variableTo) #Transformor ANY to Str
    longitud = len(textInput)  #Calculo Long
    parteA = textInput[:longitud-4] #Parte a susituir
    parteB = textInput[longitud-4:] #Parte a mantener

    for i in range(longitud-4):
        parteA = parteA.replace(parteA[i], "#") #Reemplazamos toda la parte a sustituir por #

    return parteA+parteB #Juntamos nuevamente las dos partes

quieroLlorar  = enmascareison("weg2fgg2gg2")
quieroLlorar2 = funcionenmascara("weg2fgg2gg2")
print (f"El resultado con la función más pro es: {quieroLlorar}")
print (f"El resultado con la función de tirar por casa es: {quieroLlorar}")