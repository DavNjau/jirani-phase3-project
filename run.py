from app.db_setup import init_db
from cli import main

if __name__ == "__main__":
    init_db()  
    main()     
