"""
6. Escribe una función que calcule el factorial de un número de manera recursiva.
"""
#Opción #1 - Esta la hice yo, pero no era recursiva. Cómo no sabía que era el factorial de un número, ni una manera recursiva, pregunté a Chat.
def calcFactorial (numInput: int) -> int:
    totalValue = numInput

    for index in range(numInput-1,0, -1):
        totalValue *= index   

    if numInput == 0:
        totalValue = 1

    return totalValue

#Opción #2 - Me ayudé de ChatGPT para la Opción 2, es curiosa, pero la entiendo. La he mejorado a lo de Chat sin su ayuda, porque si ponía 0 daba error.
def calcFactorialRecursivo (numInput: int) -> int:
    if numInput == 1 or numInput == 0:
        return 1
    else:
        return numInput * calcFactorialRecursivo(numInput-1)
      

numFactorial = 0
valueData = calcFactorial(numFactorial)
print(valueData)

valueData2 = calcFactorialRecursivo(numFactorial)
print(valueData2)
