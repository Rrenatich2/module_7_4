#Использование %:
team1_num = input('team1_num = ')
print('В команде Мастера кода участников: %s' % (team1_num))
team2_num = input('team2_num = ')
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

#Использование format():
score_1 = input('score_1 = ')
score_2 = input('score_2 = ')
print('Команда Волшебники данных решила задач: {}'.format(score_2))
team1_time = input('team1_time = ')
team2_time = input('team2_time = ')
print('Волшебники данных решили задачи за {} c'.format(team1_time))

#Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач')
tasks_total = input('tasks_total = ')
time_avg = input('time_avg = ')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
challenge_result = input('challenge_result = ')


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {challenge_result}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {challenge_result}!'
else:
    result = 'Ничья!'

print(result)

