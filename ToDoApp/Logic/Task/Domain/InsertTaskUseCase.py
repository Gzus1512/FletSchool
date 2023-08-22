from .TaskModel import item_to_data
from Managers.DataBaseManager import DataBaseManager as data_base_manager

def insert_tasks(task_item):
    dbm = data_base_manager()
    task_to_insert = item_to_data(task_item)
    inserted = dbm.insert('''INSERT INTO tbl_tasks VALUES (?, ?, ?)''', (None, *task_to_insert))

    return inserted