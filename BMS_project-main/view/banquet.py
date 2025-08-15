from view.base import BaseView
class BanquetView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Banquet")
        self.set_commands_description({
            "Banquet help": "Show this help message",
            "Banquet list": "list all the available banquets (login required)"
        })
        self.set_admin_commands_description({
            "Banquet create <name> <date_and_time> <address> <location> <meal_nos> <staff_no> <available> <quota>": "create a banquet record",
            "Banquet update <name> <date_and_time> <address> <location> <meal_nos> <staff_no> <available> <quota>": "update a banquet record"
        })