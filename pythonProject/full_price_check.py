import mysql.connector
from db_connection import get_connection

# Підключення до бази даних
conn = get_connection()
cur = conn.cursor()

# Запит для обчислення повної вартості проживання для кожного гостя
query = """
    SELECT 
        g.guest_id,
        g.last_name,
        g.first_name,
        r.room_number,
        r.price_per_night,
        reg.stay_duration,
        (r.price_per_night * reg.stay_duration) AS total_cost
    FROM 
        registrations reg
    JOIN 
        guests g ON reg.guest_id = g.guest_id
    JOIN 
        rooms r ON reg.room_number = r.room_number;
"""

try:
    # Виконання запиту
    cur.execute(query)

    # Виведення результатів
    result = cur.fetchall()
    for row in result:
        print(f"Гість: {row[1]} {row[2]}, Номер: {row[3]}, Вартість за ніч: {row[4]}, "
              f"Кількість днів: {row[5]}, Повна вартість: {row[6]}")

except mysql.connector.Error as e:
    print(f"Помилка: {e}")

finally:
    # Закриття курсора та підключення
    cur.close()
    conn.close()
