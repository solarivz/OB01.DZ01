# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.


class Task():
    def __init__(self, task_description, task_deadline, task_status):
        # Инициализация атрибутов обьекта класса начальными значениями
        self.task_description = task_description              # Описание задачи
        self.task_deadline = task_deadline                 # Время выполнения задачи
        self.task_status = task_status                # Статус задачи

def add_task():
    task_list.append([self.task_description, self.task_deadline, self.task_status])

def list_tasks(self):
    print("Список задач:")
    for i in range(len(self.task_list)):
            self.task_description, self.task_deadline, self.task_status = self.task_list[i]
            self.task_stat = "Выполнено" if self.task_status else "Не выполнено"
            print(f"{i + 1}. Описание: {self.task_description}, Срок выполнения: {self.task_deadline}, Статус: {self.task_stat}")


task_list = []
task_manager = Task()
task_manager.task_description, task_manager.task_deadline, task_manager.task_status = ('Подготовить презентацию', "15.05.2024", False)
task_manager.add_task()

# Выводим список задач
task_manager.list_tasks()
