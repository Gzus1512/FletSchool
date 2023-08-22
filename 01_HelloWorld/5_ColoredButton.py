import flet as ft

def main(page: ft.Page):
    def on_hover(e):
        e.control.bgcolor = "orange" if e.data == "true" else "yellow"
        e.control.update()

    page.add(
        ft.ElevatedButton(
            "I'm changing color on hover", bgcolor="yellow", on_hover=on_hover
        )
    )

ft.app(target=main)