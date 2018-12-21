from server import Server
from config import vk_api_token
import add_table


server1 = Server(vk_api_token, "server1")
server1.start()