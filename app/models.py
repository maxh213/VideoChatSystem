import sqlite3 as sql

def insert_user(username,password):
    con = sql.connect("../database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO user (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def get_users():
	con = sql.connect("../database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM user")
	users = cur.fetchall()
	con.close()
	return users

def get_user(username):
	con = sql.connect("../database.db")
	cur = con.cursor()
	cur.execute("SELECT username FROM user WHERE username = ?", (username))
	user = cur.fetchone()
	con.close()
	return user

def inset_call(host_user_id,invited_user_id):
    con = sql.connect("../database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO call_history (host_user_id,invited_user_id) VALUES (?,?)", (host_user_id,invited_user_id))
    con.commit()
    con.close()

def get_call_history_for_user(user_id):
	con = sql.connect("../database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM call_history WHERE (host_user_id = ? OR invited_user_id = ?)", (user_id))
	user = cur.fetchall()
	con.close()
	return call_history

def get_call_history():
	con = sql.connect("../database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM call_history")
	user = cur.fetchall()
	con.close()
	return call_history