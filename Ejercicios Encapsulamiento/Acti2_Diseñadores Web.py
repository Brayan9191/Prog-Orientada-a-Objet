class Empleado:
    def __init__(self, nombre, sueldo, puesto):
        self.__nombre = nombre
        self.__sueldo = sueldo
        self.__puesto = puesto

    def actualizar_sueldo(self, nuevo_sueldo):
        if nuevo_sueldo > self.__sueldo:
            self.__sueldo = nuevo_sueldo
            print("el nuevo suelo es ", self.__sueldo)
        else:
            print("politica de la agencia el sueldo no puede ser reducido")

    def cambiar_puesto(self, nuevo_puesto):
        self.__puesto = nuevo_puesto
        print("rol actualizado a", self.__puesto)

    def nombre(self):
        return self.__nombre

    def sueldo(self):
        return self.__sueldo

    def puesto(self):
        return self.__puesto


class DisenadorWeb(Empleado):
    def __init__(self, nombre, sueldo, puesto, herramientas):
        super().__init__(nombre, sueldo, puesto)
        self.__herramientas = herramientas

    def actualizar_herramientas(self, nuevas_herramientas):
        self.__herramientas = nuevas_herramientas
        print("stack tecnologico actualizado a", self.__herramientas)

    def cambiar_puesto(self, nuevo_puesto):
        puestos_validos = ["disenador UX/UI", "desarrollador frontend"]
        if nuevo_puesto in puestos_validos:
            super().cambiar_puesto(nuevo_puesto)
        else:
            print("regla del departamento: un disenador solo puede ser UX/UI o frontend")

    def herramientas(self):
        return self.__herramientas


print("pruebas de disenador web")
empleado1 = DisenadorWeb("juan", 3000.00, "disenador grafico", "figma html css")

empleado1.actualizar_sueldo(3500.00)
empleado1.cambiar_puesto("disenador UX/UI")

print("estado final del empleado")
print("nombre", empleado1.nombre())
print("salario", empleado1.sueldo())
print("rol", empleado1.puesto())
print("stack tecnologico", empleado1.herramientas())