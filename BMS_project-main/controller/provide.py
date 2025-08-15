import sqlite3
from model.provide import ProvideModel
from utils.miscellaneous.smart_input import smart_input

class ProvideController:
    __model = None
    @staticmethod
    def init(db_connection: sqlite3.Connection):
        ProvideController.__model = ProvideModel(db_connection)
        
    @staticmethod
    def create(*args):
        bin_id = args[0]
        meal_nos = (args[1][1:-1]).replace(' ', '').split(',') # example: [1, 2, 5, 6]
        if (len(meal_nos) < 4):
            print("input at least four different meals!")
            return
        for meal_no in meal_nos:
            ProvideController.__model.insert(**{
                "bin": bin_id,
                "meal": meal_no
            })