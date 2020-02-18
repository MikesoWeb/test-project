from random import choices
from collections import Counter
import json

names = []

first_names = []

with open('russian_names.json', 'r', encoding='utf-8-sig') as f:
    data = json.loads(f.read())
    for i in data:
        if i["Sex"] == "Ж" or i["Sex"] == "M":
            names.append(i["Name"])

with open('russian_surnames.json', 'r', encoding='utf-8-sig') as f_sur:
    data_sur = json.loads(f_sur.read())
    for j in data_sur:
        if j["Sex"] != "" or j["Sex"] != "":
            first_names.append(j["Surname"])

count = 0
gen_names = []
while count != 1000:
    count += 1
    for i in choices(names):
        for j in choices(first_names):
            gen_names.append(i + ' ' + j + ' ' + '\n')
print(len(gen_names))
print(Counter(gen_names))
print(gen_names)

file = open('gen_names.txt', 'w')
for k in gen_names:
    file.write(k)
file.close()

