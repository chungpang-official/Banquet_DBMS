from settings import check_admin_mode
class BaseView:
    __ARGUMENTS_PROMPT = {}
    
    @property
    def __ADMIN_MODE(self):
        return check_admin_mode()
    
    def set_commands_description(self, dic: dict):
        for key, val in dic.items():
            self.commands_desc[key] = val
    
    def set_admin_commands_description(self, dic: dict):
        for key, val in dic.items():
            self.admin_commands_desc[key] = val
            
    def set_table_name(self, x: str):
        self.table_name = x
    
    @staticmethod
    def add_argument_prompt(dic: dict):
        for key, val in dic.items():
            if key in BaseView.__ARGUMENTS_PROMPT:
                print(f"Warning: prompt for argument <{key}> overwritten to: {val}")
            BaseView.__ARGUMENTS_PROMPT[key] = val
            
    @staticmethod
    def get_argument_prompt(argument_name):
        return BaseView.__ARGUMENTS_PROMPT.get(argument_name)
        
    def get_table_name(self):
        return self.table_name
    
    def help(self):
        print(f"Commands for manipulating {self.get_table_name()} table:")
        for i, key in enumerate(self.commands_desc.keys()):
            print(f"{i+1}. {key}: {self.commands_desc[key]}")
        if self.__ADMIN_MODE:
            for i, key in enumerate(self.admin_commands_desc.keys()):
                if (i == 0):
                    print("\nadmin commands:")
                print(f"{i+1}. {key}: {self.admin_commands_desc[key]}")
            
        
    def __init__(self):
        self.results = []
        self.commands_desc = {}
        self.admin_commands_desc = {}
        
    def display(self):
        for row in self.results:
            print(row)