import os
import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)

# Database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


# Helper function to get database connection
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


# Helper function to close the database connection
@app.teardown_appcontext
def close_db(error):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/book_a_table', methods=['POST'])
def book_a_table():
    db = get_db()
    c = db.cursor()

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']

    c.execute('INSERT INTO reservations (name, email, phone, date, time) VALUES (?, ?, ?, ?, ?)',
              (name, email, phone, date, time))

    db.commit()
    db.close()

    return render_template('success.html')


@app.route('/contact', methods=['POST'])
def contact():
    db = get_db()
    c = db.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Insert data into contacts table
        c.execute("INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
                    (name, email, subject, message))
        db.commit()
        db.close()

        return render_template('success-contact.html')


if __name__ == '__main__':
    app.run(debug=False)
