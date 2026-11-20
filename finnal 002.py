from contextlib import closing
import random
import sqlite3


class GeoCapitalDB:

  def __init__(self, db_name: str = "capital_game.db"):
    self.db_name = db_name
    self._create_tables()
    self._seed_data()

  def _create_tables(self):
    """Створює таблиці для гри у столиці та статистику."""
    with closing(sqlite3.connect(self.db_name)) as conn:
      with conn:
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS capitals (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        continent TEXT NOT NULL,
                        country TEXT NOT NULL,
                        city TEXT NOT NULL UNIQUE,
                        country_hint TEXT NOT NULL,
                        city_hint TEXT NOT NULL
                    )
                """)
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS game_stats (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        capital_guessed TEXT NOT NULL,
                        total_attempts INTEGER NOT NULL,
                        played_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """)

  def _seed_data(self):
    """Заповнює базу тільки топ-країнами та їхніми столицями."""
    locations = [
        (
            "Північна Америка",
            "США",
            "Вашингтон",
            "Ця супердержава розташована на Північноамериканському континенті, відома своєю економікою та Голлівудом.",
            "Це політична столиця країни, де знаходиться Білий дім та Капітолій (але не Нью-Йорк!).",
        ),
        (
            "Європа",
            "Франція",
            "Париж",
            "Європейська країна, відома своїм вином, сирами та історією.",
            "Головний символ міста — Ейфелева вежа, а також всесвітньо відомий музей Лувр.",
        ),
        (
            "Європа",
            "Велика Британія",
            "Лондон",
            "Острівна європейська держава, якою править монарх.",
            "Тут знаходяться Біг-Бен, Тауерський міст та річка Темза.",
        ),
        (
            "Азія",
            "Японія",
            "Токіо",
            "Високотехнологічна острівна держава в Східній Азії, країна висхідного сонця.",
            "Найбільший мегаполіс світу, відомий неоновими вивісками та перехрестям Сібуя.",
        ),
        (
            "Європа",
            "Італія",
            "Рим",
            "Країна на півдні Європи, за формою схожа на чобіт, батьківщина піци та пасти.",
            "Вічне місто, де розташовані Колізей та держава у державі — Ватикан.",
        ),
        (
            "Євразія",
            "Туреччина",
            "Анкара",
            "Трансконтинентальна країна між Європою та Азією, популярна курортна зона.",
            "Це політична столиця держави (не Стамбул!), розташована в центральній частині анадольського плато.",
        ),
        (
            "Європа",
            "Німеччина",
            "Берлін",
            "Провідна економічна держава Центральної Європи, відома автопромом та пивом.",
            "Місто відоме своєю Бранденбурзькою воротами та залишками історичної стіни.",
        ),
        (
            "Європа",
            "Україна",
            "Київ",
            "Наша рідна європейська країна з багатовіковою історією та незламним духом.",
            "Столиця на могутній річці Дніпро, відома Хрещатиком та Лаврою.",
        ),
    ]
    with closing(sqlite3.connect(self.db_name)) as conn:
      with conn:
        conn.execute("DELETE FROM capitals")
        conn.executemany(
            """
                    INSERT OR IGNORE INTO capitals
                    (continent, country, city, country_hint, city_hint)
                    VALUES (?, ?, ?, ?, ?)
                """,
            locations,
        )

  def get_random_capital(self) -> tuple:
    """Отримує випадкову пару країна-столиця."""
    with closing(sqlite3.connect(self.db_name)) as conn:
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM capitals")
      all_rows = cursor.fetchall()
      return random.choice(all_rows)

  def save_stat(self, city: str, attempts: int):
    """Зберігає результат гри в SQLite."""
    with closing(sqlite3.connect(self.db_name)) as conn:
      with conn:
        conn.execute(
            "INSERT INTO game_stats (capital_guessed, total_attempts) VALUES"
            " (?, ?)",
            (city, attempts),
        )


def play_game():
  db = GeoCapitalDB()
  _, continent, country, city, country_hint, city_hint = (
      db.get_random_capital()
  )

  print("=== ГРА «ВГАДАЙ СТОЛІЦУ» ===")
  print("Правила: спочатку вгадуєш Країну, потім її Столицю.")
  print("Кожні 3 невдалі спроби ти отримуєш підказку!\n")

  total_attempts = 0

  # ЕТАП 1: ВГАДУЄМО КРАЇНУ
  stage_attempts = 0
  while True:
    guess = input("[Етап 1/2] Введи назву країни: ").strip()
    total_attempts += 1
    stage_attempts += 1

    if guess.lower() == country.lower():
      print(f"Вірно! Це дійсно {country}.\n")
      break
    else:
      print("Не вгадав!")
      if stage_attempts % 3 == 0:
        print(
            f"💡 ПІДКАЗКА (Континент / Країна): Ця країна знаходиться в"
            f" регіоні — {continent}. {country_hint}\n"
        )

  # ЕТАП 2: ВГАДУЄМО СТОЛИЦЮ
  stage_attempts = 0
  while True:
    guess = input(f"[Етап 2/2] Введи столицю країни {country}: ").strip()
    total_attempts += 1
    stage_attempts += 1

    if guess.lower() == city.lower():
      print(f"\n🎉 ПЕРЕМОГА! Столиця {country} — це {city}!")
      print(f"Загальна кількість спроб: {total_attempts}")
      db.save_stat(city, total_attempts)
      break
    else:
      print("Не вгадав!")
      if stage_attempts % 3 == 0:
        print(f"💡 ПІДКАЗКА (Столиця): {city_hint}\n")


if __name__ == "__main__":
  play_game()