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


def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))       # remember to insert a "," after entity, if there's only one entity
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=? , price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    conn.close()


insert("Wine Glass", 12, 3.5)
insert("Water Glass", 7, 16)
delete("Water Glass")
update("Wine Glass", 5, 7.5)

print(view())
