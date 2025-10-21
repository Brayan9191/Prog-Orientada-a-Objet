class persona:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre   # Atributo privado
        self.edad = edad
        self.genero = genero
        
    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, value):
        self.__nombre = value
        
p1 = persona("Brayan", 19, "Masculino")
print(p1.Nombre)

p1.Nombre = "Brayan Cespedes"
print(p1.Nombre)