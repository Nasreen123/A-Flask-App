from flask_wtf import Form
from wtforms import RadioField, StringField, validators

class FilterForm(Form):
    category = RadioField('category', [validators.Required()], choices=[('all', 'all'),('novels', 'novels'),('shortstories', 'short stories')], default='novels')

class AddForm(Form):
    title = StringField('title', [validators.Required()])
    author = StringField('author', [validators.Required()])
    category = RadioField('category', [validators.Required()], choices=[('unknown', 'unknown'),('novels', 'novels'),('shortstories', 'short stories')], default='novels')
