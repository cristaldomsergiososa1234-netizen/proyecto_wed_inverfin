# seccion_bicicletas.py
import flet as ft

def seccion_bicicletas(page: ft.Page, main_container: ft.Column):
    """
    Sección de Bicicletas con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Bicicleta Montaña 26''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Bicicleta robusta para senderos y caminos irregulares."},
        {"nombre": "Bicicleta Urbana 28''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ligera y cómoda para traslados en ciudad."},
        {"nombre": "Bicicleta Eléctrica 250W", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Asistencia eléctrica para mayor facilidad en subidas y recorridos largos."},
        {"nombre": "Bicicleta Plegable 20''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Compacta y práctica, ideal para transporte y almacenamiento."}
    ]

    fila_2 = [
        {"nombre": "Bicicleta Carretera 700C", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Diseño aerodinámico y ligera para velocidad en rutas asfaltadas."},
        {"nombre": "Bicicleta BMX 20''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Perfecta para saltos, trucos y parques de BMX."},
        {"nombre": "Bicicleta MTB 29''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Suspensión completa para terrenos difíciles y rutas largas."},
        {"nombre": "Bicicleta Híbrida 28''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Versátil para ciudad y caminos de tierra ligera."}
    ]

    fila_3 = [
        {"nombre": "Bicicleta Infantil 16''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Segura y ligera, ideal para los más pequeños."},
        {"nombre": "Bicicleta Montaña 27.5''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Con frenos de disco y suspensión delantera."},
        {"nombre": "Bicicleta Urbana 26''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cómoda y resistente para el uso diario."},
        {"nombre": "Bicicleta Plegable 24''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Compacta y fácil de guardar en apartamentos."}
    ]

    fila_4 = [
        {"nombre": "Bicicleta Carretera Carbono", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ligera y rápida, ideal para competición y entrenamiento."},
        {"nombre": "Bicicleta BMX Pro 20''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Construcción resistente para trucos y saltos extremos."},
        {"nombre": "Bicicleta MTB 24V", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cambio de 24 velocidades para todo tipo de terrenos."},
        {"nombre": "Bicicleta Eléctrica City", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ideal para ciudad, asistencia eléctrica y batería duradera."}
    ]

    fila_5 = [
        {"nombre": "Bicicleta Híbrida Pro", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Combinación de confort y rendimiento para todo tipo de rutas."},
        {"nombre": "Bicicleta Infantil 20''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Segura y divertida para niños de 6 a 10 años."},
        {"nombre": "Bicicleta Montaña 29''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ruedas grandes y suspensión para rutas complicadas."},
        {"nombre": "Bicicleta Plegable Eléctrica", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Compacta, eléctrica y perfecta para ciudad."}
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
    contenido.controls.append(ft.Text("BICICLETAS", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
