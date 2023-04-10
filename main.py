from src.app import App
from src.models.models import create_db

def main():
    create_db()
    App()

if __name__=="__main__":
    main()