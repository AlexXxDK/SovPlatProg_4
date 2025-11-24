todos = ["Что-то сделать"]
print(f"Текущие задачи: {todos}")


def add_todo(task):
    todos.append(task)
add_todo("Что-то сделать 2")
print(f"Текущие задачи: {todos}")