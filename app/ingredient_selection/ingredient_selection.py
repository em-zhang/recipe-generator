from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired
from flask_babel import _, lazy_gettext as _l

ing_bp = Blueprint('ingredient_selection', __name__, template_folder='templates')
MIN_ING = 3

@ing_bp.route('/', methods=['GET', 'POST'])
def select_ing():
    return render_template('ingredient_selection.html')

'''
validator to check that quantity >= MIN_ING
'''
def quantity_check(form, field):
    if field.data < MIN_ING:
        raise ValidationError('Recipe must have at least 3 ingredients.')

'''
User should choose 2 ingredients and desired
number of ingredients in recipe
'''
class SelectIngForm(FlaskForm):
    quantity = IntegerField(_l('Number of Ingredients In Final Recipe'), validators=[DataRequired(), quantity_check])

    submit = SubmitField(_l('Generate Recipe!'))



