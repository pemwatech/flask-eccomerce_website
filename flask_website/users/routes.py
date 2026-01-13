from . import users
from flask import render_template,request,redirect,url_for,flash,session
from werkzeug.security import check_password_hash,generate_password_hash
from database.db import connect_db

@users.route('/home')
def home():
    return render_template('home.html')

@users.route('/')
def logout():
    
    if 'customer_id' in session:
        session.clear()
        return redirect(url_for('users.shop'))
    elif 'customer_id' not in session:
            return redirect(url_for('users.shop'))

@users.route('/shop' ,methods=['POST','GET'])
def shop():
    
    db=connect_db()
    products=db.execute('SELECT * FROM products').fetchall()
    return render_template('shop.html',products=products)

@users.route('/add_to_cart' ,methods=['POST','GET'])
def add_to_cart():
    if 'customer_id' not in session:
        return redirect(url_for('auth.login'))
    else:
        customer_id=session['customer_id']
        product_id=request.form['product_id']
        db=connect_db()
        product=db.execute('SELECT * FROM cart WHERE product_id=? AND customer_id=?',(product_id,customer_id)).fetchone()
        if product:
            db.execute('UPDATE cart SET quantity=quantity+? WHERE product_id=? AND customer_id=?',(1,product['product_id'],product['customer_id']))
            db.commit()
            return redirect (url_for('users.cart')) 
        else:
            db.execute('INSERT INTO cart (customer_id,product_id) VALUES(?,?)',(customer_id,product_id))
            db.commit()
            return redirect (url_for('users.cart')) 
            
           
    
    
    
@users.route('/cart')
def cart():
    if 'customer_id' not in session:
        return redirect(url_for('auth.login'))
    
    else:
        customer_id=session['customer_id']
        db=connect_db()
        cart_items=db.execute('SELECT cart.product_id,cart.total_amount,cart.quantity,products.product_name,products.product_price,products.image_url FROM cart JOIN products ON cart.product_id = products.id WHERE cart.customer_id=?',(customer_id,)).fetchall()
        total_quantity=sum(item['quantity'] for item in cart_items)
        total_amount=sum(item['quantity'] * item['product_price'] for item in cart_items)
        return render_template('cart.html',cart_items=cart_items,total_amount=total_amount,total_quantity=total_quantity)

    


@users.route('/checkout')
def checkout():
    return render_template('checkout.html')


@users.route('/orders')
def orders():
    if 'customer_id' not in session:
        return redirect(url_for('auth.login'))
    else:
        customer_id=session['customer_id']
        db=connect_db()
        orders=db.execute('SELECT * FROM orders WHERE customer_id=?',(customer_id,)).fetchall()
    return render_template('orders.html')


@users.route('/about')
def about():
    return render_template('about.html')