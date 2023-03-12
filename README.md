# python-fastapi-postgresql

## Environment
python -m venv env
source env/bin/activate

## Dependencies
pip install fastapi

pip install uvicorn

pip install sqlalchemy

pip install psycopg2-binary


## Pycharm interpreter settings
pycharm project - settings - python interpreter - add interpreter / local - virtual env


## Console
### Create tables
python create_db.py
### Start app
uvicorn main:app --reload


## Python console
from models import Item

new_item=Item(name="Milk",price=2,description="Nice milk",on_offer=True)


## Console:

python create_db.py

## Furter info
https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

