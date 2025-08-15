import sqlite3
class ProvideModel:
    __db_connection = None
    def __init__(self, db_connection: sqlite3.Connection):
        ProvideModel.__db_connection = db_connection
        try:
            with open("./model/sql_scripts/provide/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor = ProvideModel.__db_connection.cursor()
        cursor.execute(sql_command)
        ProvideModel.__db_connection.commit()
        
    @staticmethod
    def insert(**kwargs):
        cursor = ProvideModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/provide/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs)) # **this part needs to format keyword arguments
            ProvideModel.__db_connection.commit()
            return ["Meal record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
    
    