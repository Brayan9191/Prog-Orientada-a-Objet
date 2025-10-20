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
            3: 'Depositar',
            4: 'Retirar',
            5: 'Consultar Saldo',
            6: 'Aplicar Interés (Solo Ahorros)',
            7: 'Mostrar cuentas registradas',
            8: 'Salir'
        }
        
    def mostrar_menu(self):
        print("****Banco PROFE DARIO****")
        for clave in self.menu_options.keys():
            print(f"{clave}: {self.menu_options[clave]}")
        print("*****************")
        
    def ejecutar(self, opcion, cuentas):
        while True:
            self.mostrar_menu()
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 8:
                print("Saliendo del sistema.")
                break
            
            if opcion == 1:
                numero_cuenta = input("Número de cuenta: ")
                titular = input("Nombre del titular: ")
                saldo = float(input("Saldo inicial: "))
                cuentas[numero_cuenta] = CuentaAhorros(numero_cuenta, titular, saldo)
                print(f"Cuenta de ahorros creada para {titular} con saldo ${saldo}")
                
            elif opcion == 2:
                numero_cuenta = input("Número de cuenta: ")
                titular = input("Nombre del titular: ")
                saldo = float(input("Saldo inicial: "))
                cuentas[numero_cuenta] = CuentaCorriente(numero_cuenta, titular, saldo)
                print(f"Cuenta corriente creada para {titular} con saldo ${saldo}")
                
            elif opcion == 3:
                numero_cuenta = input("Número de cuenta para depositar: ")
                if numero_cuenta in cuentas:
                    monto = float(input("Monto a depositar: "))
                    cuentas[numero_cuenta].depositar(monto)
                else:
                    print("Cuenta no encontrada.")
                    
            elif opcion == 4:
                numero_cuenta = input("Número de cuenta para retirar: ")
                if numero_cuenta in cuentas:
                    monto = float(input("Monto a retirar: "))
                    cuentas[numero_cuenta].retirar(monto)
                else:
                    print("Cuenta no encontrada.")
                    
            elif opcion == 5:
                numero_cuenta = input("Número de cuenta para consultar saldo: ")
                if numero_cuenta in cuentas:
                    cuenta = cuentas[numero_cuenta]
                    print(f"Saldo actual de {cuenta.titular}: ${cuenta.consultar_saldo():.2f}")
                else:
                    print("Cuenta no encontrada.")
                    
            elif opcion == 6:
                numero_cuenta = input("Número de cuenta de ahorros para aplicar interés: ")
                if numero_cuenta in cuentas and isinstance(cuentas[numero_cuenta], CuentaAhorros):
                    cuentas[numero_cuenta].aplicar_interes()
                else:
                    print("Cuenta de ahorros no encontrada o tipo incorrecto.")
                    
            elif opcion == 7:
                print("Cuentas registradas:")
                for num, cuenta in cuentas.items():
                    tipo = "Ahorros" if isinstance(cuenta, CuentaAhorros) else "Corriente"
                    print(f"N°: {num} | Titular: {cuenta.titular} | Tipo: {tipo} | Saldo: ${cuenta.saldo:.2f}")

# --- Pruebas ---
if __name__ == "__main__":
    cuentas = {}
    menu_banco = menu()
    menu_banco.ejecutar(0, cuentas)