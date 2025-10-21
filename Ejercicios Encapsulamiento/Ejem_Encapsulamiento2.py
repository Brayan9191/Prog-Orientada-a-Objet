class persona:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre   # Atributo privado
        self.edad = edad
        self.genero = genero
        
    @property
    def Nombre(self):
        return self.__nombre
    
p1 = persona("Brayan", 19, "Masculino")
print(p1.Nombre)
p1.edad = 20
print(p1.edad)
print(p1.genero)
