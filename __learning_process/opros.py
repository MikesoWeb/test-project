name = input('Ваше имя: ')
print(f'Здравствуйте, {name}\n! ')
print('Чтобы мы смогли подобрать вам интересный контент, ответьте пожалуйста на нашу небольшую анкету.')
print('Так же мы начислим вам по 5 токенов за каждый ответ. Спасибо.\n')

surname = input('Ваша фамилия: ')
age = int(input('Ваш возраст: '))
like_color = input('Ваш любимый цвет: ')
city = input('Город проживания: ')
country = input('Страна проживания: ')
car = input('У вас  есть автомобиль? ')
like_woman_name = input('Любимое женское имя: ')
like_game = input('Ваша любимая компьютерная игра: ')
home_animals = input('У вас есть домашние животные? Если есть, то какие? ')

data_users = {
    'Имя: ': name,
    'Фамилия: ': surname,
    'Возраст: ': age,
    'Любимый цвет: ': like_color,
    'Город: ': city,
    'Страна: ': country,
    'Есть авто?: ': car,
    'Любимое женское имя: ': like_woman_name,
    'Любимая компьютерная игра: ': like_game,
    'Есть ли домашние животные: ': home_animals
}
count_question = 0
count_answer = 0
a = input('')

for data_is_empty in data_users.values():
    if data_is_empty != '':
        count_answer += 1

for data in data_users.items():
    print(data)
    count_question += 1


print('Всего вопросов: ', count_question)
print()
print(f'Спасибо за участие. Токены в размере {count_answer * 5} будут начислены вам в течении пары минут.')
