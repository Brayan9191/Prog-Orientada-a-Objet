class CuentaBancaria:
    def __init__(self, titular, saldo_inicial =0):
        self._titular = titular         #   Atributo protegido
        self._saldo = saldo_inicial     #   Atributo Protegido  (_ con una sola linea)
        self._activa = True
        
    @property
    def saldo(self):
        """Getter automatico se usa como un atributo"""
        return self._saldo
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular (self, valor):
        if len(valor) > 0:
            self.titular = valor
        else:
            self._activa = False
            raise ValueError("Titular no puede estar vacio o en ceros")
        
    @property
    def esta_activa (self):
        return self._activa


cuenta1 = CuentaBancaria("Brayan", 0)
cuenta2 = CuentaBancaria("Jhojan", 10000)

print("***** Datos de la cuenta 1 *****")
print(cuenta1.titular)
print(cuenta1.saldo)
print(cuenta1.esta_activa)

print("***** Datos de la cuenta 2 *****")
print(cuenta2.titular)
print(cuenta2.saldo)
print(cuenta2.esta_activa)