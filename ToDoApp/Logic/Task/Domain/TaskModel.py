from dataclasses import dataclass

@dataclass
class TaskModel:
    name: str
    is_checked: bool

def item_to_data(task_item):
    data_task = (task_item.task_name, task_item.completed)
    return data_task

def data_to_model(data_task_list):
    task_model_list = []
    for task in data_task_list:        
        task_model_list.append(
            TaskModel(name=task[1], is_checked=bool(task[2]))
        )
    return task_model_list
