from gestion_empleados import Camarero, Cocinero, Maitre, Director, Gerente, Horario, GestorHorarios

# Crear el gestor de horarios
gestor_horarios = GestorHorarios()

# Crear horarios comunes
horario_general = Horario("10:00", "22:00", "16:00", "18:00")

# Agregar empleados de diferentes roles con sus horarios
gestor_horarios.agregar_empleado(Camarero("Laura", horario_general))
gestor_horarios.agregar_empleado(Cocinero("Pedro", horario_general))
gestor_horarios.agregar_empleado(Maitre("Roberto", horario_general))
gestor_horarios.agregar_empleado(Director("Marta", horario_general))
gestor_horarios.agregar_empleado(Gerente("Sofía", horario_general))

# Mostrar los horarios de los empleados
gestor_horarios.mostrar_horarios()



from almacen import Almacen, Producto
from pedidos_distribuidores import GestorPedidos

# Crear el almacén y añadir algunos productos
almacen = Almacen()
almacen.agregar_producto(Producto("Aceite de Oliva", 20, 10), 20)
almacen.agregar_producto(Producto("Arroz", 50, 30), 50)

# Supongamos que se usa algo de aceite de oliva
almacen.remover_producto("Aceite de Oliva", 15)

# Crear el gestor de pedidos y generar un pedido automático si es necesario
gestor_pedidos = GestorPedidos(almacen)
pedido = gestor_pedidos.generar_pedido_automatico()

# Mostrar los productos en el pedido
print("Pedido Automático al Distribuidor:")
for producto in pedido.productos:
    print(f"{producto.nombre}: {producto.cantidad} unidades")




from pedidos_distribuidores import Producto, GestorPedidos

# Crear instancia del gestor de pedidos
gestor_pedidos = GestorPedidos()

# Camareros y cocineros registran productos faltantes
gestor_pedidos.registro_faltantes.registrar_faltante(Producto("Tomates", 10))
gestor_pedidos.registro_faltantes.registrar_faltante(Producto("Lechuga", 5))

# El gerente revisa los productos faltantes
productos_faltantes = gestor_pedidos.revisar_faltantes()
print("Productos Faltantes:")
for producto in productos_faltantes:
    print(f"{producto.nombre}: {producto.cantidad} unidades")

# El gerente genera un pedido al distribuidor
pedido = gestor_pedidos.generar_pedido()
print("\nPedido al Distribuidor:")
for producto in pedido.productos:
    print(f"{producto.nombre}: {producto.cantidad} unidades")


from comandas import Restaurante
from reservas import GestorReservas
from datetime import datetime

# Crear instancia del restaurante
restaurante = Restaurante()

# Crear instancia del gestor de reservas
gestor_reservas = GestorReservas(restaurante)

# Realizar una reserva
hora_reserva = datetime.now()  # Utilizar la hora actual como ejemplo
reserva = gestor_reservas.realizar_reserva(3, hora_reserva, "Juan Pérez", "123456789")

# Verificar la disponibilidad de la mesa 3 para la misma hora
disponible = gestor_reservas.verificar_disponibilidad(3, hora_reserva)
print(f"La Mesa 3 está {'disponible' if disponible else 'no disponible'} para la hora {hora_reserva}")




from comandas import Restaurante, Pedido

# Crear instancia del restaurante
restaurante = Restaurante()

# Encontrar una mesa para 4 personas
mesa_para_cuatro = restaurante.encontrar_mesa(4)

# Crear un pedido para la mesa
pedido_mesa_cuatro = Pedido(mesa_para_cuatro)

# Agregar ítems al pedido
pedido_mesa_cuatro.agregar_item(restaurante.menu[0])  # Agregar el primer plato del menú
pedido_mesa_cuatro.agregar_item(restaurante.menu[3])  # Agregar otro plato

# Asignar el pedido a la mesa
mesa_para_cuatro.asignar_pedido(pedido_mesa_cuatro)

# Calcular el total del pedido
print(f"Total del Pedido: {pedido_mesa_cuatro.calcular_total()} euros")


