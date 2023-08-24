from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, URL, NumberRange
from enum import Enum

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

class PokemonForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired(), NumberRange(min=1)])
    attack = IntegerField('Attack', validators=[DataRequired(), NumberRange(min=0, max=100)])
    defense =IntegerField('Defense', validators=[DataRequired(), NumberRange(min=0, max=100)])
    image_url = StringField('Image_Url', validators=[DataRequired(), URL(), Length(max=255)])
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=255)])
    type = SelectField('Type',choices=types, validators=[DataRequired()])
    moves = StringField('Moves', validators=[DataRequired()])
    encounter_rate = FloatField('Encounter Rate', validators= [NumberRange(min=0, max=100)])
    catch_rate = FloatField('Catch Rate', validators= [NumberRange(min=0, max=100)])
    captured = BooleanField('Captured')

    submit = SubmitField('Submit')
