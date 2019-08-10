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
    ques = ','.join(list('?' * len(user)))
    values = tuple(user.values())
    curs = conn.cursor()
    curs.execute('INSERT INTO users (' + keys + ') VALUES (' + ques + ')', values)
    conn.commit()


def find_user_db(username):
    """ SQL Select statement that preserves parameter safety"""
    # try
    # except NoneType
    try:
        curs = conn.cursor()
        curs.execute('SELECT password FROM users WHERE username =?;', (username,))
        password = curs.fetchone()[0]
    except TypeError as e:
        return ''
    return password


def get_user_detail(username):
    """ This SQL SELECT query will retireve the user data we need to verify add on's with. """
    curs = conn.cursor()
    curs.execute('SELECT * FROM users WHERE username =?;', (username,))
    data = curs.fetchone()
    return data
