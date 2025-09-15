from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
# A seceret key is necessary for session management and flash messaging
app.secret_key ='some_secret_key'

def get_db_connection():
    conn = sqlite3.connect('workshops.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workshops')
def workshops():
    conn = get_db_connection()
    workshops = conn.execute('SELECT * FROM workshops').fetchall()
    conn.close()
    return render_template('workshops.html', workshops=workshops)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        workshop_id = request.form['workshop_id']

        if not name or not email or not workshop_id:
            flash('All fields are required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO bookings (name, email, workshop_id) VALUES (?, ?, ?)',
                         (name, email, workshop_id))
            conn.commit()
            conn.close()
            flash('Booking successful!')
            return redirect(url_for('index'))

    conn = get_db_connection()
    workshops = conn.execute('SELECT * FROM workshops').fetchall()
    conn.close()
    return render_template('book.html', workshops=workshops)

@app.route('/bookings')
def bookings():
    conn = get_db_connection()
    bookings = conn.execute('''
        SELECT b.id, b.name, b.email, w.title 
        FROM bookings b 
        JOIN workshops w ON b.workshop_id = w.id
    ''').fetchall()
    conn.close()
    return render_template('bookings.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
