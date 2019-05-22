import requests
import function
import datetime as d

server, key, ts = function.long_poll()
keyboard_status = {}

while True:
    try:
        function.time_check()
        homework = function.homework_file()
        data = function.homework_file()
        new_ts = function.vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
        ts = new_ts['ts']
        long_poll = requests.get(
            '{server}?act={act}&key={key}&ts={ts}&wait=15000'.format(server=server,
                                                                           act='a_check', key=key, ts=ts)).json()
        update = long_poll['updates']
        for element in update:
            if element['type'] == 'message_new':
                user = function.vk_bot.method('users.get', {'user_ids': element['object']['from_id']})
                print('%s %s %s: %s' % (str(d.datetime.today())[10: 19], user[0]['first_name'], user[0]['last_name'], element['object']['text']))
                if element['object']['text'] == 'получить дз':
                    function.write_msg(element['object']['from_id'], 'выбери предмет', function.choice_keyboard)
                    keyboard_status['%s' % element['object']['from_id']] = 0
                    print('%s HomeWorkBot: выбери предмет' % str(d.datetime.today())[10: 19])
                elif element['object']['text'] == 'назад':
                    function.write_msg(element['object']['from_id'], 'выбери действие', function.start_keyboard)
                    print('%s HomeWorkBot: выбери действие' % str(d.datetime.today())[10: 19])
                elif element['object']['text'] == 'задать дз' and keyboard_status['%s' % element['object']['from_id']] == 0:
                    function.write_msg(element['object']['from_id'], 'выбери предмет', function.choice_keyboard)
                    keyboard_status['%s' % element['object']['from_id']] = 1
                elif element['object']['text'] in data:
                    if keyboard_status['%s' % element['object']['from_id']] == 0:
                        function.write_msg(element['object']['from_id'], homework['%s' % element['object']['text']], None)
                        print('%s HomeWorkBot: %s' % (str(d.datetime.today())[10: 19], homework['%s' % element['object']['text']]))
                    elif keyboard_status['%s' % element['object']['from_id']] == 1:
                        function.write_msg(element['object']['from_id'],'старое значение: %s' % homework['%s' % element['object']['text']], None)
                        function.write_msg(element['object']['from_id'], 'введи текст', None)
                        print('%s HomeWorkBot: введи текст' % str(d.datetime.today())[10: 19])
                        subject = element['object']['text']
                        keyboard_status['%s' % element['object']['from_id']] = 2
                    else:
                        None
                elif keyboard_status['%s' % element['object']['from_id']] == 2:
                    function.homework_new_file(subject, element['object']['text'])
                    function.write_msg(element['object']['from_id'], 'значение обновлено', function.start_keyboard)
                    print('%s HomeWorkBot: значеие обновлено' % str(d.datetime.today())[10: 19])
                    print('value updated: %s: %s' % (subject, element['object']['text']))
                    keyboard_status['%s' % element['object']['from_id']] = 0
                elif keyboard_status['%s' % element['object']['from_id']]
                else:
                    function.write_msg(element['object']['from_id'], 'неизвестная команда', function.start_keyboard)
                    print('%s HomeWorkBot: неизвестная команда' % str(d.datetime.today())[10: 19])

    except KeyError:
        if long_poll == {'failed': 2}:
            server, key, ts = function.long_poll()
        else:
            print('crushed')