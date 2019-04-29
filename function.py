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

def homework_new_file(subject, new_homework):
    homework = homework_file()
    homework[subject] = new_homework
    homework = str(homework).replace('\'', '\"')
    with codecs.open("subjects.txt", "w", "utf-8-sig") as test:
        test.write(homework)
        test.close()

def today():
    day = str(datetime.datetime.today().weekday())
    with codecs.open("schedule.txt", "r", "utf-8-sig") as json_data:
        data = json.load(json_data)
        today_schedule = data[str(day)]
        time = (str(str(datetime.datetime.today()).split(' ')[1].split('.')[0]))
        info = [day, time, today_schedule]
    return info

def time_check():
    with codecs.open("subjects.txt", "r", "utf-8-sig") as json_data:
        subjects = json.load(json_data)
        print(today())
        if today()[1] in subjects:
            print('test')
            if today()[2][1] != None:
                print('test1')
                subjects[today()[2][1]] = None

vk_bot = vk_api.VkApi(token=TOKEN)
long_poll = vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
homework = homework_file()

print('HomeWorkBot is online')