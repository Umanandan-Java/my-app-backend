from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chromePassword12",
    database="pd"
)
cursor = db.cursor()

# Submit user
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    cursor.execute("INSERT INTO students (name, regno, mobile) VALUES (%s, %s, %s)",
                   (data['name'], data['regno'], data['mobile']))
    db.commit()
    return jsonify({'message': 'User added'}), 200

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT id, name, regno, mobile FROM students")
    users = [{'id': row[0], 'name': row[1], 'regno': row[2], 'mobile': row[3]} for row in cursor.fetchall()]
    return jsonify(users)

# Get one user
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor.execute("SELECT name, regno, mobile FROM students WHERE id = %s", (user_id,))
    row = cursor.fetchone()
    return jsonify({'name': row[0], 'regno': row[1], 'mobile': row[2]}) if row else ('', 404)

# Update user
@app.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    cursor.execute("UPDATE students SET name=%s, regno=%s, mobile=%s WHERE id=%s",
                   (data['name'], data['regno'], data['mobile'], user_id))
    db.commit()
    return jsonify({'message': 'User updated'}), 200
#delete user
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor.execute("DELETE FROM students WHERE id = %s", (user_id,))
    db.commit()
    return jsonify({'message': 'User deleted'}), 200
if __name__ == '__main__':
    app.run(debug=True)
