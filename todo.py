#!/usr/bin/python3

# Программа для составления списка дел.
# Создана для того, чтобы разобраться как работать с БД SQLite из Python
# (C) ArkJzzz, 2017-11-19

import sqlite3


# Функция вывода списка задач
def view_tasks():
	print("id" + '\t' + "date, time" + '\t\t' + "task")
	for row in cursor.execute('SELECT id, dt_create, task from Task WHERE dt_close IS NULL'):
		print(str(row[0])+ '\t' + str(row[1]) + '\t' + row[2])

# Функция добавления задачи
def add_task(task_text):
	cursor.execute('''INSERT INTO Task (task) VALUES ('%s')'''%(task_text))
	connection.commit()

# Функция изменения задачи
def modify_task(task_text, task_id):
	cursor.execute('''UPDATE Task SET task = '%s' WHERE  id = %s '''%(task_text, task_id))
	connection.commit()

# Функция завершения задачи
def done_task(task_id):
	cursor.execute('''UPDATE Task SET dt_close = CURRENT_TIMESTAMP WHERE  id = %s'''%(task_id))
	connection.commit()

def main():

	choice = None
	while choice != "0":
		print("""
		
		ToDo-list:
		0 - Закрыть
		1 - Вывести список задач
		2 - Добавить задачу
		3 - Изменить задачу
		4 - Завершить задачу
		""")

		choice = input("Ваш выбор: ")
		print()
		# Закрыть
		if choice == "0":
			print("До свидания.")
		# Вывести список задач
		elif choice == "1":
			view_tasks()
		# Добавить задачу
		elif choice == "2":
			task_text = input("Введите текст задачи: ")
			add_task(task_text)
			view_tasks()
		# Изменить задачу
		elif choice == "3":
			task_id = input("Введите id задачи, которую хотите изменить: ")
			task_text = input("Введите текст задачи: ")
			modify_task(task_text, task_id)
			view_tasks()
		# Завершить задачу
		elif choice == "4":
			task_id = str(input("Введите id задачи, которую хотите завершить: "))
			done_task(task_id)
			view_tasks()
		# непонятный ввод
		else:
			print("Извините, в меню нет пункта", choice)


connection = sqlite3.connect('todo_db.sqlite')
cursor = connection.cursor()

main()

cursor.close()
connection.close()

input("Введите ENTER, чтобы выйти.")