import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Consumer, Product, Order, OrderList, Base
from datetime import datetime

engine = create_engine("sqlite:///db/app.db")
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass


@cli.command()
def consumers():
    """List all consumers."""
    session = Session()
    for c in session.query(Consumer).all():
        print(c.id, c.name, c.location, c.phone)


@cli.command()
@click.argument("consumer_id", type=int)
def place_order(consumer_id):
    """Place a new order."""
    session = Session()

    order = Order(consumer_id=consumer_id, created_at=datetime.utcnow())
    session.add(order)
    session.commit()

    click.echo(f"Created Order #{order.id}")

    while True:
        pid = click.prompt("Product ID (x to exit)", default="x")

        if pid == "x":
            break

        qty = click.prompt("Quantity", type=int)
        item = OrderList(order_id=order.id, product_id=int(pid), quantity=qty)
        session.add(item)
        session.commit()

    click.echo("Order complete!")


if __name__ == "__main__":
    cli()
