import mysql.connector
from db_connection import get_connection

# Підключення до бази даних
conn = get_connection()
cur = conn.cursor()

# Запит для обчислення кінцевої дати проживання для кожного гостя
query = """
    SELECT 
        g.guest_id,
        g.last_name,
        g.first_name,
        g.patronymic,
        g.city,
        r.room_number,
        r.check_in_date,
        r.stay_duration,
        DATE_ADD(r.check_in_date, INTERVAL r.stay_duration DAY) AS check_out_date
    FROM 
        registrations r
    JOIN 
        guests g ON r.guest_id = g.guest_id;
"""

try:
    # Виконання запиту
    cur.execute(query)

    # Виведення результатів
    result = cur.fetchall()
    for row in result:
        print(row)

except mysql.connector.Error as e:
    print(f"Помилка: {e}")

finally:
    # Закриття курсора та підключення
    cur.close()
    conn.close()
