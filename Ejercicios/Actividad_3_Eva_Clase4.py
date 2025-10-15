import time

class ReproductorMusica:
    def __init__(self):
        self.lista_Canciones = []
        self.lista_Artistas = []
        self.duracion = "0:00 >---------------------- 1:30"

    def Agregar_Cancion(self):
        cancion = input("¿Qué canción deseas agregar?: ")
        artista = input("Nombre del artista de la canción: ")
        if cancion in self.lista_Canciones:
            print("La canción ya existe en la Playlist.")
        else:
            self.lista_Canciones.append(cancion)
            self.lista_Artistas.append(artista)
            print("Canción agregada con éxito.")
            
    def enlistar_canciones(self):
        if not self.lista_Canciones:
            print("No hay canciones en la lista.")
            return
        print("\nLista de canciones:")
        for i, (cancion, artista) in enumerate(zip(self.lista_Canciones, self.lista_Artistas), 1):
            print(f"{i}. {cancion} - Artista: {artista}")
            
    def Reproducir(self):
        if  not self.lista_Canciones:
            print("No hay canciones en la lista.")
            return
        self.enlistar_canciones()
        try:
            eleccion = int(input("Selecciona el número de la canción que deseas reproducir: ")) - 1
            if 0 <= eleccion < len(self.lista_Canciones):
                cancion = self.lista_Canciones[eleccion]
                artista = self.lista_Artistas[eleccion]
                print(f"\nReproduciendo: {cancion} - Artista{artista}")
                print(self.duracion)
            else:
                print("Número de canción no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            
    def Eliminar_Cancion(self):
        if not self.lista_Canciones:
            print("No hay canciones en la lista.")
            return
        self.enlistar_canciones()
        try:
            eleccion = int(input("Selecciona el número de la canción que deseas eliminar: ")) - 1
            if 0 <= eleccion < len(self.lista_Canciones):
                cancion = self.lista_Canciones.pop(eleccion)
                artista = self.lista_Artistas.pop(eleccion)
                print(f"Canción eliminada: {cancion} - Artista{artista}")
            else:
                print("Número de canción no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

class CalculadoraTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        descripcion = input("Describe la tarea: ")
        fecha = input("Fecha de entrega (YYYY/MM/DD): ")
        try:
            duracion = int(input("¿Cuántos minutos tomará?: "))
            self.tareas.append((descripcion, duracion, fecha))
            print(f"Tarea agregada: {descripcion} ({duracion} min, fecha límite {fecha})")
        except ValueError:
            print("Por favor, ingresa un número válido para la duración.")

    def calcular_tiempo_total(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return 0
        total = sum(duracion for _, duracion, _ in self.tareas)
        print(f"Tiempo total estimado: {total} minutos")
        return total
    
    def enlistar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        print("\nLista de tareas:")
        for i, (descripcion, duracion, fecha) in enumerate(self.tareas, 1):
            print(f"{i}. {descripcion} - {duracion} min - Fecha límite: {fecha}")
            
    def completar_tarea(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        self.enlistar_tareas()
        try:
            eleccion = int(input("Selecciona el número de la tarea que has completado: ")) - 1
            if 0 <= eleccion < len(self.tareas):
                tarea = self.tareas.pop(eleccion)
                print(f"Tarea completada: {tarea[0]}")
            else:
                print("Número de tarea no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        
    def mostrar_tarea_proxima(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        tarea_proxima = min(self.tareas, key=lambda x: x[2])
        print(f"Tarea próxima: {tarea_proxima[0]} - Fecha límite: {tarea_proxima[2]}")
        print(f"Duración estimada: {tarea_proxima[1]} minutos")

class AsistenteMultifuncional(ReproductorMusica, CalculadoraTareas):
    def __init__(self):
        ReproductorMusica.__init__(self)
        CalculadoraTareas.__init__(self)
        self.nombreIA = "AI"
        self.menu = {
            '1': 'Agregar canción',
            '2': 'Agregar tarea',
            '3': 'Reproducir canción',
            '4': 'Calcular tiempo total de tareas',
            '5': 'Lista de tareas',
            '6': 'Lista de canciones',
            '7': 'Eliminar canción',
            '8': 'Completar / Eliminar tarea',
            '9': 'Salir'
        }

    def saludar(self):
        print(f"\n¡Hola! Soy {self.nombreIA}, tu asistente multifuncional.\n")

    def mostrar_menu(self):
        print("\nMenú de opciones:")
        for clave, descripcion in self.menu.items():
            print(f"{clave}. {descripcion}")

    def Ejecutar(self):
        self.saludar()
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion in ['9', 'Salir', 'salir']:
                print("Hasta luego. ¡Que tengas un gran día!")
                break
            elif opcion == '1':
                self.Agregar_Cancion()
            elif opcion == '2':
                self.agregar_tarea()
            elif opcion == '3':
                self.Reproducir()
                self.mostrar_tarea_proxima()
                input()
                #time.sleep(5)
            elif opcion == '4':
                self.calcular_tiempo_total()
            elif opcion == '5':
                self.enlistar_tareas()
            elif opcion == '6':
                self.enlistar_canciones()
            elif opcion == '7':
                self.Eliminar_Cancion()
            elif opcion == '8':
                self.completar_tarea()
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    Asistente = AsistenteMultifuncional()
    Asistente.Ejecutar()