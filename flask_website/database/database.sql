PRAGMA foreign_keys = ON;




CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email NOT NULL,
    phone_number TEXT NOT NULL,   
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user'
);

CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    image_url TEXT NOT NULL,
    product_price INTEGER NOT NULL,
    
    product_description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- employers TABLE
CREATE TABLE IF NOT EXISTS employers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employer_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,   
    location TEXT NOT NULL,
    description TEXT NOT NULL,
    created_ast TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ONE ORDER PER CHECKOUT
CREATE TABLE IF NOT EXISTS cart( 
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER DEFAULT 1,
    total_amount INTEGER
);

-- ONE ORDER PER CHECKOUT
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    customer_id INTEGER,
    total_amount INTEGER,
    status TEXT,
    payment_status TEXT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES users(id)
);



-- PRODUCTS INSIDE AN ORDER
CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price INTEGER 
);



