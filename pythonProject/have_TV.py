import mysql.connector
from db_connection import get_connection


def show_rooms_with_television():
    """Вивести всі номери, в яких є телевізор"""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM rooms WHERE tv = TRUE"
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        connection.close()


show_rooms_with_television()
