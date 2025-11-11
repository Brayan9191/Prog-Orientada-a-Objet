class Animal:
    def __init__(self, _nombre):
        self._nombre = _nombre
        
    @property
    def nombre(self):
        return self._nombre
        
    def presentarce(self):
        print(f"Hola, soy un animal llamado {self.nombre} y estoy listo para comunicarme.")
        
    def Accion_Principal(self):
        print("Mi acción es comer.")
   
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def presentarce(self):
        print(f"Guau. Soy un Perro llamado {self.nombre}")
        
    def Accion_Principal(self):
        print("Guau. Estoy persiguiendo la pelota. 🎾")
    
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def presentarce(self):
        print(f"Miau. Soy un Gato llamado {self.nombre}")
        
    def Accion_Principal(self):
        print("Miau. Estoy durmiendo en el teclado. 💻")
    
class Delfin(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def presentarce(self):
        print(f"Eeeeek-eeeek. Soy el delfin {self.nombre}")
        
    def Accion_Principal(self):
        print("Eeeeek-eeeek. Estoy navegando en el océano.🌊")
 
My_perro = Perro("Eduard")
My_gato = Gato("Gaspar")
My_delfin = Delfin("Dolpin")
    
simposio = [My_perro, My_gato, My_delfin]
    
#   Funcion polimorfismo
for animal in simposio:
    animal.presentarce()
    animal.Accion_Principal()
    print("------")