# main.py
from model import Base
from sqlalchemy import create_engine

def create_db():
    engine = create_engine("sqlite:///db/app.db")
    Base.metadata.create_all(engine)
    print("Database created!")

if __name__ == "__main__":
    create_db()
