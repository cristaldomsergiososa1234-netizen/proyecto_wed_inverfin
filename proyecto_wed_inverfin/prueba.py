from db import crear_tablas
from registros import (
    agregar_usuario, agregar_producto, agregar_sucursal, 
    agregar_sucursal_producto, agregar_pedido
)

# Crear tablas
crear_tablas()

# Usuarios
agregar_usuario("admin", "12345", "Admin")
agregar_usuario("vendedor1", "12345", "Vendedor")
agregar_usuario("usuario1", "12345", "Usuario")

# Productos
prod1 = agregar_producto("Heladera 550L", "Electrodomésticos", "Gran capacidad con hielo", "1500", "")
prod2 = agregar_producto("Lavarropas 10kg", "Electrodomésticos", "15 programas", "800", "")
prod3 = agregar_producto("Cocina 5 Hornallas", "Electrodomésticos", "Horno a gas incluido", "700", "")

# Sucursales
id_piribebuy = agregar_sucursal("Piribebuy")
id_coronel = agregar_sucursal("Coronel Oviedo")

# Sucursal-Producto
agregar_sucursal_producto(prod1, id_piribebuy, "1550")
agregar_sucursal_producto(prod1, id_coronel, "1500")
agregar_sucursal_producto(prod2, id_piribebuy, "820")
agregar_sucursal_producto(prod2, id_coronel, "800")
agregar_sucursal_producto(prod3, id_piribebuy, "720")
agregar_sucursal_producto(prod3, id_coronel, "700")

# Pedidos de ejemplo
def obtener_id_sucursal_producto(id_producto, id_sucursal):
    from registros import obtener_sucursales_producto
    sucursales = obtener_sucursales_producto(id_producto)
    for s in sucursales:
        if s["sucursal"] == "Piribebuy" and s["id"]:
            return s["id"]
    return None

id_s1 = obtener_id_sucursal_producto(prod1, id_piribebuy)
id_s2 = obtener_id_sucursal_producto(prod2, id_piribebuy)
id_s3 = obtener_id_sucursal_producto(prod3, id_piribebuy)

agregar_pedido(id_s1, prod1, "Pendiente")
agregar_pedido(id_s2, prod2, "Proceso")
agregar_pedido(id_s3, prod3, "Terminado")

print("Base de datos inicializada con éxito.")
