class CuentaBancaria:
    def __init__(self, titular, saldo_inicial =0):
        self._titular = titular         #   Atributo protegido
        self.__saldo = saldo_inicial    #   Atributo privado
        
    def depositar (self, monto):
        if monto > 0:
            self.__saldo += monto
            print (f"Depósito exitoso, Su saldo es: ${self.__saldo}")
        else:
            print ("El monto debe ser positivo, es decir mayor a Cero (0)")
            
    def retirar (self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print (f"El retiro fue exitoso, su saldo es: ${self.__saldo}")
        else:
            print ("Fondos insuficientes o monto invalido")
            
#   Getter acceso controlado
    def get_saldo (self):
        return self.__saldo
    def get_titular (self):
        return self._titular
    
cuenta1 = CuentaBancaria("Brayan", 1000000)
cuenta1.depositar(10000)
cuenta1.retirar(500000)
cuenta1.depositar(-4000)
cuenta1.retirar(99999999999)

print(f"Nombre del titular {cuenta1.get_titular()}")
print(f"El saldo de la cuenta es: ${cuenta1.get_saldo()}")