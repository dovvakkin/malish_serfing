import sqlite3


def open_db():  # open if exist, or create db
    conn = sqlite3.connect("logins_database.sqlite")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE botnet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(14),
            password VARCHAR(20)
            )
        """)
        cursor.execute(""" 
            INSERT INTO botnet (login, password)
            VALUES ("89258396534", "k0zhepnin@")
        """)
        cursor.execute(""" 
            INSERT INTO botnet (login, password)
            VALUES ("89104696981", "cherep/")
        """)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        pass


def amount_of_bots():
    conn = sqlite3.connect("logins_database.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT MAX (id) from botnet")

    amount = cursor.fetchall()

    return amount[0][0]


def get_bot(id):
    conn = sqlite3.connect("logins_database.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM botnet WHERE id = ?", str(id))

    bot = cursor.fetchall()

    return bot[0]


#
# def add_bot(login, password):
#     open_db()
#



