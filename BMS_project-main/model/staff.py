import sqlite3
class StaffModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        StaffModel.__db_connection = db_connection
        cursor = StaffModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/staff/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        StaffModel.__db_connection.commit()
    
    def insert(*args):
        cursor = StaffModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/staff/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(*args)) # **this part needs to format keyword arguments
            StaffModel.__db_connection.commit()
            return ["Staff record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]