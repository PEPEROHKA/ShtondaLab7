import mysql.connector
from db_connection import get_connection

# Отримання підключення до бази даних
conn = get_connection()
cur = conn.cursor()

try:
    # Вставка даних у таблицю "Гості"
    guests_data = [
        ('1', 'Петренко', 'Іван', 'Іванович', 'Київ'),
        ('2', 'Іванов', 'Олександр', 'Іванович', 'Одеса'),
        ('3', 'Сидоренко', 'Марія', 'Петриківна', 'Львів'),
        ('4', 'Мельник', 'Василь', 'Сергійович', 'Харків'),
        ('5', 'Коваленко', 'Анатолій', 'Михайлович', 'Чернівці'),
        ('6', 'Шевченко', 'Юрій', 'Володимирович', 'Дніпро'),
        ('7', 'Литвин', 'Тетяна', 'Олексіївна', 'Запоріжжя')
    ]

    for guest in guests_data:
        cur.execute("INSERT INTO guests (guest_id, last_name, first_name, patronymic, city) VALUES (%s, %s, %s, %s, %s)", guest)

    # Вставка даних у таблицю "Номери"
    rooms_data = [
        (101, 1, 1, True, True, 2, 'полу люкс', 1200.00),
        (102, 1, 1, True, False, 2, 'звичайний', 800.00),
        (103, 2, 1, True, True, 4, 'люкс', 1800.00),
        (201, 1, 2, False, True, 2, 'звичайний', 900.00),
        (202, 2, 2, True, True, 4, 'полу люкс', 1500.00),
        (203, 3, 2, True, False, 4, 'люкс', 2000.00),
        (301, 1, 3, False, False, 2, 'звичайний', 700.00),
        (302, 2, 3, True, True, 4, 'полу люкс', 1600.00),
        (303, 3, 3, True, True, 4, 'люкс', 2200.00),
        (304, 1, 3, True, False, 2, 'звичайний', 950.00)
    ]

    for room in rooms_data:
        cur.execute("""
            INSERT INTO rooms (room_number, room_count, floor, tv, fridge, bed_count, category, price_per_night)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, room)

    # Вставка даних у таблицю "Реєстрація гостей"
    registrations_data = [
        ('1', 1, 101, '2024-11-01', 2),
        ('2', 2, 102, '2024-11-02', 2),
        ('3', 3, 103, '2024-11-03', 2),
        ('4', 4, 201, '2024-11-04', 2),
        ('5', 5, 202, '2024-11-05', 2),
        ('6', 6, 203, '2024-11-06', 2),
        ('7', 7, 301, '2024-11-07', 2)
    ]

    for registration in registrations_data:
        cur.execute("""
            INSERT INTO registrations (registration_id, guest_id, room_number, check_in_date, stay_duration)
            VALUES (%s, %s, %s, %s, %s)
        """, registration)

    # Збереження змін
    conn.commit()

except mysql.connector.Error as e:
    print(f"Помилка: {e}")
    conn.rollback()
finally:
    # Закриття курсора і підключення
    cur.close()
    conn.close()
