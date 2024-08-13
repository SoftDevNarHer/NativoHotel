import sqlite3

def check_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for user in users:
        print(user)
    conn.close()

check_users()