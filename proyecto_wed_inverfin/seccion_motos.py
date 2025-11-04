# seccion_motos.py
import flet as ft

def seccion_motos(page: ft.Page, main_container: ft.Column):
    """
    Sección de Motos con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos el contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Moto Scooter 125cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Scooter ágil, ideal para la ciudad y recorridos cortos."},
        {"nombre": "Moto Deportiva 300cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto deportiva con motor potente y diseño aerodinámico."},
        {"nombre": "Moto Enduro 250cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ideal para terrenos difíciles, con suspensión reforzada."},
        {"nombre": "Moto Custom 500cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto estilo cruiser, cómoda para recorridos largos."}
    ]

    fila_2 = [
        {"nombre": "Moto Naked 400cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto sin carenado, ligera y versátil para la ciudad."},
        {"nombre": "Moto Touring 600cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto de turismo con maleteros y gran autonomía."},
        {"nombre": "Moto Off-Road 300cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Perfecta para aventuras fuera de la carretera."},
        {"nombre": "Moto Electrica 1500W", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto eléctrica compacta, silenciosa y ecológica."}
    ]

    fila_3 = [
        {"nombre": "Moto Trial 250cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Diseñada para maniobras técnicas y saltos."},
        {"nombre": "Moto Scooter 150cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Scooter potente para ciudad con buen rendimiento de combustible."},
        {"nombre": "Moto Deportiva 600cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto rápida y estable con excelente agarre en curvas."},
        {"nombre": "Moto Custom 750cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Diseño clásico, motor potente y cómoda para rutas largas."}
    ]

    fila_4 = [
        {"nombre": "Moto Naked 300cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto ligera, maniobrable y perfecta para principiantes."},
        {"nombre": "Moto Touring 800cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Para viajes largos con confort y maleteros grandes."},
        {"nombre": "Moto Off-Road 500cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto robusta para rutas extremas y terrenos difíciles."},
        {"nombre": "Moto Electrica 2000W", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto eléctrica de mayor potencia, ideal para ciudad y suburbios."}
    ]

    fila_5 = [
        {"nombre": "Moto Trial 300cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Alta maniobrabilidad y resistencia para saltos y obstáculos."},
        {"nombre": "Moto Scooter 200cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Scooter con motor eficiente, ágil para ciudad."},
        {"nombre": "Moto Deportiva 1000cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto de alta velocidad y gran rendimiento en carretera."},
        {"nombre": "Moto Custom 1000cc", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Moto cruiser con motor potente y diseño elegante."}
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
    contenido.controls.append(ft.Text("MOTOS", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
