class Perro:
    def sonido(self):
        return "¡Guau!"
   
class Gato:
    def sonido(self):
        return "¡Miau!"
    
class Vaca:
    def sonido(self):
        return "¡Muu!"
    
#   Funcion polimorfismo
def hacer_sonido(animal):
    return animal.sonido()

#   Crear instancias
mi_perro = Perro()
mi_gato = Gato()
mi_vaca = Vaca()

#   usar el polimorfismo
print(hacer_sonido(mi_perro))
print(hacer_sonido(mi_vaca))
print(hacer_sonido(mi_gato))