class TipoVehiculo:
    def __init__(self, nombre, tarifa_base):
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    def obtener_descripcion(self):
        return f"{self.nombre} - Tarifa base: {self.tarifa_base}"


class MetodoPago:
    def __init__(self, tipo, datos=""):
        self.tipo = tipo  # "Tarjeta de Crédito", "Paypal", "Efectivo"
        self.datos = datos

    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto} con {self.tipo}.")
        return True


class User:
    def __init__(self, nombre, id_usuario, numero):
        self.Nombre = nombre
        self.Id = id_usuario
        self.Numero = numero
        self.Origen = ""
        self.Destino = ""
        self.Tipo_Servicio = ""
        self.Tarifa = 0
        self.metodo_pago = None

    def Ruta(self):
        self.Origen = input("Ingrese su ubicación: ")
        self.Destino = input("Ingrese su destino: ")

    def TipVehiculo(self):
        while True:
            opciones = int(input(""" Selecciona el tipo de servicio
            1. Uber X
            2. Uber Black
            3. Uber Pool
            4. Uber Van
            5. Cancelar
            """))
            
            if opciones == 5:
                print("Cancelado.")
                break
            elif opciones == 1:
                self.Tipo_Servicio = "Uber X"
                break
            elif opciones == 2:
                self.Tipo_Servicio = "Uber Black"
                break
            elif opciones == 3:
                self.Tipo_Servicio = "Uber Pool"
                break
            elif opciones == 4:
                self.Tipo_Servicio = "Uber Van"
                break
            else:
                print("Opción NO válida")

    def tarifa(self):
        if self.Tipo_Servicio == "Uber X":
            self.Tarifa = 5000
        elif self.Tipo_Servicio == "Uber Black":
            self.Tarifa = 10000
        elif self.Tipo_Servicio == "Uber Pool":
            self.Tarifa = 3000
        elif self.Tipo_Servicio == "Uber Van":
            self.Tarifa = 8000
        else:
            self.Tarifa = 0
        
        print(f"La tarifa por el tipo de vehículo es: {self.Tarifa}")

    def seleccionar_metodo_pago(self):
        print("Seleccione el método de pago:")
        op = int(input("1. Tarjeta de Crédito\n2. Paypal\n3. Efectivo\n"))
        if op == 1:
            self.metodo_pago = MetodoPago("Tarjeta de Crédito")
        elif op == 2:
            self.metodo_pago = MetodoPago("Paypal")
        elif op == 3:
            self.metodo_pago = MetodoPago("Efectivo")
        else:
            print("Opción no válida")


class Ruta:
    def __init__(self, distancia, coor_origen, coor_destino):
        self.Distancia = distancia
        self.Coord_Origen = coor_origen
        self.Coord_Destino = coor_destino
        self.Tarifa_Dis = 0

    def calcular_distancia(self):
        # Simulación: retorna el valor ya dado
        return self.Distancia


class Conductor:
    def __init__(self, nombre, id_conductor, numero_conductor):
        self.Nombre_Conductor = nombre
        self.Id_Conductor = id_conductor
        self.Numero_Conductor = numero_conductor
        self.Tarifa = 0
        self.Estado = "Sin reserva"

    def Aceptar_Servicio(self):
        while True:
            opciones = int(input(f""" 
            1. Aceptar
            2. Rechazar
            """))
            
            if opciones == 1:
                self.Estado = "Reservado"
                print("Servicio aceptado.")
                break
            elif opciones == 2:
                print("Servicio rechazado.")
                break


class Viaje:
    def __init__(self, usuario, conductor, ruta, tipo_vehiculo, metodo_pago):
        self.usuario = usuario
        self.conductor = conductor
        self.ruta = ruta
        self.tipo_vehiculo = tipo_vehiculo
        self.metodo_pago = metodo_pago
        self.tarifa = self.calcular_tarifa()
        self.estado = "Solicitado"

    def calcular_tarifa(self):
        return self.ruta.Distancia * (self.tipo_vehiculo.tarifa_base if self.tipo_vehiculo else 1)

    def iniciar_viaje(self):
        self.estado = "En curso"
        print("Viaje iniciado.")

    def finalizar_viaje(self):
        self.estado = "Finalizado"
        if self.metodo_pago:
            self.metodo_pago.procesar_pago(self.tarifa)
        print("Viaje finalizado y pagado.")


# Ejemplo de uso
if __name__ == "__main__":
    usuario = User("Juan", "1*1*5*8*8*5", "300*******")
    usuario.Ruta()
    usuario.TipVehiculo()
    usuario.tarifa()
    usuario.seleccionar_metodo_pago()

    ruta = Ruta(10, usuario.Origen, usuario.Destino)
    conductor = Conductor("Pedro", "1*1*5*8*8*5", "300*******")
    tipo_vehiculo = TipoVehiculo(usuario.Tipo_Servicio, usuario.Tarifa)

    viaje = Viaje(usuario, conductor, ruta, tipo_vehiculo, usuario.metodo_pago)
    print(f"Tarifa total del viaje: {viaje.tarifa}")
    conductor.Aceptar_Servicio()
    viaje.iniciar_viaje()
    viaje.finalizar_viaje()