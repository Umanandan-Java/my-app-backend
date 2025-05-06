# backend/db/config.py

import mysql.connector

def get_db():
    # Change these values to your MySQL credentials
    conn = mysql.connector.connect(
        host="localhost",          # MySQL host
        user="root",    # Your MySQL username
        password="chromePassword12",  # Your MySQL password
        database="pd"    # The database name
    )
    cursor = conn.cursor(dictionary=True)
    return conn, cursor
