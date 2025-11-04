import flet as ft
from db import crear_tablas

# Inicializar DB
crear_tablas()

# Usuarios de prueba para login
USUARIOS = {"admin": "12345"}

def main(page: ft.Page):
    page.title = "INVERFIN"
    page.bgcolor = "#F5F5F5"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # --- Login ---
    usuario = ft.TextField(label="Usuario", width=250)
    contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)
    mensaje = ft.Text("", color="red")

    def iniciar_sesion(e):
        user = usuario.value.strip()
        pwd = contraseña.value.strip()
        if user in USUARIOS and USUARIOS[user] == pwd:
            page.controls.clear()
            portal(page)
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


# --- Portal con menú lateral ---
def portal(page: ft.Page):
    # Contenedor principal donde se cargarán todas las secciones
    main_container = ft.Column(expand=True, spacing=10)
    contenido_scroll = ft.Column(controls=[main_container], scroll="auto", expand=True)
    page.add(contenido_scroll)

    # Función para cambiar sección
    def cambiar_seccion(index):
        main_container.controls.clear()
        if index == 0:
            from seccion_consulta import seccion_consulta
            seccion_consulta(page, main_container)
        elif index == 1:
            from seccion_electrodomesticos import seccion_electrodomesticos
            seccion_electrodomesticos(page, main_container)
        elif index == 2:
            from seccion_muebles import seccion_muebles
            seccion_muebles(page, main_container)
        elif index == 3:
            from seccion_motos import seccion_motos
            seccion_motos(page, main_container)
        elif index == 4:
            from seccion_bicicletas import seccion_bicicletas
            seccion_bicicletas(page, main_container)
        elif index == 5:
            from seccion_tecnologia import seccion_tecnologia
            seccion_tecnologia(page, main_container)
        elif index == 6:
            from seccion_herramientas import seccion_herramientas
            seccion_herramientas(page, main_container)
        elif index == 7:
            from seccion_deportes import seccion_deportes
            seccion_deportes(page, main_container)
        elif index == 8:
            from seccion_airelibre import seccion_airelibre
            seccion_airelibre(page, main_container)
        elif index == 9:
            from seccion_jardineria import seccion_jardineria
            seccion_jardineria(page, main_container)
        elif index == 10:
            from seccion_bebes import seccion_bebes
            seccion_bebes(page, main_container)
        page.update()

    # Drawer (menú lateral)
    drawer = ft.NavigationDrawer(
        bgcolor="#FFD700",
        on_change=lambda e: cambiar_seccion(e.control.selected_index),
        controls=[
            ft.Container(ft.Text("Menú principal", size=18, weight="bold", color="#D71920"), padding=10),
            ft.NavigationDrawerDestination(label="Pedidos / Consulta"),
            ft.NavigationDrawerDestination(label="Electrodomésticos"),
            ft.NavigationDrawerDestination(label="Muebles"),
            ft.NavigationDrawerDestination(label="Motos"),
            ft.NavigationDrawerDestination(label="Bicicletas"),
            ft.NavigationDrawerDestination(label="Tecnología"),
            ft.NavigationDrawerDestination(label="Herramientas"),
            ft.NavigationDrawerDestination(label="Deportes"),
            ft.NavigationDrawerDestination(label="Aire Libre"),
            ft.NavigationDrawerDestination(label="Jardinería"),
            ft.NavigationDrawerDestination(label="Bebés"),
        ]
    )
    page.drawer = drawer

    # AppBar
    def abrir_menu(e):
        drawer.open = True
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.MENU, on_click=abrir_menu),
        title=ft.Text("INVERFIN S.A.", weight="bold", size=20, color="white"),
        actions=[ft.IconButton(ft.Icons.LOGOUT, tooltip="Cerrar sesión", on_click=lambda e: volver_login(page))],
        center_title=True,
        bgcolor="#0033A0",
    )

    # Cargar sección inicial
    cambiar_seccion(0)


def volver_login(page):
    page.controls.clear()
    page.appbar = None
    main(page)
    page.update()


ft.app(target=main)
