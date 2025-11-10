#Clases PADRE
class CitaMedica:
    """Clase base para todas las citas médicas"""

    def __init__(self, paciente, fecha, hora, medico):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.medico = medico
        self.estado = "programada"

    def mostrar_info(self):
        """Método que mostrará información de la cita"""
        return f"Cita general - Paciente: {self.paciente}, Médico: {self.medico}"

    def calcular_duracion(self):
        """Método polimórfico - cada tipo de cita tendrá duración diferente"""
        return 30 # 30 minutos por defecto

    def realizar_cita(self):
        """Simula la realización de la cita"""
        self.estado = "completada"
        return f"Cita realizada con {self.medico}"
    
#Clases HIJA
class CitaGeneral(CitaMedica):
    """Cita con médico general - HEREDA de CitaMedica"""

    def __init__(self, paciente, fecha, hora, medico, motivo):
        # Llamar al constructor del padre
        super().__init__(paciente, fecha, hora, medico)
        self.motivo = motivo

    # POLIMORFISMO: Mismo método, comportamiento diferente
    def mostrar_info(self):
        return f"👨‍⚕️ CITA GENERAL - Paciente: {self.paciente}, Motivo: {self.motivo}"

    def calcular_duracion(self):
        return 20 # Citas generales duran 20 min

class CitaEspecialista(CitaMedica):
    """Cita con especialista - HEREDA de CitaMedica"""

    def __init__(self, paciente, fecha, hora, medico, especialidad, estudios):
        super().__init__(paciente, fecha, hora, medico)
        self.especialidad = especialidad
        self.estudios = estudios

    # POLIMORFISMO: Mismo método, comportamiento diferente
    def mostrar_info(self):
        return f"🎯 CITA ESPECIALISTA - {self.especialidad}, Estudios: {self.estudios}"

    def calcular_duracion(self):
        return 45 # Citas con especialistas duran 45 min
    
class CitaOdontologia(CitaMedica):
    def __init__(self, paciente, fecha, hora, medico, motivo):
        super().__init__(paciente, fecha, hora, medico)
        self.motivo = motivo
        self.Odontologia = "Odontología"
        
        # POLIMORFISMO: Mismo método, comportamiento diferente
    def mostrar_info(self):
        return f"CITA - {self.Odontologia}, Motivo: {self.Motivo}"

    def calcular_duracion(self):
        return 40
        
class CitaPediatria(CitaMedica):
    def __init__(self, paciente, fecha, hora, medico, motivo):
        super().__init__(paciente, fecha, hora, medico)
        self.motivo = motivo
        self.Pediatria = "Pediatría"
        
        # POLIMORFISMO: Mismo método, comportamiento diferente
    def mostrar_info(self):
        return f"CITA - {self.Pediatria}, Motivo: {self.Motivo}"

    def calcular_duracion(self):
        return 30

class CitaUrgencias(CitaMedica):
    """Cita de urgencias - HEREDA de CitaMedica"""

    def __init__(self, paciente, fecha, hora, medico, nivel_urgencia):
        super().__init__(paciente, fecha, hora, medico)
        self.nivel_urgencia = nivel_urgencia

    # POLIMORFISMO: Mismo método, comportamiento diferente
    def mostrar_info(self):
        return f"URGENCIAS - Nivel: {self.nivel_urgencia}, Paciente: {self.paciente}"

    def calcular_duracion(self):
        return 60 # Urgencias duran 60 min
    

        
# POLIMORFISMO
def procesar_citas(lista_citas):
    """Función que demuestra polimorfismo - trata diferentes tipos de citas de manera uniforme"""
    print("PROCESANDO CITAS MÉDICAS:")
    print("-" * 40)

    total_minutos = 0

    for cita in lista_citas:
        # POLIMORFISMO: mismo método, diferente comportamiento según el tipo de cita
        print(cita.mostrar_info())
        duracion = cita.calcular_duracion()
        print(f" Duración: {duracion} minutos")
        print(f" Estado: {cita.realizar_cita()}")
        total_minutos += duracion
        print("-" * 40)

    print(f" El total de minutos programados: {total_minutos}")

# RESULTADOS
def main():
    """Función principal que crea y procesa diferentes tipos de citas"""

    # Crear diferentes tipos de citas (HERENCIA)
    cita1 = CitaGeneral("María González", "2024-01-15", "09:00", "Dr. Pérez", "Control anual")
    cita2 = CitaEspecialista("Carlos Ruiz", "2024-01-15", "10:00", "Dra. López", "Cardiología", "Electrocardiograma")
    cita3 = CitaUrgencias("Ana Martínez", "2024-01-15", "11:00", "Dr. Rodríguez", "Alta")
    cita4 = CitaGeneral("Pedro Sánchez", "2024-01-15", "14:00", "Dra. García", "Gripe")

    # Lista con diferentes tipos de citas
    citas_del_dia = [cita1, cita2, cita3, cita4]

    # Procesar todas las citas (POLIMORFISMO)
    procesar_citas(citas_del_dia)

    # Demostrar que son objetos de diferentes clases
    print("\n TIPOS DE CITAS:")
    for i, cita in enumerate(citas_del_dia, 1):
        print(f"Cita {i}: {type(cita).__name__}")

# Ejecutar el programa
if __name__ == "__main__":
 main()