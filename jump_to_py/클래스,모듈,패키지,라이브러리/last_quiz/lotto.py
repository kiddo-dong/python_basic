import random

def lotto():
    li = []
    for i in range(6):
        a = random.randrange(1,46)
        li.append(a)
    return print(li)

lotto()