import json
from random import choice


def gen_person():
    name = ''
    tel = ''
    letters = ['a', 'b', 'c', 'd', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7']

    while len(name) != 5:
        name = name + choice(letters)


    while len(tel) != 7:
        tel = tel + choice(nums)


    person = {
        'name': name,
        'tel': tel
    }
    return person

persons = []


def main():
    for i in range(5):
        persons.append(gen_person())

    print(persons)

    with open('persons.json', 'w') as file:
        json.dump(persons, file, indent=2, ensure_ascii=False)

if __name__ == 'main':
    main()


main()