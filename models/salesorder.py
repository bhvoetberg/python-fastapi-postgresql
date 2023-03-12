from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, Numeric, ForeignKey


class SalesOrder(Base):
    __tablename__ = 'salesorder'
    id = Column(Integer, primary_key=True)
    # One to many relationship
    product_id = Column(Integer, ForeignKey('products.id'))

