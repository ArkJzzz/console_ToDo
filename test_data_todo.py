#!/usr/bin/python3

import sqlite3

connection = sqlite3.connect('todo_db.sqlite')
cursor = connection.cursor()

cursor.execute('''INSERT INTO Task 
	(task)
	VALUES
	("test1"),
	("test2"),
	("test3"),
	("test4")
	''')

connection.commit()

cursor.execute('''UPDATE Task SET dt_close = CURRENT_TIMESTAMP WHERE  id = 4 ''')
connection.commit()

cursor.close()
connection.close()