import vk_api
import random
from config import *

vk_bot = vk_api.VkApi(token=ACCESS_TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
homework = {'алгебра': None, 'геометрия': None, 'Физика': None, 'химия': None, 'русский язык': None, 'английский язык': None, 'информатика': None, 'литература': None, 'музыка': None, 'изо': None, 'физ-ра': None, 'география': None, 'биология': None, 'история': None, 'обществознание': None}

print('готов к работе')

def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})