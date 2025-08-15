import sqlite3
from model.attendee import AttendeeModel
from view.attendee import AttendeeView
from utils.exceptions.InadequateArgumentsException import InadequateArgumentsException
from utils.miscellaneous.smart_input import smart_input
from settings import get_session_data
class AttendeeController:
    __view: AttendeeView = None
    __model: AttendeeModel = None
    @staticmethod
    def init(db_connection: sqlite3.Connection):
        AttendeeController.__model = AttendeeModel(db_connection)
        AttendeeController.__view = AttendeeView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0].lower()
        args = args[1:]
        if command == "help":
            AttendeeController.__view.help()
        elif command == 'register':
            AttendeeController.register(*args)
        elif command == 'login':
            AttendeeController.login(*args)
        elif command == 'update':
            AttendeeController.update(*args)
        elif command == 'getByEmail':
            AttendeeController.get_information_by_email(*args)
        
    def __init__(self):
        AttendeeController.init()

    @staticmethod
    def login(*args):
        kwargs = smart_input(*args, **{
            "email_address": None,
            "password": None
        })
        
        AttendeeController.__view.results = AttendeeController.__model.login(**kwargs)
        AttendeeController.__view.display()

    @staticmethod
    def update(*args):
        kwargs = smart_input(*args, **{
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        })
        kwargs["email_address"] = get_session_data("email_address")
        kwargs["password"] = get_session_data("password")
        AttendeeController.__view.results = AttendeeController.__model.update(**kwargs)
        AttendeeController.__view.display()
        
    @staticmethod
    def register(*args):
        kwargs = smart_input(*args, **{
            "email_address": None,
            "password": None,
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        })
        AttendeeController.__view.results = AttendeeController.__model.insert(**kwargs)
        AttendeeController.__view.display()
        
    @staticmethod
    def get_information_by_email(*args):
        AttendeeController.__view.results = AttendeeController.__model.get_information_by_email(args[0])
        AttendeeController.__view.display()
        
    @staticmethod
    def update_information_by_email(*args):
        kwargs = smart_input(*args, **{
            "email_address": None,
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        })
        AttendeeController.__view.results = AttendeeController.__model.update_information_by_email(**kwargs)
        AttendeeController.__view.display()