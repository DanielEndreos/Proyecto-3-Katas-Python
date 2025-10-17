"""
30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
"""

palabraA = "caracol"
palabraB = "locarac"

def anagramaAmargana(strA: str,strB:str) -> str:
    if strA.lower() == strB.lower()[::-1]:
        return "Las dos palabras son anagramas"
    else:
        return "Las dos palabras son distintas"
    
print(anagramaAmargana(palabraA,palabraB))
