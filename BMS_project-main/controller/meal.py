import sqlite3
from model.meal import MealModel
from view.meal import MealView
class MealController:
    __view = None
    __model = None
    @staticmethod
    def init(db_connection: sqlite3.Connection):
        MealController.__model = MealModel(db_connection)
        MealController.__view = MealView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
        if command == "help":
            MealController.__view.help()
