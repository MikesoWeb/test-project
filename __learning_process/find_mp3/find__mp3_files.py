import glob
import os
from random import randint
from path_dir_func import path_dirs

count = 0
lst = []
path_dir = path_dirs()
os.chdir(path_dir)
for file in glob.glob("*.mp3"):
    lst.append(file)

lst_edit = str(lst)


print(len(lst_edit))

for i in lst:
    count += 1
    print(count, i)

rnd = randint(0, 100)

os.system(f'audacious {lst[rnd]}')

print('Случайный клип номер: ', rnd, '---', lst[rnd])

