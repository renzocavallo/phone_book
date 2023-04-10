import sqlite3

conn = sqlite3.connect('db_diary.db')

table_users = '''CREATE TABLE IF NOT EXISTS users
                   (id INTEGER PRIMARY KEY, name VARCHAR(250), lastname VARCHAR(250), email VARCHAR(250) UNIQUE, password VARCHAR(250))'''

table_contacts = '''CREATE TABLE IF NOT EXISTS contacts
                    (id INTEGER PRIMARY KEY, id_user INTEGER,
                    name VARCHAR(250), lastname VARCHAR(250), email VARCHAR(250) , phone VARCHAR(250) ,
                    FOREIGN KEY (id_user) REFERENCES users (id))'''

table_users_contacts = '''CREATE TABLE IF NOT EXISTS users_contacts
                             (id INTEGER PRIMARY KEY, id_user INTEGER, id_contact INTEGER,
                             FOREIGN KEY (id_user) REFERENCES users (id),
                             FOREIGN KEY (id_contact) REFERENCES contacts (id))'''

def create_db():
    try:
        conn.execute(table_users)
        conn.execute(table_contacts)
        conn.execute(table_users_contacts)
        print("Tablas creadas exitosamente")   

    except sqlite3.Error as error:
        print("Error al crear la tabla:", error)
        conn.rollback()

    finally:
        conn.commit()