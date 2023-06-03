import sqlite3


conn = sqlite3.connect('store.db')
c = conn.cursor()



c.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                price INTEGER
             )''')

c.execute("INSERT OR IGNORE INTO products (name, price) VALUES ('Product 1', 10)")
c.execute("INSERT OR IGNORE INTO products (name, price) VALUES ('Product 2', 20)")
c.execute("INSERT OR IGNORE INTO products (name, price) VALUES ('Product 3', 30)")

price=''
c=0
name=''

q=0
conn.commit()
while True:
    
    print('dobavit 1')
    print('stoimost 2')
    print('vihod 3')
    v=input()
    if v==1:
        name=input()
        price=input()
        c.execute("INSERT OR IGNORE INTO products (name, price) VALUES (?, ?)",(name, price))
        conn.commit()

        
    


