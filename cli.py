from app.db_setup import Session, engine
from app.models import Consumer, Product, Order, OrderList
from datetime import datetime
import sys

session = Session()

# ------------------------------
# MENU DISPLAY
# ------------------------------
def menu():
    print("\n" + "="*40)
    print("      CONSUMER & ORDER SYSTEM")
    print("="*40)
    print("1. List all consumers")
    print("2. Add a consumer")
    print("3. List all products")
    print("4. Add a product")
    print("5. Create an order")
    print("6. View orders")
    print("0. Exit")
    print("="*40)

# ------------------------------
# MENU FUNCTIONS
# ------------------------------
def list_consumers():
    consumers = session.query(Consumer).all()
    print("\n-- Consumers --")
    for c in consumers:
        print(f"{c.id}: {c.name} | {c.location} | {c.phone}")

def add_consumer():
    name = input("Name: ")
    location = input("Location: ")
    phone = input("Phone: ")
    consumer = Consumer(name=name, location=location, phone=phone)
    session.add(consumer)
    session.commit()
    print("Consumer added!")

def list_products():
    products = session.query(Product).all()
    print("\n-- Products --")
    for p in products:
        print(f"{p.id}: {p.name} | Business {p.business_id}")

def add_product():
    name = input("Product Name: ")
    business_id = input("Business ID: ")
    product = Product(name=name, business_id=business_id)
    session.add(product)
    session.commit()
    print("Product added!")

def create_order():
    consumer_id = input("Consumer ID for order: ")
    order = Order(consumer_id=int(consumer_id), created_at=datetime.now())
    session.add(order)
    session.commit()
    print(f"Created Order ID {order.id}")

    while True:
        product_id = input("Product ID to add (or 'done'): ")
        if product_id.lower() == "done":
            break
        quantity = input("Quantity: ")
        item = OrderList(order_id=order.id, product_id=int(product_id), quantity=int(quantity))
        session.add(item)
        session.commit()
        print("Product added to order.")

    print("Order completed!")

def view_orders():
    orders = session.query(Order).all()
    print("\n-- Orders --")
    for o in orders:
        print(f"\nOrder {o.id} by Consumer {o.consumer_id} at {o.created_at}")
        for item in o.items:
            print(f"   - Product {item.product_id} | Quantity: {item.quantity}")

# ------------------------------
# MAIN LOOP
# ------------------------------
def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            list_consumers()
        elif choice == "2":
            add_consumer()
        elif choice == "3":
            list_products()
        elif choice == "4":
            add_product()
        elif choice == "5":
            create_order()
        elif choice == "6":
            view_orders()
        elif choice == "0":
            print("Goodbye!")
            session.close()
            sys.exit()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
