import json
import sqlite3

from const.CONSTANTS import default_account, default_settings, ENCODING


def reset():
    with open('data/account.json', 'w') as account:
        json.dump(default_account, account)

    with open('data/settings.json', 'w') as settings:
        json.dump(default_settings, settings)

    with open('data/times.txt', 'w') as times:
        times.write('')

    con = sqlite3.connect("data.db")
    cur = con.cursor()

    with open('data/create_db.sql', 'r', encoding=ENCODING) as sql_file:
        sql = sql_file.read()
    result = cur.executescript(sql)
    con.close()


if __name__ == '__main__':
    reset()
