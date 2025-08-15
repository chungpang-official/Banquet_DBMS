from view.base import BaseView
class MealView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Meal")
        self.set_commands_description({
            "Meal help": "Show this help message",
        })
        self.set_admin_commands_description({
            "Meal create <type> <dish_name> <price> <special_cuisine>": "create a Meal record",
            "Meal update <type> <dish_name> <price> <special_cuisine>": "update a Meal record"
        })
        BaseView.add_argument_prompt({
            "meal_nos": 'Input the MealNo in a list (e.g.: "[1, 4, 7, 2]" if the targeted meals is 1, 2, 4 and 7)'
        })