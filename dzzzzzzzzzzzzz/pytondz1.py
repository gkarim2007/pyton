import sqlite3


conn = sqlite3.connect('store.db')
c = conn.cursor()



c.execute('''CREATE TABLE IF NOT EXISTS otels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
                
             )''')

c.execute("INSERT OR IGNORE INTO otels (name) VALUES ('otel 1')")

c.execute('''CREATE TABLE IF NOT EXISTS cheloveki (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ima TEXT UNIQUE
                
             )''')

c.execute("INSERT OR IGNORE INTO cheloveki (ima) VALUES ('kolia')")


ima=''
c=0
name=''

q=False
conn.commit()
while True:
    
    print('rigistrirovat 1')
    print('otel 2')
    print('otchet 3')
    c=input()
    if c==1:
        name=input()
        price=input()
        c.execute("INSERT OR IGNORE INTO products (name, price) VALUES (?, ?)",(name, price))
        q=True
    if c==2 and q==True:
        
        


        
    


