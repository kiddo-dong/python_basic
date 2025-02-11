# 반복 과정에서 조건 판단하기2

n = int(input("+와 -번갈아 출력\n수 입력 : "))

for i in range(n):
    if i % 2:
        print("-",end="")
    else : print("+",end="")