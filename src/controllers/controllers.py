from src.models.models import conn
import sqlite3
from bcrypt import checkpw

def create_user(name, lastname, email, password):
    data = (name, lastname, email, password)
    query = "INSERT INTO users (name, lastname, email, password) VALUES(?, ?, ?, ?)"
    try:
        cursor = conn.cursor()
        cursor.execute(query, data)

    except sqlite3.Error:
        return False
    
    finally:
        conn.commit()
        cursor.close()
        
    return True

def log_success(email, password):
    data = (email,)
    query = "SELECT id, password FROM users WHERE email=?"
    cursor = conn.cursor()
    cursor.execute(query, data)
    result = cursor.fetchone()
    cursor.close()
    if result:
        stored_password = result[1]
        if checkpw(password.encode('utf-8') ,stored_password ):
            return result[0]
    return 0

def create_contact(id_user, name, lastname, email, phone):
    query_insert_contact = "INSERT INTO contacts (name, lastname, email, phone) VALUES (?, ?, ?, ?)"
    query_insert_user_contact = "INSERT INTO users_contacts (id_user, id_contact) VALUES (?, ?)"
    contact_data = (name, lastname, email, phone)
    
    with conn:
        cursor = conn.cursor()
        cursor.execute(query_insert_contact, contact_data,)
        conn.commit()
        contact_id = cursor.lastrowid
        
        user_contact_data = (id_user, contact_id)
        cursor.execute(query_insert_user_contact, user_contact_data,)
        
def get_user_contacts(user_id):
    query = '''
        SELECT contacts.id, contacts.name, contacts.lastname, contacts.email, contacts.phone
        FROM contacts
        INNER JOIN users_contacts ON contacts.id = users_contacts.id_contact
        WHERE users_contacts.id_user = ?
    '''
    cursor = conn.cursor()
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    cursor.close()
    return results

def edit_contact(name, lastname, email, phone, user_id):
     data = (name, lastname, email, phone, user_id)
     query='''
         UPDATE contacts
         SET name = ? , lastname = ? , email = ?, phone = ?
         WHERE id = ?;
     '''
     cursor = conn.cursor()
     cursor.execute(query, data)
     conn.commit()
     cursor.close()

def delete_contact(id):   
    query = '''
        DELETE FROM  contacts WHERE id = ?;
    '''   
    query_2 = '''
        DELETE FROM users_contacts WHERE id_contact = ?;
    '''
    cursor = conn.cursor()
    cursor.execute(query, (id,))
    cursor.execute(query_2, (id,))
    conn.commit()
    cursor.close()

def get_user_email(id):
    query = '''
        SELECT email FROM users WHERE id = ?
    '''
    cursor =  conn.cursor()
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def search_contact(user_id, name):
    query = '''
        SELECT c.id, c.name, c.lastname, c.email, c.phone
        FROM contacts AS c
        JOIN users_contacts AS uc ON c.id = uc.id_contact
        WHERE uc.id_user = ? AND c.name LIKE ?
    '''
    cursor = conn.cursor()
    cursor.execute(query, (user_id, f'%{name}%'))
    results = cursor.fetchall()
    cursor.close()
    return results