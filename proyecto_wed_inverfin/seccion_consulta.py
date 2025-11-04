import flet as ft
from registros import obtener_pedidos, actualizar_estado_pedido
from datetime import datetime, timedelta
import random

def seccion_consulta(page: ft.Page, main_container: ft.Column):
    main_container.controls.clear()

    contenido = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    buscador = ft.TextField(label="Buscar pedido", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", bgcolor="#0033A0", color="white")
    resultados = ft.Column(spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def cambiar_estado(e, id_pedido, dropdown):
        nuevo_estado = dropdown.value
        actualizar_estado_pedido(id_pedido, nuevo_estado)
        buscar_pedidos(None)

    def buscar_pedidos(e):
        term = buscador.value.strip().lower()
        resultados.controls.clear()
        pedidos = obtener_pedidos()
        if term:
            pedidos = [p for p in pedidos if term in p["producto"].lower()]

        if pedidos:
            for p in pedidos:
                dropdown_estado = ft.Dropdown(
                    width=120,
                    value=p["estado"],
                    options=[
                        ft.dropdown.Option("Pendiente"),
                        ft.dropdown.Option("Proceso"),
                        ft.dropdown.Option("Terminado")
                    ],
                    on_change=lambda e, id_p=p["id_pedido"]: cambiar_estado(e, id_p, e.control)
                )

                dias_espera = random.randint(2, 3)
                fecha_entrega = datetime.now() + timedelta(days=dias_espera)
                fecha_str = fecha_entrega.strftime("%d/%m/%Y")

                tarjeta = ft.Card(
                    content=ft.Container(
                        padding=10,
                        alignment=ft.alignment.center,
                        content=ft.Column([
                            ft.Text(f"Pedido #{p['id_pedido']}", weight="bold"),
                            ft.Text(f"{p['sucursal']} solicita '{p['producto']}' por ${p['precio']}"),
                            ft.Text(f"Fecha estimada de entrega: {fecha_str}", italic=True),
                            dropdown_estado
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ),
                    elevation=3,
                    shadow_color=ft.Colors.BLACK45,
                    width=400
                )
                resultados.controls.append(tarjeta)
        else:
            resultados.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("No se encontraron pedidos")
                )
            )

        resultados.update()

    buscar_btn.on_click = buscar_pedidos

    contenido.controls.append(ft.Row([buscador, buscar_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=10))
    contenido.controls.append(resultados)

    main_container.controls.append(contenido)
    main_container.update()

    buscar_pedidos(None)
