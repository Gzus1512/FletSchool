from Data.DataBaseRepository import DataBaseRepository as data_base_repository
from .TaskModel import TaskModel

def insert_task(task_name):
    dbr = data_base_repository()
    task_to_insert = TaskModel(name=task_name)
    inserted_id = dbr.insert_task(task_to_insert)

    if inserted_id is None:
        return False
    else:
        task_to_insert.id = inserted_id
        return task_to_insert