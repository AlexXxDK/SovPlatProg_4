todos = ["Что-то сделать"]
print(f"Текущие задачи: {todos}")

def add_todo(task):
    todos.append(task)
add_todo("Что-то сделать 2")
print(f"Текущие задачи: {todos}")

def add_todo_secure(task, password="secret"):
    if password == "secret":
        todos.append(task)
        print("Задача добавлена!")
    else:
        print("Ошибка: неверный пароль")
add_todo_secure("Сделать отчёт", "secret")

with open('todos.txt', 'w') as f:
    f.write(str(todos))
print("Задачи сохранены в файл")