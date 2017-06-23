from flask_wtf import Form
from wtforms import RadioField, validators

class FilterForm(Form):
    category = RadioField('category', [validators.Required()], choices=[('novels', 'novels'),('shortstories', 'short stories')], default='novels')
