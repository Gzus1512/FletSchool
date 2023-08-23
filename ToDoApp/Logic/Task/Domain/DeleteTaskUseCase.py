from Data.DataBaseRepository import DataBaseRepository as data_base_repository

def delete_task(task_id):
    dbr = data_base_repository()
    deleted = dbr.delete_task(task_id)

    return deleted