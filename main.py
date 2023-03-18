from fastapi import FastAPI, status, HTTPException
from database import SessionLocal
from models.item import Item as ModelItem

from schema import Item as SchemaItem

app = FastAPI()

db = SessionLocal()


@app.get('/items', response_model=list[SchemaItem], status_code=200)
def get_all_items():
    items = db.query(ModelItem).all()

    return items


@app.get('/item/{item_id}', response_model=SchemaItem, status_code=status.HTTP_200_OK)
def get_an_item(item_id: int):
    item = db.query(ModelItem).filter(ModelItem.id == item_id).first()
    return item


@app.post('/items', response_model=SchemaItem,
          status_code=status.HTTP_201_CREATED)
def create_an_item(item: SchemaItem):
    db_item = db.query(ModelItem).filter(ModelItem.name == item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = ModelItem(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db.add(new_item)
    db.commit()

    return new_item


@app.put('/item/{item_id}', response_model=SchemaItem, status_code=status.HTTP_200_OK)
def update_an_item(item_id: int, item: SchemaItem):
    item_to_update = db.query(ModelItem).filter(ModelItem.id == item_id).first()
    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.description = item.description
    item_to_update.on_offer = item.on_offer

    db.commit()

    return item_to_update


@app.delete('/item/{item_id}')
def delete_item(item_id: int):
    item_to_delete = db.query(ModelItem).filter(ModelItem.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
