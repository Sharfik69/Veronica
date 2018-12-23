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
    def send_msg(self, send_id, message, key_board):
        self.vk_api.messages.send(peer_id = send_id,
                                  message = message,
                                  random_id = random.randint(1, 1000000000),
                                  keyboard = new_key_board(key_board)
                                  #keyboard=open("keyboard.json", "r", encoding = "UTF-8").read()
                                  )

    def start(self):
        test_list = add_table.table_list()
        test_list.LoadTable()
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if self.step[event.user_id] == 0:
                    self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                    self.step[event.user_id] = 1
                elif self.step[event.user_id] == 1:

                    def print_list_table(cnt_person):
                        check_table = False
                        for i in range(test_list.FreeTable()):
                            s = test_list.AboutTable(i, cnt_person)
                            if s != 'about':
                                check_table = True
                                self.send_msg(event.user_id, s, test_list.List_of_free_table(cnt_person))
                        return check_table

                    if event.text == 'Столик на двоих':
                        if print_list_table(2) == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на двоих заняты', [['Назад']])
                        else:
                            self.send_msg(event.user_id, 'Желаете забронировать этот столик?', [['да'],['нет']])
                            if event.text == 'да':
                                self.step[event.user_id] = 2
                    elif event.text == 'Столик на троих':
                        if print_list_table(3) == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на троих заняты', [['Назад']])
                        else:
                            self.send_msg(event.user_id, 'Желаете забронировать этот столик?', [['да'],['нет']])
                            if event.text == 'да':
                                self.step[event.user_id] = 2
                    elif event.text == 'Столик на четверых':
                        if print_list_table(4) == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на четверых заняты', [['Назад']])
                        else:
                            self.send_msg(event.user_id, 'Желаете забронировать этот столик?', [['да'],['нет']])
                            if event.text == 'да':
                                self.step[event.user_id] = 2
                    elif event.text == 'Столик на большую компанию':
                        if print_list_table(5) == False:
                            self.send_msg(event.user_id, 'На данный момент все столики на большую компанию заняты', [['Назад']])
                        else:
                            self.send_msg(event.user_id, 'Желаете забронировать этот столик?', [['да'],['нет']])
                            if event.text == 'да':
                                self.step[event.user_id] = 2
                    elif event.text == 'Назад':
                        self.step[event.user_id] = 1
                        self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])

                elif self.step[event.user_id] == 2:
                    self.send_msg(event.user_id, 'Выбранный Вами столик забронирован!',[])

                    
                    





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
# your code goes here