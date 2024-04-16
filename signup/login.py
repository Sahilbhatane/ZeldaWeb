from flask import Flask, request, jsonify, redirect
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        # Redirect to a success page
        return redirect('/success')
    else:
        # Redirect to a failure page
        return redirect('/failure')

if __name__ == '__main__':
    app.run(debug=True)
