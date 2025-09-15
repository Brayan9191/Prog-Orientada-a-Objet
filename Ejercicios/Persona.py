class Persona:
    nombre: str = False;
    Cantidad_Ojos: int = False;
    Cantidad_Manos: int = False;
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

Personal = Persona("Ana", 30)
Personal.saludar()
Personal2 = Persona("Brayan", 18)
Personal2.saludar()