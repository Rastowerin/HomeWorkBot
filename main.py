import requests
import function

homework = function.homework_file()
data = function.homework_file()

while True:
    new_ts = function.vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
    function.ts = new_ts['ts']
    long_poll = requests.get(
        '{server}?act={act}&key={key}&ts={ts}&wait=15000'.format(server=function.server,
                                                                       act='a_check',
                                                                       key=function.key,
                                                                       ts=function.ts)).json()
    update = long_poll['updates']
    for element in update:
        if element['type'] == 'message_new':
            command = element['object']['text'].split(': ')[0]
            subject = element['object']['text'].split(': ')[1]
            if command == '!дз' and '%s' % subject in function.homework:
                print('test')
                function.write_msg(element['object']['from_id'], function.homework['%s' % subject])
            elif command == '!!дз':
                subject = element['object']['text'].split(': ')[1]
                homework = element['object']['text'].split(': ')[2]
                print(subject)
                print(homework)
                if '%s' % subject in data:
                    function.homework_new_file(subject, homework)
                    print([subject])
                else:
                    user_id = element['object']['from_id']
                    user_name = function.vk_bot.method('users.get', {'user_ids': user_id})