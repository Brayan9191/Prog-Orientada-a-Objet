class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Saldo actual: ${self.saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def consultar_saldo(self):
        return self.saldo

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0):
        super().__init__(numero_cuenta, titular, saldo)
        
    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes para el retiro.")

    def aplicar_interes(self):
        interes = self.saldo * 0.05
        self.saldo += interes
        print(f"Interés aplicado. Nuevo saldo: ${self.saldo:.2f}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0):
        super().__init__(numero_cuenta, titular, saldo)
        
    def retirar(self, monto):
        if monto > 0 and (self.saldo - monto) >= -1000:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Límite de sobregiro excedido (-1000).")
        
# --- Pruebas ---
if __name__ == "__main__":
    # Crear cuentas
    ahorros = CuentaAhorros("001", "Ana", 1000)
    corriente = CuentaCorriente("002", "Luis", 500)

    # Operaciones
    ahorros.depositar(200) # Saldo: 1200
    ahorros.retirar(100) # Saldo: 1100
    ahorros.aplicar_interes() # Saldo: 1155.00

    corriente.retirar(1000) # Saldo: -500 (dentro del límite)
    corriente.retirar(600) # Error: límite excedido

    # Consultar saldos
    print("****Banco PROFE DARIO****")
    print(f"Cuenta del titular: {ahorros.titular} Saldo Ahorros: ${ahorros.consultar_saldo():.2f}") # 1155.00
    print("*****************")
    print(f"Cuenta del titular: {corriente.titular} Saldo Corriente: ${corriente.consultar_saldo()}") # -500