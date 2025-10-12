class Operacion:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def Realizar_Operacion():
        pass
    
class Suma(Operacion):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        
    def Realizar_Operacion(self):
        return self.n1 + self.n2
    
class Resta(Operacion):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        
    def Realizar_Operacion(self):
        return self.n1 + self.n2
    
class Producto(Operacion):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        
    def Realizar_Operacion(self):
        return self.n1 * self.n2
    
class Dividir(Operacion):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        
    def Realizar_Operacion(self):
        return self.n1 / self.n2
    
class Menu:
    def __init__(self):
        self.operaciones = {
            '1' : ('Suma: ', Suma),
            '2' : ('Resta: ', Resta),
            '3' : ('Multiplicacion: ', Producto),
            '4' : ('Division', Dividir)
        }
        
    def Mostrar_Menu(self):
        print ("\n --- Calculadora de operaciones POO --- ")
        for clave, valor in self.operaciones.items():
            print (f"{clave}.{valor [0]}")
        print("5. Salir")
        
    def Ejecutar(self):
        while True:
            self.Mostrar_Menu()
            opcion = input ("Selecione una operacion: ")
            
            if opcion == '5':
                print("Hasta luego")
                break
            
            if opcion in self.operaciones:
                try:
                    n1 = float(input("Ingrese el primer numero: "))
                    n2 = float(input("Ingrese el segundo numero: "))
                    
                    nombre_operacion, clase_operacion = self.operaciones [opcion]
                    Operacion = clase_operacion (n1, n2)
                    resultado = Operacion.Realizar_Operacion()
                    print (f" \n Resultado de {nombre_operacion}: {resultado}")
                    break
                except ValueError:
                    print("Error: Ingrese la opcion segun la informacion")
            else:
                print("Opcion no valida, intente de nuevo")

if __name__ == "__main__":
    calculadora = Menu()
    calculadora.Ejecutar()