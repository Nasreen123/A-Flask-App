from app import db


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    books = db.relationship("Book")


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
