from os import getenv
from werkzeug.security import generate_password_hash
from database.db import connect_db,initialize_db
from dotenv import load_dotenv
load_dotenv()

def create_admin_user(db):
    db = connect_db()
    hashed_password = generate_password_hash(getenv('password'))
    db.execute("INSERT INTO users (name, email, phone_number, password, role) VALUES (?, ?, ?, ?, ?)",
               ('admin', 'your email', 'your phone number', hashed_password, 'admin'))
    db.commit()
    print("Admin user created successfully.")
    
if __name__ == '__main__':
    db = initialize_db()
    create_admin_user(db)
# -*- coding: utf-8 -*-
# SQL statements for initializing the database