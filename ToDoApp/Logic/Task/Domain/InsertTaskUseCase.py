from Data.DataBaseRepository import DataBaseRepository as data_base_repository

def insert_task(task_model):
    dbr = data_base_repository()
    inserted = dbr.insert_task(task_model)

    return inserted