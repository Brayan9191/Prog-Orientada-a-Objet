class Perro:
    def int (self,nombre,raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        return "¡Guau! ¡Guau!"
    
    def datos_del_perro(self):
        return f"{self.nombre} es de raza {self.raza}"
    
p1 = Perro("Rex", "Pastor Aleman")
p2 = Perro("Luna", "Labrador")
    
print(p1.nombre)
print(p2.ladrar())
print(p1.datos_del_perro())
