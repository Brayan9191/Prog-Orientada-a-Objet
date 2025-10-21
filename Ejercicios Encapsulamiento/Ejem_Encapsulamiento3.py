class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    @property
    def saldo(self):
        """Metodo getter para obtener el saldo"""
        print("Accediendo al saldo...")
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        """Metodo setter para modificar el saldo con una validacion"""
        if nuevo_saldo >= 0:
            print("Modificando saldo......")
            self.__saldo = nuevo_saldo
        else:
            print("Error: el saldo no puede ser negativo negativo")
            
cuenta1 = CuentaBancaria(1000)
print(cuenta1.saldo)

cuenta1.saldo = 1500
cuenta1.saldo = -400
