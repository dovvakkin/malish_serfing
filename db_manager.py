import sqlite3


def open_db():  # open if exist, or create db
    conn = sqlite3.connect("logins_database.sqlite")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE botnet
            (num INTEGER,
            vk_login TEXT,
            vk_password TEXT)
        """)
        cursor.execute(""" 
            INSERT INTO botnet (num, vk_login, vk_password)
            VALUES (0, "maria", "is_the_best")
        """)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        pass


open_db()
#
#
# def add_bot(login, password):
#     open_db()
#



