from sqlite3 import *

conn = connect('F:\gui_LK_naryad\/bd\/bd.db')


# Запрос на поиск пользователей в таблице account(для проверки, есть ли такой пользователь
# c таким паролем.
def serch_user_profile(users):
    sql = "SELECT id, users,password FROM accaunt WHERE users = ?"
    cursor = conn.cursor()
    a = cursor.execute(sql,[(users)])
    return a.fetchall()

# Запрос в бд - поиск профилей пользователей из таблице users_data
def serch_users_data(id):
    sql = "SELECT * FROM users_data WHERE id = ?"
    cursor = conn.cursor()
    a = cursor.execute(sql,[(id)])
    return a.fetchall()

def close_connection():
    conn.close()


