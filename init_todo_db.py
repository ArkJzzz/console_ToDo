#!/usr/bin/python3

import sqlite3

connection = sqlite3.connect('todo_db.sqlite')
cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS Task''')
cursor.execute('''DROP TABLE IF EXISTS Execute_Status''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Task (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
	dt_create TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, 
	task TEXT, 
	dt_close TIMESTAMP DEFAULT NULL)
	''')


connection.commit()

cursor.close()
connection.close()