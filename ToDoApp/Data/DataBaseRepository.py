from Logic.Task.Domain.TaskModel import data_to_model, model_to_data
from Data.DataBaseManager import DataBaseManager as data_base_manager

class DataBaseRepository(data_base_manager):

    def get_tasks(self):        
        tasks_model = self.select('''SELECT * FROM tbl_tasks ORDER BY id''', data_to_model)

        return tasks_model

    def insert_task(self, task):
        task_to_insert = model_to_data(task)
        inserted = self.insert('''INSERT INTO tbl_tasks VALUES (?, ?, ?)''', (None, *task_to_insert))

        return inserted
    
    def set_task_completed(self, task):
        updated = self.update('''UPDATE tbl_tasks SET completed = ? WHERE id = ?''', (task.completed, task.id))
        
        return updated
    
    def edit_task_name(self, task):
        updated = self.update('''UPDATE tbl_tasks SET name = ? WHERE id = ?''', (task.name, task.id))
        
        return updated
    
    def delete_task(self, task_id):
        deleted = self.delete('''DELETE FROM tbl_tasks WHERE id = ?''', (task_id,))
        
        return deleted