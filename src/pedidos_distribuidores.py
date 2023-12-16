class Producto:
    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad

class RegistroFaltantes:
    def __init__(self):
        self.productos_faltantes = []

    def registrar_faltante(self, producto):
        self.productos_faltantes.append(producto)

class PedidoDistribuidor:
    def __init__(self, productos):
        self.productos = productos

class GestorPedidos:
    def __init__(self):
        self.registro_faltantes = RegistroFaltantes()

    def revisar_faltantes(self):
        return self.registro_faltantes.productos_faltantes

    def generar_pedido(self):
        productos_a_pedir = self.revisar_faltantes()
        return PedidoDistribuidor(productos_a_pedir)

class GestorPedidos:
    def __init__(self, almacen):
        self.almacen = almacen

    def generar_pedido_automatico(self):
        productos_a_pedir = self.almacen.verificar_reabastecimiento()
        return PedidoDistribuidor(productos_a_pedir)
