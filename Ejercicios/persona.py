class persona:
    nombre = ""
    edad = 0
    altura = 0
    genero = ""
    
    #Agregamos los metodos (Acciones)
    
    def caminar (self):
        return f"hola soy {self.nombre} y estoy caminando..."
    
    def hablar(self):
        return f"me gusta estar en clase"
    
#Creamos instancias
#Creamos objetos, en este caso son 3 (Persona1, Persona2, Persona3)
persona1 = persona()
persona2 = persona()
persona3 = persona()

persona1.nombre = "Dario"
persona1.edad = "42"
persona1.altura = "170"
persona1.genero = "Masculino"
persona2.nombre = "Samuel"
persona3.nombre = "Ana Maria"

print(persona1.nombre)
print(persona1.edad)
print(persona1.altura)
print(persona1.genero)
print(persona2.nombre)
print(persona3.nombre)

print(persona1.caminar())
print(persona1.hablar())