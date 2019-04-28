import vk_api
import random
import codecs
import json
import datetime
from config import *

def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})

def write_msg_attach(user_id, text, att_url):
    vk_bot.method('messages.send',
                  {'user_id': user_id,
                   'attachment': att_url,
                   'message': text,
                   'random_id': random.randint(0, 1000)})

def homework_file():
    with codecs.open("subjects.txt", "r", "utf-8-sig") as json_data:
        data = json.load(json_data)
        return data

def today():
    day = datetime.datetime.today().weekday()
    with codecs.open("schedule.txt", "r", "utf-8-sig") as json_data:
        data = json.load(json_data)
        today = data[str(day)]
        return today

def

def homework_new_file(subject, new_homework):
    homework = homework_file()
    homework[subject] = new_homework
    homework = str(homework).replace('\'', '\"')
    with codecs.open("subjects.txt", "w", "utf-8-sig") as test:
        test.write(homework)
        test.close()

vk_bot = vk_api.VkApi(token=TOKEN)
long_poll = vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
homework = homework_file()

print('HomeWorkBot is online')