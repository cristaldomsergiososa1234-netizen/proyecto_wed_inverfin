import sqlite3

def get_connection():
    return sqlite3.connect("inverfin.db")


# === Función para crear tablas si no existen ===
def crear_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        contraseña TEXT NOT NULL,
        rol TEXT NOT NULL
    )
    """)

    # Tabla de productos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS producto (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        descripcion TEXT,
        precio TEXT,
        img TEXT
    )
    """)

    # Tabla de sucursales
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sucursal (
        id_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    """)

    # Tabla de sucursal_producto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sucursal_producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER,
        id_sucursal INTEGER,
        precio TEXT,
        FOREIGN KEY(id_producto) REFERENCES producto(id_producto),
        FOREIGN KEY(id_sucursal) REFERENCES sucursal(id_sucursal)
    )
    """)

    # Tabla de pedidos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sucursal INTEGER NOT NULL,
        id_producto INTEGER NOT NULL,
        estado TEXT NOT NULL DEFAULT 'Pendiente',
        FOREIGN KEY (id_sucursal) REFERENCES sucursal(id_sucursal),
        FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
    )
    """)

    conn.commit()
    conn.close()


# === Función para obtener productos por categoría ===
def obtener_productos(categoria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto WHERE categoria = ?", (categoria,))
    productos = cursor.fetchall()
    conn.close()
    return productos
