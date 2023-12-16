class Item:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.pedido_actual = None

    def asignar_pedido(self, pedido):
        self.pedido_actual = pedido

class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        return sum(item.precio for item in self.items)

class Restaurante:
    def __init__(self):
        # Crear 10 mesas con diferentes capacidades
        self.mesas = [Mesa(i, 4 if i < 5 else 3 if i < 7 else 2 if i < 9 else 1) for i in range(1, 11)]
        self.menu = [Item(f"Plato {i}", i * 2.5) for i in range(1, 11)]  # 10 platos

    def encontrar_mesa(self, capacidad):
        # Encuentra la primera mesa disponible con la capacidad deseada
        for mesa in self.mesas:
            if mesa.capacidad == capacidad and mesa.pedido_actual is None:
                return mesa
        return None
