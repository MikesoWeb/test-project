import os
from find__mp3_files import lst

for i in lst:
    if i.__contains__(" "):
        ren = i.replace(" ", "_")
        os.rename(i, ren)
        print(i)

print(lst)
