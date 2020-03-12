import sqlite3

def connect():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):      # its (variable="") to take care as the user will input ony one of these
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
#insert("The Earth", "John Smith", 1978, 56423987264 )
#insert("Harry Potter", "J.K.Rowlings", 1992, 9853157619 )

#delete(2)
#update(3,"The Earth", "John Smith", 2012, 56423987264)
#print(view())
#print(search(title="1984"))
