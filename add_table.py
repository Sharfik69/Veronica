import requests
import sqlite3

class table(object):
    def __init__(self, number, person, photo, about, checker):
        self.number = number
        self.person = person
        self.photo = photo
        self.about = about
        self.checker = checker

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
        l = 1
        for i in self.ListOfTable:
            if i.number == id1 + 1 and i.checker == 1:
                new_tabe = 'Номер стола: ' + str(i.number) + '\nКол-во персон: ' + str(i.person) + '\nО столике: ' + i.about   
            l += 1 
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

