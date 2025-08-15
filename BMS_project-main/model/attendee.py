import sqlite3
from utils.auth.decorators import admin_required
from utils.exceptions.ForbiddenException import ForbiddenException
from settings import start_session
class AttendeeModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        AttendeeModel.__db_connection = db_connection
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        AttendeeModel.__db_connection.commit()
        
    @staticmethod
    def login(**kwargs):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/auth/query_user_by_credentials.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command.format(**kwargs))
        result = cursor.fetchone()
        if result is None:
            return ["Invalid username or password"]
        else:
            start_session(**kwargs)
            return ["Login successful"]
    
    @staticmethod
    def insert(**kwargs):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs))
            AttendeeModel.__db_connection.commit()
            return ["Attendee record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
    @staticmethod
    def update(**kwargs):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs))
            AttendeeModel.__db_connection.commit()
            return ["Attendee record updated successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
    @staticmethod
    @admin_required
    def get_information_by_email(email_address):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/query_by_email.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(email_address=email_address))
            return cursor.fetchone()
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
    @staticmethod
    @admin_required
    def update_information_by_email(**kwargs):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/update_by_email.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs))
            return cursor.fetchone()
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
        