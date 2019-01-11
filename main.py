import requests
import function
import datetime

d = datetime.date.today()
tomm = datetime.datetime.isoweekday(d) + 1
homework = function.homework_file()
data = function.homework_file()

while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=15000'.format(server=function.server,
                                                                       act='a_check',
                                                                       key=function.key,
                                                                       ts=function.ts)).json()
    update = long_poll['updates']
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
                function.homework_new_file(subject, homework)
                print([subject])
        print(update)
        user_id = update[0][3]
        user_name = function.vk_bot.method('users.get', {'user_ids': user_id})
        if 'расписание' in update[0][6]:
            if tomm == 8:
                function.write_msg(user_id, 'Технология, '
                                   'география, '
                                   'алгебра, '
                                   'физика, '
                                   'химия, '
                                   'физра')
            elif tomm == 2:
                function.write_msg(user_id, 'Литра, '
                                   'черчение, '
                                   'общество, '
                                   'инглиш, '
                                   'биология, '
                                   'геометрия, '
                                   'кл. час')
            elif tomm == 3:
                function.write_msg(user_id, 'Русский, '
                                   'инглиш, '
                                   'физра, '
                                   'история, '
                                   'алгебра, '
                                   'химия')
            elif tomm == 4:
                function.write_msg(user_id, 'Физика, '
                                   'география, '
                                   'русский, '
                                   'инглиш, '
                                   'обж, '
                                   'геометрия')
            elif tomm == 5:
                function.write_msg(user_id, 'Музыка, '
                                   'изо, '
                                   'инфа, '
                                   'биология, '
                                   'русский, '
                                   'история')
            elif tomm == 6:
                function.write_msg(user_id, 'Литра, '
                                   'геометрия, '
                                   'физра, '
                                   'история, '
                                   'спб, '
                                   'алгебра')
            elif tomm == 7:
                function.write_msg(user_id, 'завтра мы не учимся')