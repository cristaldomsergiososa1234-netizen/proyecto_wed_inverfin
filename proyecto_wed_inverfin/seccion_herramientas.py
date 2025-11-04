# seccion_herramientas.py
import flet as ft

def seccion_herramientas(page: ft.Page, main_container: ft.Column):
    """
    Sección de Herramientas con 5 filas y 4 productos por fila.
    Colores adaptados a blanco, azul y amarillo para Inverfin.
    """

    # Limpiamos contenido previo
    main_container.controls.clear()

    # --- Productos por fila ---
    fila_1 = [
        {"nombre": "Taladro Inalámbrico 18V", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Taladro potente con batería recargable y luz LED integrada."},
        {"nombre": "Amoladora Angular 115mm", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Ideal para cortar, desbastar y pulir con discos de 115mm."},
        {"nombre": "Sierra Circular 1200W", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Sierra portátil para cortes precisos en madera y paneles."},
        {"nombre": "Juego de Destornilladores 20 Piezas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Destornilladores de diferentes tamaños y tipos para todo uso."}
    ]

    fila_2 = [
        {"nombre": "Llave Inglesa Ajustable", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Llave robusta con ajuste rápido para distintos tamaños de tuercas."},
        {"nombre": "Martillo de Carpintero 500g", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Martillo ligero y ergonómico para trabajos de carpintería."},
        {"nombre": "Nivel de Burbuja 60cm", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Nivel resistente para trabajos de construcción y decoración."},
        {"nombre": "Cinta Métrica 5m", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cinta métrica con cierre automático y carcasa resistente."}
    ]

    fila_3 = [
        {"nombre": "Llaves Allen 10 Piezas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Juego de llaves hexagonales de acero para montaje y mantenimiento."},
        {"nombre": "Sierra de Mano 22''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Sierra manual para cortar madera y materiales blandos."},
        {"nombre": "Alicates Universales 200mm", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Alicates resistentes para cortar y sujetar con precisión."},
        {"nombre": "Pistola de Calor 2000W", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Herramienta ideal para decapado de pintura y termorretracción."}
    ]

    fila_4 = [
        {"nombre": "Compresor de Aire 24L", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Compresor portátil con manómetro y regulador de presión."},
        {"nombre": "Llave de Torque 1/2''", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Llave de torque precisa para mecánica y ensamblaje."},
        {"nombre": "Cepillo Manual de Alambre", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cepillo resistente para limpiar superficies metálicas."},
        {"nombre": "Guantes de Trabajo", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Guantes resistentes para protección en trabajos manuales."}
    ]

    fila_5 = [
        {"nombre": "Sierra de Calar 450W", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Sierra versátil para cortes curvos y rectos en madera y plástico."},
        {"nombre": "Caja de Herramientas 50 Piezas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Set completo con herramientas básicas para el hogar y taller."},
        {"nombre": "Brocas para Taladro 13 Piezas", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Juego de brocas de diferentes tamaños para madera, metal y plástico."},
        {"nombre": "Cúter Profesional", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg", "descripcion": "Cúter resistente con cuchilla retráctil y agarre ergonómico."}
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
    contenido.controls.append(ft.Text("HERRAMIENTAS", size=32, weight="bold", color="#FFD600"))

    # Agregar filas de productos
    for fila in filas:
        contenido.controls.append(
            ft.Row(controls=[crear_tarjeta(prod) for prod in fila], alignment="spaceEvenly")
        )

    # Agregamos al main_container
    main_container.controls.append(contenido)
    main_container.update()
