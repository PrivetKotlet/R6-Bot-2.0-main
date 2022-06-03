from multiprocessing import connection
import sqlite3



try:
    conn = sqlite3.connect(r'C:\Users\rusla\OneDrive\Рабочий стол\R6-Bot-2.0-main\bot\modules\Operatives.db')
    print("Connection to the database is successful")
    cur = conn.cursor()
except ConnectionRefusedError:
    print("Connection to the database is unsuccessful")





def Attack_parss():
    s = 0 
    Operatives =  '''''' # Строка в которую записываються оперативники 
    while s < 31:
        request_tuple = cur.execute("SELECT DISTINCT Attack FROM Operative").fetchall()# Запрос в БД для получения кортежа значений
        Operative = request_tuple[s] # Получение одного кортежа с нужным значением
        Operative = Operative[0] # Получение значения
        Operatives += Operative + "\n"
        s += 1
    return Operatives




def Protection_parss():
    s = 0 
    Operatives =  '''''' # Строка в которую записываються оперативники 
    while s < 31:
        request_tuple = cur.execute("SELECT DISTINCT protection FROM Operative").fetchall()# Запрос в БД для получения кортежа значений
        Operative = request_tuple[s] # Получение одного кортежа с нужным значением
        Operative = Operative[0] # Получение значения
        Operatives += Operative + "\n"
        s += 1
    return Operatives






