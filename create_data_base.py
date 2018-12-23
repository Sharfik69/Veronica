import sqlite3
import random

def create_data_base(name_data_base):
    global conn
    conn = sqlite3.connect(name_data_base + ".db")
    global cursor
    cursor = conn.cursor()
    #cursor.execute("""drop table new_table""")

def create_table(name_table):
    cursor.execute("""CREATE TABLE """ + name_table +  """
                  (number int, person int, photo text, type int, checker int)
               """) 

def add_new_record(name_table):
    '''
    number_table = int(input('Number of table: '))
    person = int(input('Person: '))
    photo_link = input('Photo link:')
    type_table = int(input('About table: '))
    checker = int(input('Free: '))
    new_record = [(number_table, person, photo_link, type_table, checker)]
    cursor.executemany("INSERT INTO " + name_table + " VALUES (?, ?, ?, ?, ?)", new_record)
    '''
    for i in range(100):
        number_table = i + 1
        person = random.randint(2, 5)
        photo_link = 'norm_table'
        type_table = random.randint(1, 3)
        checker = 1
        new_record = [(number_table, person, photo_link, type_table, checker)]
        cursor.executemany("INSERT INTO " + name_table + " VALUES (?, ?, ?, ?, ?)", new_record)

def show_table(name_table):
    for i in cursor.execute("""select * from """ + name_table):
        print(i)
def data_base_commit():
    conn.commit()
def free_table():
    cursor.execute("""update new_table set checker = 1""")



def create_table_for_orders(name_table):
    cursor.execute("""CREATE TABLE """ + name_table +  """
                  (table_number int, id_user int, state int, date_time real)
               """)

def add_new_order(name_table):
    table_number = int(input('table_number: '))
    id_user = int(input('id_user: '))
    state = int(input('state : '))
    cursor.execute("INSERT INTO " + name_table + " VALUES (" + str(table_number) + "," + str(id_user) + "," + str(state) + ", datetime('now', 'localtime'))")



while True:
    print('1 - Создать базу данных')
    print('2 - Создать таблицу')
    print('3 - Добавить запись')
    print('4 - Показать таблицу')
    print('5 - Закомитить')
    print('6 - Изменить все столы на свободные')
    print('7 - Создать таблицу с заказами')
    print('8 - Добавить запис в таблицу с заказами')
    print('9 - Выход')
    what_to_do = int(input())
    if what_to_do == 1:
        create_data_base('test_data_base')
    if what_to_do == 2:
        create_table('new_table')
    if what_to_do == 3:
        add_new_record('new_table')
    if what_to_do == 4:
        show_table('new_table')
    if what_to_do == 5:
        data_base_commit()
    if what_to_do == 6:
        free_table()
    if what_to_do == 7:
        create_table_for_orders('new_table_orders')
    if what_to_do == 8:
        add_new_order('new_table_orders')
    if what_to_do == 9:
        break

