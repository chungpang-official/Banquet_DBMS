from view.base import BaseView
class StaffView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Staff")
        self.set_commands_description({
            "Staff help": "Show this help message",
        })
        self.set_admin_commands_description({
            "Staff create <first_name> <last_name> <department>": "create a Staff record",
            "Staff update <first_name> <last_name> <department>": "update a Staff record"
        })
        BaseView.add_argument_prompt({
            "staff_no": "Input the staff no. of the contact staff"
        })