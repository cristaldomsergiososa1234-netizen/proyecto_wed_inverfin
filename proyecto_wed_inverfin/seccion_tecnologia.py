# seccion_tecnologia.py
import flet as ft

def seccion_tecnologia(page: ft.Page, main_container: ft.Column):
    """
    Sección de Tecnología con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Laptop Gamer 16GB RAM", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Laptop con tarjeta gráfica dedicada para juegos exigentes."},
        {"nombre": "Smartphone 128GB", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Teléfono inteligente con cámara triple y pantalla AMOLED."},
        {"nombre": "Tablet 10'' 64GB", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Tablet con sistema Android, ideal para estudios y trabajo."},
        {"nombre": "Monitor 27'' 144Hz", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Monitor curvo para gaming y diseño gráfico con alta tasa de refresco."}
    ]

    fila_2 = [
        {"nombre": "Auriculares Inalámbricos", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Auriculares con cancelación de ruido y micrófono integrado."},
        {"nombre": "Teclado Mecánico RGB", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Teclado mecánico con iluminación RGB personalizable."},
        {"nombre": "Mouse Gamer 16000 DPI", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Mouse ergonómico con botones programables y sensor avanzado."},
        {"nombre": "Router WiFi 6", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Router de última generación con cobertura extendida y alta velocidad."}
    ]

    fila_3 = [
        {"nombre": "Smartwatch Fitness", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Reloj inteligente con monitor de ritmo cardíaco y GPS."},
        {"nombre": "Cámara DSLR 24MP", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cámara réflex digital para fotografía profesional."},
        {"nombre": "Proyector LED 1080p", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Proyector portátil para cine en casa con buena luminosidad."},
        {"nombre": "Disco Duro SSD 1TB", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Almacenamiento rápido y confiable para tus datos."}
    ]

    fila_4 = [
        {"nombre": "Impresora Multifunción", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Impresora, escáner y copiadora en un solo equipo."},
        {"nombre": "Altavoz Bluetooth 50W", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Altavoz portátil con sonido potente y batería duradera."},
        {"nombre": "Teclado y Mouse Inalámbricos", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Set inalámbrico para oficina y gaming."},
        {"nombre": "Cámara Web 1080p", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cámara para videollamadas con buena calidad de imagen."}
    ]

    fila_5 = [
        {"nombre": "Tablet Gráfica", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ideal para diseño, dibujo digital y edición de fotos."},
        {"nombre": "Smart Home Kit", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Kit para automatización del hogar con control por app."},
        {"nombre": "Power Bank 20000mAh", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Batería portátil para cargar dispositivos múltiples."},
        {"nombre": "Cable HDMI 2m", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cable de alta velocidad para conexión de audio y video."}
    ]

    filas = [fila_1, fila_2, fila_3, fila_4, fila_5]

    # Contenedor principal centrado
    contenido = ft.Column(expand=True, spacing=30, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # Función para crear tarjeta
    def crear_tarjeta(prod):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=prod["img"], width=200, height=150, fit=ft.ImageFit.COVER),
                ft.Text(prod["nombre"], size=18, weight="bold", color="#FFD600", text_align="center"),
                ft.Text(prod["descripcion"], text_align="center")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            bgcolor="#1565C0",
            border_radius=15,
            padding=10,
            width=240,
            shadow=ft.BoxShadow(blur_radius=5, color="#000000", offset=ft.Offset(2,2))
        )

    # Título principal
    contenido.controls.append(ft.Text("TECNOLOGÍA", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
