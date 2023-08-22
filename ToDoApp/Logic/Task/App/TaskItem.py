import flet as ft

class TaskItem(ft.UserControl):
    
    def __init__(self, task_name, task_status_change, task_delete, is_checked = False):
        super().__init__()
        self.completed = is_checked
        self.task_name=task_name
        self.task_status_change=task_status_change
        self.task_delete=task_delete

    def build(self):
        self.display_task = ft.Checkbox(
            label=self.task_name,
            value=self.completed,
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
        self.completed = self.display_task.value
        self.task_status_change()

    def edit_click(self, e):
        self.display_view.visible=False
        self.edit_view.visible=True
        self.edit_name.value=self.display_task.label
        self.update()

    def save_click(self, e):
        self.edit_view.visible=False
        self.display_view.visible=True
        self.display_task.label=self.edit_name.value        
        self.update()

    def delete_click(self, e):
        self.task_delete(self)
