"""
34. Crea la clase Arbol

            Define un árbol genérico con un tronco y ramas como atributos.
        Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
        Código a seguir:

          -  Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
          -  Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
          -  Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
          -  Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
          -  Implementar el método quitar_rama para eliminar una rama en una posición específica.
            Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

        Caso de uso:
                a. Crear un árbol.
                b. Hacer crecer el tronco una unidad.
                c. Añadir una nueva rama.
                d. Hacer crecer todas las ramas una unidad.
                e. Añadir dos nuevas ramas.
                f. Retirar la rama situada en la posición 2.
                g. Obtener información sobre el árbol.
"""
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
        return

    def crecer_tronco(self):
        self.tronco +=1
        return self.tronco
    
    def nueva_rama(self):
        return self.ramas.append(1)
    
    def crecer_ramas(self):
        for i in range(0,len(self.ramas)):
            self.ramas[i]+=1
        return self.ramas
    
    def quitar_ramas(self, pos: int):
        self.ramas.pop(pos)
        return self.ramas
    
    def info_arbol(self):
        return print(f"El arbol tiene una longitud de {miArbol.tronco} troncos y {miArbol.ramas} ramas.")
    

#Caso de uso:
#a. Crear un árbol.
miArbol = Arbol()

#b. Hacer crecer el tronco una unidad.
miArbol.crecer_tronco()

#c. Añadir una nueva rama.
miArbol.nueva_rama()

#d. Hacer crecer todas las ramas una unidad.
miArbol.crecer_ramas()

#e. Añadir dos nuevas ramas.
miArbol.nueva_rama()
miArbol.nueva_rama()

#f. Retirar la rama situada en la posición 2.
miArbol.quitar_ramas(2)

#g. Obtener información sobre el árbol. 
miArbol.info_arbol()
