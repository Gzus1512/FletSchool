import os
import sqlite3 as sql

class DataBaseManager():

    def __init__(self):
        self.data_base_path = f'{os.path.dirname(__file__)}/tasks.db'
        print(self.data_base_path)

    def create_table(self, query):

        conexion = sql.connect(self.data_base_path)
        cursor = conexion.cursor()

        # Crear la tabla
        cursor.execute(query)
        
        conexion.commit()
        conexion.close()

    def select(self, query, do_with_data):
        try:
            conexion = sql.connect(self.data_base_path)
            cursor = conexion.cursor()

            # Obtener los datos
            response = cursor.execute(query)
            data = do_with_data(response)

            cursor.close()
            conexion.close()

            return data
        
        except sql.Error as e:
            print("Error executing SELECT query", e)
            return None
    
    def insert(self, query, params):
        try:
            conexion = sql.connect(self.data_base_path)
            cursor = conexion.cursor()            

            # Insertar los datos
            inserted = cursor.execute(query, params)

            conexion.commit()
            conexion.close()

            return inserted
        
        except sql.Error as e:
            print("Error executing Insert", e)
            return None

# dbm = DataBaseManager()
# dbm.create_table(
#     '''CREATE TABLE IF NOT EXISTS tbl_tasks
#     (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     completed BOOLEAN NOT NULL
#     )
#     '''
# )

# task_list = [
#         ("Completar informe", False),
#         ("Hacer la compra", True),
#         ("Ejercicio diario", False)
#     ]
# for task in task_list:
#     dbm.insert("INSERT INTO tbl_tasks (name, completed) VALUES (?, ?)", (task[0], task[1]))