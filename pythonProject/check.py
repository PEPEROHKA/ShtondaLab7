from db_connection import get_connection


def check():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM guests;")

    print("Вміст таблиці guests:")
    for row in cur.fetchall():
        print(row)

    cur.execute("SELECT * FROM rooms;")

    print("Вміст таблиці rooms:")
    for row in cur.fetchall():
        print(row)

    cur.execute("SELECT * FROM registrations;")

    print("Вміст таблиці registrations:")
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    check()