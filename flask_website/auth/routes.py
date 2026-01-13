from flask import redirect,url_for,render_template,Blueprint,flash,request,session
from . import auth
from database.db import connect_db
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from dotenv import load_dotenv
import os
load_dotenv()

@auth.route('/register')
def register():
    # Flask will automatically look in the 'templates' folder for about.html
    return render_template('register.html')

@auth.route('/register_user',methods=['POST','GET'])
def register_user():
    if request.method=='POST':
        #get form data
        name=request.form['name']
        email=request.form['email']
        phone_number=request.form['phone_number']
        password1=request.form['password']
        password2=request.form['Confirm_password']
        password=generate_password_hash(password1)
        


        if password1 != password2:
            flash('password mismatch')
            return render_template ('register.html')
        else:
            try:
                db=connect_db()
                users=db.execute('SELECT * FROM users WHERE email=? AND phone_number=? ',(email,phone_number)).fetchall() 
                if users:
                    flash('user already exists')
                    return redirect(url_for('auth.login'))   
                    
                else:
                    #insert data into database
                    db.execute('INSERT INTO USERS(name,email,phone_number,password) VALUES (?,?,?,?)',(name,email,phone_number,password))
                    db.commit()
                    db.close()
                    flash('registration successful')
                    #return render_template('register.html')
                    return redirect ('/login')
            except Exception as e:
                flash(f'{e}')
                return render_template('register.html')
            except sqlite3.IntegrityError as e:
                flash(f'{e}')
                return render_template('register.html')
    
  
@auth.route('/login')
def login():
    # Flask will automatically look in the 'templates' folder for about.html
    
    return render_template('login.html')

@auth.route('/check_users',methods=['POST','GET'])
def check_users():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        db=connect_db()
        user=db.execute('SELECT * FROM users WHERE email=?',(email,)).fetchone()
        if user and user['role'] == 'admin' and check_password_hash(user['password'],password):
            session['admin_id']=user['id']
            session['admin_role']=user['role']
            return redirect(url_for('admin.admin_dashboard'))
           

        elif user and check_password_hash(user['password'],password) and user['role']=='user': 
            session['customer_id']=user['id']
            return redirect(url_for('users.shop'))
            db.close()
        else:
            flash('wrong credentials')
            return render_template('login.html')