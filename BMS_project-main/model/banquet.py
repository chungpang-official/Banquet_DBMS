import sqlite3
from utils.auth.decorators import admin_required, authenticated_required

class BanquetModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        BanquetModel.__db_connection = db_connection
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        BanquetModel.__db_connection.commit()
        
    @staticmethod
    @authenticated_required
    def list_all():
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/query_all.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        results = cursor.fetchall()
        return results
        
        
    @staticmethod
    @admin_required
    def insert(return_instance=False, **kwargs):
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs)) # **this part needs to format keyword arguments
            BanquetModel.__db_connection.commit()
            if return_instance:
                print("cursor.lastrowid: ", cursor.lastrowid)
                return cursor.lastrowid
            return ["Banquet record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
    @staticmethod
    @admin_required
    def update(**kwargs):
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs)) # **this part needs to format keyword arguments
            BanquetModel.__db_connection.commit()
            return ["Banquet record updated successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]