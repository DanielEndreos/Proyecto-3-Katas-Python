"""
35. Crea la clase UsuarioBanco
        Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
        Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
        Código a seguir:

            Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
            Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
            Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
            Implementar agregar_dinero para aumentar el saldo del usuario.

        Caso de uso:
                a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
                b. Agregar 20 unidades al saldo de Bob.
                c. Transferir 80 unidades de Bob a Alicia.
                d. Retirar 50 unidades del saldo de Alicia.
                
"""

class UsuarioBanco:
    def __init__(self, nombre: str, saldo: int, cuentaCorriente: bool):
        self.nombre = nombre
        self.saldo = saldo
        self.cuentaCorriente = cuentaCorriente
        return

    def retirar_dinero(self, cantidad:int):
        if self.saldo < cantidad:
            return print(f"{self.nombre} No es posible retirar la cantidad de dinero, el saldo es {self.saldo}€ y la cantidad a retirar es mayor que el saldo, siendo esta {cantidad}€.")
        else:
            self.saldo -= cantidad
        return print(f"Se ha retirado {cantidad}€, quedan {self.saldo}€ en la cuenta bancaria. {self.nombre}, tu verás que haces...")
    
    def transferir_dinero(self, cantidad: int, usuarioDestino: "UsuarioBanco"):
        if self.saldo < cantidad:
             return print(f"No es posible realizar la transferencia... ¿a donde vas {self.nombre}?, tienes {self.saldo}€ y la cantidad que quieres transferir a {usuarioDestino.nombre} es {cantidad}€.")
        else: 
            self.saldo -= cantidad
            usuarioDestino.saldo += cantidad
        return print(f"Se ha transferido {cantidad}€ de {self.nombre} a {usuarioDestino.nombre}.")
    
    def agregar_dinero(self, cantidad:int):
        self.saldo += cantidad
        return print(f"Se ha ingresado la cantidad de {cantidad}€, actualmente dispones de {self.saldo}€. ¡Muy bien {self.nombre}, Vas en buen camino!")
    
#Caso de uso:
#a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

#b. Agregar 20 unidades al saldo de Bob.
bob.agregar_dinero(20)

#c. Transferir 80 unidades de Bob a Alicia.
bob.transferir_dinero(80, alicia)

#d. Retirar 50 unidades del saldo de Alicia. 
alicia.retirar_dinero(50)
