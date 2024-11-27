import mysql.connector
from mysql.connector import Error

def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="user",       # Ваше ім'я користувача MySQL
            password="userpassword",  # Ваш пароль для MySQL
            database="rental_db"  # Назва вашої бази даних
        )
