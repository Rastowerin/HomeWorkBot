import random
import datetime
import requests
import vk_api
import function
from config import *

d = datetime.date.today()
tomm = datetime.datetime.isoweekday(d) + 1

vk_bot = vk_api.VkApi(token=TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print("готов к работе")

while True:
 long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=15000'.format(server=server,
                                                                       act='a_check',
                                                                       key=key,
                                                                       ts=ts)).json()
 update = long_poll['updates']
 if update[0][0] == 4:
     if update[0][0] == 4 and '!дз' in update[0][6] and '!!дз' not in update[0][6] and update[0][6] != '!дз':
         subject = update[0][6].split(': ')[1]
         if '%s' % subject in homework:
             write_msg(update[0][3], homework['%s' % subject])
     elif update[0][0] == 4 and update[0][3] == 321056236 and '!!дз' in update[0][6] and update[0][6] != '!!дз':
         subject = update[0][6].split(': ')[1]
         print(subject)
         if '%s' % subject in homework:
             homework['%s' % subject] = update[0][6].split(': ')[2]
             print(homework['%s' % subject])
        print(update)
        user_id = update[0][3]
        user_name = vk_bot.method('users.get', {'user_ids': user_id})
        if 'привет' in update[0][6]:
            write_msg(user_id, 'здоров, ' + (user_name[0]['first_name']))  # cooбщение пользователю
        print(str(user_name[0]['first_name']) + ' ' +
              str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(update[0][6]))  # cooбщение пользователя
        if 'расписание' in update[0][6]:
            if tomm == 8:
                write_msg(user_id, 'Технология, '
                                   'география, '
                                   'алгебра, '
                                   'физика, '
                                   'химия, '
                                   'физра')
            elif tomm == 2:
                write_msg(user_id, 'Литра, '
                                   'черчение, '
                                   'общество, '
                                   'инглиш, '
                                   'биология, '
                                   'геометрия, '
                                   'кл. час')
            elif tomm == 3:
                write_msg(user_id, 'Русский, '
                                   'инглиш, '
                                   'физра, '
                                   'история, '
                                   'алгебра, '
                                   'химия')
            elif tomm == 4:
                write_msg(user_id, 'Физика, '
                                   'география, '
                                   'русский, '
                                   'инглиш, '
                                   'обж, '
                                   'геометрия')
            elif tomm == 5:
                write_msg(user_id, 'Музыка, '
                                   'изо, '
                                   'инфа, '
                                   'биология, '
                                   'русский, '
                                   'история')
            elif tomm == 6:
                write_msg(user_id, 'Литра, '
                                   'геометрия, '
                                   'физра, '
                                   'история, '
                                   'спб, '
                                   'алгебра')
            elif tomm == 7:
                write_msg(user_id, 'завтра мы не учимся')

    # меняем ts для след запроса
 ts = long_poll['ts']