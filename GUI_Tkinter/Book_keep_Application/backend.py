import sqlite3

def connect():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER,author TEXT, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, year, author, isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)",(title, year, author,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", year="", author="", isbn=""):      # its (variable="") to take care as the user will input ony one of these
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR year=? OR author=? OR isbn=?",(title, year, author, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, year, author, isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, year=?, author=?, isbn=? WHERE id=?",(title, year, author, isbn, id))
    conn.commit()
    conn.close()


connect()
#insert("The Earth", 1978, "John Smith", 56423987264 )
#delete(2)
#update(3,"The Earth", 2012, "John Smith", 56423987264)
#print(view())
#print(search(title="1984"))
