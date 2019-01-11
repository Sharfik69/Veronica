import add_table
import random

from collections import defaultdict
from create_key_board import new_key_board
from collections import defaultdict
from vk_api.longpoll import VkLongPoll, VkEventType
from list_of_ordered_tables import but

def first_action(event, test_list, server1):
    def print_type_table(result): #функция, которая отправляет пользователю свободные столики
        s = str()
        for i in result:
                for j in i:
                    if j != 'Назад':
                        s += test_list.print_about_table(int(j)) + '\n\n'
        server1.send_msg(event.user_id, s, [['Одну минуту']])

    if event.text == 'Назад': #если нажата кнопка "Назад", то переходим на шаг назад и выводим предыдущую клавиатуру
        server1.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])

    if event.text == 'Столик на двоих': #если нажата кнопка "Столик на двоих"
        result = test_list.select_table(2) #Проверяем свободные столики в функции select_table из файла add_table.py
        if result == False:
            server1.send_msg(event.user_id, 'На данный момент все столики на двоих заняты, посмотрите столики на троих', [['Назад']])
        else:
            print_type_table(result) 
            server1.send_msg(event.user_id, 'Имеются следующие виды столов на два человека', result) #Отправляем пользователю свободные столики
            server1.step[event.user_id] = 2 #переводим пользователя на следующий этап заказа
            #server1.person = 2
            server1.person[event.user_id] = 2 #Запоминаем на сколько человек пользователь заказал столик
    if event.text == 'Столик на троих':
        result = test_list.select_table(3)
        if result == False:
            server1.send_msg(event.user_id, 'На данный момент все столики на троих заняты', [['Назад']])
        else:
            print_type_table(result)
            server1.send_msg(event.user_id, 'Имеются следующие виды столов на три человека', result)
            server1.step[event.user_id] = 2
            server1.person[event.user_id] = 3

            
    if event.text == 'Столик на четверых': #Аналогичные действия, как и для столика на двоих
        result = test_list.select_table(4)
        if result == False:
            server1.send_msg(event.user_id, 'На данный момент все столики на четверых заняты', [['Назад']])
        else:
            print_type_table(result)
            server1.send_msg(event.user_id, 'Имеются следующие виды столов на четыре человека', result)
            server1.step[event.user_id] = 2
            server1.person[event.user_id] = 4
            
    if event.text == 'Столик на большую компанию':
        result = test_list.select_table(5)
        if result == False:
            server1.send_msg(event.user_id, 'На данный момент все столики на четверых заняты', [['Назад']])
        else:
            print_type_table(result)
            server1.send_msg(event.user_id, 'Имеются следующие виды столов на большую человека', result)
            server1.step[event.user_id] = 2
            server1.person[event.user_id] = 5

def second_action(event, test_list, server1):
    def reservration_of_table(person):
        choosen_type = int(event.text) #здесь мы запоминаем тип столика, который выбрал пользователь
        server1.user_table[event.user_id] = test_list.table_for_user(person, choosen_type)
        if server1.user_table[event.user_id] == None: #если случилась ошибка и столика с таким типом нет, сообщаем об этом
            server1.step[event.user_id] = 1
            server1.send_msg(event.user_id, 'Столика с таким типом нет, извините', 
                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
        else:
            test_list.Reservation(server1.user_table[event.user_id]) #если столик есть, в таблице базы данных ставим счетчик чекер в 0, функция Reservation в файле add_table.py
            server1.send_msg(event.user_id, 'Вы выбираете столик на ' + str(server1.person[event.user_id]) + ' человек\nВыберете дату заказа', test_list.date_list())
            server1.step[event.user_id] = 3 #переводим на следующий этап

    if event.text == 'Назад': #если нажата кнопка назад, то переходим на первый этап и выводим сообщения о выборе столика
        server1.step[event.user_id] = 1
        server1.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
    elif server1.person[event.user_id] == 2 and event.text.isdigit():
        reservration_of_table(2)
    elif server1.person[event.user_id] == 3 and event.text.isdigit():
        reservration_of_table(3)
    elif server1.person[event.user_id] == 4 and event.text.isdigit():
        reservration_of_table(4)
    elif server1.person[event.user_id] == 5 and event.text.isdigit():
        reservration_of_table(5)

def third_action(event, test_list, server1):
    if event.text == 'Назад':
        server1.step[event.user_id] = 1
        server1.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
    elif event.text == 'Сегодня': #Если пользователь выбрал кнопку заказа столика на сегодня, то парси
        server1.date_z[event.user_id] = test_list.today_to_string() #вызываем функцию, котора возвращает сегодняшнюю дату, today_to_string из файла add_table
        server1.send_msg(event.user_id, 'Вы выбираете столик на ' + str(server1.person[event.user_id]) + ' человек\nВыберете время заказа', test_list.time_list(15)) #сообщаем пользователю, что он выбрал дату и сейчас ему надо выбрать время заказа. Вызываем функцию time_list из add_table.py
        server1.step[event.user_id] = 4
    else:
        server1.date_z[event.user_id] = event.text
        server1.send_msg(event.user_id, 'Вы выбираете столик на ' + str(server1.person[event.user_id]) + ' человек\nВыберете время заказа', test_list.time_list(30))
        server1.step[event.user_id] = 4

def four_action(event, test_list, server1):
    if event.text == 'Назад':
        server1.step[event.user_id] = 1
        server1.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                 [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
    else:
        server1.step[event.user_id] = 5 #в этой функции мы запоминаем всю информацию о дате и времени заказа и просим пользователя ввести имя и номер телефона для подтверждения заказа
        server1.time_z[event.user_id] = event.text
        server1.text_about_table = 'Ваш столик на ' + str(server1.person[event.user_id]) + ' персоны назначен на ' + str(server1.date_z[event.user_id]) + ' ' + str(server1.time_z[event.user_id])
        server1.send_msg(event.user_id, 'Пожалуйста отправтье ваше имя и номер телефона, мы свяжемся с вами, чтобы подтвердить заказ', [['Ok']])
        test_list.Add_Order(server1.user_table[event.user_id],
         event.user_id, 1, test_list.str_to_numb(server1.date_z[event.user_id], server1.time_z[event.user_id]))

def fifth_action(event, test_list, server1):
    server1.send_msg(event.user_id, 'Спасибо за заказ, мы скоро с вами свяжемся', [['Ok']])
    server1.about_user[event.user_id] = event.text
                    
