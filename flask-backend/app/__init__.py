from flask import Flask, request, render_template, jsonify
from flask_migrate import Migrate
from app.config import Config
import os
import json
from decimal import Decimal
from enum import Enum
from sqlalchemy import update, delete, insert
from .forms.items_form import ItemForm
from .forms.pokemon_form import PokemonForm
from .models.pokemon import Pokemon
from .models.item import Item
from .models.db import db

# import statement for CSRF

from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# after request code for CSRF token injection


class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(item.to_dict())


@app.route('/pokemon')
def list_pokemon():
    pokemons = Pokemon.query.all()
    pokemon_list = [pokemon.to_dict() for pokemon in pokemons]
    print('pokemon == ', pokemon_list)
    return json.dumps(pokemon_list, cls=EnumEncoder)


@app.route('/pokemon/<int:id>')
def pokemon_detail(id):
    res = Pokemon.query.get(id)
    pokemon = res.to_dict()
    return json.dumps(pokemon, cls=EnumEncoder)


@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print(form.validate_on_submit())
    print("Name:", form.data['name'])
    print("Type:", form.data['type'])
    if form.validate_on_submit():
        new_pokemon = Pokemon(
            number = form.data['number'],
            attack = form.data['attack'],
            defense	 = form.data['defense'],
            image_url = form.data['image_url'],
            name = form.data['name'],
            type = form.data['type'],
            moves = form.data['moves'],
            encounter_rate = form.data['encounter_rate'],
            catch_rate = form.data['catch_rate'],
            captured = form.data['captured']
        )
        db.session.add(new_pokemon)
        db.session.commit()

        return 'created new pokemon'
    else:
        errors = []
        for field, error_list in form.errors.items():
            errors.extend([f"{field}: {error}" for error in error_list])

        return ', '.join(errors)


@app.route('/pokemon/<int:id>', methods=['DELETE'])
def delete_pokemon(id):
    pokemon = Pokemon.query.get(id)
    if pokemon:
        db.session.delete(pokemon)
        db.session.commit()
        return json.dumps({'message': 'Pokemon deleted successfully'}), 200
    else:
        return json.dumps({'message': 'Pokemon not found'}), 404
