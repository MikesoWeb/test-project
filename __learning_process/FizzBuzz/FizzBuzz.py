def fizz_buzz(i):
    if not (i % 3) and not (i % 5):
        print('FizzBuzz')

    elif i % 3 == 0:
        print('Fizz')

    elif i % 5 == 0:
        print('Buzz')

    else:
        print(i)


fizz_buzz(5)
fizz_buzz(3)
fizz_buzz(9)
fizz_buzz(15)
fizz_buzz(11)
fizz_buzz(1)
fizz_buzz(2)
