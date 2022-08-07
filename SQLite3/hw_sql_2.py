import sqlite3

a = [12,'number',3456,'world',423,5678]
conn = sqlite3.connect('z_4.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

for i in a:
    if type(i) is str:
        cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''',(i,))
        conn.commit()
        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''',(len(i),))
        conn.commit()
    elif type(i) is int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''',(i,))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO tab_1 (col_1) VALUES ('odd number')''')
            conn.commit()

cursor.execute('''SELECT col_1 FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT col_1 FROM tab_2''')
e = cursor.fetchall()
print(e)
if len(e) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
    conn.commit()
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')
    conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
q = cursor.fetchall()
print(q)
cursor.execute('''SELECT * FROM tab_2''')
r = cursor.fetchall()
print(r)
