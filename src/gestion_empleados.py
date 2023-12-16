class Horario:
    def __init__(self, hora_inicio, hora_fin, pausa_inicio, pausa_fin):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.pausa_inicio = pausa_inicio
        self.pausa_fin = pausa_fin

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fin} (Pausa: {self.pausa_inicio} - {self.pausa_fin})"

class Empleado:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario

    def __str__(self):
        return f"{self.nombre} - {self.horario}"

class Camarero(Empleado):
    tipo = "Camarero"

class Cocinero(Empleado):
    tipo = "Cocinero"

class Maitre(Empleado):
    tipo = "Maitre"

class Director(Empleado):
    tipo = "Director"

class Gerente(Empleado):
    tipo = "Gerente"

    def __str__(self):
        return f"{self.tipo} {self.nombre} - Horario: {self.horario}"

class GestorHorarios:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_horarios(self):
        for empleado in self.empleados:
            print(empleado)
