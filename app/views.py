from flask import render_template, request
from app import app
from .forms import FilterForm, AddForm
import json

@app.route('/', methods=['GET', 'POST'])
def index():
    json_data = open('app/books.json').read()
    books = json.loads(json_data)
    form = FilterForm()
    print books
    if request.method == 'POST':
        if form.validate_on_submit() and form.category.data:
            category = form.category.data
            if category != 'all':
                books = [book for book in books if book['category'] == category]
            print(category)
    return render_template('index.html', books=books, form=form)

@app.route('/add', methods=['GET', 'POST'])
def add():
    json_data = open('app/books.json').read()
    books = json.loads(json_data)
    form = AddForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            author = form.author.data
            category = form.category.data
            book_id = len(books)+1
            book = {"title": title, "author": author, "id": book_id, "category": category}
            books.append(book)
            with open('app/books.json', 'w') as outfile:
                json.dump(books, outfile)
            form.title.data = ""
            form.author.data = ""
            form.category.data = ""
    return render_template('add.html', books=books, form=form)
