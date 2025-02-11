# 10 - 99 사이의 난수 n개 생성(13 나오면 중단)
import random

num = int(input("생성할 난수 갯수 : "))

for i in range(num) :
    ran_num = random.randint(10,99)
    print(ran_num,end =" ")
    if ran_num == 13:
        print("\n프로그램 종료")
        break
else : print("\n프로그램 종료")