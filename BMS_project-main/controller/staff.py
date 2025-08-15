import sqlite3
from model.staff import StaffModel
from view.staff import StaffView
class StaffController:
    __view = None
    __model = None
    @staticmethod
    def init(db_connection: sqlite3.Connection):
        StaffController.__model = StaffModel(db_connection)
        StaffController.__view = StaffView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
        if command == "help":
            StaffController.__view.help()
