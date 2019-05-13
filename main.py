import requests
import function
import datetime as d

server, key, ts = function.long_poll()

while True:
    try:
        function.time_check()
        homework = function.homework_file()
        data = function.homework_file()
        new_ts = function.vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
        ts = new_ts['ts']
        long_poll = requests.get(
            '{server}?act={act}&key={key}&ts={ts}&wait=15000'.format(server=server,
                                                                           act='a_check',
                                                                           key=key,
                                                                           ts=ts)).json()
        update = long_poll['updates']
        for element in update:
            if element['type'] == 'message_new':
                user = function.vk_bot.method('users.get', {'user_ids': element['object']['from_id']})
                print('%s %s %s: %s' % (str(d.datetime.today())[10: 19], user[0]['first_name'], user[0]['last_name'], element['object']['text']))
                if element['object']['text'].split(': ')[0] == '!дз':
                    subject = str(element['object']['text'].split(': ')[1]).lower()
                    if subject in function.homework:
                        function.write_msg(element['object']['from_id'], homework['%s' % subject])
                        print('%s HomeWorkBot: %s' % (str(d.datetime.today())[10: 19], homework['%s' % subject]))
                    else:
                        function.write_msg(element['object']['from_id'], 'неизвестная команда')
                        print('%s HomeWorkBot: неизвестная команда' % str(d.datetime.today())[10: 19])
                elif element['object']['text'].split(': ')[0] == '!!дз':
                    subject = element['object']['text'].split(': ')[1]
                    homework = element['object']['text'].split(': ')[2]
                    if '%s' % subject in data:
                        function.homework_new_file(subject, homework)
                        function.write_msg(element['object']['from_id'], 'значение обновлено')
                        print('%s HomeWorkBot: значеие обновлено' % str(d.datetime.today())[10: 19])
                        print('value updated: %s: %s' % (subject, homework))
                    else:
                        user_id = element['object']['from_id']
                        user_name = function.vk_bot.method('users.get', {'user_ids': user_id})
                else:
                    function.write_msg(element['object']['from_id'], 'неизвестная команда')
                    print('%s HomeWorkBot: неизвестная команда' % str(d.datetime.today())[10: 19])

    except KeyError:
        if long_poll == {'failed': 2}:
            server, key, ts = function.long_poll()
        else:
            print('crushed')