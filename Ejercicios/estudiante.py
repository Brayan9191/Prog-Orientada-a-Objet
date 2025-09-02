class estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre + "hola"
        self.edad = edad
        self.grado = grado
        
dario = estudiante("Dario", 42, "Semestre 3")
julian = estudiante("Julian", 19, "Semestre 3")
print(dario.edad)
print(julian.edad)