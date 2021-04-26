import time

HELP = """
help - список команд
add - добавить событие
show - показать элемент
remove - удалить элемент
exit - закрыть программу
"""

todo = {} 
print("Введите команду или help, для вывода доступных команд")

def checkDate(uDate):
    try:
        time.strptime(uDate, '%d.%m.%Y')
        return True
    except ValueError:
			  print("Error. Неправильный формат даты")
        return False

while True:
  userAnswer = input()

  if userAnswer == "add":
    userDate = input("Введите дату:\n")
    userTask = input("Что нужно сделать?")

    if userDate in todo.keys():
      todo[ userDate ].append( userTask )
    else:
      todo[ userDate ] = ( userTask )
    todo[ userDate] = userTask
    print(f" [ {userDate} ] - добавленная задача '{userTask}' ")
  elif userAnswer == "help":
    print(HELP) 
  elif userAnswer == "show":
    for date in sorted( todo.keys() ):
      for tasks in todo[ date ]:
        print( f"[{date}] - {tasks}" ) 
  elif userAnswer == "exit":
    break 
  elif userAnswer == "help":
    print("Работает") 

