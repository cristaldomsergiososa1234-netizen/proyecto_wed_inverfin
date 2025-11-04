# seccion_bebes.py
import flet as ft

def seccion_bebes(page: ft.Page, main_container: ft.Column):
    """
    Sección de Bebés con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Cochecito Convertible", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cochecito 3 en 1 con silla de auto incluida."},
        {"nombre": "Silla de Auto Grupo 0+", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Segura y acolchada, con arnés ajustable."},
        {"nombre": "Cuna de Madera", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cuna regulable en altura con barrotes de seguridad."},
        {"nombre": "Colchón Antialergénico", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Colchón cómodo y seguro para recién nacidos."}
    ]

    fila_2 = [
        {"nombre": "Monitor de Bebé con Cámara", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Monitoreo de audio y video con visión nocturna."},
        {"nombre": "Bañera para Bebé", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Bañera plegable con soporte antideslizante."},
        {"nombre": "Cojín de Lactancia", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cojín ergonómico para alimentar al bebé cómodamente."},
        {"nombre": "Set de Ropa Bebé 5 Piezas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ropita suave y segura para recién nacidos."}
    ]

    fila_3 = [
        {"nombre": "Chupetes x2", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Chupetes de silicona, seguros y suaves para bebés."},
        {"nombre": "Biberón Anticólicos", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Biberón de flujo controlado, fácil de limpiar."},
        {"nombre": "Portabebés Ergonomico", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Portabebés cómodo para padres y seguro para el bebé."},
        {"nombre": "Móvil de Cuna Musical", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Móvil con luces y melodías para estimular al bebé."}
    ]

    fila_4 = [
        {"nombre": "Humidificador de Vapor Frío", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ideal para mantener el aire húmedo en la habitación."},
        {"nombre": "Termómetro Digital", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Medición rápida y precisa de la temperatura del bebé."},
        {"nombre": "Pañales Talla 1 x50", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Pañales desechables suaves y absorbentes."},
        {"nombre": "Toallitas Húmedas x80", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Toallitas delicadas para la piel sensible del bebé."}
    ]

    fila_5 = [
        {"nombre": "Silla Alta para Comer", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Silla ajustable y segura para la hora de la comida."},
        {"nombre": "Set de Juguetes Blandos", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Juguetes seguros y educativos para bebés."},
        {"nombre": "Cambiador Portátil", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cambiador plegable y fácil de transportar."},
        {"nombre": "Bolsa de Pañales Multifuncional", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Bolsa espaciosa y organizada para salir con el bebé."}
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
    contenido.controls.append(ft.Text("BEBÉS", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
