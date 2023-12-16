class Producto:
    def __init__(self, nombre, cantidad, umbral_reabastecimiento):
        self.nombre = nombre
        self.cantidad = cantidad
        self.umbral_reabastecimiento = umbral_reabastecimiento

    def necesita_reabastecimiento(self):
        return self.cantidad <= self.umbral_reabastecimiento

class Almacen:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.inventario:
            self.inventario[producto.nombre].cantidad += cantidad
        else:
            producto.cantidad = cantidad
            self.inventario[producto.nombre] = producto

    def remover_producto(self, nombre_producto, cantidad):
        if nombre_producto in self.inventario and self.inventario[nombre_producto].cantidad >= cantidad:
            self.inventario[nombre_producto].cantidad -= cantidad
            return True
        return False

    def verificar_reabastecimiento(self):
        return [producto for producto in self.inventario.values() if producto.necesita_reabastecimiento()]
