from db import get_connection

# === Usuarios ===
def agregar_usuario(nombre, contraseña, rol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuario (nombre, contraseña, rol) VALUES (?, ?, ?)",
        (nombre, contraseña, rol)
    )
    conn.commit()
    conn.close()

def obtener_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario, nombre, rol FROM usuario")
    usuarios = cursor.fetchall()
    conn.close()
    return [{"id": u[0], "nombre": u[1], "rol": u[2]} for u in usuarios]


# === Productos ===
def agregar_producto(nombre, categoria, descripcion, precio, img):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO producto (nombre, categoria, descripcion, precio, img) VALUES (?, ?, ?, ?, ?)",
        (nombre, categoria, descripcion, precio, img)
    )
    producto_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return producto_id

def obtener_productos_categoria(categoria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id_producto, nombre, descripcion, precio, img FROM producto WHERE categoria = ?",
        (categoria,)
    )
    productos = cursor.fetchall()
    conn.close()
    return [{"id": p[0], "nombre": p[1], "descripcion": p[2], "precio": p[3], "img": p[4]} for p in productos]


# === Sucursales ===
def agregar_sucursal(nombre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sucursal (nombre) VALUES (?)",
        (nombre,)
    )
    sucursal_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return sucursal_id

def obtener_sucursales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_sucursal, nombre FROM sucursal")
    sucursales = cursor.fetchall()
    conn.close()
    return [{"id": s[0], "nombre": s[1]} for s in sucursales]


# === Sucursal_Producto ===
def agregar_sucursal_producto(id_producto, id_sucursal, precio):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sucursal_producto (id_producto, id_sucursal, precio) VALUES (?, ?, ?)",
        (id_producto, id_sucursal, precio)
    )
    conn.commit()
    conn.close()

def obtener_sucursales_producto(id_producto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sp.id, s.nombre, sp.precio FROM sucursal_producto sp "
        "JOIN sucursal s ON sp.id_sucursal = s.id_sucursal "
        "WHERE sp.id_producto = ?",
        (id_producto,)
    )
    sucursales = cursor.fetchall()
    conn.close()
    return [{"id": s[0], "sucursal": s[1], "precio": s[2]} for s in sucursales]


# === Pedidos ===
def agregar_pedido(id_sucursal_producto, id_producto, estado="Pendiente"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pedido (id_sucursal, id_producto, estado) VALUES (?, ?, ?)",
        (id_sucursal_producto, id_producto, estado)
    )
    pedido_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return pedido_id

def obtener_pedidos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id_pedido, s.nombre, pr.nombre, sp.precio, p.estado
        FROM pedido p
        JOIN sucursal_producto sp ON p.id_sucursal = sp.id
        JOIN sucursal s ON sp.id_sucursal = s.id_sucursal
        JOIN producto pr ON p.id_producto = pr.id_producto
        ORDER BY p.id_pedido DESC
    """)
    pedidos = cursor.fetchall()
    conn.close()
    return [
        {"id_pedido": p[0], "sucursal": p[1], "producto": p[2], "precio": p[3], "estado": p[4]}
        for p in pedidos
    ]

def actualizar_estado_pedido(id_pedido, nuevo_estado):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE pedido SET estado = ? WHERE id_pedido = ?",
        (nuevo_estado, id_pedido)
    )
    conn.commit()
    conn.close()
