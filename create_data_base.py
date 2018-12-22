import sqlite3

def create_data_base(name_data_base):
    global conn
    conn = sqlite3.connect(name_data_base + ".db")
    global cursor
    cursor = conn.cursor()

def create_table(name_table):
    cursor.execute("""CREATE TABLE """ + name_table +  """
                  (number int, person int, photo text, about text, checker int)
               """) 

def add_new_record(name_table):
    number_table = int(input('Number of table: '))
    person = int(input('Person: '))
    photo_link = input('Photo link:')
    about_table = input('About table: ')
    checker = int(input('Free: '))
    new_record = [(number_table, person, photo_link, about_table, checker)]
    cursor.executemany("INSERT INTO " + name_table + " VALUES (?, ?, ?, ?, ?)", new_record)
def show_table(name_table):
    for i in cursor.execute("""select * from """ + name_table):
        print(i)
def data_base_commit():
    conn.commit()
def free_table():
    cursor.execute("""update new_table set checker = 1""")

while True:
    print('1 - Создать базу данных')
    print('2 - Создать таблицу')
    print('3 - Добавить запись')
    print('4 - Показать таблицу')
    print('5 - Закомитить')
    print('6 - Изменить все столы на свободные')
    print('7 - Выход')
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
        break


def create_table_for_orders(name_table):
    cursor.execute("""CREATE TABLE """ + name_table +  """
                  (table_number int, phone text, state int)
               """)

def add_new_order(name_table):
    table_number = int(input('table_number: '))
    phone = input('phone: ')
    state = int(input('state : '))