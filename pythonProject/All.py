import mysql.connector
from db_connection import get_connection
from prettytable import PrettyTable


def show_tables_and_data(connection):
    cursor = connection.cursor()

    # Отримуємо список всіх таблиць у БД
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"\nТаблиця: {table_name}")

        # Виведення структури таблиці
        cursor.execute(f"DESCRIBE {table_name}")
        structure = cursor.fetchall()
        print("\nСтруктура таблиці:")
        pt = PrettyTable()
        pt.field_names = ["Field", "Type", "Null", "Key", "Default", "Extra"]
        for row in structure:
            pt.add_row(row)
        print(pt)

        # Виведення даних таблиці
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        print("\nДані таблиці:")
        if data:
            pt = PrettyTable()
            pt.field_names = [i[0] for i in cursor.description]  # Заголовки стовпців
            for row in data:
                pt.add_row(row)
            print(pt)
        else:
            print("Таблиця порожня.")


def show_query_results(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            pt = PrettyTable()
            pt.field_names = [i[0] for i in cursor.description]  # Заголовки стовпців
            for row in results:
                pt.add_row(row)
            print(pt)
        else:
            print("Запит не дав результатів.")
    except mysql.connector.Error as err:
        print(f"Помилка при виконанні запиту: {err}")


def main():
    connection = get_connection()
    if connection:
        # Показуємо таблиці та дані
        show_tables_and_data(connection)

        # Приклад виконання запитів

        # 1. Вивести всіх гостей, які зареєстровані в номерах з телевізором
        query_1 = """
            SELECT 
                g.guest_id,
                g.last_name,
                g.first_name,
                g.patronymic,
                g.city,
                r.room_number,
                r.category
            FROM 
                guests g
            JOIN 
                registrations reg ON g.guest_id = reg.guest_id
            JOIN 
                rooms r ON reg.room_number = r.room_number
            WHERE 
                r.tv = TRUE;
        """
        print("\nГості, які проживають в номерах з телевізором:")
        show_query_results(connection, query_1)

        # 2. Вивести загальну вартість проживання для кожного гостя
        query_2 = """
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
        print("\nЗагальна вартість проживання для кожного гостя:")
        show_query_results(connection, query_2)

        # 3. Підрахувати кількість номерів кожної категорії на кожному поверсі
        query_3 = """
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
        print("\nКількість номерів кожної категорії на кожному поверсі:")
        show_query_results(connection, query_3)

        # 4. Підсумок кількості номерів кожної категорії
        query_4 = """
            SELECT 
                category,
                COUNT(room_number) AS number_of_rooms
            FROM 
                rooms
            GROUP BY 
                category;
        """
        print("\nПідсумок кількості номерів кожної категорії:")
        show_query_results(connection, query_4)

        # 5. Перелік гостей, які проживали в кожній категорії номерів
        query_5 = """
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
        print("\nГості, які проживали в номерах кожної категорії:")
        show_query_results(connection, query_5)

        # Закриваємо з'єднання
        connection.close()


if __name__ == "__main__":
    main()
