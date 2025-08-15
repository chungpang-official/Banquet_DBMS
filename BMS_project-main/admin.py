from settings import enable_admin_mode, check_admin_mode
from main import main as start_app

def main():
    enable_admin_mode()
    start_app()

if __name__ == "__main__":
    main()