from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, DateTime
)
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


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    type = Column(String)

    businesses = relationship("Business", back_populates="category")


class Business(Base):
    __tablename__ = "business"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    name = Column(String)
    location = Column(String)

    category = relationship("Category", back_populates="businesses")
    products = relationship("Product", back_populates="business")


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey("business.id"))
    name = Column(String)
    price = Column(Float)

    business = relationship("Business", back_populates="products")
    order_items = relationship("OrderList", back_populates="product")


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
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
