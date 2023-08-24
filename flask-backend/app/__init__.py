from flask import Flask, request, render_template
from flask_migrate import Migrate
from app.config import Config
import os
# from sqlalchemy import update, delete
from .forms.items_form import ItemForm
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
    item = Item.query.where(id=id).one()
    print(item)
    return render_template('update_item_form.html', form=form)


@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = update(Item).where(Item.id == id).one()
    data = request.form

    updated_item = (
        update(Item)
        .where(Item.id == id)
        .values(data)
    )

    return updated_item



@app.route('/pokemon')
def list_pokemon():
    pokemon = Pokemon.query.all()
    print(pokemon)
    return pokemon


@app.route('/pokemon/<int:id>')
def pokemon_detail():
    pokemon = Pokemon.query.where(id == id).one()

    print(pokemon)
    return pokemon



@app.route('/pokemon', methods=['POST'])
def pokemon_detail():
    data = request.form
    pokemon = insert(Pokemon).values(data)

    print(pokemon)
    return pokemon



@app.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    data = request.form
    updated_pokemon = update(Pokemon).where(Pokemon.id == id).values(data)

    return updated_pokemon
