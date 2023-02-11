import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "marcos213", hashlib.sha256("senhamarcos".encode()).hexdigest()
username2, password2 = "joao", hashlib.sha256("cachorro887".encode()).hexdigest()
username3, password3 = "robo999", hashlib.sha256("azul7531".encode()).hexdigest()
username4, password4 = "estudante47", hashlib.sha256("estudospython".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()