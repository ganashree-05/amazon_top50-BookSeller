from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# User Model
class User(db.Model):
    __tablename__ = 'users'  # Correct table name declaration

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"


# Book Model
class Book(db.Model):
    __tablename__ = 'books'  # You should also define the table name for the Book model

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each book entry
    name = db.Column(db.String(100), nullable=False)  # Book name
    author = db.Column(db.String(100), nullable=False)  # Author of the book
    user_rating = db.Column(db.Float, nullable=False)  # Rating from users (e.g., 4.5, 3.8, etc.)
    reviews = db.Column(db.Text, nullable=True)  # Reviews for the book
    price = db.Column(db.Float, nullable=False)  # Price of the book
    year = db.Column(db.Integer, nullable=False)  # Year of publication
    genre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Book {self.name}>"


# Cart Model (for shopping cart functionality)
class Cart(db.Model):
    __tablename__ = 'carts'  # Define table name for cart model

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)  # Link to Book model
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=False)  # Link to User model (optional but recommended)

    # Relationship to Book (one cart entry is associated with one book)
    book = db.relationship('Book', backref='cart_entries', lazy=True)

    # Relationship to User (one cart entry belongs to one user)
    user = db.relationship('User', backref='cart_entries', lazy=True)

    def __repr__(self):
        return f"<Cart {self.id}, Book {self.book.name}, User {self.user.email}>"
