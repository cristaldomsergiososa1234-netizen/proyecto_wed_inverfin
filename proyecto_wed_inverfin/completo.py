import flet as ft
from flet import Icons

# === Datos de usuario ===
USUARIOS = {"sergio": "12345"}

# === Portal de Inverfin ===
def portal_inverfin(page: ft.Page):

    # --- Función para cerrar sesión ---
    def cerrar_sesion(e):
        page.controls.clear()
        page.appbar = None
        main(page)
        page.update()

    contenido = ft.Column(expand=True, spacing=30, horizontal_alignment="center")

    contenido_scroll = ft.Column(
        controls=[contenido],
        scroll="auto",   # permite scroll
        expand=True
    )

    # --- Función para mostrar sucursales ---
    def mostrar_sucursales(producto):
        page.dialog = ft.AlertDialog(
            title=ft.Text(f"Sucursales con {producto['nombre']}"),
            content=ft.Column([
                ft.Text(f"{suc}: {precio}") for suc, precio in zip(producto["sucursales"], producto["precios"])
            ]),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: page.dialog.close())]
        )
        page.dialog.open = True
        page.update()

    # --- Función para mostrar productos de una categoría ---
    def mostrar_productos_categoria(categoria):
        contenido.controls.clear()  # limpiar el contenido actual
        contenido.controls.append(ft.Text(f"{categoria}s", size=32, weight="bold", color="#D71920", text_align="center"))
        contenido.controls.append(generar_productos(categoria))  # usa tu función existente generar_productos
        page.update()

    # --- Función para mostrar detalle de producto ---
    def mostrar_detalle_producto(producto):
        contenido.controls.clear()
        detalle = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Image(src=producto["img"], width=300, height=300, fit=ft.ImageFit.COVER),
                    padding=10
                ),
                ft.Column(
                    controls=[
                        ft.Text(producto["nombre"], size=24, weight="bold", color="#D71920", text_align="center"),
                        ft.Text(f"Categoría: {producto['categoria']}", size=18, text_align="center"),
                        ft.Text(f"Descripción: {producto['descripcion']}", size=16, text_align="justify"),
                        ft.Text(f"Precio: {producto['precio']}", size=18, weight="bold", color="#007700", text_align="center"),
                        ft.Text(f"Sucursales: {', '.join(producto['sucursales'])}", size=16, text_align="center"),
                        ft.ElevatedButton("Ubicar", on_click=lambda e: mostrar_sucursales(producto), bgcolor="#FFD700", color="black"),
                        ft.ElevatedButton(
                            "Volver a la categoría",
                            on_click=lambda e, cat=producto["categoria"]: mostrar_productos_categoria(cat),
                            bgcolor="#0033A0",
                            color="white"
                        )
                    ],
                    spacing=10,
                    alignment="center",
                    horizontal_alignment="center",
                    expand=True
                )
            ],
            spacing=20,
            vertical_alignment="center",
            alignment="center"
        )
        contenido.controls.append(detalle)
        page.update()

    # --- Función para generar productos ---
    def generar_productos(categoria):
        productos_por_categoria = {
            "Electrodoméstico": [
                {"nombre": "Heladera Whirlpool 340L", "categoria":"Electrodoméstico", "descripcion":"Heladera de bajo consumo con freezer", "precio":"G. 5.000.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Ciudad del Este","Encarnación"], "precios":["G. 5.000.000","G. 5.100.000","G. 4.950.000"]},
                {"nombre": "Cocina Longvie 56cm", "categoria":"Electrodoméstico", "descripcion":"Cocina a gas con horno amplio", "precio":"G. 3.500.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Luque","San Lorenzo"], "precios":["G. 3.500.000","G. 3.600.000","G. 3.450.000"]},
                {"nombre": "Lavarropas Samsung 9Kg", "categoria":"Electrodoméstico", "descripcion":"Lavarropas automático de 9Kg", "precio":"G. 4.200.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Capiatá","San Lorenzo"], "precios":["G. 4.200.000","G. 4.250.000"]},
                {"nombre": "Aire Acondicionado LG", "categoria":"Electrodoméstico", "descripcion":"Aire acondicionado split 3000F", "precio":"G. 3.800.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Ciudad del Este","Encarnación"], "precios":["G. 3.800.000","G. 3.750.000"]},
                {"nombre": "Microondas Panasonic", "categoria":"Electrodoméstico", "descripcion":"Microondas de 25L con grill", "precio":"G. 1.200.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Encarnación"], "precios":["G. 1.200.000","G. 1.180.000"]},
                {"nombre": "Freezer Vertical", "categoria":"Electrodoméstico", "descripcion":"Freezer vertical de gran capacidad", "precio":"G. 2.500.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Luque","Encarnación"], "precios":["G. 2.500.000","G. 2.450.000"]},
                {"nombre": "Cafetera eléctrica", "categoria":"Electrodoméstico", "descripcion":"Cafetera de 12 tazas con timer", "precio":"G. 450.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Luque"], "precios":["G. 450.000","G. 460.000"]},
                {"nombre": "Extractor de jugos", "categoria":"Electrodoméstico", "descripcion":"Extractor potente y silencioso", "precio":"G. 750.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Luque","Encarnación"], "precios":["G. 750.000","G. 760.000","G. 740.000"]},
                {"nombre": "Plancha de ropa", "categoria":"Electrodoméstico", "descripcion":"Plancha a vapor profesional", "precio":"G. 300.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Luque","Encarnación"], "precios":["G. 300.000","G. 295.000"]}
            ],
            "Mueble": [
                {"nombre": "Sillón Reclinable Relax", "categoria":"Mueble", "descripcion":"Sillón cómodo con reclinación eléctrica", "precio":"G. 1.800.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Luque"], "precios":["G. 1.800.000","G. 1.850.000"]},
                {"nombre": "Mesa de Comedor Roble", "categoria":"Mueble", "descripcion":"Mesa de comedor para 6 personas", "precio":"G. 2.200.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Encarnación"], "precios":["G. 2.200.000","G. 2.180.000"]},
                {"nombre": "Cama Queen Sommier", "categoria":"Mueble", "descripcion":"Cama con sommier incluido y colchón", "precio":"G. 3.000.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Luque","Encarnación"], "precios":["G. 3.000.000","G. 2.950.000"]},
                {"nombre": "Placard Moderno", "categoria":"Mueble", "descripcion":"Placard de 4 puertas con estantes", "precio":"G. 2.500.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Luque"], "precios":["G. 2.500.000","G. 2.450.000"]},
                {"nombre": "Silla Ergonómica", "categoria":"Mueble", "descripcion":"Silla ergonómica de oficina", "precio":"G. 450.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Luque","Encarnación"], "precios":["G. 450.000","G. 440.000"]},
                {"nombre": "Escritorio Minimalista", "categoria":"Mueble", "descripcion":"Escritorio moderno para estudio o trabajo", "precio":"G. 750.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Encarnación"], "precios":["G. 750.000","G. 740.000"]},
                {"nombre": "Biblioteca de madera", "categoria":"Mueble", "descripcion":"Biblioteca con estantes y puertas", "precio":"G. 1.300.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Luque"], "precios":["G. 1.300.000","G. 1.280.000"]},
                {"nombre": "Mesa de noche", "categoria":"Mueble", "descripcion":"Mesa de noche de 2 cajones", "precio":"G. 400.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Luque","Encarnación"], "precios":["G. 400.000","G. 390.000"]},
                {"nombre": "Sofá cama", "categoria":"Mueble", "descripcion":"Sofá cama de 2 plazas, plegable", "precio":"G. 1.600.000",
                 "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                 "sucursales":["Asunción","Encarnación"], "precios":["G. 1.600.000","G. 1.580.000"]}
            ],
            # --- Productos Dispositivos ---
            "Dispositivo": [
                {"nombre": "Laptop HP Pavilion", "categoria":"Dispositivo", "descripcion":"Laptop de 15.6 pulgadas con 16GB RAM", "precio":"G. 4.500.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Luque"], "precios":["G. 4.500.000","G. 4.480.000"]},
                {"nombre": "Tablet Samsung Galaxy", "categoria":"Dispositivo", "descripcion":"Tablet de 10.4 pulgadas con S-Pen", "precio":"G. 2.100.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Encarnación"], "precios":["G. 2.100.000","G. 2.080.000"]},
                {"nombre": "Smartphone Xiaomi 12", "categoria":"Dispositivo", "descripcion":"Teléfono con cámara de 108MP", "precio":"G. 2.800.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Luque","San Lorenzo"], "precios":["G. 2.800.000","G. 2.780.000","G. 2.790.000"]},
                {"nombre": "Smartwatch Apple Watch 8", "categoria":"Dispositivo", "descripcion":"Reloj inteligente con GPS y ECG", "precio":"G. 3.200.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Luque"], "precios":["G. 3.200.000","G. 3.180.000"]},
                {"nombre": "Auriculares Bose QC35", "categoria":"Dispositivo", "descripcion":"Auriculares con cancelación de ruido", "precio":"G. 1.500.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Encarnación"], "precios":["G. 1.500.000","G. 1.480.000"]},
                {"nombre": "Cámara Canon EOS R", "categoria":"Dispositivo", "descripcion":"Cámara mirrorless profesional", "precio":"G. 7.200.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Luque"], "precios":["G. 7.200.000","G. 7.150.000"]},
                {"nombre": "Disco Duro Externo 2TB", "categoria":"Dispositivo", "descripcion":"Almacenamiento portátil USB 3.0", "precio":"G. 550.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Luque"], "precios":["G. 550.000","G. 540.000"]},
                {"nombre": "Router Wi-Fi 6", "categoria":"Dispositivo", "descripcion":"Router de alta velocidad con cobertura amplia", "precio":"G. 650.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Encarnación"], "precios":["G. 650.000","G. 640.000"]},
                {"nombre": "Monitor 24\" LED", "categoria":"Dispositivo", "descripcion":"Monitor Full HD con soporte ajustable", "precio":"G. 900.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Luque","San Lorenzo"], "precios":["G. 900.000","G. 890.000"]}
            ],

            # --- Productos Motocicletas ---
            "Moto": [
                {"nombre": "Moto Yamaha FZ-S", "categoria":"Moto", "descripcion":"Motocicleta deportiva 150cc", "precio":"G. 18.500.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Encarnación"], "precios":["G. 18.500.000","G. 18.400.000"]},
                {"nombre": "Moto Honda CB125", "categoria":"Moto", "descripcion":"Motocicleta urbana 125cc", "precio":"G. 15.200.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Luque"], "precios":["G. 15.200.000","G. 15.150.000"]},
                {"nombre": "Moto Bajaj Pulsar 150", "categoria":"Moto", "descripcion":"Motocicleta deportiva 150cc", "precio":"G. 16.800.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["San Lorenzo","Capiatá"], "precios":["G. 16.800.000","G. 16.750.000"]},
                {"nombre": "Moto Suzuki Gixxer", "categoria":"Moto", "descripcion":"Motocicleta 155cc con estilo deportivo", "precio":"G. 17.500.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","Luque"], "precios":["G. 17.500.000","G. 17.450.000"]},
                {"nombre": "Moto KTM Duke 200", "categoria":"Moto", "descripcion":"Motocicleta 200cc con diseño agresivo", "precio":"G. 21.000.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Encarnación","Capiatá"], "precios":["G. 21.000.000","G. 20.950.000"]},
                {"nombre": "Moto Honda CRF250", "categoria":"Moto", "descripcion":"Motocross 250cc para off-road", "precio":"G. 23.500.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","San Lorenzo"], "precios":["G. 23.500.000","G. 23.450.000"]},
                {"nombre": "Moto Yamaha MT-03", "categoria":"Moto", "descripcion":"Motocicleta naked 321cc", "precio":"G. 27.000.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Luque","Encarnación"], "precios":["G. 27.000.000","G. 26.950.000"]},
                {"nombre": "Moto Bajaj Avenger 220", "categoria":"Moto", "descripcion":"Motocicleta cruiser 220cc", "precio":"G. 19.800.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Asunción","San Lorenzo"], "precios":["G. 19.800.000","G. 19.750.000"]},
                {"nombre": "Moto Hero Splendor", "categoria":"Moto", "descripcion":"Motocicleta económica 125cc", "precio":"G. 14.500.000",
                "img":"https://upload.wikimedia.org/wikipedia/commons/3/3f/Placeholder_view_vector.svg",
                "sucursales":["Capiatá","Luque"], "precios":["G. 14.500.000","G. 14.450.000"]}
            ],

        }
        productos = productos_por_categoria.get(categoria, [])
        return ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=ft.Column([
                        ft.ElevatedButton(
                            content=ft.Image(src=p["img"], width=200, height=150, fit=ft.ImageFit.COVER),
                            on_click=lambda e, p=p: mostrar_detalle_producto(p),
                            bgcolor="white"
                        ),
                        ft.Text(p["nombre"], size=16, weight="bold", color="#D71920", text_align="center"),
                    ], horizontal_alignment="center"),
                    padding=10,
                    border_radius=10,
                    bgcolor="#F5F5F5",
                    col={"xs": 12, "sm": 6, "md": 4},
                    alignment=ft.alignment.center,
                    shadow=ft.BoxShadow(blur_radius=6, color="#000000", offset=ft.Offset(2, 2))
                ) for p in productos
            ],
            spacing=10,
            run_spacing=10
        )

    # --- Secciones informativas ---
    def seccion(titulo, texto):
        return ft.Container(
            content=ft.Column([
                ft.Text(titulo, size=22, weight="bold", color="#D71920", text_align="center"),
                ft.Text(texto, size=16, color="#000000", text_align="justify")
            ], spacing=8),
            padding=ft.padding.symmetric(horizontal=40)
        )

    # --- Control de navegación ---
    def cambiar_seccion(index):
        contenido.controls.clear()
        if index == 0:
            contenido.controls.clear()
            contenido.controls.append(ft.Container(
                content=ft.Text("Información Institucional", size=32, weight="bold", color="#D71920", text_align="center"),  # título centrado
                padding=ft.padding.only(top=20, bottom=20)
            ))
            contenido.controls.append(seccion("Sobre la empresa",
                "INVERFIN S.A.E.C.A. fue fundada en 1996 en Coronel Oviedo, Paraguay. "
                "Comenzó como un pequeño local de venta de repuestos y motocicletas, y hoy es una de las principales empresas de retail del país. "
                "Cuenta con presencia en varias ciudades importantes como Asunción, Ciudad del Este, Encarnación y Luque."
            ))
            contenido.controls.append(seccion("Misión",
                "Brindar productos y servicios de calidad a la población paraguaya, facilitando el acceso a bienes esenciales mediante soluciones financieras accesibles."
            ))
            contenido.controls.append(seccion("Visión",
                "Ser reconocidos como la empresa líder en retail a nivel nacional, innovando continuamente en la atención al cliente y en la oferta de productos."
            ))
            contenido.controls.append(seccion("Valores",
                "- Compromiso con la calidad\n- Honestidad y transparencia\n- Innovación y mejora continua\n- Atención centrada en el cliente\n- Responsabilidad social"
            ))
            contenido.controls.append(seccion("Sucursales principales",
                "- Asunción\n- Ciudad del Este\n- Encarnación\n- Luque\n- San Lorenzo\n- Capiatá"
            ))
            contenido.controls.append(seccion("¿Para qué se creó?",
                "Inverfin nació para acercar productos esenciales a las familias paraguayas, especialmente en zonas del interior, mediante créditos accesibles."
            ))
            contenido.controls.append(seccion("¿Qué artículos provee?",
                "- Electrodomésticos\n- Muebles\n- Tecnología\n- Motocicletas\n- Artículos para el hogar y deportivos\n- Línea blanca y marrón"
            ))
        elif index == 1:
            contenido.controls.append(ft.Text("Electrodomésticos", size=32, weight="bold", color="#D71920"))
            contenido.controls.append(generar_productos("Electrodoméstico"))
        elif index == 2:
            contenido.controls.append(ft.Text("Muebles", size=32, weight="bold", color="#D71920"))
            contenido.controls.append(generar_productos("Mueble"))
        elif index == 3:
            contenido.controls.append(ft.Text("Dispositivos", size=32, weight="bold", color="#D71920"))
            contenido.controls.append(generar_productos("Dispositivo"))
        elif index == 4:
            contenido.controls.append(ft.Text("Motocicletas", size=32, weight="bold", color="#D71920"))
            contenido.controls.append(generar_productos("Moto"))
        page.update()

    # --- Menú lateral ---
    drawer = ft.NavigationDrawer(
        bgcolor="#FFD700",
        on_change=lambda e: cambiar_seccion(e.control.selected_index),
        controls=[
            ft.Container(ft.Text("Menú principal", size=18, weight="bold", color="#D71920"), padding=10),
            ft.NavigationDrawerDestination(icon=Icons.INFO, label="Información"),
            ft.NavigationDrawerDestination(icon=Icons.KITCHEN, label="Electrodomésticos"),
            ft.NavigationDrawerDestination(icon=Icons.CHAIR, label="Muebles"),
            ft.NavigationDrawerDestination(icon=Icons.DEVICE_HUB, label="Dispositivos"),
            ft.NavigationDrawerDestination(icon=Icons.DIRECTIONS_BIKE, label="Motocicletas"),
        ]
    )
    page.drawer = drawer

    def abrir_menu(e):
        drawer.open = True
        page.update()

    # --- AppBar ---
    page.appbar = ft.AppBar(
        leading=ft.IconButton(Icons.MENU, on_click=abrir_menu),
        title=ft.Text("INVERFIN S.A.", weight="bold", size=20, color="white"),
        actions=[ft.IconButton(Icons.LOGOUT, tooltip="Cerrar sesión", on_click=cerrar_sesion)],
        center_title=True,
        bgcolor="#0033A0",
    )

    cambiar_seccion(0)
    page.add(contenido_scroll)
    page.update()


# === Login ===
def main(page: ft.Page):
    page.title = "Inicio de Sesión - INVERFIN"
    page.bgcolor = "#F5F5F5"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    usuario = ft.TextField(label="Usuario", width=250)
    contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)
    mensaje = ft.Text("", color="red")

    def iniciar_sesion(e):
        user = usuario.value.strip()
        pwd = contraseña.value.strip()
        if user in USUARIOS and USUARIOS[user] == pwd:
            page.controls.clear()
            portal_inverfin(page)
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            page.update()

    login_box = ft.Container(
        content=ft.Column([
            ft.Text("INVERFIN - Acceso", size=28, weight="bold", color="#0033A0"),
            usuario,
            contraseña,
            ft.ElevatedButton("Ingresar", on_click=iniciar_sesion, bgcolor="#0033A0", color="white"),
            mensaje
        ], alignment="center", horizontal_alignment="center", spacing=15),
        padding=40,
        bgcolor="white",
        border_radius=20,
        shadow=ft.BoxShadow(blur_radius=15, color="#000000", offset=ft.Offset(2, 2))
    )

    page.add(login_box)
    page.update()


ft.app(target=main)
