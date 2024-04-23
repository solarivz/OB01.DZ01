# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, deadline):
        self.description = description          # описание задачи
        self.deadline = deadline                # срок выполнения задачи
        self.completed = False                  # изначально задача не выполнена


# Функция для добавления новой задачи - добавляется задача типа обьект вновь
# созданный с атрибутами переданными функции

def add_task(tasks, description, deadline):
    tasks.append(Task(description, deadline))
    print(f"Задача {tasks} добавлена в список\n")


# Функция для отметки задачи как выполненной
def mark_task_as_completed(task):
    task.completed = True
    print(f"Отмечаем задачу {task} как выполненную")
    print()

# Функция для вывода списка задач
def list_tasks(tasks, completed=False):
    print("Список задач:")
    for i, task in enumerate(tasks, start=1):
        if completed == task.completed:
            status = "Выполнено" if task.completed else "Не выполнено"
            print(f"{i}. Описание: {task.description}, Срок выполнения: {task.deadline}, Статус: {status}")
    print()

# Пример использования

tasks = []  # Список задач

# Добавляем задачи через вызов функции, передаем аргументы ссылку на обьект типа список, и две строковые переменные
add_task(tasks, "Сделать уроки", "30.04.2024")
add_task(tasks, "Подготовить презентацию", "15.05.2024")

# Выводим список задач
list_tasks(tasks)

# Отмечаем первую задачу как выполненную
mark_task_as_completed(tasks[0])

# Выводим список задач
list_tasks(tasks)