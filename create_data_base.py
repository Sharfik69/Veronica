import sqlite3

def create_data_base(name_data_base):
    global conn
    conn = sqlite3.connect(name_data_base + ".db")
    global cursor
    cursor = conn.cursor()

def create_table(name_table):
    cursor.execute("""CREATE TABLE """ name_table """
                  (number int, person int, photo text, about text)
               """) 

def add_new_record():
    number_table = int(input('Number of table: '))
    person = int(input('Person: '))
    photo_ling = input('Photo_Link')
    about_photo