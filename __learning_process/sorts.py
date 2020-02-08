children = ['Мухин_максим_Павлович', 'павлов_Альберт_мансурович', 'Манков_александр_Федорович']

for name in children:
    s_name = name.split('_')[0].title()
    s_surname = name.split('_')[1].title()
    s_family = name.split('_')[2].title()
    print(s_name + ' ' + s_surname + ' ' + s_family)


def chld_family(names):
    return names.split('_')[0].title()  # сортировка по фамилии.


print(chld_family(children[0]))
print(chld_family(children[1]))
print(chld_family(children[2]))


def chld_name(names):
    return names.split('_')[1].title()  # сортировка по имени.


print(chld_name(children[0]))
print(chld_name(children[1]))
print(chld_name(children[2]))


def chld_surname(names):
    return names.split('_')[2].title()  # сортировка по отчеству.


print(chld_surname(children[0]))
print(chld_surname(children[1]))
print(chld_surname(children[2]))

sorted_children_name = sorted(children, key=chld_name)
print(sorted_children_name)
