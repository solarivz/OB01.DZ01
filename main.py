# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

# Функция для добавления новой задачи
def add_task(tasks, description, deadline):
    task = Task(description, deadline)
    tasks.append(task)
    print(f"Задача '{task.description}' срок выполнения '{task.deadline}' добавлена в список.\n")

# Функция для вывода списка задач
def list_tasks(tasks, completed=False):
    print("Список задач:")
    i = 1
    for task in tasks:
        if completed == task.completed:
            status = "Выполнено" if task.completed else "Не выполнено"
            print(f"{i}. Описание: '{task.description}', Срок выполнения: '{task.deadline}', Статус: {status}")
            i += 1
    print()

# Функция для отметки задачи как выполненной
def mark_task_as_completed(task):
    task.completed = True
    print(f"Задача '{task.description}', Срок выполнения: '{task.deadline}', Статус: Выполнена\n")


# Пример использования
tasks = []  # Список задач

# Добавляем задачи
add_task(tasks, "Выполнить задание 1 ", "30.04.2024")
add_task(tasks, "Подготовиться к экзамену", "01.05.2024")

# Выводим список задач
list_tasks(tasks)

# Отмечаем первую задачу как выполненную
mark_task_as_completed(tasks[0])


# Выводим список задач
list_tasks(tasks)