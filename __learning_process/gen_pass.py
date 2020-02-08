import random
from colorama import Fore, Back, Style


chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


number = int(input('Кол-во паролей: '))
lenght = int(input('Длинна паролей: '))

for x in range(number):
    password = ' '
    for i in range(lenght):
        password += random.choice(chars)
    print(Style.DIM+Fore.LIGHTGREEN_EX+password)

