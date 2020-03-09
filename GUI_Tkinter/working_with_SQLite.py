import sqlite3

# 1. Connect to a database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close database connection

def create_table():

    conn = sqlite3.connect("lite.db")   # if you don't have a database file, than it will create this file
    cur = conn.cursor()
    # Here we should declare that if there's not any database then create otherwise don't create
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")     # REAL means float
    conn.commit()
    conn.close()

def insert(item,quantity,price):
        conn = sqlite3.connect("lite.db")   # if you don't have a database file, than it will create this file
        cur = conn.cursor()
        # Here we should declare that if there's not any database then create otherwise don't create
        cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
        conn.commit()
        conn.close()

insert("Water Glass", 10, 23.5)
insert("Coffee Cup", 4, 8.5)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
