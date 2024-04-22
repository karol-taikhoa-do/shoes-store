from flask import abort, make_response

from shoe_shared.models.ShoeModel import Shoe, shoe_schema, shoes_schema
from shoe_api.config import db

def read_all():
    """Get all shoes in json format"""
    shoes = Shoe.query.all()
    return shoes_schema.dump(shoes)

def get_shoe(name: str):
    """Get a specific shoe in json format"""
    shoe = Shoe.query.filter(Shoe.name == name).one_or_none()

    if shoe is not None:
        return shoe_schema.dump(shoe)
    
    abort(404, f"{name} - Invalid name")

def add_shoe(shoe):
    """Add new shoe to the database and return 201 status code if success,
     else 406"""
    new_name = shoe.get("name")
    existing_shoe = Shoe.query.filter(Shoe.name == new_name).one_or_none()

    if existing_shoe is None:
        new_shoe = shoe_schema.load(shoe, session=db.session)
        db.session.add(new_shoe)
        db.session.commit()
        return shoe_schema.dump(new_shoe), 201
    
    abort(406, f"Shoe with name {new_name} already exist")


def edit_shoe(name: str, new_shoe):
    existing_shoe = Shoe.query.filter(Shoe.name == name).one_or_none()

    if existing_shoe:
        update_shoe = shoe_schema.load(new_shoe, session=db.session)
        existing_shoe.name = update_shoe.name
        db.session.merge(existing_shoe)
        db.session.commit()
        return shoe_schema.dump(existing_shoe), 201
    
    abort(404, f"Shoe with name {name} already exist")

def delete_shoe(name: str):
    existing_shoe = Shoe.query.filter(Shoe.name == name).one_or_none()

    if existing_shoe:
        db.session.delete(existing_shoe)
        db.session.commit()
        return make_response(f"{name} successfully deleted", 200)
    
    abort(404, f"Shoe with name {name} not found")