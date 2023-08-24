from flask import Flask, request, render_template, jsonify
from flask_migrate import Migrate
from app.config import Config
import os
import json
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


@app.route('/items/<int:id>')
def update_item_form(id):
    form = ItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    item = Item.query.where(id=id).one()
    print(item)
    return render_template('update_item_form.html', form=form)


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
        return json.dumps(pokemon_list, cls=EnumEncoder)



@app.route('/pokemon/<int:id>')
def pokemon_detail(id):
    res = Pokemon.query.get(id)
    pokemon = res.to_dict()
    return json.dumps(pokemon, cls=EnumEncoder)


@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    form = PokemonForm
    form['csrf_token'].data = request.cookies['csrf_token']

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



@app.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    pokemon = Pokemon.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(pokemon, key, value)
    db.session.commit()
    return jsonify(pokemon.to_dict())
