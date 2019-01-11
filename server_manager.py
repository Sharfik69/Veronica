from server import Server
from config import vk_api_token
import add_table

'''
Основной исполняемый файл
Создаем экземпляр класса Server из файла server.py и запускаем его
'''
server1 = Server(vk_api_token, "server1")
server1.start()