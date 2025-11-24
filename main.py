todos = ["Что-то сделать"]
print(f"Текущие задачи: {todos}")

with open('todos.txt', 'w') as f:
    f.write(str(todos))
print("Задачи сохранены в файл")