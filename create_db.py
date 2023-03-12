from database import Base, engine

# from models import *
from models.item import Item
from models.product import Product
from models.salesorder import SalesOrder


print("Creating database ...")

Base.metadata.create_all(engine)
