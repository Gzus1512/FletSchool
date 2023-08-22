from .TaskModel import data_to_model
from Managers.DataBaseManager import DataBaseManager as data_base_manager


def get_tasks():
    dbm = data_base_manager()
    tasks_model = dbm.select("SELECT * FROM tbl_tasks ORDER BY id", data_to_model)

    return tasks_model