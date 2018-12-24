import requests
import sqlite3

class table(object):
    def __init__(self, number, person, photo, about, checker):
        self.number = number
        self.person = person
        self.photo = photo
        self.about = about
        self.checker = checker
        self.today = str()
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
    

    def Add_Order(self, table_number, id_user, state, time_order):
        order = [(str(table_number), str(id_user), str(state), time_order)] 
        self.cursor_table.executemany("INSERT INTO new_table_orders VALUES (?, ?, ?, ?)", order)
        #self.cursor_table.execute("UPDATE new_table_orders SET date_time = DATETIME(date_time, '+30 minutes')")
        self.data_base_of_table.commit() 
    
    def table_for_user(self, person, type_table):
        for i in self.cursor_table.execute("select * from new_table where person = " + str(person) + " and type = " + str(type_table) + " and checker = 1 order by number"):
            return i[0]

    def Reservation(self, number_table):
        self.cursor_table.execute("update new_table set checker = 0 where number = " + str(number_table))

    def date_list(self):
        number_to_date = {
            '01': ' Января', 
            '02': ' Февраля', 
            '03': ' Марта', 
            '04': ' Апреля',
            '05': ' Мая', 
            '06': ' Июня', 
            '07': ' Июля', 
            '08': ' Августа', 
            '09': ' Сентября',
            '10': ' Октября',
            '11': ' Ноября', 
            '12': ' Декабря'
        }
        date_list_return = []
        for dayz in range(3):
            for i in self.cursor_table.execute ("""select date(datetime('now', 'localtime'), '+"""  + str(dayz) + """ day')"""):
                if dayz == 0:
                    date_list_return.append(['Сегодня'])
                    date_r = str(i[0][5:])
                    date_r = date_r.replace(date_r[0:3], number_to_date[date_r[0:2]])
                    date_r = date_r[-2:] + date_r[:-2]
                    self.today = date_r
                else:
                    date_r = str(i[0][5:])
                    date_r = date_r.replace(date_r[0:3], number_to_date[date_r[0:2]])
                    date_r = date_r[-2:] + date_r[:-2]
                    date_list_return.append([date_r])
        date_list_return.append(['Назад'])
        return date_list_return
    

    def time_list(self, checker):
        time_list_ret = []
        time_list_true = []
        for hh in range(10, 24, 1):
            for mm in range(0, 60, checker):
                tme = str()
                if hh < 10:
                    tme = '0' + str(hh)
                else:
                    tme = str(hh)
                if mm < 10:
                    tme += ':0' + str(mm)
                else:
                    tme += ':' + str(mm)
                time_list_ret.append(tme)
        now_time = str()
        for i in self.cursor_table.execute ("""select time(datetime('now', 'localtime'))"""):
            now_time = str(i[0][:-3])
        for i in time_list_ret:
            if checker == 15:
                if int(now_time[:-3]) == int(i[:-3]):
                    if int(now_time[3:]) < int(i[3:]):
                        time_list_true.append([str(i)])
                elif int(now_time[:-3]) < int(i[:-3]):
                    time_list_true.append([str(i)])
            else:
                time_list_true.append([str(i)])
            if len(time_list_true) == 9:
                break
        time_list_true.append(['Назад'])
        return time_list_true

    def today_to_string(self):
        return self.today
        

    def str_to_numb(self, data_text, time_text):
        date_to_number = {
            'Января': '01', 
            'Февраля': '02', 
            'Марта': '03', 
            'Апреля': '04',
            'Мая': '05', 
            'Июня': '06', 
            'Июля': '07', 
            'Августа': '08', 
            'Сентября': '09',
            'Октября': '10',
            'Ноября': '11', 
            'Декабря': '12'
        }
        return_date_time = '2018-'
        #2018-12-17 19:00:00
        data_number = date_to_number[data_text[3:]]
        return_date_time += data_number + '-' + data_text[:2] + ' ' + time_text + ':00'
        return return_date_time