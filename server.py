#!/usr/bin/python
# -*- coding: utf-8 -*-
#test1337

import vk_api.vk_api
import add_table
import random
import create_data_base
import sqlite3

from collections import defaultdict
from create_key_board import new_key_board
from vk_api import VkUpload
from collections import *
from vk_api.longpoll import VkLongPoll, VkEventType
from list_of_ordered_tables import but
from action_for_user import *

class Server:
    def __init__(self, api_token, server_name: str = "Empty"):
        self.server_name = server_name
        self.vk = vk_api.VkApi(token = api_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_api = self.vk.get_api()
        self.step = defaultdict(int)
        self.person = defaultdict(int)
        self.date_z = defaultdict(str)
        self.time_z = defaultdict(str)
        self.text_now = defaultdict(list)
        self.user_table = defaultdict(int)
        self.about_user = defaultdict(str)
        self.text_about_table = str()
    def send_msg(self, send_id, message, key_board):
        self.vk_api.messages.send(peer_id = send_id,
                                  message = message,
                                  random_id = random.randint(1, 1000000000),
                                  keyboard = new_key_board(key_board)
                                  #keyboard=open("keyboard.json", "r", encoding = "UTF-8").read()
                                  )
        self.text_now[send_id] = key_board
    def check_message(self, event_text, send_id):
        for i in self.text_now[send_id]:
            for j in i:
                if j == event_text:
                    return True
        return False
    def start_for_manager(self, event):
        if self.step[event.user_id] == 0:
                    self.send_msg(event.user_id, 'Этап 1', [['Поступившие заявки'], ['Одобренные заявки']]) 
                    self.step[event.user_id] = 1
        elif self.step[event.user_id] == 1 and self.check_message(event.text, event.user_id) == True:
            if event.text == 'Поступившие заявки':
                self.send_msg(event.user_id, 'Этап 2',but())
            elif event.text == 'Одобренные заявки':
                self.send_msg(event.user_id, 'Этап 2',but())
            elif event.text == 'Назад':
                self.step[event.user_id] = 1
                self.send_msg(event.user_id, 'Этап 1', [['Поступившие заявки'], ['Одобренные заявки']])
                #elif event.text == id_столика:


    def start(self):
        test_list = add_table.table_list()
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == 340883759:
                self.start_for_manager(event)
            elif event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if self.step[event.user_id] == 0:
                    self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', 
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                    self.step[event.user_id] = 1
                elif self.step[event.user_id] == 1 and self.check_message(event.text, event.user_id) == True:
                   first_action(event, test_list, self)
                elif self.step[event.user_id] == 2 and self.check_message(event.text, event.user_id) == True:
                    second_action(event, test_list, self)
                elif self.step[event.user_id] == 3 and self.check_message(event.text, event.user_id) == True:
                    third_action(event, test_list, self)
                elif self.step[event.user_id] == 4 and self.check_message(event.text, event.user_id) == True:
                    four_action(event, test_list, self)
                elif self.step[event.user_id] == 5:
                    fifth_action(event, test_list, self)

                    

                    
                    


                    





    def test(self):
        self.send_msg(340883758, "Ку пацаны", [['Сосать']])