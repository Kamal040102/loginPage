import sqlite3
import string
import random
import datetime

global upper;
global lower;
global num;
global var;

upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
var = upper + lower + num

def insertUser(username, email, password):
    key = f"{datetime.datetime.now().strftime('%d%m%Y%H%M%S')}{''.join(random.sample(var, 20))}"
    con = sqlite3.connect("login.db")
    cur = con.cursor()
    cur.execute("insert into users (api_key, username, email, password) values (?,?,?,?)",(key, username, email, password))
    con.commit()
    con.close()

def retrieveUser():
    con = sqlite3.connect("login.db")
    cur = con.cursor()
    cur.execute("select * from users")
    users = cur.fetchall()
    con.close()
    return users