from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/signup/Register/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('../users.db')
        cursor = conn.cursor()

        try:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Registration successful'})
        except sqlite3.IntegrityError:
            conn.close()
            return jsonify({'success': False, 'message': 'Username or email already exists'})
    else:
        return render_template('signup/Register/index_signup.html')

if __name__ == '__main__':
    app.run(debug=True)
