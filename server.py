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
        self.server_name = server_name #имя для экземпляра класса
        self.vk = vk_api.VkApi(token = api_token) # подключение к vk_api
        self.longpoll = VkLongPoll(self.vk) 
        self.vk_api = self.vk.get_api() 
        self.step = defaultdict(int) # создаем словарь, в котором ключ - это id пользователя, а значение - это этап, на котором пользователь
        self.person = defaultdict(int) # здесь в словаре ключ - id, значение - на сколько персон заказывает пользователь столик
        self.date_z = defaultdict(str) #здесь значение хранит дату, на которую выполняется заказ
        self.time_z = defaultdict(str) #здесь храним время, на которое выполняется заказ
        self.text_now = defaultdict(list) #здесь храним двумерный массив, который в дальнейшем нужен для проверки - нажал ли пользователь кнопку или ввел текст с клавиатуры самостоятельно
        self.user_table = defaultdict(int) #здесь храним номер столика, который достался пользователю
        self.about_user = defaultdict(str) 
        self.text_about_table = str()
    def send_msg(self, send_id, message, key_board): #функция отправки сообщения, send_id - id юзера, которому нужно отправить сообщение, message - сообщение, key_board - клавиатура для пользователя
        self.vk_api.messages.send(peer_id = send_id,
                                  message = message,
                                  random_id = random.randint(1, 1000000000), #id - сообщения
                                  keyboard = new_key_board(key_board) #функция new_key_board находится в файле create_key_board.py и преобразовывает двумерный массив в json формат
                                  #keyboard=open("keyboard.json", "r", encoding = "UTF-8").read()
                                  )
        self.text_now[send_id] = key_board #сохраняем двумерный массив
    def check_message(self, event_text, send_id): #Функция проверяет отправленое пользователем сообщение
        for i in self.text_now[send_id]:
            for j in i:
                if j == event_text: #если отправленное сообщение есть в двумерном массиве, значит пользователь нажал кнопку
                    return True
        return False
    def start_for_manager(self, event): #Функция, которая обрабатывает сообщения менеджера
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


    def start(self): #основная функция
        test_list = add_table.table_list()
        for event in self.longpoll.listen(): #Слушаем события в группе
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.user_id == 340883759: #если поступило новое сообщение и сообщение от менеджера
                self.start_for_manager(event) #Запускаем функцию, которая обрабатывает сообщения менеджера
            elif event.type == VkEventType.MESSAGE_NEW and event.to_me: #если сообщение от обычного пользователя
                if self.step[event.user_id] == 0: #если пользователь пишет в первый раз, то выводим приветственное сообщение
                    self.send_msg(event.user_id, 'Добро пожаловать, выбери на сколько человек', #отправляем приветственное сообщение и выводим клавиатуру с выбором на сколько человек нужен столик
                                [['Столик на двоих'], ['Столик на троих'], ['Столик на четверых'], ['Столик на большую компанию']])
                    self.step[event.user_id] = 1 #переводим пользователя на следюущий этап
                elif self.step[event.user_id] == 1 and self.check_message(event.text, event.user_id) == True:
                   first_action(event, test_list, self) #запускаем функцию, для первого этапа из файла action_for_user.py
                elif self.step[event.user_id] == 2 and self.check_message(event.text, event.user_id) == True:
                    second_action(event, test_list, self) #Запускаем функция для второго этапа
                elif self.step[event.user_id] == 3 and self.check_message(event.text, event.user_id) == True:
                    third_action(event, test_list, self)
                elif self.step[event.user_id] == 4 and self.check_message(event.text, event.user_id) == True:
                    four_action(event, test_list, self)
                elif self.step[event.user_id] == 5:
                    fifth_action(event, test_list, self)

                    

                    
                    


                    





    def test(self):
        self.send_msg(340883758, "Ку пацаны", [['Сосать']])