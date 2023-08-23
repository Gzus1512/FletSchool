import flet as ft
from ..Res.Strings import Strings
from ..Res.Colors import Colors
from Logic.Task.App.TaskItem import TaskItem
from Logic.Task.Domain.TaskModel import TaskModel
import Logic.Task.Domain.GetTasksUseCase as GetUseCase
import Logic.Task.Domain.InsertTaskUseCase as InsertUseCase
import Logic.Task.Domain.UpdateTaskUseCase as UpdateUseCase
import Logic.Task.Domain.DeleteTaskUseCase as DeleteUseCase

class TasksApp(ft.UserControl):

    def __init__(self, show_snackbar):
        super().__init__()        
        self.show_snackbar=show_snackbar

    def build(self):
        self.text_field = ft.TextField(width=350, color=Colors.FWG, label=Strings.TEXT_FIELD_ADD_TASK_LABEL)
        self.add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_click)
        self.tasks = ft.Column()
        self.items_left = ft.Text()

        task_data_list = GetUseCase.get_tasks()
        count = 0
        if task_data_list is None:
            self.items_left.value = f"{count} active item(s) left"
            # self.show_snackbar("Can not find tasks")
        else:            
            for task_data_model in task_data_list:
                task = TaskItem(
                    task_data_model=task_data_model,
                    on_status_change=self.task_status_change,
                    on_delete=self.task_delete,
                    on_save=self.task_save_name
                    )
                self.tasks.controls.append(task)

                if not task.task_data.completed:
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
                or (status == "active" and task.task_data.completed == False)
                or (status == "completed" and task.task_data.completed)
            )
            if not task.task_data.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.task_data.completed:
                self.task_delete(task)

    def tabs_changed(self, e):
        self.update()

    def add_click(self, e):
        task_to_insert = TaskModel(name=self.text_field.value)
        inserted_id = InsertUseCase.insert_task(task_to_insert)
        
        if inserted_id is None:
            self.show_snackbar("Can not add task")
        else:
            task_to_insert.id=inserted_id

            task = TaskItem(
                task_data_model=task_to_insert,
                on_status_change=self.task_status_change,
                on_delete=self.task_delete,
                on_save=self.task_save_name
                )

            self.tasks.controls.append(task)
            self.text_field.value=Strings.EMPTY_VALUE
            self.update()

    def task_delete(self, task: TaskItem):
        DeleteUseCase.delete_task(task.task_data.id)
        self.tasks.controls.remove(task)
        self.show_snackbar(f"Task {task.task_data.name} has been deleted")
        self.update()

    def task_status_change(self, task: TaskModel):
        UpdateUseCase.set_task_completed(task)
        self.update()

    def task_save_name(self, task: TaskModel):
        UpdateUseCase.edit_task_name(task)
        self.show_snackbar(f"Task successfully edited: {task.name}")
