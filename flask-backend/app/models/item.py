from .db import db

class Item(db.Model):
    __tablename__='items'

    id = db.Column(db.Integer,primary_key=True)
    happiness = db.Column(db.Integer)
    image_url = db.Column(db.String(255),nullable=False)
    name = db.Column(db.String(255),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    pokemon_id = db.Column(db.Integer,db.ForeignKey("pokemons.id"))

    #relationships
    #many items belong to ONE pokemon
    pokemon = db.relationship("Pokemon", back_populates='items')

    def to_dict(self):
        return {
            'id': self.id,
            'happiness': self.happiness,
            'image_url': self.image_url,
            'name': self.name,
            'price': self.price,
            'pokemon_id': self.pokemon_id,
        }
