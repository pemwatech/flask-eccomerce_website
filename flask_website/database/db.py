import sqlite3
from dotenv import load_dotenv
import os
load_dotenv()



db=os.getenv('db')
sql=os.getenv('sql')


def initialize_db():
    conn=connect_db()
    with open(sql) as f:
        conn.executescript(f.read())
        conn.commit()
        conn.close()
        return conn
    

def connect_db():
    conn=sqlite3.connect(db)
    conn.row_factory=sqlite3.Row
    return conn
    
