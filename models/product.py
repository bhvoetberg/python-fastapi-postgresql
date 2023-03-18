from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, Numeric, ForeignKey


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column('title', String(32))
    in_stock = Column('in_stock', Boolean)
    quantity = Column('quantity', Integer)
    price = Column('price', Numeric)
