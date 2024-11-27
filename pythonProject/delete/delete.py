import mysql.connector
from db_connection import get_connection

# Функція для отримання підключення до бази даних
get_connection()

# Підключення до бази даних
conn = get_connection()
cur = conn.cursor()

try:
    # Очищення таблиць (видалення всіх записів)
    cur.execute("DELETE FROM registrations;")
    cur.execute("DELETE FROM rooms;")
    cur.execute("DELETE FROM guests;")

    # Збереження змін
    conn.commit()
    print("Таблиці були очищені.")

except mysql.connector.Error as e:
    print(f"Помилка: {e}")
    conn.rollback()

finally:
    # Закриття курсора і підключення
    cur.close()
    conn.close()
