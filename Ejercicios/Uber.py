class User():
    Nombre = "Juan"
    Id = "1*1*5*8*8*5"
    Numero = "300*******"
    Origen = ""
    Destino = ""
    Tipo_Servicio = ""
    Tarifa = 0
    
    def __init__(self, atributo_Nombre, atributo_Id, atributo_Numero, atributo_Origen, atributo_Destino, atributo_TipServicio):
        self.Nombre = atributo_Nombre
        self.Id = atributo_Id
        self.Numero = atributo_Numero
        self.Origen = atributo_Origen
        self.Destino = atributo_Destino
        self.Tipo_Servicio = atributo_TipServicio
        
    def Ruta(self):
        Origen = input("Ingrese su ubicación: ")
        Destino = input("Ingrese su destino: ")
    
    def TipVehiculo(self):
        while True:
            opciones = int (input(""" Selecciona el tipo de servicio
            1. Uber X
            2. Uber Black
            3. Uber Pool
            4. Uber Van
            5. Cancelar """))
            
            if opciones == 5:
                break
            elif opciones == 1:
                Tipo_Servicio = "Uber X"
            elif opciones == 2:
                Tipo_Servicio = "Uber Black"
            elif opciones == 3:
                Tipo_Servicio = "Uber Pool"
            elif opciones == 4:
                Tipo_Servicio = "Uber Van"
            else:
                print ("Opcion NO valida")
    
    def tarifa(self):
        if self.Tipo_Servicio == "Uber X":
            Tarifa += 5000
        elif self.Tipo_Servicio == "Uber Black":
            Tarifa += 10000
        elif self.Tipo_Servicio == "Uber Pool":
            Tarifa += 3000
        elif self.Tipo_Servicio == "Uber Van":
            Tarifa += 8000
            
        print(f"La tarifa por el tipo de vehiculo es: {self.Tarifa}")

class Ruta():
    Distancia = 0.0
    Coord_Origen = ""
    Coord_Destino = ""
    Tarifa_Dis = 0
    
    def __init__(self, Atributo_Distancia, atributo_CoorOrigen, atributo_CoorDestino):
        self.Distancia = Atributo_Distancia
        self.Coord_Origen = atributo_CoorOrigen
        self.Coord_Destino = atributo_CoorDestino
        
class Conductor():
    Nombre_Conductor = "Pedro"
    Id_Conductor = "1*1*5*8*8*5"
    Numero_Conductor = "300*******"
    Tarifa = 0
    Estado = "Sin reserva"
    
    def __init__(self, atributo_Nombre, atributo_Id, atributo_Numero):
        self.Nombre_Conductor = atributo_Nombre
        self.Id_Conductor = atributo_Id
        self.Numero_Conductor = atributo_Numero

    
    def Aseptar_Servicio(self):
        while True:
            opciones = int (input(f""" 
            1. Aseptar
            2. Rechazar """))
            
            if opciones == 1:
                self.Estado = "Reservado"
            elif opciones == 2:
                break