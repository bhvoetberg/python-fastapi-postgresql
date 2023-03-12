from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, Numeric, ForeignKey


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"name={self.name}"