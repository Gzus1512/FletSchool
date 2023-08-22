import flet as ft
from ..Res.Strings import Strings
from ..Res.Colors import Colors
from Logic.Task.App.TaskItem import TaskItem
import Logic.Task.Domain.GetTasksUseCase as GetUseCase
import Logic.Task.Domain.InsertTaskUseCase as InsertUseCase

class TasksApp(ft.UserControl):

    def __init__(self, show_snackbar):
        super().__init__()        
        self.show_snackbar=show_snackbar

    def build(self):
        self.text_field = ft.TextField(width=350, color=Colors.FWG, label=Strings.TEXT_FIELD_ADD_TASK_LABEL)
        self.add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_click)
        self.tasks = ft.Column()
        self.items_left = ft.Text()

        task_items = GetUseCase.get_tasks()
        count = 0
        if task_items is None:
            self.items_left.value = f"{count} active item(s) left"
            # self.show_snackbar("Can not find tasks")
        else:            
            for item_task in task_items:
                task = TaskItem(
                    task_name=item_task.name,
                    task_status_change=self.task_status_change,
                    task_delete=self.task_delete,
                    is_checked=item_task.is_checked
                    )
                self.tasks.controls.append(task)

                if not item_task.is_checked:
                    count += 1

            self.items_left.value = f"{count} active item(s) left"        

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed")],
        )

        task_row = ft.Column(
            controls=[
            ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[self.text_field, self.add_button]
            ),
            self.filter,
            self.tasks,
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                self.items_left,
                ft.OutlinedButton(
                    text="Clear completed", on_click=self.clear_clicked
                ),
                ]
            )
        ])
        return task_row
    
    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def tabs_changed(self, e):
        self.update()

    def add_click(self, e):        
        task = TaskItem(
            task_name=self.text_field.value,
            task_status_change=self.task_status_change,
            task_delete=self.task_delete
            )
        inserted = InsertUseCase.insert_tasks(task)
        if inserted is None:
            self.show_snackbar("Can not add task")
        else:
            self.tasks.controls.append(task)
            self.text_field.value=Strings.EMPTY_VALUE
            self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.show_snackbar(f"Task {task.display_task.label} has been deleted")
        self.update()

    def task_status_change(self):
        self.update()
