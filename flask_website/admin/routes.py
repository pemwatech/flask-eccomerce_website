from flask import redirect,render_template, request,url_for,session,flash
from . import admin
from database.db import connect_db
import sqlite3



@admin.route('/search',methods=['POST','GET'])
def search():
    search_item=request.form['q']
    db=connect_db()
    product=db.execute('SELECT * FROM products WHERE product_name=?',(search_item,)).fetchall()
    if product:
        return render_template('products.html',product=product)
    else:
        flash('item not found')
        return render_template('products.html')


@admin.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin.html')

@admin.route('/admin_orders')
def admin_orders():
    db=connect_db()
    cursor=db.cursor()
    cursor.execute('SELECT * FROM orders')
    admin_orders_list=cursor.fetchall()
    return render_template('admin_orders.html', admin_orders_list=admin_orders_list)   

@admin.route('/products')
def products():
    db=connect_db()
    cursor=db.cursor()
    cursor.execute('SELECT * FROM products')
    products=cursor.fetchall()
    return render_template('products.html', products=products)





@admin.route('/add_product',methods=['POST','GET'])
def add_product():
    product_name=request.form['product_name']
    product_price=request.form['product_price']
    image_url=request.form['image_url']
    product_description=request.form['product_description']
    db=connect_db()
    product=db.execute('SELECT * FROM products WHERE product_name=? AND product_price=? AND image_url=? AND product_description=?',(product_name,product_price,image_url,product_description)).fetchall()
    if product:
        flash('product already exist')
        return render_template('add_product_form.html')
        db.close()

    try:
        product_price=int(product_price)
        db=connect_db()
        cursor=db.cursor()
        cursor.execute('INSERT INTO products (product_name,image_url,product_price,product_description ) VALUES (?,?,?,?)',
                    (product_name,image_url,product_price,product_description))
        db.commit()
        message='Product added successfully'
        flash(message)
        return render_template('add_product_form.html')
    except Exception as e:
        flash(f'{e}')
        return render_template('add_product_form.html')
    
@admin.route('/add_product_form')
def add_product_form():   
    return render_template('add_product_form.html')

    

