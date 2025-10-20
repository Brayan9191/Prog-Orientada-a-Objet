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
            
class menu:
    def __init__(self):
        self.menu_options = {
            1: 'Crear Cuenta de Ahorros',
            2: 'Crear Cuenta Corriente',
            3: 'Mostrar cuentas registradas',
            4: 'Salir'
        }
        
    def mostrar_menu(self):
        print("****Banco PROFE DARIO****")
        for clave in self.menu_options.keys():
            print(f"{clave}: {self.menu_options[clave]}")
        print("*****************")
        
    def ejecutar(self, opcion, cuentas):
        contador_cuentas = 1
        while True:
            self.mostrar_menu()
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 4:
                print("Saliendo del sistema.")
                break
            
            if opcion == 1:
                numero_cuenta = f"{contador_cuentas:03d}"
                titular = input("Nombre del titular: ")
                saldo = float(input("Saldo inicial: "))
                cuentas[numero_cuenta] = CuentaAhorros(numero_cuenta, titular, saldo)
                print(f"Cuenta de ahorros creada. Número: {numero_cuenta}, Titular: {titular}, Saldo: ${saldo}")
                contador_cuentas += 1
            elif opcion == 2:
                numero_cuenta = f"{contador_cuentas:03d}"
                titular = input("Nombre del titular: ")
                saldo = float(input("Saldo inicial: "))
                cuentas[numero_cuenta] = CuentaCorriente(numero_cuenta, titular, saldo)
                print(f"Cuenta corriente creada. Número: {numero_cuenta}, Titular: {titular}, Saldo: ${saldo}")
                contador_cuentas += 1
            elif opcion == 3:
                print("Cuentas registradas:")
                for num, cuenta in cuentas.items():
                    tipo = "Ahorros" if isinstance(cuenta, CuentaAhorros) else "Corriente"
                    print(f"N°: {num} | Titular: {cuenta.titular} | Tipo: {tipo} | Saldo: ${cuenta.saldo:.2f}")

# --- Pruebas ---
if __name__ == "__main__":
    cuentas = {}
    menu_banco = menu()
    menu_banco.ejecutar(0, cuentas)
    
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