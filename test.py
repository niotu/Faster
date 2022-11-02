import sqlite3

con = sqlite3.connect("data/data.db")

cur = con.cursor()

# with open('create_db.sql', 'r', encoding='utf-8') as sql_file:
#     sql = sql_file.read()
# result = cur.executescript(sql)
# print(f"create : {result}")


result = cur.execute(f"""SELECT * FROM texts """).fetchall()

for item in result:
    print(item)

con.close()
