from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, URL


class ItemForm(FlaskForm):
    happiness = IntegerField('Happiness')
    image_url = StringField('Image Url', validators=[DataRequired(), URL(), Length(max=255)])
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    price = IntegerField('Price', validators=[DataRequired()])
    pokemon_id = IntegerField('Pokemon Id', validators=[DataRequired()])
    submit = SubmitField('Submit')
