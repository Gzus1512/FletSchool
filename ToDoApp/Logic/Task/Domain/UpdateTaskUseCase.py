from Data.DataBaseRepository import DataBaseRepository as data_base_repository

def set_task_completed(task_data):
    dbr = data_base_repository()
    updated = dbr.set_task_completed(task_data)

    return updated

def edit_task_name(task_data):
    dbr = data_base_repository()
    updated = dbr.edit_task_name(task_data)

    return updated