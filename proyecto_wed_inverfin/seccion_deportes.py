# seccion_deportes.py
import flet as ft

def seccion_deportes(page: ft.Page, main_container: ft.Column):
    """
    Sección de Deportes con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Pelota de Fútbol Oficial", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Pelota profesional para partidos y entrenamiento."},
        {"nombre": "Balón de Básquet 7", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Balón de caucho resistente para interiores y exteriores."},
        {"nombre": "Raqueta de Tenis Profesional", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Raqueta ligera con gran control y potencia."},
        {"nombre": "Guantes de Boxeo 12oz", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Guantes acolchados para entrenamiento y sparring."}
    ]

    fila_2 = [
        {"nombre": "Mancuernas 5kg (Par)", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Mancuernas recubiertas de neopreno para entrenamientos de fuerza."},
        {"nombre": "Bicicleta Estática Indoor", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Bicicleta ergonómica con resistencia ajustable y monitor digital."},
        {"nombre": "Cuerda para Saltar", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cuerda ligera con agarres antideslizantes y regulable."},
        {"nombre": "Colchoneta Yoga 1.5cm", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Colchoneta antideslizante para yoga y pilates."}
    ]

    fila_3 = [
        {"nombre": "Set de Pesas Ajustables 10-30kg", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Pesas con ajuste rápido y seguro para entrenamiento completo."},
        {"nombre": "Saco de Boxeo 1.2m", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Saco resistente para entrenamiento de golpeo y fuerza."},
        {"nombre": "Pelota de Pilates 65cm", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Pelota de estabilidad para ejercicios de core y equilibrio."},
        {"nombre": "Red de Vóley Portátil", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Red ajustable para entrenamiento y partidos al aire libre."}
    ]

    fila_4 = [
        {"nombre": "Zapatillas Running Hombre", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Zapatillas ligeras y cómodas para entrenamiento y competición."},
        {"nombre": "Balón de Vóley Oficial", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Balón resistente para uso en interiores y exteriores."},
        {"nombre": "Set de Bandas Elásticas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Bandas de resistencia de diferentes niveles para tonificación."},
        {"nombre": "Casco Ciclismo Adulto", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Casco ligero con ajuste rápido y ventilación optimizada."}
    ]

    fila_5 = [
        {"nombre": "Palo de Hockey de Campo", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Palo profesional de fibra para hockey sobre césped."},
        {"nombre": "Raqueta de Bádminton", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Raqueta ligera y resistente para juegos recreativos y profesionales."},
        {"nombre": "Balón de Rugby Oficial", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Balón de alta durabilidad para entrenamientos y partidos."},
        {"nombre": "Set de Conos de Entrenamiento", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Conos de plástico para agilidad y coordinación en entrenamientos."}
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
    contenido.controls.append(ft.Text("DEPORTES", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
