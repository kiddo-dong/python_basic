# 삼각형 만들기

num = int(input("가장 짧은 변 입력 : "))

for i in range(num):
    for j in range(i+1):
        print('*', end = "")
    print()

for i in range(num):
    for _ in range(num-i-1):
        print(" ", end="")
    for _ in range(i+1):
        print('*', end="")
    print()

