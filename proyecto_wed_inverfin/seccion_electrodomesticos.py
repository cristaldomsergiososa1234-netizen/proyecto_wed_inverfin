# seccion_electrodomesticos.py
import flet as ft

def seccion_electrodomesticos(page: ft.Page, main_container: ft.Column):
    """
    Sección de electrodomésticos con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos el contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Heladera Side‑by‑Side 550L", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Heladera de gran capacidad con dispensador de agua y hielo."},
        {"nombre": "Congeladora Vertical 300L", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Congeladora de una puerta con estantes ajustables."},
        {"nombre": "Lavarropas Carga Superior 10kg", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Lavarropas automático con 15 programas."},
        {"nombre": "Secadora de Ropa Inverter", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Secadora de alta eficiencia con sensor de humedad."}
    ]

    fila_2 = [
        {"nombre": "Cocina a Gas 5 Hornallas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cocina moderna de 90 cm con horno a gas."},
        {"nombre": "Microondas Sensor 32L", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Microondas con sensor de cocción y modo crujiente."},
        {"nombre": "Horno Eléctrico Multifunción 60cm", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Horno eléctrico con programación digital."},
        {"nombre": "Aspiradora Robot Roomba", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Robot aspirador con mapeo inteligente."}
    ]

    fila_3 = [
        {"nombre": "Aire Acondicionado Split 24000 BTU", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Split frío/calor con conectividad WiFi."},
        {"nombre": "Ventilador de Techo LED", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ventilador de 132 cm con luz LED integrada."},
        {"nombre": "Plancha a Vapor Profesional", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Plancha de suela cerámica con autolimpieza."},
        {"nombre": "Licuadora de Vidrio + 5 Velocidades", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Licuadora potente de 1200 W."}
    ]

    fila_4 = [
        {"nombre": "Freidora de Aire 6L", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Freidora sin aceite con pantalla táctil."},
        {"nombre": "Batidora de Pie KitchenAid", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Batidora de pie con accesorios incluidos."},
        {"nombre": "Sistema de Audio Home Theater", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Home theater con subwoofer inalámbrico."},
        {"nombre": "Televisor OLED 65″ 4K", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "TV OLED 65 pulgadas con 120Hz, HDR10+."}
    ]

    fila_5 = [
        {"nombre": "Enfriador de Vinos 50 Botellas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Enfriador de vinos de 2 zonas con control digital."},
        {"nombre": "Máquina de Café Automática", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cafetera automática con molinillo integrado."},
        {"nombre": "Purificador de Aire HEPA", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Purificador para ambientes de hasta 50 m²."},
        {"nombre": "Calefactor Infrarrojo Digital", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Calefactor con temporizador y termostato remoto."}
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
    contenido.controls.append(ft.Text("ELECTRODOMÉSTICOS", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
