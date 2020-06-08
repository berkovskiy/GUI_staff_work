from sqlite3 import *

conn = connect('F:\gui_LK_naryad\/bd\/bd.db')
cursor = conn.cursor()

def serch_user_profile(users):
    sql = "SELECT users,password FROM accaunt WHERE users = ?"
    a = cursor.execute(sql,[(users)])
    return a.fetchall()

