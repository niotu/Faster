import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

sql = ('PRAGMA foreign_keys = off;'
       'BEGIN TRANSACTION;'

       'DROP TABLE IF EXISTS texts;'

       'CREATE TABLE texts ('
       '    id   INTEGER PRIMARY KEY AUTOINCREMENT,'
       'text TEXT'
       ');')
result = cur.executescript(sql)
con.close()
