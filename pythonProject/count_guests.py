import mysql.connector
from db_connection import get_connection

# Підключення до бази даних
conn = get_connection()
cur = conn.cursor()

# Запит для отримання гостей, які проживали в номерах, згрупованих за категорією
query = """
    SELECT 
        ro.category AS category,
        g.last_name, 
        g.first_name, 
        g.patronymic, 
        g.city
    FROM 
        guests g
    JOIN 
        registrations r ON g.guest_id = r.guest_id
    JOIN 
        rooms ro ON r.room_number = ro.room_number
    ORDER BY 
        ro.category, g.last_name;
"""

try:
    # Виконання запиту
    cur.execute(query)

    # Виведення результатів
    result = cur.fetchall()
    if result:
        current_category = None
        for row in result:
            # Якщо змінилася категорія, вивести її
            if row[0] != current_category:
                current_category = row[0]
                print(f"\nКатегорія: {current_category}")
            # Вивести інформацію про гостя
            print(f"  Прізвище: {row[1]}, Ім'я: {row[2]}, По батькові: {row[3]}, Місто: {row[4]}")
    else:
        print("Немає гостей у системі.")

except mysql.connector.Error as e:
    print(f"Помилка: {e}")

finally:
    # Закриття курсора та підключення
    cur.close()
    conn.close()
