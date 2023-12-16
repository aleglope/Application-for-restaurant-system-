from datetime import datetime

class Reserva:
    def __init__(self, mesa, hora, nombre_cliente, contacto_cliente):
        self.mesa = mesa
        self.hora = hora
        self.nombre_cliente = nombre_cliente
        self.contacto_cliente = contacto_cliente

class GestorReservas:
    def __init__(self, restaurante):
        self.reservas = []
        self.restaurante = restaurante

    def realizar_reserva(self, numero_mesa, hora, nombre_cliente, contacto_cliente):
        mesa = self.restaurante.mesas[numero_mesa - 1]
        nueva_reserva = Reserva(mesa, hora, nombre_cliente, contacto_cliente)
        self.reservas.append(nueva_reserva)
        return nueva_reserva

    def verificar_disponibilidad(self, numero_mesa, hora):
        for reserva in self.reservas:
            if reserva.mesa.numero == numero_mesa and reserva.hora == hora:
                return False
        return True
