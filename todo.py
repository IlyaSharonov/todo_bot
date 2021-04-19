HELP = """
help - список команд
add - добавить событие
show - показать элемент
remove - удалить элемент
exit - закрыть программу
"""

todo = {}
# 1 - запрос даты
# 2 - запрос задачи
# 0 - none


print('Введите команду , введите help для вывода списка команд')
while True:
  userAnswer = input()

	if userAnswer == "add":
		print("Работает\n")
	elif userAnswer == "help":
		print(HELP)
	elif userAnswer == "show":
		print("Работает\n")
	elif userAnswer == "done":
		print("Работает\n")
