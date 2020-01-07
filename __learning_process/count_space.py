# Считаем сколько пробелов в тексте

s = "      gnjh"
count = 0
for i in s:
    if i == ' ':
        count += 1

print(count)

