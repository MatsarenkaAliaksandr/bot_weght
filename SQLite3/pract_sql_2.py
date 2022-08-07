import sqlite3

conn = sqlite3.connect('name.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT,col_3 INTEGER)''')

# Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES('hello','world',7)''')
# Сохраняем изменения
conn.commit()

# Вы также можете использовать функцию fetchone() для получения первого результата.
a = 'hello'
cursor.execute('''SELECT*FROM tab_1 WHERE col_1='hello' ''')
conn.commit()
k = cursor.fetchone()
print(k)

# Список всех записей отсортированных относительно третьей колонки
cursor.execute('''SELECT*FROM tab_1 ORDER BY col_3 DESC''')
conn.commit()
k = cursor.fetchall()
print(k)

# В нашем случае мы искали по всей таблице записи третьей колонки, которые начинаются с 7
# Знак процента (%) является подстановочным оператором
cursor.execute('''SELECT*FROM tab_1 WHERE col_3 LIKE '7%' ''')
conn.commit()
k = cursor.fetchall()
print(k)