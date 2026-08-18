import sqlite3
import json

conn = sqlite3.connect('/working_dir/slingshot-shop/shop.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL,
    image TEXT,
    description TEXT
)
''')
c.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id TEXT PRIMARY KEY,
    customer_name TEXT,
    phone TEXT,
    address TEXT,
    shipping_provider TEXT,
    total_amount REAL,
    status TEXT,
    tracking_number TEXT,
    items_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()
conn.close()
print("Database initialized successfully!")
