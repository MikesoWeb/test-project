def is_year_leap(year):
    return not year % 400 or (year % 100 and not year % 4)


print(is_year_leap(1984))
