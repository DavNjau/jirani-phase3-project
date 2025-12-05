from app.db_setup import Session, engine, Base
from app.models import Consumer, Product, Order, OrderList
from datetime import datetime

Base.metadata.create_all(engine)
session = Session()

consumers = [
    Consumer(name="Alice", location="Nairobi", phone="0711111111"),
    Consumer(name="Bob", location="Mombasa", phone="0722222222"),
    Consumer(name="Charlie", location="Kisumu", phone="0733333333")
]
session.add_all(consumers)
session.commit()

products = [
    Product(name="Laptop", business_id=1),
    Product(name="Phone", business_id=2),
    Product(name="Headphones", business_id=1)
]
session.add_all(products)
session.commit()

order1 = Order(consumer_id=1, created_at=datetime.utcnow())
order2 = Order(consumer_id=2, created_at=datetime.utcnow())
session.add_all([order1, order2])
session.commit()

items = [
    OrderList(order_id=1, product_id=1, quantity=1),
    OrderList(order_id=1, product_id=3, quantity=2),
    OrderList(order_id=2, product_id=2, quantity=1)
]
session.add_all(items)
session.commit()

print("Sample data added successfully!")
session.close()
