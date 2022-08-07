import sqlite3


conn = sqlite3.connect("z_1.db")
cursor = conn.cursor()
a = int(input())
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT,col_3 INTEGER) ''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES('HELLO','WORLD',?)''',(a,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
for i in k:
    i = list(i)
    h = 0
    print(' '.join(str(h) for h in i))