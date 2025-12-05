# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Category, Business, Product, Consumer

engine = create_engine("sqlite:///db/app.db")
Session = sessionmaker(bind=engine)
session = Session()

def seed():
    # Add categories
    cat1 = Category(type="Electronics")
    cat2 = Category(type="Groceries")

    session.add_all([cat1, cat2])
    session.commit()

    # Add businesses
    biz1 = Business(name="TechZone", location="Nairobi", category=cat1)
    biz2 = Business(name="FreshMart", location="Thika", category=cat2)

    session.add_all([biz1, biz2])
    session.commit()

    # Add products
    p1 = Product(name="Laptop", price=55000, business=biz1)
    p2 = Product(name="Headphones", price=2500, business=biz1)
    p3 = Product(name="Bananas", price=120, business=biz2)

    session.add_all([p1, p2, p3])
    session.commit()

    # Add consumers
    c1 = Consumer(name="John Doe", location="Nairobi", phone="0700000000")
    c2 = Consumer(name="Alice", location="Kiambu", phone="0712345678")

    session.add_all([c1, c2])
    session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
