import mysql.connector
import flet as ft

# -------------------------------
# FUNCIÓN PARA CREAR LA BASE DE DATOS Y TABLAS
# -------------------------------
def inicializar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS comparador_inverfin")
        conn.database = "comparador_inverfin"

        # -------------------------------
        # 1️⃣ ROLES
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS roles (
            id_Rol INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(50) NOT NULL UNIQUE,
            Descripcion VARCHAR(150)
        )
        """)

        # -------------------------------
        # 2️⃣ USUARIOS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_Usuario INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(100) NOT NULL,
            Correo VARCHAR(120) UNIQUE,
            Contrasena VARCHAR(255) NOT NULL,
            id_Rol INT NOT NULL,
            Fecha_Registro DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_Rol) REFERENCES roles(id_Rol)
        )
        """)

        # -------------------------------
        # 3️⃣ CIUDADES
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ciudades (
            id_Ciudad INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(100) NOT NULL
        )
        """)

        # -------------------------------
        # 4️⃣ SUCURSALES
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sucursales (
            id_Sucursal INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(100) NOT NULL,
            Direccion VARCHAR(255),
            id_Ciudad INT,
            Telefono VARCHAR(30),
            FOREIGN KEY (id_Ciudad) REFERENCES ciudades(id_Ciudad)
        )
        """)

        # -------------------------------
        # 5️⃣ CATEGORIAS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id_Categoria INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(100) NOT NULL,
            Descripcion VARCHAR(255)
        )
        """)

        # -------------------------------
        # 6️⃣ PRODUCTOS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id_Producto INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(150) NOT NULL,
            Descripcion VARCHAR(255),
            id_Categoria INT,
            FOREIGN KEY (id_Categoria) REFERENCES categorias(id_Categoria)
        )
        """)

        # -------------------------------
        # 7️⃣ DESCUENTOS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS descuentos (
            id_Descuento INT AUTO_INCREMENT PRIMARY KEY,
            id_Producto INT,
            Porcentaje DECIMAL(5,2),
            Fecha_Inicio DATE,
            Fecha_Fin DATE,
            FOREIGN KEY (id_Producto) REFERENCES productos(id_Producto)
        )
        """)

        # -------------------------------
        # 8️⃣ PRECIOS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS precios (
            id_Precio INT AUTO_INCREMENT PRIMARY KEY,
            id_Producto INT NOT NULL,
            id_Sucursal INT NOT NULL,
            Precio DECIMAL(10,2) NOT NULL,
            Fecha_Actualizacion DATE DEFAULT (CURRENT_DATE),
            FOREIGN KEY (id_Producto) REFERENCES productos(id_Producto),
            FOREIGN KEY (id_Sucursal) REFERENCES sucursales(id_Sucursal)
        )
        """)

        # -------------------------------
        # 9️⃣ HISTORIAL_Precios
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial_precios (
            id_Historial INT AUTO_INCREMENT PRIMARY KEY,
            id_Precio INT NOT NULL,
            Precio_Antiguo DECIMAL(10,2),
            Fecha_Cambio DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_Precio) REFERENCES precios(id_Precio)
        )
        """)

        # -------------------------------
        # 🔟 FAVORITOS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS favoritos (
            id_Favorito INT AUTO_INCREMENT PRIMARY KEY,
            id_Usuario INT NOT NULL,
            id_Producto INT NOT NULL,
            Fecha_Agregado DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario),
            FOREIGN KEY (id_Producto) REFERENCES productos(id_Producto)
        )
        """)

        # -------------------------------
        # 1️⃣1️⃣ RESEÑAS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS resenas (
            id_Resena INT AUTO_INCREMENT PRIMARY KEY,
            id_Usuario INT NOT NULL,
            id_Producto INT NOT NULL,
            Comentario TEXT,
            Calificacion INT CHECK(Calificacion >= 1 AND Calificacion <= 5),
            Fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario),
            FOREIGN KEY (id_Producto) REFERENCES productos(id_Producto)
        )
        """)

        # -------------------------------
        # 1️⃣2️⃣ CONSULTAS
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id_Consulta INT AUTO_INCREMENT PRIMARY KEY,
            id_Usuario INT NOT NULL,
            Producto_Buscado VARCHAR(150),
            Fecha_Consulta DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario)
        )
        """)

        # -------------------------------
        # 1️⃣3️⃣ EMPRESA
        # -------------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresa (
            id_Empresa INT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(150) NOT NULL,
            Mision TEXT,
            Vision TEXT,
            Valores TEXT
        )
        """)

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Base de datos 'comparador_inverfin' con 13 tablas creada correctamente.")
    except mysql.connector.Error as err:
        print(f"❌ Error al crear la base de datos: {err}")


# -------------------------------
# INTERFAZ FLET BÁSICA
# -------------------------------
def main(page: ft.Page):
    page.title = "Comparador de Precios - INVERFIN"
    page.bgcolor = "#FFFFFF"
    page.scroll = "adaptive"

    def crear_bd(e):
        inicializar_bd()
        page.snack_bar = ft.SnackBar(ft.Text("Base de datos creada exitosamente ✅"), open=True)
        page.update()

    page.add(
        ft.Column([
            ft.Text("Sistema Comparador de Precios - INVERFIN", size=28, weight="bold", color="#0078D7"),
            ft.Text("Presiona el botón para crear la base de datos.", size=16),
            ft.ElevatedButton("Crear Base de Datos", on_click=crear_bd, bgcolor="#0078D7", color="white")
        ], alignment="center", horizontal_alignment="center")
    )

# Ejecutar aplicación
if __name__ == "__main__":
    ft.app(target=main)
