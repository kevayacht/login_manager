import sqlite3

conn = sqlite3.connect('login.db')


def create_db_table():
    """ Builds the sqlite db table to store the user information """
    curs = conn.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS users(first_name,last_name,username,email,phone_number,password)')
    conn.commit()


def create_user_db(user):
    curs = conn.cursor()
    curs.execute("""INSERT INTO users(first_name,last_name,username,email,phone_number,password) 
    VALUES ('{first_name}','{last_name}','{username}','{email}','{phone_number}','{password}')""".format(**user))
    conn.commit()


def find_user_db():
    curs = conn.cursor()