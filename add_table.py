import requests
import sqlite3

class table(object):
    def __init__(self, number, person, photo, about, checker):
        self.number = number
        self.person = person
        self.photo = photo
        self.about = about
        self.checker = checker
#(number int, person int, photo text, type int, checker int)
class table_list():
    data_base_of_table = sqlite3.connect("test_data_base.db")
    #data_base_of_table = sqlite3.connect("test_table.db")
    cursor_table = data_base_of_table.cursor()
    def select_table(self, cnt_persons):
        type_of_table = set()
        key_board = []
        new_row = []
        for i in self.cursor_table.execute("select * from new_table where person = " + str(cnt_persons) + " and checker = 1 order by type"):
            if not(i[3] in type_of_table):
                new_row.append(str(i[3]))
                if len(new_row) == 3:
                    key_board.append(new_row)
                    new_row = []
            type_of_table.add(i[3])
        if len(new_row) > 0:
            key_board.append(new_row)
        if len(key_board) == 0:
            return False
        key_board.append(['Назад'])
        return key_board
    

    def print_about_table(self, table_type):
        for i in self.cursor_table.execute("select * from type_of_table where type_table = " + str(table_type)):
            return i[1]
    

    def Add_Order(self, table_number, id_user, state):
        self.cursor_table.execute("INSERT INTO new_table_orders VALUES (" + str(table_number) + "," + str(id_user) + "," + str(state) + ", datetime('now', 'localtime'))")
        self.cursor_table.execute("UPDATE new_table_orders SET date_time = DATETIME(date_time, '+30 minutes')")
        self.data_base_of_table.commit() 
    
    def table_for_user(self, person, type_table):
        for i in self.cursor_table.execute("select * from new_table where person = " + str(person) + " and type = " + str(type_table) + " and checker = 1 order by number"):
            return i[0]

    def Reservation(self, number_table):
        self.cursor_table.execute("update new_table set checker = 0 where number = " + str(number_table))







