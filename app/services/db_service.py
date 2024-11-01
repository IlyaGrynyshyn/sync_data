from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from app.models import model


class DataBaseService:
    def __init__(self, db: Session):
        self.db = db

    def get_item_by_id(self, model, item_id: int):
        return self.db.query(model).filter(model.id == item_id).first()

    def get_all_items(self, model):
        return self.db.query(model).all()

    def create_item(self, model, **kwargs):
        new_item = model(**kwargs)
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def update_item(self, model, item_id: int, **kwargs):
        item = self.get_item_by_id(model, item_id)
        if item:
            for key, value in kwargs.items():
                setattr(item, key, value)
            self.db.commit()
            self.db.refresh(item)
        return item

    def delete_item(self, model, item_id: int):
        item = self.get_item_by_id(model, item_id)
        if item:
            self.db.delete(item)
            self.db.commit()
        return item
