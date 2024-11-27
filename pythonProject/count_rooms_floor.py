import mysql.connector
from db_connection import get_connection

# Підключення до бази даних
conn = get_connection()
cur = conn.cursor()

# Запит для підрахунку кількості номерів кожної категорії на кожному поверсі
query = """
    SELECT 
        r.floor, 
        r.category, 
        COUNT(r.room_number) AS room_count
    FROM 
        rooms r
    GROUP BY 
        r.floor, r.category
    ORDER BY 
        r.floor, r.category;
"""

try:
    # Виконання запиту
    cur.execute(query)

    # Виведення результатів
    result = cur.fetchall()
    for row in result:
        print(f"Поверх: {row[0]}, Категорія: {row[1]}, Кількість номерів: {row[2]}")

except mysql.connector.Error as e:
    print(f"Помилка: {e}")

finally:
    # Закриття курсора та підключення
    cur.close()
    conn.close()
