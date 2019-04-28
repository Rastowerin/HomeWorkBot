import requests
import function
from time import sleep

homework = function.homework_file()
data = function.homework_file()
print(data)

while True:
    sleep(1)
    new_ts = function.vk_bot.method('groups.getLongPollServer', {'group_id': 181347142, 'lp_version': 3})
    function.ts = new_ts['ts']
    long_poll = requests.get(
        '{server}?act={act}&key={key}&ts={ts}&wait=15000'.format(server=function.server,
                                                                       act='a_check',
                                                                       key=function.key,
                                                                       ts=function.ts)).json()
    update = long_poll['updates']
    print(update)
    if update[0][0] == 4:
        if update[0][0] == 4 and '!дз' in update[0][6] and '!!дз' not in update[0][6] and update[0][6] != '!дз':
            subject = update[0][6].split(': ')[1]
            if '%s' % subject in function.homework:
                function.write_msg(update[0][3], function.homework['%s' % subject])
        elif update[0][0] == 4 and update[0][3] == 321056236 and '!!дз' in update[0][6] and update[0][6] != '!!дз':
            subject = update[0][6].split(': ')[1]
            homework = update[0][6].split(': ')[2]
            print(subject)
            if '%s' % subject in data:
                print(1)
                function.homework_new_file(subject, homework)
                print([subject])
            else:
                print(0)
        user_id = update[0][3]
        user_name = function.vk_bot.method('users.get', {'user_ids': user_id})