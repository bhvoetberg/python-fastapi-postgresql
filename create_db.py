from database import Base, engine

from Models.customer import Customer
from Models.item import Item
from Models.product import Product
from Models.salesorder import SalesOrder


print("Creating database ...")

Base.metadata.create_all(engine)
