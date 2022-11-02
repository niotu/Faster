import sqlite3

con = sqlite3.connect("data/data.db")

cur = con.cursor()

# with open('create_db.sql', 'r', encoding='utf-8') as sql_file:
#     sql = sql_file.read()
# result = cur.executescript(sql)
# print(f"create : {result}")


result = cur.execute(f"""SELECT text FROM texts WHERE id={1}""").fetchone()[0]
print(result)
res = []
# for item in result:
#     res.append(item[0])
# print(res)

con.close()
