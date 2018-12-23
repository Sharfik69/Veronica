#!/usr/bin/python
# -*- coding: utf-8 -*-
#test1337

import vk_api.vk_api
import add_table
import random

from collections import defaultdict
from create_key_board import new_key_board
from vk_api import VkUpload
from collections import defaultdict
from vk_api.longpoll import VkLongPoll, VkEventType

class Server:
    def __init__(self, api_token, server_name: str = "Empty"):
        self.server_name = server_name
        self.vk = vk_api.VkApi(token = api_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_api = self.vk.get_api()
        self.step = defaultdict(int)
        self.person = 0
        self.date_z = str()
        self.time_z = str()
        self.text_now = [[]]
    def send_msg(self, send_id, message, key_board):
        self.vk_api.messages.send(peer_id = send_id,
                                  message = message,
                                  random_id = random.randint(1, 1000000000),
                                  keyboard = new_key_board(key_board)
                                  #keyboard=open("keyboard.json", "r", encoding = "UTF-8").read()
                                  )
        self.text_now = key_board
    def check_message(self, event_text):
        for i in self.text_now:
            for j in i:
                if j == event_text:
                    return True
        return False
    def start(self):
        test_list = add_table.table_list()
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if self.step[event.user_id] == 0:
                    self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                    self.step[event.user_id] = 1
                elif self.step[event.user_id] == 1 and self.check_message(event.text) == True:
                    
                    def print_type_table(result):
                        for i in result:
                                for j in i:
                                    if j != 'Назад':
                                        self.send_msg(event.user_id, test_list.print_about_table(int(j)), [['Одну минуту']])

                    if event.text == 'Назад':
                        self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])

                    if event.text == 'Столик на двоих':
                        result = test_list.select_table(2)
                        if result == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на двоих заняты', [['Назад']])
                        else:
                            print_type_table(result)
                            self.send_msg(event.user_id, 'Выберет тип стола, который вас интересует', result)
                            self.step[event.user_id] = 2
                            self.person = 2
                    if event.text == 'Столик на троих':
                        result = test_list.select_table(3)
                        if result == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на троих заняты', [['Назад']])
                        else:
                            print_type_table(result)
                            self.send_msg(event.user_id, 'Выберет тип стола, который вас интересует', result)
                            self.step[event.user_id] = 2
                            self.person = 3

                            
                    if event.text == 'Столик на четверых':
                        result = test_list.select_table(4)
                        if result == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на четверых заняты', [['Назад']])
                        else:
                            print_type_table(result)
                            self.send_msg(event.user_id, 'Выберет тип стола, который вас интересует', result)
                            self.step[event.user_id] = 2
                            self.person = 4
                            
                    if event.text == 'Столик на большую компанию':
                        result = test_list.select_table(5)
                        if result == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на четверых заняты', [['Назад']])
                        else:
                            print_type_table(result)
                            self.send_msg(event.user_id, 'Выберет тип стола, который вас интересует', result)
                            self.step[event.user_id] = 2
                            self.person = 5
                elif self.step[event.user_id] == 2 and self.check_message(event.text) == True:
                    def reservration_of_table(person):
                        choosen_type = int(event.text)
                        user_table = test_list.table_for_user(person, choosen_type)
                        if user_table == None:
                            self.step[event.user_id] = 1
                            self.send_msg(event.user_id, 'Столика с таким типом нет, извините', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                        else:
                            test_list.Reservation(user_table)
                            test_list.Add_Order(user_table, event.user_id, 1)
                            self.send_msg(event.user_id, 'Выберете дату заказа', test_list.date_list())
                            self.step[event.user_id] = 3

                    if event.text == 'Назад':
                        self.step[event.user_id] = 1
                        self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                    elif self.person == 2 and event.text.isdigit():
                        reservration_of_table(2)
                    elif self.person == 3 and event.text.isdigit():
                        reservration_of_table(3)
                    elif self.person == 4 and event.text.isdigit():
                        reservration_of_table(4)
                    elif self.person == 5 and event.text.isdigit():
                        reservration_of_table(5)
                elif self.step[event.user_id] == 3 and self.check_message(event.text) == True:
                    if event.text == 'Назад':
                        self.step[event.user_id] = 1
                        self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                    elif event.text == 'Сегодня':
                        self.date_z = event.text
                        self.send_msg(event.user_id, 'Выберете время заказа', test_list.time_list(15))
                        self.step[event.user_id] = 4
                    else:
                        self.date_z = event.text
                        self.send_msg(event.user_id, 'Выберете время заказа', test_list.time_list(30))
                        self.step[event.user_id] = 4
                elif self.step[event.user_id] == 4 and self.check_message(event.text) == True:
                    if event.text == 'Назад':
                        self.step[event.user_id] = 1
                        self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                    else:
                        self.step[event.user_id] = 5
                        self.time_z = event.text
                        self.send_msg(event.user_id, 'Ваш заказ был добавлен', [['Ok']])


                    

                    
                    


                    





                '''
                if event.text == 'Столы':
                    for i in range(test_list.FreeTable()):
                        s = test_list.AboutTable(i, 2)
                        if s != 'about':
                            self.send_msg(event.user_id, s, test_list.List_of_free_table(2))
                elif event.text >= '1' and event.text <= '5':
                    num_of_table = int(event.text)
                    if test_list.Table_is_free(num_of_table) == 1:
                        self.send_msg(event.user_id, 'Стол забронирован', [['Ok']])
                    else:
                        self.send_msg(event.user_id, 'Стол занят', [['Назад']])
                '''


    def test(self):
        self.send_msg(340883758, "Ку пацаны", [['Сосать']])