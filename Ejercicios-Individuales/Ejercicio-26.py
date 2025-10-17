"""
26. Crea una función lambda que calcule el resto de la división entre dos números dados.  
"""
#Función lambda, recibe dos inputs y gestiona la operación
restoDivision = (lambda numeroA, numeroB: numeroA%numeroB)

#Entradas desde Consola
numA = int(input("Introduce un número:"))
numB = int(input("Introduce otro número:"))

print("El resto es:", restoDivision(numA,numB))