from flask import render_template, redirect, request, session, redirect, url_for, escape
import sqlite3 as sql
import os.path

app = Flask(__name__)
app.database = 'career-map.db' # Name of database

def connect_db():
    return sql.connect(app.database)

def retrieve_class():
    # retrieve top 5 classes 
    g.db = connect_db() # g = flask specific temporary object during a request to store database connection

def insert_review(review):
    # Insert user's review in table course_reviews
    ...

def retrieve_review():
    # display review retrieved from table course_review_vw
    ...

def retrieve_rating():
    # Retrieve average rating from database
    ...


"""
def insert_data(company,email,phone,first_name,last_name,street_address,city,state,country,zip_code):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con: # giving connection a name 'con', 
        con.execute('pragma foreign_keys = ON')
        cur = con.cursor() #associates sql connection, importatnt because cursor allows us to execute sql statements
        cur.execute("INSERT INTO customers (company,email,phone,first_name,last_name) VALUES (?,?,?,?,?)",(company,email,phone,first_name,last_name)) #size will start increasing with more attributes/columns
        con.commit()
        new_cur = con.cursor()
        new_cur.execute("INSERT INTO address (street_address,city,state,country,zip_code,customer_id) VALUES (?,?,?,?,?,?)",(street_address,city,state,country,zip_code,cur.lastrowid))
        con.commit() 

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.execute('pragma foreign_keys = ON')
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select * from customers").fetchall()
    return result #convert all rows in dictionary format for every customer, e.g. Result['Company']

def retrieve_address():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.execute('pragma foreign_keys = ON')
        con.row_factory = sql.Row
        cur = con.cursor()
        result2 = cur.execute("select * from address").fetchall()
    return result2 #convert all rows in dictionary format for every customer, e.g. Result['Company']


##You might have additional functions to access the database
def insert_order(name_of_part,manufacturer_of_part,value):
    with sql.connect("app.db") as con: # giving connection a name 'con', 
        con.execute('pragma foreign_keys = ON')
        cur = con.cursor() 
        cur.execute("INSERT INTO orders (name_of_part,manufacturer_of_part) VALUES (?,?)",(name_of_part,manufacturer_of_part))
        con.commit()
        new_cur=con.cursor()
        new_cur.execute("INSERT INTO customer_order (customer_id, order_id) VALUES (?,?)",(value,cur.lastrowid))

def retrieve_order():
    with sql.connect("app.db") as con:
        con.execute('pragma foreign_keys = ON')
        con.row_factory = sql.Row
        cur = con.cursor()
        result3 = cur.execute("select * from orders").fetchall()
    return result3
