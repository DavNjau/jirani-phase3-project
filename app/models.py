from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Consumer(Base):
    __tablename__ = "consumer"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    phone = Column(String)
    orders = relationship("Order", back_populates="consumer")

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    business_id = Column(Integer)
    orders = relationship("OrderList", back_populates="product")

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    consumer_id = Column(Integer, ForeignKey("consumer.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    consumer = relationship("Consumer", back_populates="orders")
    items = relationship("OrderList", back_populates="order")

class OrderList(Base):
    __tablename__ = "order_list"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, default=1)
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="orders")
