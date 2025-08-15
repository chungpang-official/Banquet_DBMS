import sqlite3
from model.maintain import MaintainModel
from utils.miscellaneous.smart_input import smart_input
class MaintainController:
    __view = None
    __model = None
    @staticmethod
    def init(db_connection: sqlite3.Connection):
        MaintainController.__model = MaintainModel(db_connection)
        
    @staticmethod
    def create(*args):
        kwargs = smart_input(*args, **{
            "present": None,
            "staff_no": None,
            "bin": None,
        })
        MaintainController.__model.insert(**kwargs)