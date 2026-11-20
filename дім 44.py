class Task:
    def __init__(self, title: str, description: str, deadline: str):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.is_completed = False  # Стандартний стан: не виконано (False)

    def mark_as_completed(self):
        """Змінює статус завдання на виконано"""
        self.is_completed = True

    def __str__(self):
        status = "Виконано ✅" if self.is_completed else "Не виконано ❌"
        return (
            f"Назва: {self.title}\n"
            f"Опис: {self.description}\n"
            f"Дедлайн: {self.deadline}\n"
            f"Статус: {status}"
        )


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список для зберігання завдань

    def add_task(self, task: Task):
        """Додає нове завдання до менеджера"""
        self.tasks.append(task)
        print(f"Створено та додано завдання: «{task.title}»")

    def remove_task(self, title: str):
        """Видаляє завдання за його назвою"""
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання «{title}» було видалено.")
                return
        print(f"Помилка: завдання з назвою «{title}» не знайдено.")

    def mark_task_as_completed(self, title: str):
        """Відмічає завдання як виконане за назвою"""
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f"Завдання «{title}» відзначено як виконане!")
                return
        print(f"Помилка: завдання з назвою «{title}» не знайдено.")

    def show_tasks(self):
        """Виводить список усіх завдань"""
        if not self.tasks:
            print("Список завдань наразі порожній.")
            return

        print("\n" + "=" * 30)
        print("СПИСОК ЗАВДАНЬ:")
        print("=" * 30)
        for i, task in enumerate(self.tasks, 1):
            print(f"[{i}]")
            print(task)
            print("-" * 30)


# Приклад використання програми:
if __name__ == "__main__":
    # Створюємо менеджер завдань
    manager = TaskManager()

    # Створюємо кілька завдань
    task1 = Task(
        title="Прибрати кімнату",
        description="Пропилососити та витерти пил",
        deadline="Сьогодні, 20:00"
    )
    task2 = Task(
        title="Вивчити ООП",
        description="Розібратися з класами та об'єктами в Python",
        deadline="Завтра, 12:00"
    )

    # Додаємо завдання до менеджера
    manager.add_task(task1)
    manager.add_task(task2)

    # Виводимо список завдань
    manager.show_tasks()

    # Відмічаємо одне завдання як виконане
    manager.mark_task_as_completed("Прибрати кімнату")

    # Переглядаємо оновлений список
    manager.show_tasks()

    # Видаляємо завдання
    manager.remove_task("Вивчити ООП")

    # Фінальний перегляд списку
    manager.show_tasks()