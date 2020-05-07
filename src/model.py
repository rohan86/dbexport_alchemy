from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    level = Column(Integer, nullable=False)
    published = Column(Boolean, nullable=False)
    created_on = Column(TIMESTAMP)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_on = Column(TIMESTAMP)