from .db import db
from enum import Enum
from .pokemon_type import PokemonType
import json
from enum import Enum


class Pokemon(db.Model):
    __tablename__='pokemons'

    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.Enum(PokemonType))
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Numeric(3,2))
    catch_rate = db.Column(db.Numeric(3,2))
    captured = db.Column(db.Boolean)

    #relationships
    #One pokemon has MANY items
    items_pokemon = db.relationship("Item", back_populates='pokemon_items')

    @property
    def captured_image_url(self):
        unknown = '/images/unknown.png'
        if self.captured:
            return self.image_url
        else:
            return unknown

    @property
    def parsed_moves(self):
        if self.moves:
            return json.loads(self.moves)
        else:
            return None

    @parsed_moves.setter
    def parsed_moves(self, value):
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

    def to_json(self):
        return json.dumps(self.to_dict(), cls=EnumEncoder)
