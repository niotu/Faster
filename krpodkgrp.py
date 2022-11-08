import sqlite3

con = sqlite3.connect('data.db')

cur = con.cursor()

with open('create_db.sql', 'r', encoding='utf-8') as sql_file:
    sql = sql_file.read()
result = cur.executescript(sql)
con.close()
