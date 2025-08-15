import sqlite3
class MaintainModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        MaintainModel.__db_connection = db_connection
        cursor = MaintainModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/maintain/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        
        cursor.execute(sql_command)
        MaintainModel.__db_connection.commit()
    
    def insert(**kwargs):
        cursor = MaintainModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/maintain/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs)) # **this part needs to format keyword arguments
            MaintainModel.__db_connection.commit()
            return ["Maintain record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
        