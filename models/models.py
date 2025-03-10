from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.email}>"



# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(150), nullable=False)  # New field for author
    rating = db.Column(db.Float, nullable=False)  # New field for rating

    def __repr__(self):
        return f"<Book {self.name}>"



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)  # Foreign key for Book
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key for User
    quantity = db.Column(db.Integer, nullable=False)

    # Relationships
    book = db.relationship('Book', backref='cart_entries', lazy=True)
    user = db.relationship('User', backref='cart_entries', lazy=True)

    def __repr__(self):
        return f"<Cart {self.id}, Book {self.book.name}, User {self.user.email}>"



