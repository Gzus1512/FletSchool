from Data.DataBaseRepository import DataBaseRepository as data_base_repository

def get_tasks():
    dbr = data_base_repository()
    tasks_model = dbr.get_tasks()

    return tasks_model