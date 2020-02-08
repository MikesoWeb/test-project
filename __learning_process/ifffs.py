users_pass = {'Mike': '12345', 'Tom': '12346'}

while True:
    user = input("Введите логин: ")
    pswd = input("Введите пароль: ")

    if user in users_pass and pswd == users_pass[user]:
        print("Добро пожаловать ", user)
        break
    else:
        users_pass[user] = pswd
        print("Регистрация завершена, войдите в систему ")
print('Всего пользователей в базе: ', users_pass.__len__())
lst = list(users_pass.keys())
print('Список пользователей: ', lst.__str__())
