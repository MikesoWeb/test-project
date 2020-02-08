a = range(0, 15)
count = 0

for i in a:
    i = i + 1

    count = count + 1
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')

    elif i % 5 == 0:
        print('Buzz')

    else:
        print(i)

print()
print('Всего сгенерировано чисел: ', count)
