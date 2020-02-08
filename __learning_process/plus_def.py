from pyperclip import copy, paste

x = " К а м е р у  в ы р у б а й , н a х у й ! "


def insert_between_characters(x):
    a = '&#0822;'.join(x.split())
    copy(a)
    paste()


insert_between_characters(x)
