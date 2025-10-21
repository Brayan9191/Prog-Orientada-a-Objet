class CuentaBancaria:
    tasa_interes = 0.05  # Atributo de clase
    
    def __init__(self, titular, balance):
        self.titular = titular 
        self.balance = balance 
    
    @classmethod
    def actualizar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa
        
    def mostrar_info(self):
        return f'Titular: {self.titular}, Balance: {self.balance}, Tasa de Interés: {self.tasa_interes}'
    
cuenta1 = CuentaBancaria("Alice", 1000)
cuenta2 = CuentaBancaria("Bob", 2000)

CuentaBancaria.actualizar_tasa_interes(0.07)

cuenta1.actualizar_tasa_interes(0.1)
cuenta2.actualizar_tasa_interes(0.15)

print(cuenta1.mostrar_info()) 
print(cuenta2.mostrar_info()) 