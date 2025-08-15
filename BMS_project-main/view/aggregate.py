from view.base import BaseView
class AggregateView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("all")
        self.set_commands_description({
            "help": "Show this help message",
            "Attendee help": "Show help messages for Attendee table",
            "Banquet help": "Show help messages for Banquet table",
            "Meal help": "Show help messages for Meal table",
            "Staff help": "Show help messages for Staff table",
        })