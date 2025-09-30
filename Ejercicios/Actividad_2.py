class Vehiculo():
    marca = ""
    modelo = ""
    año = 0
    color = ""
    velocidad = 0
    def __init__(self, atributo_marca, atributo_modelo, atributo_año, atributo_color):
        self.marca = atributo_marca
        self.modelo = atributo_modelo
        self.año = atributo_año
        self.color = atributo_color
        self.velocidad = atributo_velocidad
            
    def Acelerar (self):
        velocidad += input("Escriba la velocidad que aumento: ")
    def Hablar (self):
        return f"Mi profesion es: {self.profesion} y estoy hablando sobre el metodo constructor"
    def Estudiar (self):
        return f"Estoy en UNIMINUTO y tengo {self.edad} "
   
Personas_Encuestadas = []
while True:
    opciones = int (input(""" Selecciona
    1 Ingresar datos
    2 Ver los datos
    3 Salir """))
    
    if opciones == 3:
        break
    elif opciones == 1:
        nombre = input("Escriba su nombre: ")
        edad = int(input("Escriba su edad: "))
        estatura = float(input("Escriba su estatura: "))
        profesion = input("Escriba su profesion: ")
        
        persona = Persona (nombre, edad, estatura, profesion)
        Personas_Encuestadas.append(persona)
    
    elif opciones == 2:
        for persona in Personas_Encuestadas:
            print("\n", persona.Enseñar(), "\n", persona.Hablar(), "\n", persona.Estudiar())
            print("\n************")
            
    else:
        print ("Opcion NO valida")

