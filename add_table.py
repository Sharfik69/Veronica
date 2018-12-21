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
    def LoadTable(self):
        data_base_of_table = sqlite3.connect("test_table.db")
        cursor_table = data_base_of_table.cursor()
        for i in cursor_table.execute("""select * from table1"""):
            self.ListOfTable.append(table(i[0], [1], i[2], i[3], i[4]))
    def FreeTable(self):
        return len(self.ListOfTable)
    def PhotoTable(self, id):
        return self.ListOfTable[id].photo
    def AboutTable(self, id1):
        new_tabe = str()
        l = 0
        for i in self.ListOfTable:
            if l == id1:
                new_tabe = 'Номер стола: ' + str(i.number) + '\nКол-во персон: ' + str(i.person) + '\nО столике: ' + i.about   
            l += 1 
        return new_tabe