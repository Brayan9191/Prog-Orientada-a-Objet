class Coche:
    def __init__(self, marca, modelo, color="negro"):
        self.Marca = marca
        self.Modelo = modelo
        self.Color = color
        
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Tesla", "Model S", "Rojo")
print(coche1.Marca, coche1.Modelo, coche1.Color)

print(coche2.Marca, coche2.Modelo, coche2.Color)