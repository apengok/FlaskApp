import sqlite3

DATABASE_URI = "/var/www/FlaskApp/FlaskApp/pythonprogramming.db"
def connection():
    conn = sqlite3.connect(DATABASE_URI)
    
    c = conn.cursor()
    
    return c,conn