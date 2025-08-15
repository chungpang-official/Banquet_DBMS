import sqlite3
class MealModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        MealModel.__db_connection = db_connection
        cursor = MealModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/meal/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        MealModel.__db_connection.commit()
        
    @staticmethod
    def list_all():
        cursor = MealModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/meal/query_all.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command)
            return cursor.fetchall()
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
    
    @staticmethod
    def insert(**kwargs):
        cursor = MealModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/meal/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs)) # **this part needs to format keyword arguments
            MealModel.__db_connection.commit()
            return ["Meal record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]