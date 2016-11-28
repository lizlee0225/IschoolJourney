'''
code adapted from 2016 FA INFO 290 TA project assignment
'''

import sqlite3 as sql

"""
Database functions:
* Handle information retrieval and database updates
"""

# ---------- User Updates ----------
# Login
def validate_user(email, pwd):
    result = retrieve_user_info(email)
    if result is None: return None
    else:
        result = result[0]
        if result['insecure_password'] == pwd:
            return result['first_name']
        else: return None

# Sign Up
def signup_user(email, fname, lname, pwd):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys = ON')

        sql_command = \
        "INSERT INTO users (email, first_name, last_name, insecure_password, active) VALUES (?, ?, ?, ?, ?)"

        cur.execute(sql_command, (email, fname, lname, pwd, 'TRUE'))
        trip_id = cur.lastrowid
        con.commit()

# Get list of existing users in the system
def get_users():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()

        sql_command = "SELECT first_name, email FROM users"

        db_result = cur.execute(sql_command).fetchall()

    result = []
    for email in db_result:
        result += [(email['email'], email['first_name'] + ' (' + email['email'] + ')')]
    return result

# ---------- Helper Functions ----------
# retrieve password and first name of a user given their email address
def retrieve_user_info(email):
    # SQL statement to query database goes here
    # Returns None if no match is found
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys = ON')

        sql_command = \
        "SELECT first_name, insecure_password \
        FROM users WHERE email = \'" + email + "\'"

        result = cur.execute(sql_command).fetchall()
    if not result:
        return None
    else: return result

# retrieve ID of a user given their email address
def retrieve_user_id(email):
    # SQL statement to query database goes here
    # Returns None if no match is found
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys = ON')

        sql_command = \
        "SELECT user_id \
        FROM users WHERE email = \'" + email + "\'"

        result = cur.execute(sql_command).fetchall()
    if not result:
        return None
    else: return result
