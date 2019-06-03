import requests
import function
import codecs
import json
import datetime as d

server, key, ts = function.long_poll()

while True:
    try:
        with codecs.open("keyboard_status.txt", "r", "utf-8-sig") as json_data:
            keyboard_status = json.load(json_data)
        homework = function.homework_file()
        data = function.homework_file()
        new_ts = function.vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
        ts = new_ts['ts']
        long_poll = requests.get('%s?act=%s&key=%s&ts=%s&wait=15000' % (server, 'a_check', key, ts)).json()
        update = long_poll['updates']
        for element in update:
            if element['type'] == 'message_new':
                user = function.vk_bot.method('users.get', {'user_ids': element['object']['from_id']})
                print('%s %s %s: %s' % (str(d.datetime.today())[10: 19], user[0]['first_name'], user[0]['last_name'], element['object']['text']))
                print(element['object']['from_id'])
                if str(element['object']['from_id']) not in keyboard_status:
                    keyboard_status['%s' % element['object']['from_id']] = 0
                    with codecs.open("keyboard_status.txt", "w", "utf-8-sig") as old_keyboard_status:
                        old_keyboard_status.write(str(keyboard_status).replace('\'', '\"'))
                        old_keyboard_status.close()
                    function.write_msg(element['object']['from_id'], 'ты добавлен в список пользователей', function.start_keyboard)
                    print('%s HomeWorkBot: ты добавлен в список пользователей' % str(d.datetime.today())[10: 19])
                else:
                    None
                if element['object']['text'] == 'получить дз':
                    function.write_msg(element['object']['from_id'], 'выбери предмет', function.choice_keyboard)
                    keyboard_status['%s' % element['object']['from_id']] = 0
                    with codecs.open("keyboard_status.txt", "w", "utf-8-sig") as old_keyboard_status:
                        old_keyboard_status.write(str(keyboard_status).replace('\'', '\"'))
                        old_keyboard_status.close()
                    print('%s HomeWorkBot: выбери предмет' % str(d.datetime.today())[10: 19])
                elif element['object']['text'] == 'назад':
                    function.write_msg(element['object']['from_id'], 'выбери действие', function.start_keyboard)
                    print('%s HomeWorkBot: выбери действие' % str(d.datetime.today())[10: 19])
                elif element['object']['text'] == 'задать дз' and keyboard_status['%s' % element['object']['from_id']] == 0:
                    function.write_msg(element['object']['from_id'], 'выбери предмет', function.choice_keyboard)
                    keyboard_status['%s' % element['object']['from_id']] = 1
                    with codecs.open("keyboard_status.txt", "w", "utf-8-sig") as old_keyboard_status:
                        old_keyboard_status.write(str(keyboard_status).replace('\'', '\"'))
                        old_keyboard_status.close()
                elif element['object']['text'] in data:
                    if keyboard_status['%s' % element['object']['from_id']] == 0:
                        function.write_msg(element['object']['from_id'], homework['%s' % element['object']['text']], None)
                        print('%s HomeWorkBot: %s' % (str(d.datetime.today())[10: 19], homework['%s' % element['object']['text']]))
                    elif keyboard_status['%s' % element['object']['from_id']] == 1:
                        function.write_msg(element['object']['from_id'], 'старое значение: %s' % homework['%s' % element['object']['text']], None)
                        function.write_msg(element['object']['from_id'], 'введи текст', None)
                        print('%s HomeWorkBot: введи текст' % str(d.datetime.today())[10: 19])
                        subject = element['object']['text']
                        keyboard_status['%s' % element['object']['from_id']] = 2
                        with codecs.open("keyboard_status.txt", "w", "utf-8-sig") as old_keyboard_status:
                            old_keyboard_status.write(str(keyboard_status).replace('\'', '\"'))
                            old_keyboard_status.close()
                elif keyboard_status['%s' % element['object']['from_id']] == 2:
                    function.homework_new_file(subject, element['object']['text'])
                    function.write_msg(element['object']['from_id'], 'значение обновлено', function.start_keyboard)
                    print('%s HomeWorkBot: значеие обновлено' % str(d.datetime.today())[10: 19])
                    print('value updated: %s: %s' % (subject, element['object']['text']))
                    keyboard_status['%s' % element['object']['from_id']] = 0
                else:
                    function.write_msg(element['object']['from_id'], 'неизвестная команда', function.start_keyboard)
                    print('%s HomeWorkBot: неизвестная команда' % str(d.datetime.today())[10: 19])

    except KeyError:
        if long_poll == {'failed': 2}:
            server, key, ts = function.long_poll()
        else:
            print('crushed')