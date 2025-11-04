# seccion_jardineria.py
import flet as ft

def seccion_jardineria(page: ft.Page, main_container: ft.Column):
    """
    Sección de Jardinería con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Cortacésped Eléctrico", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cortacésped ligero con bolsa recolectora de 30L."},
        {"nombre": "Tijera de Podar Profesional", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Tijera ergonómica con hojas de acero inoxidable."},
        {"nombre": "Manguera Extensible 20m", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Manguera flexible que se expande con el agua."},
        {"nombre": "Guantes de Jardinería", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Guantes resistentes con protección para espinas."}
    ]

    fila_2 = [
        {"nombre": "Rastrillo Plegable", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Rastrillo ajustable para hojas y césped."},
        {"nombre": "Regadera de Metal 10L", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Regadera duradera con boquilla ajustable."},
        {"nombre": "Fertilizante Orgánico", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Fertilizante natural para todo tipo de plantas."},
        {"nombre": "Carretilla de Jardín 60L", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Carretilla resistente y ligera para traslado de tierra y plantas."}
    ]

    fila_3 = [
        {"nombre": "Set Herramientas Jardín 7 Piezas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Incluye palas, rastrillo y cultivador."},
        {"nombre": "Macetas de Cerámica x4", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Macetas elegantes para interiores y exteriores."},
        {"nombre": "Aspersor Giratorio", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Aspersor con alcance de hasta 10m, ideal para césped."},
        {"nombre": "Cuerda de Jardín 20m", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cuerda resistente para sujetar plantas o delimitaciones."}
    ]

    fila_4 = [
        {"nombre": "Cortasetos Eléctrico", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cortasetos potente y ligero con protección de seguridad."},
        {"nombre": "Bomba de Agua Portátil", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Bomba eléctrica para riego de jardines o trasvase de agua."},
        {"nombre": "Plantas Ornamentales x4", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Set de plantas variadas para decorar interiores y exteriores."},
        {"nombre": "Tijera Cortacésped Manual", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ideal para recortar bordes de césped con precisión."}
    ]

    fila_5 = [
        {"nombre": "Riego por Goteo x10", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Sistema de riego eficiente para macetas y huertos pequeños."},
        {"nombre": "Semillas Variadas 5 Tipos", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Set de semillas de flores y vegetales para plantar."},
        {"nombre": "Abono Líquido Concentrado", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Fertilización rápida y nutritiva para plantas."},
        {"nombre": "Protector Solar para Plantas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Protege plantas delicadas del sol intenso."}
    ]

    filas = [fila_1, fila_2, fila_3, fila_4, fila_5]

    # Contenedor principal
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
    contenido.controls.append(ft.Text("JARDINERÍA", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
