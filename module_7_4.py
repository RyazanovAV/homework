team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
name1 = 'Мастера кода!'
name2 = 'Волшебники Данных'

# print('В команде Мастера кода участников: %s' % '5 ! ' )
# print('Итого сегодня в командах участников: %s и %s' % ('5', '6'))
# print('Команда Волшебники данных решила задач: {}' .format(42))
# print('Волшебники данных решили задачи за {} {}' .format(team1_time, 'с !'))
# print(f'Команды решили {score_1} и {score_2} задач.')
# print(f'Результат битвы: победа команды {name1}!')
# print (f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = name1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = name2
else:
    result = 'Ничья'

print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print('Команда {} решила задачи: {}' .format(name2, score_2))
print('{} решили задачи за {} с ! ' .format(name2, team2_time))
print('Команда {} решила задачи: {}' .format(name1, score_1))
print('{} решили задачи за {} с ! ' .format(name1, team2_time))
print (f'Сегодня было решено {score_1 + score_2} задач, в среднем по {team1_time + team2_time} секунды на задачу!.')
print (f'Победа команды {result} !')