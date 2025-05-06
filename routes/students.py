from flask import Blueprint, request, jsonify
from db.config import get_db

students_bp = Blueprint('students', __name__)

@students_bp.route('/api/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    regno = data.get('regno')
    mobile = data.get('mobile')

    if not (name and regno and mobile):
        return jsonify({"error": "Missing fields"}), 400

    conn, cursor = get_db()
    cursor.execute("INSERT INTO students (name, regno, mobile) VALUES (%s, %s, %s)", (name, regno, mobile))
    conn.commit()

    return jsonify({"message": "Student added successfully"}), 201
