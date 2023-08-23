import flet as ft
from ..Domain.TaskModel import TaskModel

class TaskItem(ft.UserControl):
    
    def __init__(self, task_data_model: TaskModel, on_status_change, on_delete, on_save):
        super().__init__()
        self.task_data=task_data_model
        self.on_status_change=on_status_change
        self.on_delete=on_delete
        self.on_save=on_save

    def build(self):
        self.display_task = ft.Checkbox(
            label=self.task_data.name,
            value=self.task_data.completed,
            on_change=self.status_changed
            )
        self.edit_name = ft.TextField(width=350)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
            self.display_task,
            ft.Row(            
            controls=[
                ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.edit_click),
                ft.IconButton(ft.icons.DELETE_OUTLINED, on_click=self.delete_click)
                ])
        ])

        self.edit_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            visible=False,
            controls=[
            self.edit_name,
            ft.Row(        
            controls=[            
                ft.IconButton(ft.icons.CHECK, on_click=self.save_click)                
                ])
        ])

        return ft.Column(controls=[self.display_view, self.edit_view])
    
    def status_changed(self, e):
        self.task_data.completed = self.display_task.value
        self.on_status_change(self.task_data)

    def edit_click(self, e):
        self.display_view.visible=False
        self.edit_view.visible=True
        self.edit_name.value=self.display_task.label
        self.update()

    def save_click(self, e):
        self.edit_view.visible=False
        self.display_view.visible=True        
        self.task_data.name=self.edit_name.value
        self.display_task.label=self.task_data.name
        self.on_save(self.task_data)
        self.update()

    def delete_click(self, e):
        self.on_delete(self)
