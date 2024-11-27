import mysql.connector
from db_connection import get_connection

# Підключення до бази даних
conn = get_connection()
cur = conn.cursor()

# Запит для підсумку кількості номерів кожної категорії
query = """
    SELECT 
        category,
        COUNT(room_number) AS number_of_rooms
    FROM 
        rooms
    GROUP BY 
        category;
"""

try:
    # Виконання запиту
    cur.execute(query)

    # Виведення результатів
    result = cur.fetchall()
    for row in result:
        print(f"Категорія: {row[0]}, Кількість номерів: {row[1]}")

except mysql.connector.Error as e:
    print(f"Помилка: {e}")

finally:
    # Закриття курсора та підключення
    cur.close()
    conn.close()
