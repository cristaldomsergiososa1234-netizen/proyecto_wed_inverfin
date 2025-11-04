import flet as ft
from db import obtener_productos

def seccion_airelibre(page: ft.Page):
    contenido = ft.Column(expand=True, spacing=10)

    productos = obtener_productos("Aire Libre")  # Trae productos desde la DB

    # --- Crear filas de 4 productos ---
    filas = []
    for i in range(0, min(len(productos), 20), 4):  # Máximo 20 productos
        fila = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column([
                        ft.Image(src=p[4], width=150, height=100, fit=ft.ImageFit.COVER),  # img
                        ft.Text(p[1], size=14, weight="bold", color="#D71920", text_align="center"),
                        ft.ElevatedButton("Ver detalle", on_click=lambda e, prod=p: mostrar_detalle(prod), bgcolor="#0033A0", color="white")
                    ], horizontal_alignment="center"),
                    padding=5,
                    border_radius=5,
                    bgcolor="#F5F5F5",
                    alignment=ft.alignment.center,
                    shadow=ft.BoxShadow(blur_radius=4, color="#000000", offset=ft.Offset(1, 1))
                )
                for p in productos[i:i+4]
            ],
            spacing=10
        )
        filas.append(fila)

    contenido.controls.extend(filas)

    # --- Función para mostrar detalle ---
    def mostrar_detalle(producto):
        detalle = ft.AlertDialog(
            title=ft.Text(producto[1], weight="bold", color="#D71920"),  # nombre
            content=ft.Column([
                ft.Image(src=producto[4], width=300, height=200, fit=ft.ImageFit.COVER),
                ft.Text(f"Categoría: {producto[2]}"),
                ft.Text(f"Descripción: {producto[3]}"),
                ft.Text(f"Precio: {producto[5]}")
            ], spacing=10),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: page.dialog.close())]
        )
        page.dialog = detalle
        page.dialog.open = True
        page.update()

    return contenido
