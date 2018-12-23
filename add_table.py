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
class table_list(list):
    ListOfTable = []
    data_base_of_table = sqlite3.connect("test_data_base.db")
    cursor_table = data_base_of_table.cursor()
    def LoadTable(self):
        for i in self.cursor_table.execute("""select * from new_table"""):
            self.ListOfTable.append(table(i[0], i[1], i[2], i[3], i[4]))
    def FreeTable(self):
        return len(self.ListOfTable)
    def PhotoTable(self, id):
        return self.ListOfTable[id].photo
    def AboutTable(self, id1, cnt_persons):
        new_tabe = 'about'
        for i in self.ListOfTable:
            if i.number == id1 + 1 and i.checker == 1 and cnt_persons == i.person:
                new_tabe = 'Номер стола: ' + str(i.number) + '\nКол-во персон: ' + str(i.person) + '\nО столике: ' + i.about   
        return new_tabe
    def Table_is_free(self, id1):
        for i in self.ListOfTable:
            if i.number == id1:
                if i.checker == 0:
                    return 0
                else:
                    i.checker = 0
                    self.cursor_table.execute("""update new_table set checker = 0 where number = """ + str(i.number))   
                    self.data_base_of_table.commit()                 
                    return 1
    def List_of_free_table(self, cnt_person):
        new_list_table = []
        new_table_row = []
        for i in self.ListOfTable:
            if i.checker == 1 and cnt_person == i.person:
                new_table_row.append(str(i.number))
                if len(new_table_row) == 3:
                    new_list_table.append(new_table_row)
                    new_table_row = []
        if len(new_table_row) != 0:
            new_list_table.append(new_table_row)
        new_list_table.append(['Назад'])
        return new_list_table



