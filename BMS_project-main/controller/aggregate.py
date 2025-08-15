from controller.attendee import AttendeeController
from controller.banquet import BanquetController
from controller.meal import MealController
from controller.staff import StaffController

from view.aggregate import AggregateView

class AggregateController:
    __view: AggregateView = None
    @staticmethod
    def init(db_connection):
        AttendeeController.init(db_connection)
        BanquetController.init(db_connection)
        MealController.init(db_connection)
        StaffController.init(db_connection)
        AggregateController.__view = AggregateView()
        AggregateController.__view.help()
    
    def __init__(self, db_connection):
        AggregateController.init(db_connection)
        
    @staticmethod
    def redirect(input: str):
        print()
        args = input.split(' ')
        table = args[0].lower() # might as well just make the commands case-insensitive
        if table == "help":
            AggregateController.__view.help()
            return
        args = args[1:]
        if table == "attendee":
            AttendeeController.handle_input(*args)
        elif table == "banquet":
            BanquetController.handle_input(*args)
        elif table == "staff":
            StaffController.handle_input(*args)
        elif table == "meals":
            MealController.handle_input(*args)