#!/usr/bin/python
# -*- coding: utf-8 -*-
#test123

import vk_api.vk_api
import add_table

from vk_api import VkUpload
from collections import defaultdict
from vk_api.longpoll import VkLongPoll, VkEventType

class Server:
    def __init__(self, api_token, server_name: str = "Empty"):
        self.server_name = server_name
        self.vk = vk_api.VkApi(token = api_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_api = self.vk.get_api()
    def send_msg(self, send_id, message):
        self.vk_api.messages.send(peer_id = send_id,
                                  message = message)

    def start(self, some_text):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.send_msg(event.user_id, some_text)

    def test(self):
        self.send_msg(340883758, "Ку пацаны")