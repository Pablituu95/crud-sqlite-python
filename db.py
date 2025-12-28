import sqlite3

def criar_db():
    db = sqlite3.connect('database.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    numero TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL)""")
    db.commit()
    return db