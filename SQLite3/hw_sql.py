import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50),author VARCHAR(30),price DECIMAL(8, 2),amount INT)''')
cursor.execute('''INSERT INTO book(title,author,price,amount)
 VALUES('Way','Jack',12345.78,25)''')
cursor.execute('''INSERT INTO book(title,author,price,amount)
 VALUES('Drive','Fred',145.78,5)''')
cursor.execute('''INSERT INTO book(title,author,price,amount)
 VALUES('End','Gry',125.8,2)''')
conn.commit()
cursor.execute('''SELECT*FROM book''')
k = cursor.fetchall()
for i in k:
    i = list(i)
    h = 0
    print(' '.join(str(h) for h in i))