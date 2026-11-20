import logging
from datetime import datetime


def setup_and_log_info():
    # 1. Налаштовуємо базову конфігурацію логування
    # stream=sys.stdout за замовчуванням виводить і в консоль, а filename записує у файл
    logging.basicConfig(
        filename="app_log.txt",  # Файл, куди будуть записуватись логи
        level=logging.INFO,  # Встановлюємо мінімальний рівень логування INFO
        encoding="utf-8",
        format="%(asctime)s [%(levelname)s] — %(message)s",  # Формат рядка логу
        datefmt="%Y-%m-%d"  # Формат дати: Рік-Місяць-День (наприклад, 2026-11-20)
    )

    # 2. Отримуємо поточну дату у потрібному форматі через модуль datetime (як додатковий акцент завдання)
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 3. Формуємо та записуємо повідомлення рівня INFO
    log_message = f"Поточна дата системи: {current_date}. Програма успішно виконала запис логу рівня INFO."

    logging.info(log_message)
    print("Лог успішно записано у файл 'app_log.txt'!")


if __name__ == "__main__":
    setup_and_log_info()