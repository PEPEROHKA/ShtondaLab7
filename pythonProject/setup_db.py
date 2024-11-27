from db_connection import get_connection

# Створення підключення до бази даних

get_connection()
conn = get_connection()

if conn:
    cur = conn.cursor()

    # Створення таблиці "Гості"
    cur.execute("""
        CREATE TABLE guests (
            guest_id INT ,
            last_name VARCHAR(100),
            first_name VARCHAR(100),
            patronymic VARCHAR(100),
            city VARCHAR(100)
        );
    """)

    # Створення таблиці "Номери"
    cur.execute("""
        CREATE TABLE rooms (
            room_number INT ,
            room_count INT,
            floor INT,
            tv BOOLEAN,
            fridge BOOLEAN,
            bed_count INT,
            category VARCHAR(50),
            price_per_night DECIMAL(10, 2)
        );
    """)

    # Створення таблиці "Реєстрація гостей"
    cur.execute("""
        CREATE TABLE registrations (
    registration_id ,
    guest_id INT,
    room_number INT,
    check_in_date DATE,
    stay_duration INT,  -- кількість днів перебування
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_number) REFERENCES rooms(room_number)
);
    """)

    # Підтвердження змін
    conn.commit()

    # Закриття з'єднання
    cur.close()
    conn.close()