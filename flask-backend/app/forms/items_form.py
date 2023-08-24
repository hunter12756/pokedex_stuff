from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, URL


class ItemForm(FlaskForm):
    happiness = IntegerField('Happiness')
    image_url = StringField('Image_Url', validators=[DataRequired(), URL(), Length(max=255)])
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    price = IntegerField('Price', validators=[DataRequired()])
    pokemon_id = IntegerField('Pokemon_Id', validators=[DataRequired()])
