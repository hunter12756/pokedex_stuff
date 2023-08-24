from flask import Flask, request, render_template, jsonify
from flask_migrate import Migrate
from app.config import Config
import os
import json
from sqlalchemy import update, delete, insert
from .forms.items_form import ItemForm
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

    return json.dumps([p.to_dict() for p in pokemons])


@app.route('/pokemon/<int:id>')
def pokemon_detail(id):
    pokemon = Pokemon.query.get_or_404(id)
    return jsonify(pokemon.to_dict())


@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    data = request.json
    new_pokemon = Pokemon(**data)
    db.session.add(new_pokemon)
    db.session.commit()
    return jsonify(new_pokemon.to_dict())


@app.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    pokemon = Pokemon.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(pokemon, key, value)
    db.session.commit()
    return jsonify(pokemon.to_dict())
