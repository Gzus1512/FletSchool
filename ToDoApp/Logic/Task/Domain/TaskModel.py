from dataclasses import dataclass

@dataclass
class TaskModel:
    id: int = 0
    name: str = ""
    completed: bool = False

def model_to_data(task_model):
    data_task = (task_model.name, task_model.completed)
    return data_task

def data_to_model(data_task_list):
    task_model_list = []
    for task in data_task_list:
        task_model_list.append(
            TaskModel(id=task[0], name=task[1], completed=bool(task[2]))
        )
    return task_model_list
