import sqlite3


def create_database():
    conn = sqlite3.connect('app_database')
    c = conn.cursor()

    # create a table if not exists that hold users information including id, username, password and email
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text, email text)''')

    # create a table if not exists that hold users purchases
    c.execute('''CREATE TABLE IF NOT EXISTS purchases
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username_id text, product text, price text, date text)''')

    # # delete all rowes in users table
    # c.execute("DELETE FROM users")

    conn.commit()
    conn.close()
