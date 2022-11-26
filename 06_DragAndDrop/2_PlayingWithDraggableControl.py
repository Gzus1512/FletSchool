# let's build the same app again but let's change few `Draggable` properties

import flet as ft

def main(page: ft.Page):
    page.title = "Simple Drag N Drop App"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)

        # update the text inside draggable control
        src.content.content.value = "0"

        # update the text inside drag target control
        e.control.content.content.value = "1"

        # let's update the page
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center
                    ),
                    # `content_when_dragging` will execute when user drags the Draggable
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5
                    ),
                    content_feedback=ft.Text("1"), # this will show only "1" while dragging not the entire container (box)
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center
                    ),
                    on_accept=drag_accept
                )
            ]
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)