import flet as ft
from UI.Views.TasksApp import TasksApp

def main(page: ft.Page):
    page.title="Tasks App by JRB"
    page.window_width=500
    page.window_height=700

    def show_snackbar(message):
        page.snack_bar = ft.SnackBar(ft.Text(message))
        page.snack_bar.open = True
        page.update()

    page.add(TasksApp(show_snackbar))

ft.app(target=main)
