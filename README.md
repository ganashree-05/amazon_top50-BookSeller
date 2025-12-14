# Amazon Top 50 Book Seller 📚

## 📌 Project Overview

The **Amazon Top 50 Book Seller** is a **Flask-based web application** that simulates an online book store inspired by Amazon. The project allows users to register, log in, browse books, add them to a cart, perform checkout, and visualize book price analysis using interactive charts.

This project demonstrates **full-stack development** concepts including backend development with Flask, database management using SQLAlchemy, user authentication, session handling, and data visualization using Plotly.

---

## 🎯 Features

* User Registration & Login (Authentication)
* Secure password hashing
* Add, edit, delete books (Admin-like functionality)
* Display books on dashboard
* Search books by name
* Add books to cart
* Update cart quantity & remove items
* Checkout with Cash on Delivery option
* Order success confirmation
* Interactive book price analysis using Plotly
* SQLite database integration

---

## 🛠️ Technologies Used

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, Jinja2 Templates
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Authentication:** Werkzeug Password Hashing
* **Visualization:** Plotly
* **Version Control:** Git & GitHub

---

## 🗂️ Database Models

* **User** – Stores user credentials
* **Book** – Stores book details (name, price, author, rating, image)
* **Cart** – Stores cart items mapped to users

---

## 📁 Project Structure

```
amazon_top50-Book-Seller/
│── app.py
│── models/
│   └── models.py
│── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_book.html
│   ├── edit_book.html
│   ├── cart.html
│   ├── checkout.html
│   ├── success.html
│   └── analysis.html
│── static/
│── amazon.db
│── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/amazon_top50-Book-Seller.git
   ```
2. Navigate to the project directory:

   ```bash
   cd amazon_top50-Book-Seller
   ```
3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
4. Install required dependencies:

   ```bash
   pip install flask flask-sqlalchemy werkzeug plotly
   ```
5. Run the Flask application:

   ```bash
   python app.py
   ```
6. Open your browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📊 Data Analysis Module

The **Analysis** page visualizes book prices using an interactive **Plotly bar chart**, allowing users to compare prices of all available books dynamically.

---

## 🔐 Authentication Flow

* New users can register using email and password
* Passwords are securely hashed before storage
* Logged-in users can add books to cart and checkout
* Session management is used to maintain login state

---

## 🚀 Future Enhancements

* Role-based access (Admin & User)
* Online payment gateway integration
* Order history for users
* Recommendation system for books
* Deploy on cloud platform (AWS / Render / Railway)


