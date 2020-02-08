from import_bd_users import bd_users_old

original_users = ["Mike", "Tom", "Lera"]

another_users = ["Mary", "Gera", "Tim"]


def print_users(users):
    for user in users:
        print("Hello, " + user)


print_users(original_users)
print_users(another_users)
print_users(bd_users_old)
