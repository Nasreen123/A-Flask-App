from flask import render_template, request
from app import app
from .forms import FilterForm

@app.route('/', methods=['GET', 'POST'])
def index():
    books = [
        {
            'title': 'The God of Small Things',
            'author': 'Arundhati Roy',
            'category': 'novels'
        },
        {
            'title': 'Drown',
            'author': 'Junot Diaz',
            'category': 'shortstories'
        },
        {
            'title': 'A Map of Home',
            'author': 'Randa Jarrar',
            'category': 'novels'
        }
    ]
    form = FilterForm()
    for book in books:
        print(book['category'])
    if request.method == 'POST':
        if form.validate_on_submit() and form.category.data:
            category = form.category.data
            books = [book for book in books if book['category'] == category]
            print(category)
    return render_template('index.html', books=books, form=form)



"""def index():
books = [
    {
        'title': 'The God of Small Things',
        'author': 'Arundhati Roy',
        'category': 'novel'
    },
    {
        'title': 'Drown',
        'author': 'Junot Diaz',
        'category': 'short stories'
    },
    {
        'title': 'A Map of Home',
        'author': 'Randa Jarrar',
        'category': 'novel'
    }
]
return render_template('index.html', books=books)
@app.route('/', methods=['GET', 'POST'])"""
