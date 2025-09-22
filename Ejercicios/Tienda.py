class Tienda:
    def __init__(self, nom_Tienda, nom_Producto, Precio_Base, Descuento):
        self.Tienda = nom_Tienda
        self.Producto = nom_Producto
        self.Precio_Base = Precio_Base
        self.Descuento = Descuento
        self.Precio_Final = 0
        
    #   Convertir porcentaje segun descuento
        Descuento_Decimal = self.Descuento/100
        
    #   Operaacion aritmetica de precio con el descuento
        self.Precio_Final = self.Precio_Base * (1- Descuento_Decimal)
    
    #   Condicionales    
        if Precio_Base >= 200:
            print("Producto de alto valor, se aplica un descuento adicional del 15% al precio final")
            self.Precio_Final = self.Precio_Final * 0.85
            
        elif(Precio_Base < 200 & Precio_Base > 100):
            print("Producto de mediano valor, se aplica un descuento adicional del 10% al precio final")
            self.Precio_Final = self.Precio_Final * 0.90
            
        elif(Precio_Base < 100):
            print("Producto de bajo valor, se aplica un descuento adicional del 5% al precio final")
            self.Precio_Final = self.Precio_Final * 0.95
            
    def mostrar_info(self):
        print ("\n---- DETALLES DEL PRODUCTO ----")
        print (f" Tienda: {self.Tienda}")                #   Siempre se inicia los corchetes del print con "(f"")" para poder ingresar variables
        print (f" Producto: {self.Producto}")
        print (f" Precio base: {self.Precio_Base}")
        print (f" Descuento aplicado al producto: {self.Descuento}")
        print (f" Total a pagar ${self.Precio_Final}")
        print ("----------\n")

Producto1 = Tienda("D1", "Queso", 300, 0)
Producto2 = Tienda("Tecno_UNIMINUTO", "Portatil", 500, 10)
Producto3 = Tienda("D1", "Mouse", 50, 5)
Producto4 = Tienda("Tecno_UNIMINUTO", "Teclado", 99, 6)

Producto1.mostrar_info()
Producto2.mostrar_info()
Producto3.mostrar_info()
Producto4.mostrar_info()