import psycopg2
# install PostGREs in windows first
# go to 'pgadmin4.exe' from start and crate a new database to work with

# 1. Connect to a database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close database connection

def create_table():

    conn = psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    # Here we should declare that if there's not any database then create otherwise don't create
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")     # REAL means float
    conn.commit()
    conn.close()

def insert(item,quantity,price):
        conn = psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")   # if you don't have a database file, than it will create this file
        cur = conn.cursor()
        # Here we should declare that if there's not any database then create otherwise don't create any
        cur.execute("INSERT INTO store VALUES('%s','%s','%s')" %(item,quantity,price))      # its prone to SQL injections
        #OR
        #cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
        conn.commit()
        conn.close()


def view():
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))       # remember to insert a "," after entity, if there's only one entity
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s , price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()


create_table()          # check with 'pgadmin4' exe
ite = input("Enter the ITEM")
quan= input("Enter its quantity")
pri = input("Enter its price")
insert(ite,quan,pri)
delete("Banana")
insert("Wine Glass", 12, 3.5)
insert("Water Glass", 7, 16)
delete("Water Glass")
update("Wine Glass", 5, 7.5)

print(view())
