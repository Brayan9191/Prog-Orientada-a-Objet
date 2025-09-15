class Tienda:
    def __init__(self, nom_Tienda, nom_Producto, Precio_Base, Descuento):
        self.Tienda = nom_Tienda
        self.Producto = nom_Producto
        self.Precio = Precio_Base
        self.Descuento = Descuento
        
        if(Precio_Base >= 200):
            Descuento = ((Precio_Base / 100) * 15)
            
        if(Precio_Base < 200 & Precio_Base > 100):
            Descuento = ((Precio_Base / 100) * 10)
            
        if(Precio_Base < 100):
            Descuento = ((Precio_Base / 100) * 5)
        

Tienda1 = Tienda("D1", "Queso", 1200)
Tienda2 = Tienda("D1", "Queso", 85)
Tienda3 = Tienda("D1", "Queso", 150)

print(Tienda1.Tienda, Tienda1.Producto, Tienda1.Precio, Tienda1.Descuento)
            