class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        self._nombre = nombre
        self._precio = float(precio)
        self._marca = marca
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @property
    def marca(self):
        return self._marca

class Dron(ProductoElectronico):
    def __init__(self, nombre, precio, marca, autonomia_minutos):
        super().__init__(nombre, precio, marca)
        self._autonomia_minutos = int(autonomia_minutos)

    @property
    def autonomia(self):
        return self._autonomia_minutos
    
    @autonomia.setter
    def autonomia(self, valor):
        if len(valor) > 0:
            self._autonomia_minutos = valor
        else:
            raise ValueError("La autonomía debe ser un valor positivo")

    @property
    def precio(self):
        precio_base = super().precio
        return round(precio_base * 1.15, 2)

if __name__ == "__main__":
    dron_modelo_x = Dron("SkyHawk X100", 500.00, "AeroTech", 45)
    print(dron_modelo_x.nombre)
    print(dron_modelo_x.precio)
    print(dron_modelo_x.marca)
    print(dron_modelo_x.autonomia)