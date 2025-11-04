# seccion_muebles.py
import flet as ft

def seccion_muebles(page: ft.Page, main_container: ft.Column):
    """
    Sección de muebles con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos el contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Sofá 3 Plazas Gris", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Sofá cómodo de tela gris con cojines incluidos."},
        {"nombre": "Silla de Oficina Ergonomica", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Silla con soporte lumbar y ruedas giratorias."},
        {"nombre": "Mesa de Centro Madera", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Mesa rectangular de madera maciza de 1.2m."},
        {"nombre": "Estantería 5 Niveles", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Estantería metálica para libros y decoración."}
    ]

    fila_2 = [
        {"nombre": "Cama Queen Size", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cama con somier incluido y cabecera acolchada."},
        {"nombre": "Armario 4 Puertas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Armario de madera con compartimientos y cajones."},
        {"nombre": "Mesa de Comedor 6 Personas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Mesa rectangular de madera con acabado natural."},
        {"nombre": "Silla Tapizada Azul", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Silla cómoda para comedor o escritorio."}
    ]

    fila_3 = [
        {"nombre": "Sofá Cama 2 Plazas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Sofá que se transforma en cama, ideal para espacios pequeños."},
        {"nombre": "Mesa Auxiliar Redonda", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Mesa de apoyo con estructura metálica y madera."},
        {"nombre": "Silla Gaming Roja", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Silla ergonómica para largas sesiones de juego."},
        {"nombre": "Librero Modular", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Librero de MDF con múltiples compartimentos."}
    ]

    fila_4 = [
        {"nombre": "Escritorio 1.5m", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Escritorio con cajones y superficie espaciosa."},
        {"nombre": "Sillón Reclinable Marrón", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Sillón de cuero con función reclinable."},
        {"nombre": "Banco de Madera", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Banco resistente para interior o exterior."},
        {"nombre": "Vitrina 2 Puertas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Vitrina de vidrio y madera para exhibición de objetos."}
    ]

    fila_5 = [
        {"nombre": "Cama Individual", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cama de 1 plaza con somier incluido."},
        {"nombre": "Cómoda 5 Cajones", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cómoda de madera con acabado natural y tiradores metálicos."},
        {"nombre": "Mesa de Noche", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Mesa pequeña con cajón para dormitorio."},
        {"nombre": "Silla Plegable Negra", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Silla ligera, ideal para eventos y espacios reducidos."}
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
    contenido.controls.append(ft.Text("MUEBLES", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
