import vk_api
import random
import codecs
import json
import datetime
from threading import Thread
from config import *

with codecs.open("start_keyboard.txt", "r", "utf-8-sig") as json_data:
    start_keyboard = json.load(json_data)
    
start_keyboard = json.dumps(start_keyboard, ensure_ascii=False).encode('utf-8')
start_keyboard = str(start_keyboard.decode('utf-8'))

with codecs.open("choice_keyboard.txt", "r", "utf-8-sig") as json_data:
    choice_keyboard = json.load(json_data)
choice_keyboard = json.dumps(choice_keyboard, ensure_ascii=False).encode('utf-8')
choice_keyboard = str(choice_keyboard.decode('utf-8'))

with codecs.open("back_keyboard.txt", "r", "utf-8-sig") as json_data:
    back_keyboard = json.load(json_data)
back_keyboard = json.dumps(back_keyboard, ensure_ascii=False).encode('utf-8')
back_keyboard = str(back_keyboard.decode('utf-8'))

def control():
    while True:
        homework = homework_file()
        command = input()
        if command == 'reset':
            for subject in homework:
                homework[subject] = 'None'
            homework = str(homework).replace('\'', '\"')
            with codecs.open("subjects.txt", "w", "utf-8-sig") as file:
                file.write(homework)
                file.close()
            print('homework reseted')
        elif 'reset' in command and command.split(' ')[1] in homework:
            homework[command.split(' ')[1]] = 'None'
            homework = str(homework).replace('\'', '\"')
            with codecs.open("subjects.txt", "w", "utf-8-sig") as file:
                file.write(homework)
                file.close()
                print('subject reseted')
        else:
            print('wrong command')

def write_msg(user_id, text, keyboard):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000), 'keyboard': keyboard})

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

homework = homework_file()

def homework_new_file(subject, new_homework):
    homework = homework_file()
    homework[subject] = new_homework
    homework = str(homework).replace('\'', '\"')
    with codecs.open("subjects.txt", "w", "utf-8-sig") as file:
        file.write(homework)
        file.close()

def today():
    day = str(datetime.datetime.today().weekday())
    with codecs.open("schedule.txt", "r", "utf-8-sig") as json_data:
        data = json.load(json_data)
        today_schedule = data[str(day)]
        time = (str(str(datetime.datetime.today()).split(' ')[1].split('.')[0]))
        info = [day, time, today_schedule]
    return info

def long_poll():
    long_poll = vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
    server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
    return server, key, ts

today_schedule = {}
today_schedule = today()[2]
for element in today_schedule:
    today_schedule[element] = [today_schedule[element], 0]

def time_check():
    for subject_time in today_schedule:
        print(homework)
        print(today_schedule)
        print(homework[today_schedule[subject_time][0]])
        if homework[today_schedule[subject_time][0]] != 'None' and today_schedule[subject_time][1] == 0:
            print('test')
            time = homework[today_schedule[subject_time]][1]
            time = time.split(' ')[1]
            if time.split(':')[0] > subject_time.split(':')[0] or today()[1].split(':')[0] == subject_time.split(':')[0] and today()[1].split(':')[1] > subject_time.split(':')[1]:
                homework_new_file(today_schedule[subject_time], 'None')
            None

with codecs.open("schedule.txt", "r", "utf-8-sig") as json_data:
    day = json.load(json_data)['day']

thread = Thread(target=control)
thread.start()

vk_bot = vk_api.VkApi(token=TOKEN)

print('HomeWorkBot is online')