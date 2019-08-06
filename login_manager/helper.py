import sqlite3

conn = sqlite3.connect('login.db')


def create_db_table():
    """ Builds the sqlite db table to store the user information """
    curs = conn.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS users(first_name,last_name,username,email,phone_number,password)')
    conn.commit()


def create_user_db(user):
    """ SQL Insert statement that preserves parameter safety"""
    keys = ','.join(user.keys())
    ques = ','.join(list('?'*len(user)))
    values = tuple(user.values())
    curs = conn.cursor()
    curs.execute('INSERT INTO users ('+keys+') VALUES ('+ques+')', values)
    conn.commit()


def find_user_db(username):
    """ SQL Select statement that preserves parameter safety"""
    print("username = [%s]" % username)
    curs = conn.cursor()
    curs.execute('SELECT password FROM users WHERE username =?;', (username,))
    print(curs.fetchone())
    return curs.fetchone()
