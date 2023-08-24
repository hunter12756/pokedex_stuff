from .db import db
from enum import Enum
from pokemon_type import types
import json

from images import *
class Pokemon(db.Models):
    __tablename__='pokemons'

    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.Enum(types))
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Numeric(3,2))
    catch_rate = db.Column(db.Numeric(3,2))
    captured = db.Column(db.Boolean)


    #relationships
    #One pokemon has MANY items
    items = db.relationship("Item",back_populates='pokemon',as_alias='pokemon')

    def validate(self):
        if self.number < 1:
            raise ValueError("Number must be greater than 1")
        if self.attack < 0 or self.attack > 100:
            raise ValueError("Attack must be between 0 and 100")
        if self.defense < 0 or self.defense > 100:
            raise ValueError("Defense must be between 0 and 100")
        if len(self.name) < 3 or len(self.name) > 255:
            raise ValueError("Name must be between 3 and 255 characters")
        if self.encounter_rate < 0 or self.encounter_rate > 100:
            raise ValueError("Encounter rate must be between 0 and 100")
        if self.catch_rate < 0 or self.catch_rate > 100:
            raise ValueError("Catch rate must be between 0 and 100")


    @property
    def image_url(self):
        unknown = '/images/unknown.png'
        if self.captured:
            return self.image_url
        else:
            return unknown

    @property
    def moves(self):
        if self.moves:
            return json.loads(self.moves)
        else:
            return None
    @moves.setter
    def moves(self,value):
        self.moves = json.dumps(value)


    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'attack': self.attack,
            'defense': self.defense,
            'image_url': self.image_url,
            'name': self.name,
            'type': self.type,
            'moves': self.moves,
            'encounter_rate': self.encounter_rate,
            'catch_rate': self.catch_rate,
            'captured': self.captured
        }
