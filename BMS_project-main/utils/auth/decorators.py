from settings import check_admin_mode, validate_session
from utils.exceptions.ForbiddenException import ForbiddenException

def admin_required(func):
    def wrapper(*args, **kwargs):
        if not check_admin_mode():
            raise ForbiddenException("No permission for this action!")
        func(*args, **kwargs)
    return wrapper

def authenticated_required(func):
    def wrapper(*args, **kwargs):
        validate_session()
        func(*args, **kwargs)
    return wrapper