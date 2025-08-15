from view.base import BaseView
from utils.exceptions.InadequateArgumentsException import InadequateArgumentsException
def smart_input(*args, **kwargs) -> dict[str, any]: # this is not wrong fyi, kwargs is intentional
    for i, key in enumerate(kwargs.keys()):
        if (i >= len(args)):
            key_name = key.replace('_', ' ')
            print(f"Input {key_name}: ")
            arg_prompt = BaseView.get_argument_prompt(key)
            if arg_prompt:
                print(arg_prompt)
            arg = input()
            if not arg:
                raise InadequateArgumentsException(f"{key_name} can not be null!")
            kwargs[key] = arg
        else:
            kwargs[key] = args[i]
    return kwargs