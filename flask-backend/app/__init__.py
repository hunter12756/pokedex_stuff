from flask import Flask, request
from app.config import Config
import os
from sqlalchemy import update, delete
from ..models import Item

# import statement for CSRF

from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)

app.config.from_object(Config)

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


# @app.route('/items/<int:id>')
# def update_item_form(id):



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
